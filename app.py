from flask import Flask
from routes import root_bp, auth_bp
from models import db
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

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
