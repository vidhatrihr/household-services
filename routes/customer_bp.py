from flask import Blueprint, render_template
from flask_login import current_user
from models import *

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customer/home')
def customer_home():
  customer_id = current_user.customer.id
  accepted_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='accepted'
  )
  pending_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='requested'
  )
  past_requests = ServiceRequest.query.filter_by(
      customer_id=customer_id,
      status='done'
  )
  return render_template(
      'customer_home.html',
      accepted_requests=accepted_requests,
      pending_requests=pending_requests,
      past_requests=past_requests
  )


@customer_bp.route('/customer/search')
def customer_search():
  return render_template('customer_search.html')


@customer_bp.route('/customer/summary')
def customer_summary():
  return render_template('customer_summary.html')
