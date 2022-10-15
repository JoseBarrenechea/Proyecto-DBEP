from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User
import datetime

def register():
    if request.method == "POST":
        dni = request.form["dni"]
        name = request.form["name"]
        last_name = request.form["last_name"]
        birthday = request.form["birthday"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        

        if (len(password) < 8):
            return "Contrasena muy corta"

        user1 = User.query.filter(User.dni == int(dni)).first()
        user2 = User.query.filter(User.email == email).first()
        
        if (password != confirm_password):
            return "Las contrasenas no coinciden"
        
        if user1 or user2:
            return "Usuario o email ya existe"

        user = User(dni=int(dni), password=password, email=email, name=name,last_name=last_name,birthday = datetime.strptime(date_str, '%m-%d-%Y').date())

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Internal server error."

        return "Usuario registrado"
    return render_template("register.html")
