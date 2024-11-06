from flask import Blueprint, render_template

professional_bp = Blueprint('professional', __name__)


@professional_bp.route('/professional/home')
def professional_home():
  return render_template('professional_home.html')


@professional_bp.route('/professional/search')
def professional_search():
  return render_template('professional_search.html')


@professional_bp.route('/professional/summary')
def professional_summary():
  return render_template('professional_summary.html')
