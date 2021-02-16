from app import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rent_price = db.Column(db.Integer)
    name_auto = db.Column(db.String(128))
    img_url = db.Column(db.String(128))
    transmission = db.Column(db.Boolean, default = True)
    rent = db.Column(db.String(128))
    description = db.Column(db.String(128))
    availability = db.Column(db.String(128), default = 'Свободно')

    def transmission(self):
        if transmission:
            return True
        else:
            return False