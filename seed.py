from app import app
from models import db, Pet, User, Meetup

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    pet = Pet()
    db.session.add(pet)
    db.session.commit()

    meetup = Meetup(
        user_id=1,
        pet_id=1,
        venue="my home",
        street_address="43212 Center St",
        city="Chantilly",
        state="Virginia",
        country="US",
    )

    db.session.add(meetup)
    db.session.commit()
