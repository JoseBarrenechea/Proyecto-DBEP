from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Country,City
import datetime
import json

def home():
        countries = Country.query.all()
        lista = {}
        for country_ in countries:
           lista[len(lista)+1]= {
            "Nombre" : country_.name,
            "Descripcion" : country_.description
           }
         

        return json.dumps(lista,indent=2)

def get_cities():
        cities = City.query.all()
        lista = {}
        for city in cities:
           lista[len(lista)+1]= {
            "Nombre" : city.name,
            "Descripcion" : city.description,
            "Pais" : city.ccountry,
            "Visitas" : city.visits,
            "Imagen" : city.image,
           }

        return json.dumps(lista,indent=2)
        
def most_visited_cities():
   cities = City.query.all().order_by(City.visits)
   return json.dumps(cities,indent=4)