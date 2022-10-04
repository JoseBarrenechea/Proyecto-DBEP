from flask import Blueprint

from app.controllers.UserController import register

user_bp = Blueprint('user_bp', __name__)

user_bp.route("/register", methods=["GET", "POST"]) (register)