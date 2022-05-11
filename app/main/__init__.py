from flask import Blueprint
main = Blueprint("auth",__name__)
from .views import *