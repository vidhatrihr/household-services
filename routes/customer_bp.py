from flask import Blueprint, render_template

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customer/home')
def customer_home():
  return render_template('customer_home.html')


@customer_bp.route('/customer/search')
def customer_search():
  return render_template('customer_search.html')


@customer_bp.route('/customer/summary')
def customer_summary():
  return render_template('customer_summary.html')
