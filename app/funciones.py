import datetime # Tiempo
import calendar # Calenderio
import string # Strings
import random # Random
import json # importar libreria json
from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Infovuelos

def infvue(texto):
    diccionario = {}
    archivo = open(texto, "r")
    datos = archivo.readlines()
    for i in range(len(datos)):
        vuelo = datos[i].split(",")
        d_v = {}
        for j in range(len(vuelo)):
            if j == 0:
                d_v["Origen"] = vuelo[j]
            elif j == 1:
                d_v["Destino"] = vuelo[j]
            elif j == 2:
                d_v["Dia"] = vuelo[j]
            elif j == 3:
                d_v["Hora"] = datetime.timedelta(hours=(int(vuelo[j])/100))
            elif j == 4:
                d_v["Modelo"] = vuelo[j]
            elif j == 5:
                salto = "\n"
                for k in range(len(salto)):
                    sin_salto = vuelo[j].replace(salto[k], "")
                    d_v["PrecioBase"] = int(sin_salto)
        rep = Infovuelos.query.filter(Infovuelos.origin == d_v["Origen"],Infovuelos.destiny == d_v["Destino"],Infovuelos.day == d_v["Dia"],Infovuelos.hour == d_v["Hora"],Infovuelos.model_plane == d_v["Modelo"],Infovuelos.price == d_v["PrecioBase"] ).first()
        if not (rep):
            NIV = Infovuelos(origin = d_v["Origen"],destiny=d_v["Destino"],day=d_v["Dia"],hour=d_v["Hora"],model_plane=d_v["Modelo"],price=d_v["PrecioBase"])
            try:
                db.session.add(NIV)
                db.session.commit()
            except Exception as err:
                print(err)
        diccionario[i+1] = d_v

  #  for numero, valor in diccionario.items():
        #print(numero, valor)