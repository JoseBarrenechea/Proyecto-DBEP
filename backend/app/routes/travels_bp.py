from flask import Blueprint

from app.controllers.TravelsController import home

travels_bp = Blueprint('travels_bp', __name__)
travels_bp.route("/home", methods=["GET", "POST"]) (home)