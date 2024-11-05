from flask import Blueprint

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  return 'Hello from root'
