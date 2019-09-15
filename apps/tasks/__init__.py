from flask import Blueprint

bp = Blueprint('tasks', __name__)

from apps.tasks import views
