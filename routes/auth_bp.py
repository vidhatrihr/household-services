from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import *


auth_bp = Blueprint('auth', __name__)


# ======== login ========


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect('/')

  if request.method == 'GET':
    # if error is True, an error message will be shown
    return render_template('login.html', error=False)

  elif request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    # user.password is coming from db and is hashed;
    # check user exists, and password matches
    if user and check_password_hash(user.password, password):
      login_user(user)  # do login
      return redirect('/')  # send to root; and root will redirect to dashboard
    else:
      return render_template('login.html', error=True)  # invalid email/password


# ======== logout ========


@auth_bp.route('/logout')
def logout():
  logout_user()
  return redirect('/login')


# ======== register ========


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    cities = City.query.all()  # for cities dropdown
    return render_template('register.html', cities=cities)

  elif request.method == 'POST':
    new_customer = Customer(
        user=User(
            email=request.form.get('email'),
            password=generate_password_hash(request.form.get('password')),
            type='customer',
            full_name=request.form.get('full_name'),
            address=request.form.get('address'),
            pin_code=request.form.get('pin_code'),
            city_id=request.form.get('city_id')
        )
    )
    db.session.add(new_customer)
    db.session.commit()

    # do login after register
    login_user(new_customer.user)  # this function expects a user obj not a customer obj
    return redirect('/customer/home')  # send to dashboard


# ======== register professional ========


@auth_bp.route('/register/professional', methods=['GET', 'POST'])
def register_professional():
  if request.method == 'GET':
    cities = City.query.all()  # for dropdown
    service_categories = ServiceCategory.query.all()  # for dropdown
    return render_template('register_professional.html',
                           cities=cities,
                           service_categories=service_categories)

  elif request.method == 'POST':
    new_professional = Professional(
        service_category_id=request.form.get('service_category_id'),
        bio=request.form.get('bio'),
        user=User(
            email=request.form.get('email'),
            # saving hashed password to db 👇✅
            password=generate_password_hash(request.form.get('password')),
            type='professional',
            full_name=request.form.get('full_name'),
            address=request.form.get('address'),
            pin_code=request.form.get('pin_code'),
            city_id=request.form.get('city_id')
        )
    )
    db.session.add(new_professional)
    db.session.commit()

    # do login after register
    login_user(new_professional.user)
    return redirect('/professional/home')  # send to dashboard
