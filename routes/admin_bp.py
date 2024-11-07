from flask import Blueprint, render_template, request, redirect
from models import *

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/delete-professional/<int:professional_id>')
def delete_professional(professional_id):
  professional = Professional.query.filter_by(id=professional_id).first()
  db.session.delete(professional)
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/approve-professional/<int:professional_id>')
def approve_professional(professional_id):
  professional = Professional.query.filter_by(id=professional_id).first()
  professional.is_approved = True
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/block-professional/<int:professional_id>')
def block_professional(professional_id):
  professional = Professional.query.filter_by(id=professional_id).first()
  professional.is_approved = False
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/delete-service/<int:service_id>')
def delete_service(service_id):
  service = Service.query.filter_by(id=service_id).first()
  db.session.delete(service)
  db.session.commit()
  return redirect('/admin/home')


@admin_bp.route('/admin/edit-service/<int:service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
  service = Service.query.filter_by(id=service_id).first()
  service_categories = ServiceCategory.query.all()
  if request.method == 'GET':
    return render_template('admin_edit_service.html', service=service, service_categories=service_categories)

  elif request.method == 'POST':
    service.name = request.form.get('name')
    service.price = request.form.get('price')
    service.service_category_id = request.form.get('service_category_id')
    db.session.commit()
    return redirect('/admin/home')


@admin_bp.route('/admin/add-service', methods=['GET', 'POST'])
def add_service():
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


@admin_bp.route('/admin/home')
def admin_home():
  services = Service.query.all()
  professionals = Professional.query.all()
  service_requests = ServiceRequest.query.all()
  return render_template('admin_home.html', services=services, professionals=professionals, service_requests=service_requests)


@admin_bp.route('/admin/search')
def admin_search():
  return render_template('admin_search.html')


@admin_bp.route('/admin/summary')
def admin_summary():
  return render_template('admin_summary.html')
