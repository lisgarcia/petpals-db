# Import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
import os

# Initialize our db
db = SQLAlchemy()

bcrypt = Bcrypt()


class Pet(db.Model, SerializerMixin):
    __tablename__ = "pets"

    serialize_rules = (
        "-user.pet",
        "-user.pets",
        "-user.meetups",
        "-meetups.pet",
        "-meetups_attending",
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    name = db.Column(db.String)
    birth_year = db.Column(db.Integer)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    profile_pic = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    availability = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    meetups = db.relationship("Meetup", backref="pet", cascade="all, delete-orphan")


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = (
        "-meetups.user",
        "-_password_hash",
        "-pets.user",
        "-pets.meetups",
        "-meetups_attending",
        "-meetups.pet",
        "-meetups.attendees",
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    email = db.Column(db.String)
    profile_pic = db.Column(db.String)

    meetups = db.relationship("Meetup", backref="user", cascade="all, delete-orphan")

    pets = db.relationship("Pet", backref="user", cascade="all, delete-orphan")

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    def __repr__(self):
        return f"<User {self.username}>"


class MeetupAttendee(db.Model, SerializerMixin):
    __tablename__ = "meetup_attendees"
    meetup_id = db.Column(
        "meetup_id",
        db.Integer,
        db.ForeignKey("meetups.id", ondelete="CASCADE"),
        primary_key=True,
    )
    attendee_id = db.Column(
        "pet_id", db.Integer, db.ForeignKey("pets.id"), primary_key=True
    )


class Meetup(db.Model, SerializerMixin):
    __tablename__ = "meetups"

    serialize_rules = (
        "-user.meetups",
        "-pet.meetups",
        "-pet.attendees",
        "-user.pets",
        "-attendees.meetups_attending",
        "-user.meetups_attending",
        "-pet.meetups_attending",
        "-pet.user",
        "-attendees.pet",
        "-attendees.user",
        "-meetup_attendees.meetup_id",
        "-meetup_attendees.attendee_id",
        "-pet.user",
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"))

    title = db.Column(db.String)
    details = db.Column(db.String)

    venue = db.Column(db.String)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)

    longitude = db.Column(db.String)
    latitude = db.Column(db.String)

    date = db.Column(db.String)
    time = db.Column(db.String)

    image = db.Column(db.String)

    # attendees = db.relationship(
    #     "Pet", secondary=MeetupAttendee.__tablename__, backref="meetups_attending"
    # )
