# Import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import validates

# Initialize our db
db = SQLAlchemy()


class Pet(db.Model, SerializerMixin):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)


class Owner(db.Model, SerializerMixin):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True)


class Meetup(db.Model, SerializerMixin):
    __tablename__ = "meetups"

    id = db.Column(db.Integer, primary_key=True)
