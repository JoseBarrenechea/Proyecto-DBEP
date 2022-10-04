from app import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.Date())

class Review(db.Model):
    id = db.Column(db.String,primary_key=True,autoincrement=True)
    comentary = db.Column(db.String, nullable=False)
    calification = db.Column(db.Integer, nullable=False)

    author = db.Column(db.String, db.ForeignKey('username.dni'), nullable=False)

    comment = db.relationship('Tourist_Place', backref='review')

class Country(db.Model):
    name = db.Column(db.String,primary_key=True)
    description = db.Column(db.String, nullable=False)

    into = db.relationship('City', backref='country')

class City(db.Model):
    name = db.Column(db.String,primary_key=True)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    visits = db.Column(db.Integer, nullable=False)

    ccountry = db.Column(db.String, db.foreignKey('country.name'), nullable=False)

class Tourist_place(db.Model):
    codeid = db.Column(db.String,primary_key=True)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    tour_place = db.Column(db.String, db.ForeignKey('review.id'), nullable=False)

    ddestiny = db.relationship('Travel', backref='tourist_place')


class Plane(db.Model):
    model = db.Column(db.String,primary_key=True)
    columns = db.Column(db.Integer, nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    first_class = db.Column(db.Integer, nullable=False)
    tourist_class = db.Column(db.Integer, nullable=False)
    normal_class = db.Column(db.Integer, nullable=False)

    at = db.relationship('Travel', backref='plane')

class Travel(db.Model):
    id = db.Column(db.String,primary_key=True)
    passengers = db.Column(db.Integer, nullable=False)
    date_departoure = db.Column(db.Datetime, nullable=False)
    hour = db.Column(db.String, nullable=False)

    user_tr = db.Column(db.String, db.ForeignKey('username.dni'), nullable=False)
    destiny = db.Column(db.String, db.ForeignKey('tourist_place.codeid'), nullable=False)
    model_plane = db.Column(db.String, db.ForeignKey('plane.model'), nullable=False)

    descript = db.relationship('Ticket', backref='travel')

class Ticket(db.Model):
    id = db.Column(db.String,primary_key=True)
    classes = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    date_purchased = db.Column(db.Datetime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    seats = db.Column(db.String, nullable=False)

    ttravel = db.Column(db.String, db.ForeignKey('travel.id'), nullable=False)
    payment = db.Column(db.Integer, db.ForeignKey('card.number'), nullable=False)
    user_tk = db.Column(db.String, db.ForeignKey('username.dni'), nullable=False)

class Card(db.Model):
    number = db.Column(db.Integer,primary_key=True)
    method = db.Column(db.String, nullable=False)
    name = db.Column(db.String(35))

    user_c = db.Column(db.String, db.ForeignKey('username.dni'), nullable=False)

    view = db.relationship('Ticket', backref='card')

class User(db.Model):
    dni = db.Column(db.String,primary_key=True)
    image = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,unique=True, nullable=False)
    birthday = db.Column(db.Datetime, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    registration_date = db.Column(db.Datetime, nullable=False)

    reviews = db.relationship('Review', backref='username')
    hold = db.relationship('Travel', backref='username')
    buy = db.relationship('Ticket', backref='username')
    user = db.relationship('Card', backref='username')

    






