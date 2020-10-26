from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    """
    Function to create Flask app
    """
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    #Register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app