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

        user = User.query.filter(User.email == email).first()

        if not user or not user.password == password:
            return json.dumps({ "sucess": False })

        submit = {
            "email": user.email,
            "password": user.password,
            "name": user.name,
            "lastname": user.last_name,
            "image": user.image,
            "sucess": True
        }

        return json.dumps(submit)
    # return ""

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