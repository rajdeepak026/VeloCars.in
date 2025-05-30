from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile_no = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False, default="user")  # "user" or "admin"