from flask import Flask 
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from flask_uploads import IMAGES, UploadSet,configure_uploads

db = SQLAlchemy()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.load_view = 'auth.login'
# photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    

    return app