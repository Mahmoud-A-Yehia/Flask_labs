from flask import Flask
from flask_migrate import Migrate
from .config import config_options
from .models import db

from .home import home_routes
from .books import book_routes
from .auth import auth_routes
from flask import render_template, url_for

def create_app(config_type='dev'):
    app = Flask(__name__)

    app.secret_key = '123'

    # Configure App
    current_config = config_options[config_type]
    print(current_config)
    app.config.from_object(current_config) # configure debug=True

    # Configure Database
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    migrate = Migrate(app=app, db=db)

    # Create Tables
    with app.app_context(): # production
        db.create_all()

    # Register Blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(auth_routes)

    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template("error.html")
    
    return app
