from app import app
from models import db, Pet, User

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
if __name__ == "__main__":
    with app.app_context():
        item_to_delete = User.query.filter(User.id == 14).first()
        db.session.delete(item_to_delete)
        db.session.commit()
