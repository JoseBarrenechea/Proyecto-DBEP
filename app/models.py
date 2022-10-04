from app import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.Date())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    age = db.Column(db.Integer)
    education = db.Column(db.String(20))

class Review(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    comentary = db.Column(db.String)
    califaction = db.Column(db.Integer)
    author = db.Column(db.Integer)
    city = db.Column(db.String)

class Country(db.Model):
    name = db.Column(db.String,primary_key=True)
    description = db.Column(db.String)

class City(db.Model):
    name = db.Column(db.String,primary_key=True)
    description = db.Column(db.String)
    country = db.Column(db.String)
    image = db.Column(db.String)
    visits = db.Column(db.Integer)

class Tourist_Place(db.Model):
    name = db.Column(db.String,primary_key=True)
    city = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)

class Plane(db.Model):
    model = db.Column(db.String,primary_key=True)
    columns = db.Column(db.Integer)
    rows = db.Column(db.Integer)
    first_class = db.Column(db.Integer)
    tourist_class = db.Column(db.Integer)
    normal_class = db.Column(db.Integer)

class Travel(db.Model):
    code = db.Column(db.String,primary_key=True)
    passengers = db.Column(db.Integer)
    date_departoure = db.Column(db.Date)
    hour = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    plane = db.Column(db.String)

class Ticket(db.Model):
    code = db.Column(db.String,primary_key=True)
    user = db.Column(db.Integer)
    classes = db.Column(db.String)
    names = db.Column(db.String)
    last_names = db.Column(db.String)
    seats = db.Column(db.String)
    travel = db.Column(db.String)
    method = db.Column(db.Integer)

class Credit_Card(db.Model):
    number = db.Column(db.Integer,primary_key=True)
    method = db.Column(db.String)
    user = db.Column(db.Integer)
    name = db.Column(db.String(35))

class Usern(db.Model):
    dni = db.Column(db.Integer,primary_key=True)
    image = db.Column(db.String)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String,unique=True)
    birthday = db.Column(db.Date)
    password = db.Column(db.String(40))
    registration_date = db.Column(db.Date)



    






