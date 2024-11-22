from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from models import *
from utils import *

# using 'Agg' backend to make matplotlib work in flask app
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# blueprint with all `/admin` routes
admin_bp = Blueprint('admin', __name__)


# ========== home ==========


@admin_bp.route('/admin/home')
@login_required
def admin_home():
  if current_user.type != 'admin':
    return 'Forbidden', 403
  services = Service.query.all()
  professionals = Professional.query.all()
  customers = Customer.query.all()
  service_requests = ServiceRequest.query.all()

  return render_template(
      'admin_home.html',
      services=services, professionals=professionals, customers=customers,
      service_requests=service_requests, get_avg_ratings=get_avg_ratings
  )


# ========== search ==========


@admin_bp.route('/admin/search')
@login_required
def admin_search():
  if current_user.type != 'admin':
    return 'Forbidden', 403
  return render_template('admin_search.html')


@admin_bp.route('/admin/search-results/<search_type>')
@login_required
def admin_search_results(search_type):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  """ 
  example urls:
    http://localhost:5000/admin/search-results/customers?full_name=...&pin_code=...
    http://localhost:5000/admin/search-results/professionals?full_name=...&pin_code=...
  """
  # get search parameters from query string in url (?full_name=...&pin_code=...)
  full_name = request.args.get('full_name')
  pin_code = request.args.get('pin_code')

  if search_type == 'customers':
    query = Customer.query.join(User)
    if full_name:
      # do filter if full_name is provided
      query = query.filter(User.full_name.ilike(f'%{full_name}%'))  # partially match full_name
    if pin_code:
      # do filter if pin_code is provided
      query = query.filter(User.pin_code == pin_code)

    customers = query.all()
    return render_template('admin_search_results.html', customers=customers, search_type=search_type)

  elif search_type == 'professionals':
    query = Professional.query.join(User)
    if full_name:
      query = query.filter(User.full_name.ilike(f'%{full_name}%'))
    if pin_code:
      query = query.filter(User.pin_code == pin_code)

    professionals = query.all()
    return render_template('admin_search_results.html', professionals=professionals,
                           get_avg_ratings=get_avg_ratings, search_type=search_type)


# ========== summary ==========


@admin_bp.route('/admin/summary')
@login_required
def admin_summary():
  if current_user.type != 'admin':
    return 'Forbidden', 403
  stars = {}  # {1: x, ... 5: x}, x is count of requests with that many stars
  for i in range(1, 6):
    stars[i] = ServiceRequest.query.filter_by(ratings=i).count()
  total_stars = sum(stars.values())

  requests_requested = ServiceRequest.query.filter_by(status='requested').count()
  requests_accepted = ServiceRequest.query.filter_by(status='accepted').count()
  requests_done = ServiceRequest.query.filter_by(status='done').count()

  if total_stars > 0:
    """ generate ratings pie chart """
    labels = [f'{i} Star' for i in range(1, 6)]
    data = [stars[i] for i in range(1, 6)]
    plt.pie(data, labels=labels, autopct='%1.2f%%')
    plt.title('Overall Customer Ratings')
    plt.savefig('static/overall_customer_ratings.png')
    plt.close()

  """ generate service requests bar chart """
  labels = ['Requested', 'Accepted', 'Done']
  data = [requests_requested, requests_accepted, requests_done]
  plt.bar(labels, data, color=['red', 'blue', 'green'])
  plt.title('Service Request Summary')
  plt.savefig('static/service_request_summary.png')
  plt.close()

  return render_template(
      'admin_summary.html',
      stars=stars, total_stars=total_stars,
      requests_requested=requests_requested, requests_accepted=requests_accepted,
      requests_done=requests_done
  )


# ========== details ==========


@admin_bp.route('/admin/service-details/<int:service_id>')
@login_required
def admin_service_details(service_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  service = Service.query.filter_by(id=service_id).first()
  return render_template('admin_service_details.html', service=service)


@admin_bp.route('/admin/customer-details/<int:customer_id>')
@login_required
def admin_customer_details(customer_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  customer = Customer.query.filter_by(id=customer_id).first()
  return render_template('admin_customer_details.html', customer=customer)


@admin_bp.route('/admin/professional-details/<int:professional_id>')
@login_required
def admin_professional_details(professional_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  professional = Professional.query.filter_by(id=professional_id).first()
  return render_template(
      'admin_professional_details.html',
      professional=professional, get_avg_ratings=get_avg_ratings
  )


# ========== approve/block/delete professional ==========


@admin_bp.route('/admin/approve-professional/<int:professional_id>')
@login_required
def approve_professional(professional_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  professional = Professional.query.filter_by(id=professional_id).first()
  professional.is_approved = True  # set true will update in professionals table
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/block-professional/<int:professional_id>')
@login_required
def block_professional(professional_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  professional = Professional.query.filter_by(id=professional_id).first()
  professional.is_approved = False
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/delete-professional/<int:professional_id>')
@login_required
def delete_professional(professional_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  professional = Professional.query.filter_by(id=professional_id).first()
  db.session.delete(professional)
  db.session.commit()
  return redirect('/admin/home')


# ========== add/edit/delete service ==========


@admin_bp.route('/admin/add-service', methods=['GET', 'POST'])
@login_required
def add_service():
  if current_user.type != 'admin':
    return 'Forbidden', 403
  if request.method == 'GET':
    service_categories = ServiceCategory.query.all()
    return render_template('admin_add_service.html', service_categories=service_categories)

  elif request.method == 'POST':
    new_service = Service(
        name=request.form.get('name'),
        price=request.form.get('price'),
        service_category_id=request.form.get('service_category_id')
    )
    db.session.add(new_service)
    db.session.commit()
    return redirect('/admin/home')


@admin_bp.route('/admin/edit-service/<int:service_id>', methods=['GET', 'POST'])
@login_required
def edit_service(service_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  # get `service object` for <int:service_id> path variable
  service = Service.query.filter_by(id=service_id).first()

  if request.method == 'GET':
    service_categories = ServiceCategory.query.all()
    return render_template('admin_edit_service.html', service=service, service_categories=service_categories)

  elif request.method == 'POST':
    service.name = request.form.get('name')
    service.price = request.form.get('price')
    service.service_category_id = request.form.get('service_category_id')
    db.session.commit()
    return redirect('/admin/home')


@admin_bp.route('/admin/delete-service/<int:service_id>')
@login_required
def delete_service(service_id):
  if current_user.type != 'admin':
    return 'Forbidden', 403
  # get the `service object`
  service = Service.query.filter_by(id=service_id).first()

  # delete that object
  db.session.delete(service)

  db.session.commit()
  return redirect('/admin/home')
