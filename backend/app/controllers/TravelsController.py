from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Plane,Infovuelos
import datetime
import json
import calendar

def home():
  if request.method == "POST":
    origen = request.args.get("Origin")
    destino = request.args.get("Destiny")
    partida = request.args.get("Departure")
    vuelta = request.args.get("Return")
    pasajeros = request.args.get("passengers")

    vuelos_disponibles = {}

    n_d = datetime.datetime.strptime(partida  ,"%Y-%m-%d").weekday()
    dia = calendar.day_name[n_d]
    print(calendar.day_name[n_d])

    vuelos_d = Infovuelos.query.filter(Infovuelos.day == dia,Infovuelos.origin == origen,Infovuelos.destiny == destino).all()
    #lista = f" {origen}->{destino}  ||  {dia}  ||          partida: {partida} | vuelta: {vuelta}    <br> Vuelos disponibles: <br> "
    for vuelo_ in vuelos_d:
      vuelos_disponibles[len(vuelos_disponibles)+1] = {
        "Modelo" : vuelo_.model_plane,
        "Dia" : vuelo_.day,
        "Origen" : vuelo_.origin,
        "Destino" : vuelo_.destiny,
        "Hora" : vuelo_.hour
      }

    result_json = json.dumps(vuelos_disponibles,indent = 4)
    
   # planes = Plane.query.all()
    #lista += "<br> Planes : <br> "
   # for plane_ in planes:
    #    lista += plane_.model 
     #   lista += " : "
      #  lista += f"C : {plane_.columns} R : {plane_.rows} Total : {plane_.columns*plane_.rows} , fc : {plane_.first_class} tc: {plane_.tourist_class} nc :{plane_.normal_class}  "
       # lista += "<br>"
       # for i in range(plane_.rows):
        #    for j in range(plane_.columns):
         #       lista += "[] "
          #  lista += "<br>"
        #lista += "<br>"
        #lista += "<br>"
    #print(lista)
    return result_json
  return render_template("travels.html")

def planes():
    return "a"

    