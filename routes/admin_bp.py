from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/home')
def admin_home():
  return render_template('admin_home.html')


@admin_bp.route('/admin/search')
def admin_search():
  return render_template('admin_search.html')


@admin_bp.route('/admin/summary')
def admin_summary():
  return render_template('admin_summary.html')
