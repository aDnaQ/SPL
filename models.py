# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Parkplatz(db.Model):
    __tablename__ = 'parkplatz'

    ParkplatzID = db.Column(db.Integer, primary_key=True, unique=True)
    besetzt = db.Column(db.Integer)
