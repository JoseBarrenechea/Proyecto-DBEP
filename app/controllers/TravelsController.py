from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Plane
import datetime

def planes():
    planes = Plane.query.all()
    lista = "Planes : <br> "
    for plane_ in planes:
        lista += plane_.model 
        lista += " : "
        lista += f"C : {plane_.columns} R : {plane_.rows} Total : {plane_.columns*plane_.rows} , fc : {plane_.first_class} tc: {plane_.tourist_class} nc :{plane_.normal_class}  "
        lista += "<br>"
        for i in range(plane_.rows):
            for j in range(plane_.columns):
                lista += "[] "
            lista += "<br>"
        lista += "<br>"
        lista += "<br>"
    return lista
