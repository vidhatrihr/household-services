from flask import Blueprint, redirect, render_template
from flask_login import current_user

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  if current_user.is_authenticated:
    if current_user.type == 'admin':
      return redirect('/admin/home')

    elif current_user.type == 'customer':
      return redirect('/customer/home')

    elif current_user.type == 'professional':
      return redirect('/professional/home')
  return redirect('/login')
