from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Login, User
import datetime
import json

def getLogins():
    username = request.args["username"]
    logins = Login.query.filter(Login.username == username).all()

    result = []
    for login in logins:
        result.append({"id": login.id, "username": login.username, "timestamp": str(login.timestamp)})
    
    return json.dumps(result)

def login():
    if request.method == "POST":
        email = request.args.get("email")
        password = request.args.get("password")

        email = User.query.filter(User.email == email).first()

        if not email or not email.password == password:
            return "email o contrasena incorrecta"
        ## newLogin = Login(username=username, timestamp=datetime.datetime.now())

        ##logins = Login.query.filter(Login.timestamp == newLogin.timestamp and Login.username == username).all()

        ##if len(logins) > 3:
           ## return "Se han registrado más de 3 intentos de login, su cuenta ha sido bloqueada hasta mañana"

   ##     try:
     ##       db.session.add(newLogin)
       ##     db.session.commit()
       ## except Exception as err:
         ##   print(err)
         ##   return "Internal server error"

        return "aa"##redirect("/login/viewall?username=" + email)

    return render_template("login.html")

def viewLogins():
    username = request.args["username"]
    logins = Login.query.filter(Login.username == username).all()
    htmlString = ""
    for login in logins:
        htmlString += "id: " + str(login.id) + " timestamp: " + str(login.timestamp) + ". "
    
    return render_template("view.html", htmlString=htmlString)

def submitAsync():
    body = request.get_json()
    username = body["username"]
    password = body["password"]

    user = User.query.filter(User.username == username).first()

    if not username or not username.password == password:
        return json.dumps({"success": False})

    newLogin = User(username=username, timestamp =  datetime.datetime.now())

    try:
        db.session.add(newLogin)
        db.session.commit()
    except Exception as err:
        print(err)
        return json.dumps({"success": False})

    return json.dumps({"success": True})