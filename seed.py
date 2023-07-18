from app import app
from models import db, Pet, User, Meetup

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    pet = Pet(
        owner_id=14,
        name="Ben",
        birth_year="2020",
        species="dog",
        breed="husky",
        profile_pic="https://images.wagwalkingweb.com/media/daily_wag/blog_articles/hero/1685787498.877709/fun-facts-about-siberian-huskies-1.png",
        city="chantilly",
        state="virginia",
        country="united states",
        availability="Weekend",
        longitude=2,
        latitude=2,
    )
    db.session.add(pet)
    db.session.commit()
