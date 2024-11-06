from flask import Blueprint, redirect, render_template
from flask_login import current_user

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  if current_user.is_authenticated:
    if current_user.type == 'admin':
      return render_template('admin_home.html')

    elif current_user.type == 'customer':
      return render_template('customer_home.html')

    elif current_user.type == 'professional':
      return render_template('professional_home.html')
  return redirect('/login')
