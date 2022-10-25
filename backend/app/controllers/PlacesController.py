from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Country
import datetime

def home():
        countries = Country.query.all()
        lista = "Countries : <br>"
        lista += "<br>"
        for country_ in countries:
           lista += country_.name 
           lista += "<br>"
           lista += country_.description
           lista += "<br>"
           lista += "<br>"

        return lista
