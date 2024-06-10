# IMPORTS
from flask import Flask

from .config import config
from .extensions import db, migrate, mail
from .main.views import main_bp

import os
import logging
from logging.handlers import RotatingFileHandler

    
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    app.register_blueprint(main_bp)

    # Log configuration
    if not app.debug and not app.testing:
        # Logging Error to File   
        if not os.path.exists('logs'):
            os.mkdir('logs')
            
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        # The logging.Formatter class provides custom formatting for the log messages.
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('The application was started')
        
    return app