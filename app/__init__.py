from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__,static_url_path='', 
            static_folder='static')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../yourcarsharing.sqlite"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views
from app import models