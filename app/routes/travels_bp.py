from flask import Blueprint

from app.controllers.TravelsController import planes

travels_bp = Blueprint('travels_bp', __name__)
travels_bp.route("/planes", methods=["GET", "POST"]) (planes)