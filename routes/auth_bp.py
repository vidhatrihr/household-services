from flask import Blueprint, render_template, request, session, redirect
from models import *


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html', error=False)

  elif request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
      if user.password == password:
        session['logged_in'] = True
        return redirect('/')
      return render_template('login.html', error=True)
    return render_template('login.html', error=True)
