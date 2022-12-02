from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import models, topRoutes

from app.routes.login_bp import login_bp
from app.routes.user_bp import user_bp
from app.routes.places_bp import places_bp
from app.routes.travels_bp import travels_bp

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(user_bp, url_prefix="/profile")
app.register_blueprint(places_bp, url_prefix="/places")
app.register_blueprint(travels_bp, url_prefix="/travels")

# db.create_all()

from app import funciones
#vuelosin = funciones.infvue(r"app\Info\InfoVuelos.txt")
vuelosin = funciones.infciudad(r"app\Info\InfoCiudades.json")


