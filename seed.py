from app import app
from models import db, Pet, User

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
with app.app_context():
    print("Deleting existing pets...")
    Pet.query.delete()
    print("Deleting existing owners...")
    User.query.delete()

    db.session.commit()
