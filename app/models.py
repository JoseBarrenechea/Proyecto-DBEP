from app import db

class User(db.Model):
    __tablename__ = "user"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni = db.Column(db.Integer, unique=True, nullable=False)

    email = db.Column(db.String,nullable=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    image = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    registration_date = db.Column(db.Date, nullable=False)

    reviews = db.relationship("Review", backref="user")
    hold = db.relationship("Travel", backref="user")
    buy = db.relationship("Ticket", backref="user")
    userr = db.relationship("Card", backref="user")


class Card(db.Model):
    __tablename__ = "card"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer,unique=True, nullable=False)

    method = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    user_c = db.Column(db.Integer, db.ForeignKey("user.dni"), nullable=False)

    view = db.relationship("Ticket", backref="card")

class Country(db.Model):
    __tablename__ = "country"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String,unique=True, nullable=False)
    
    description = db.Column(db.String, nullable=False)

    into = db.relationship("City", backref="country")

class Login(db.Model):
    __tablename__ = "login"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String, nullable=True)
    timestamp = db.Column(db.Date, nullable=True)

class Plane(db.Model):
    __tablename__ = "plane"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String,unique=True, nullable=False)
    
    columns = db.Column(db.Integer, nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    
    # Cantidad de asientos por clase
    first_class = db.Column(db.Integer, nullable=False)
    tourist_class = db.Column(db.Integer, nullable=False)
    normal_class = db.Column(db.Integer, nullable=False)

    at = db.relationship("Travel", backref="plane")


class Review(db.Model):
    __tablename__ = "review"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    
    comentary = db.Column(db.String, nullable=False)
    calification = db.Column(db.Integer, nullable=False)

    dni = db.Column(db.Integer, db.ForeignKey("user.dni"), nullable=False)

    comment = db.relationship("Tourist_place", backref="review")

class Tourist_place(db.Model):
    __tablename__ = "tourist_place"
    # __table_args__ = {'schema': 'proyectodbp'}
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)

    tour_place = db.Column(db.Integer, db.ForeignKey("review.id"), nullable=False)

    ddestiny = db.relationship("Travel", backref="tourist_place")

class City(db.Model):
    __tablename__ = "city"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String,unique=True, nullable=False)

    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    visits = db.Column(db.Integer, nullable=False)

    ccountry = db.Column(db.String, db.ForeignKey("country.name"), nullable=False)

class Travel(db.Model):
    __tablename__ = "travel"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)

    passengers = db.Column(db.Integer, nullable=False)
    date_departoure = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Time, nullable=False)

    user_tr = db.Column(db.Integer, db.ForeignKey("user.dni"), nullable=False)
    destiny = db.Column(db.Integer, db.ForeignKey("tourist_place.id"), nullable=False)
    model_plane = db.Column(db.String, db.ForeignKey("plane.model"), nullable=False)

    descript = db.relationship("Ticket", backref="travel")

class Ticket(db.Model):
    __tablename__ = "ticket"
    # __table_args__ = {'schema': 'proyectodbp'}

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    
    classes = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    date_purchased = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    seats = db.Column(db.String, nullable=False)

    ttravel = db.Column(db.Integer, db.ForeignKey("travel.id"), nullable=False)
    payment = db.Column(db.Integer, db.ForeignKey("card.number"), nullable=False)
    user_tk = db.Column(db.Integer, db.ForeignKey("user.dni"), nullable=False)

class Infovuelos():
    _tablename_ = "infovuelos"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    origin = db.Column(db.String,nullable =True)
    destiny = db.Column(db.String,nullable =True)

    day = db.Column(db.String,nullable=True)
    hour = db.Column(db.Time,nullable = True)
    model_plane = db.Column(db.String,nullable=True)
    price = db.Column(db.Integer,nullable=True)
