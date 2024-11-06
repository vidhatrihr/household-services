from flask import Blueprint, redirect, session

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  if 'logged_in' in session:
    return 'Welcome take money'
  return redirect('/login')
