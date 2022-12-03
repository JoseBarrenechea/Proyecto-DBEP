from flask import Blueprint

from app.controllers.LoginController import login, getLogins, viewLogins, submitAsync

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (login)
login_bp.route("/getall", methods=["GET"]) (getLogins)
login_bp.route("/viewall", methods=["GET"]) (viewLogins)
login_bp.route("/submit", methods=["GET"]) (submitAsync)