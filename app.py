from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate

from flask_restful import Api, Resource

from werkzeug.exceptions import NotFound

from models import db, Pet, Owner, Meetup

app = Flask(__name__)

# 1. Import CORS from flask_cors, invoke it with `app` as an argument

from flask_cors import CORS

CORS(app)
# 2. Start up the server and client then navigate to client/src/App.js

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///petpals.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False  # configures JSON responses to print on indented lines

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
# Views go here!

if __name__ == "__main__":
    app.run(port=5555, debug=True)
