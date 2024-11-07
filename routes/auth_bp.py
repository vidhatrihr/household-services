from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, current_user, logout_user
from models import *


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect('/')

  if request.method == 'GET':
    return render_template('login.html', error=False)

  elif request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
      if user.password == password:
        login_user(user)
        return redirect('/')
      return render_template('login.html', error=True)
    return render_template('login.html', error=True)


@auth_bp.route('/logout')
def logout():
  logout_user()
  return redirect('/login')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')

  elif request.method == 'POST':
    new_customer = Customer(
        user=User(
            email=request.form.get('email'),
            password=request.form.get('password'),
            type='customer',
            full_name=request.form.get('full_name'),
            address=request.form.get('address'),
            pin_code=request.form.get('pin_code'),
            city_id=request.form.get('city_id')
        )
    )
    db.session.add(new_customer)
    db.session.commit()
    login_user(new_customer.user)
    return redirect('/')


@auth_bp.route('/register/professional', methods=['GET', 'POST'])
def register_professional():
  if request.method == 'GET':
    return render_template('register_professional.html')

  elif request.method == 'POST':
    new_professional = Professional(
        service_category_id=request.form.get('service_category_id'),
        bio=request.form.get('bio'),
        user=User(
            email=request.form.get('email'),
            password=request.form.get('password'),
            type='professional',
            full_name=request.form.get('full_name'),
            address=request.form.get('address'),
            pin_code=request.form.get('pin_code'),
            city_id=request.form.get('city_id')
        )
    )
    db.session.add(new_professional)
    db.session.commit()
    login_user(new_professional.user)
    return redirect('/')
