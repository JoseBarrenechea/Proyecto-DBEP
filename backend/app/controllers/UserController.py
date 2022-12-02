from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User,Ticket
import datetime
import json

#https://developer.mozilla.org/ru/docs/Web/HTML/Element/Input/date

def register():
    if request.method == "POST":
        dni = request.args.get("dni")
        name = request.args.get("name")
        last_name = request.args.get("last_name")
        birthday = request.args.get("birthday")
        email = request.args.get("email")
        password = request.args.get("password")
        confirm_password = request.args.get("confirm_password")
        

        if (len(password) < 8):
            return "Contrasena muy corta"

        user1 = User.query.filter(User.dni == int(dni)).first()
        user2 = User.query.filter(User.email == email).first()
        
        if (password != confirm_password):
            return "Las contrasenas no coinciden"
        
        if user1 or user2:
            return "Usuario o email ya existe"

        user = User(dni=int(dni), password=password, email=email, name=name,last_name=last_name,birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date(),image="",registration_date=datetime.datetime.now())

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Internal server error."

        return "Usuario registrado"
    return render_template("register.html")


def get_tickers():
    if request.method == "POST":
        dni = request.args.get("dni")
        tickets = Ticket.query.filter(Ticket.user_tk == int(dni)).all()
        return json.dumps(tickets,indent=4)
