from flask import Flask
from flask_login import LoginManager
from routes import root_bp, auth_bp, admin_bp, customer_bp, professional_bp
from models import *
import populate_db


def create_app():
  # make app
  app = Flask(__name__)
  app.secret_key = '12345'  # for flask-login sessions

  # register blueprints
  app.register_blueprint(root_bp)
  app.register_blueprint(auth_bp)
  app.register_blueprint(admin_bp)
  app.register_blueprint(customer_bp)
  app.register_blueprint(professional_bp)

  # setup database
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  db.init_app(app)

  # make tables and populate
  with app.app_context():
    db.create_all()  # create all tables
    if Customer.query.count() == 0:  # no customers means no data in db, so we populate
      populate_db.populate()

  # setup flask login
  login_manager = LoginManager()
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    """ take int user_id and return the corresponding user object """
    return User.query.filter_by(id=user_id).first()

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
