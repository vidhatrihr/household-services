from flask import Blueprint, redirect, session
from flask_login import current_user

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  if current_user.is_authenticated:
    return f'Hello {current_user.full_name} from {current_user.city.name}'
  return redirect('/login')
