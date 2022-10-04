from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User
import datetime

def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        education = request.form["education"]

        if (len(password) < 8):
            return "Contrasena muy corta"

        user1 = User.query.filter(User.username == username).first()
        user2 = User.query.filter(User.email == email).first()

        if user1 or user2:
            return "Usuario o email ya existe"

        user = User(username=username, password=password, email=email, age=age, education=education)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Internal server error."

        return "Usuario registrado"
    return render_template("register.html")