from datetime import datetime
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user
from models import *

customer_bp = Blueprint('customer', __name__)


# ====== home ======


@customer_bp.route('/customer/home')
def customer_home():
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
def customer_search():
  return render_template('customer_search.html')


@customer_bp.route('/customer/search-results/<search_type>')
def customer_search_results(search_type):
  if search_type == 'services':
    name = request.args.get('name')
    query = Service.query
    if name:
      query = query.filter(Service.name.ilike(f'%{name}%'))
    services = query.all()
    return render_template('customer_search_results.html', services=services, search_type=search_type)


# ====== summary ======


@customer_bp.route('/customer/summary')
def customer_summary():
  return render_template('customer_summary.html')


# ====== book-service ======


@customer_bp.route('/customer/book-service/<int:service_id>', methods=['GET', 'POST'])
def customer_book_service(service_id):
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
def customer_close_request(request_id):
  if request.method == 'GET':
    return render_template('customer_close_request.html', request_id=request_id)

  elif request.method == 'POST':
    service_request = ServiceRequest.query.filter_by(id=request_id).first()
    service_request.status = 'done'
    service_request.ratings = request.form.get('stars')
    service_request.remarks = request.form.get('remarks')
    db.session.commit()
    return redirect('/')
