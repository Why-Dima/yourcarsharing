from app import db
from datetime import datetime


class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rent_price = db.Column(db.Integer)
    name_auto = db.Column(db.String(128))
    img_url = db.Column(db.String(128))
    img_url2 = db.Column(db.String(128))
    img_url3 = db.Column(db.String(128))
    img_url4 = db.Column(db.String(128))
    transmission = db.Column(db.Boolean, default = True)
    description = db.Column(db.String(128))
    availability = db.Column(db.Boolean, default = True)
    created = db.Column(db.DateTime, default = datetime.now())
    num_book = db.Column(db.Integer, default = 0)
    total_time = db.Column(db.Integer, default = 0)
    total_rent = db.Column(db.Integer, default = 0)

    pr = db.relationship('Journal', backref='car')

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    auto_info = db.Column(db.Integer, db.ForeignKey('car.id'))
    time_begin = db.Column(db.DateTime, default = datetime.now())
    time_end = db.Column(db.DateTime, default = datetime.now())
    total_cost = db.Column(db.Integer, default = 2)

#uselist=False

