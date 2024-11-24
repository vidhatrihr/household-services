from datetime import datetime
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required
from models import *
from utils import get_avg_ratings

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

customer_bp = Blueprint('customer', __name__)


# ====== home ======


@customer_bp.route('/customer/home')
@login_required
def customer_home():
  if current_user.type != 'customer':
    return 'Forbidden', 403
  customer_id = current_user.customer.id

  accepted_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='accepted'
  ).all()

  pending_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='requested'
  ).all()

  past_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='done'
  ).all()

  all_categories = ServiceCategory.query.all()
  """ if we need to show only those categories from customer's city """
  categories_in_same_city = []
  for category in all_categories:
    # should we include this category?
    # we can include if we find a professional in this category from customer's city
    # we do check all professionals of this category one by one
    for professional in category.professionals:
      if professional.user.city == current_user.city:
        # we found such a professional
        categories_in_same_city.append(category)
        break

  return render_template(
      'customer_home.html',
      accepted_requests=accepted_requests,
      pending_requests=pending_requests,
      past_requests=past_requests,
      categories=all_categories  # can do `categories_in_same_city`
  )


# ====== search ======


@customer_bp.route('/customer/search')
@login_required
def customer_search():
  if current_user.type != 'customer':
    return 'Forbidden', 403
  return render_template('customer_search.html')


@customer_bp.route('/customer/search-results/<search_type>')
@login_required
def customer_search_results(search_type):
  if current_user.type != 'customer':
    return 'Forbidden', 403
  """ 
  example url:
    http://localhost:5000/customer/search-results/services?name=...
  """
  if search_type == 'services':
    # get search parameters from query string in url (?name=...)
    name = request.args.get('name')
    # do query
    query = Service.query
    if name:
      query = query.filter(Service.name.ilike(f'%{name}%'))
    services = query.all()
    return render_template('customer_search_results.html', services=services, search_type=search_type)


# ====== summary ======


@customer_bp.route('/customer/summary')
@login_required
def customer_summary():
  if current_user.type != 'customer':
    return 'Forbidden', 403
  requests_requested = ServiceRequest.query.filter_by(
      customer_id=current_user.customer.id,
      status='requested'
  ).count()

  requests_accepted = ServiceRequest.query.filter_by(
      customer_id=current_user.customer.id,
      status='accepted'
  ).count()

  requests_done = ServiceRequest.query.filter_by(
      customer_id=current_user.customer.id,
      status='done'
  ).count()

  """ generate service requests bar chart """
  labels = ['Requested', 'Accepted', 'Done']
  data = [requests_requested, requests_accepted, requests_done]
  plt.bar(labels, data, color=['red', 'blue', 'green'])
  plt.title('Service Request Summary')
  plt.savefig('static/service_request_summary.png')
  plt.close()

  return render_template(
      'customer_summary.html',
      requests_requested=requests_requested, requests_accepted=requests_accepted,
      requests_done=requests_done
  )


# ====== profile ======


@customer_bp.route('/customer/profile')
@login_required
def customer_profile():
  if current_user.type != 'customer':
    return 'Forbidden', 403
  return render_template('customer_profile.html', customer=current_user.customer)


@customer_bp.route('/customer/edit-profile', methods=['GET', 'POST'])
@login_required
def customer_edit_profile():
  if current_user.type != 'customer':
    return 'Forbidden', 403
  if request.method == 'GET':
    cities = City.query.all()
    return render_template('customer_edit_profile.html', customer=current_user.customer, cities=cities)
  elif request.method == 'POST':
    current_user.email = request.form.get('email')
    current_user.full_name = request.form.get('full_name')
    current_user.city_id = request.form.get('city_id')
    current_user.address = request.form.get('address')
    current_user.pin_code = request.form.get('pin_code')
    db.session.commit()
    return redirect('/customer/profile')


# ====== customer-details ======


@customer_bp.route('/customer/professional-details/<int:professional_id>')
@login_required
def customer_professional_details(professional_id):
  if current_user.type != 'customer':
    return 'Forbidden', 403
  professional = Professional.query.filter_by(id=professional_id).first()
  return render_template('customer_professional_details.html', professional=professional,
                         get_avg_ratings=get_avg_ratings)


# ====== book-service ======


@customer_bp.route('/customer/book-service/<int:service_id>', methods=['GET', 'POST'])
@login_required
def customer_book_service(service_id):
  if current_user.type != 'customer':
    return 'Forbidden', 403
  if request.method == 'GET':
    return render_template('customer_book_service.html', service_id=service_id)

  elif request.method == 'POST':
    customer_id = current_user.customer.id
    booking_date = datetime.strptime(request.form.get('booking_date'), '%Y-%m-%d')
    new_service_request = ServiceRequest(
        customer_id=customer_id,
        service_id=service_id,
        description=request.form.get('description'),
        booking_date=booking_date
    )
    db.session.add(new_service_request)
    db.session.commit()
    return redirect('/')


# ====== close-request ======


@customer_bp.route('/customer/close-request/<int:request_id>', methods=['GET', 'POST'])
@login_required
def customer_close_request(request_id):
  if current_user.type != 'customer':
    return 'Forbidden', 403
  if request.method == 'GET':
    return render_template('customer_close_request.html', request_id=request_id)

  elif request.method == 'POST':
    service_request = ServiceRequest.query.filter_by(id=request_id).first()
    service_request.status = 'done'
    service_request.ratings = request.form.get('stars')
    service_request.remarks = request.form.get('remarks')
    db.session.commit()
    return redirect('/')
