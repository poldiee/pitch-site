from distutils.command.config import config
from distutils.debug import DEBUG
from distutils.log import debug
import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://davy:qwerty@localhost/site'
    # print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    Debug=True 

class DevConfig(Config):
    Debug=True
config_options = {
    'development':DevConfig
}