from distutils.command.config import config
from distutils.debug import DEBUG
from distutils.log import debug
import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    Debug=True 

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://davy:qwerty@localhost/site'
    Debug=True
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}