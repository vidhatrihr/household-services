from flask import Flask
from flask_login import LoginManager
from routes import root_bp, auth_bp
from models import *
import populate_db


def create_app():
  # make app
  app = Flask(__name__)
  app.secret_key = '12345'

  # register blueprints
  app.register_blueprint(root_bp)
  app.register_blueprint(auth_bp)

  # setup database
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
  db.init_app(app)

  # make tables and populate
  with app.app_context():
    db.create_all()
    populate_db.populate()

  # setup flask login
  login_manager = LoginManager()
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    """ take user_id and return the corresponding user object """
    return User.query.filter_by(id=user_id).first()

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
