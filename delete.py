from app import app
from models import db, Pet, User, Meetup

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    pets = Pet.query.all()
    # meetups = Meetup.query.all()

    for pet in pets:
        db.session.delete(pet)

    # for meetup in meetups:
    #     db.session.delete(meetup)
    db.session.commit()
