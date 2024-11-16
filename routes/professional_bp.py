from flask import Blueprint, render_template, redirect, request
from models import *
from flask_login import current_user
from datetime import datetime


import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')

professional_bp = Blueprint('professional', __name__)


# ====== home ======


@professional_bp.route('/professional/home')
def professional_home():
  professional = current_user.professional
  city_id = professional.user.city_id
  category_id = professional.service_category_id

  accepted_requests = ServiceRequest.query.filter_by(
      professional_id=professional.id,
      status='accepted'
  ).all()

  requests_available_to_accept = ServiceRequest.query.join(Customer).join(User).filter(
      User.city_id == city_id,
      ServiceRequest.service.has(service_category_id=category_id),
      ServiceRequest.status == 'requested'
  ).all()

  closed_requests = ServiceRequest.query.filter_by(
      professional_id=professional.id,
      status='done'
  ).all()

  return render_template(
      'professional_home.html',
      accepted_requests=accepted_requests,
      closed_requests=closed_requests,
      requests_available_to_accept=requests_available_to_accept
  )


# ====== search ======


@professional_bp.route('/professional/search')
def professional_search():
  services = Service.query.filter_by(service_category=current_user.professional.service_category)
  return render_template('professional_search.html', services=services)


@professional_bp.route('/professional/search-results/<search_type>')
def professional_search_results(search_type):
  """ 
  example url:
    http://localhost:5000/professional/search-results/services?booking_date=yyyy-mm-dd&pin_code=...&service_id=...
  """
  if search_type == 'accepted-requests':
    # get search parameters from query string in url (booking_date=yyyy-mm-dd&pin_code=...&service_id=...)
    booking_date = request.args.get('booking_date')
    pin_code = request.args.get('pin_code')
    service_id = request.args.get('service_id')

    # make an empty query
    query = ServiceRequest.query

    # apply filters as required
    query = query.filter(ServiceRequest.status == 'accepted',
                         ServiceRequest.professional_id == current_user.professional.id)
    if booking_date:
      # convert `booking_date str` to `datetime obj`
      y, m, d = map(int, booking_date.split('-'))
      query = query.filter(ServiceRequest.booking_date == datetime(y, m, d))
    if pin_code:
      query = query.join(Customer).join(User).filter(User.pin_code == pin_code)
    if service_id:
      query = query.filter(ServiceRequest.service_id == service_id)

      # fetch all rows
    service_requests = query.all()
    return render_template('professional_search_results.html', search_type=search_type, service_requests=service_requests)

# ====== summary ======


@professional_bp.route('/professional/summary')
def professional_summary():
  stars = {}  # {1: x, ... 5: x}, x is count of requests with that many stars
  for i in range(1, 6):
    stars[i] = ServiceRequest.query.filter_by(ratings=i, professional=current_user.professional).count()
  total_stars = sum(stars.values())

  requests_requested = ServiceRequest.query.filter_by(
      status='requested', professional=current_user.professional).count()
  requests_accepted = ServiceRequest.query.filter_by(status='accepted', professional=current_user.professional).count()
  requests_done = ServiceRequest.query.filter_by(status='done', professional=current_user.professional).count()

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
      'professional_summary.html',
      stars=stars, total_stars=total_stars,
      requests_requested=requests_requested, requests_accepted=requests_accepted,
      requests_done=requests_done
  )


# ====== accept-request ======


@professional_bp.route('/professional/accept-request/<int:request_id>')
def professional_accept_request(request_id):
  request = ServiceRequest.query.filter_by(id=request_id).first()
  request.status = 'accepted'
  request.professional = current_user.professional
  db.session.commit()
  return redirect('/')
