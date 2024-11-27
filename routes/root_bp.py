from flask import Blueprint, redirect
from flask_login import current_user

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  # if logged in, go to respective dashboards;
  if current_user.is_authenticated:  # `is_authenticated` coming from the class UserMixin
    if current_user.type == 'admin':
      return redirect('/admin/home')

    elif current_user.type == 'customer':
      return redirect('/customer/home')

    elif current_user.type == 'professional':
      return redirect('/professional/home')

  # if NOT logged in, go to login page
  return redirect('/login')
