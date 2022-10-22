import datetime # Tiempo
import calendar # Calenderio
import string # Strings
import random # Random
import json # importar libreria json
from app.models import Infovuelos

def datasave(texto):
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
                d_v["Numero"] = vuelo[j]
            elif j == 5:
                salto = "\n"
                for k in range(len(salto)):
                    sin_salto = vuelo[j].replace(salto[k], "")
                    d_v["PrecioBase"] = int(sin_salto)
        #orign = Infovuelos.query.filter(Infovuelos.Origen == d_v["Origen"]).first()
        #print(orign)
        diccionario[i+1] = d_v

  #  for numero, valor in diccionario.items():
        #print(numero, valor)

