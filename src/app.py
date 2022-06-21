#src/app.py

from flask import Flask
from flask import make_response
from .config import app_config
from .models import db
from src.api import blueprint as api


def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)
  

  @app.route("/", methods=["GET"])
  def home():
      return make_response(({"success": True}), 200)

  # Register blueprint endpoint
  app.register_blueprint(api, url_prefix='/api/v1') 
  return app 
