from flask import Blueprint

from app.controllers.UserController import register
from app.controllers.LoginController import login

user_bp = Blueprint('user_bp', __name__)

user_bp.route("/register", methods=["GET", "POST"]) (register)
user_bp.route("/login", methods=["GET", "POST"]) (login)
