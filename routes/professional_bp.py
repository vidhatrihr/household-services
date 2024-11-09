from flask import Blueprint, render_template
from models import *
from flask_login import current_user

professional_bp = Blueprint('professional', __name__)


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


@professional_bp.route('/professional/search')
def professional_search():
  return render_template('professional_search.html')


@professional_bp.route('/professional/summary')
def professional_summary():
  return render_template('professional_summary.html')
