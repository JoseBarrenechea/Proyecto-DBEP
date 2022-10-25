from flask import Blueprint

from app.controllers.PlacesController import home

places_bp = Blueprint('places_bp', __name__)
places_bp.route("/", methods=["GET", "POST"]) (home)