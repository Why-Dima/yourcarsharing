from app import db
from app.models import Car


name = Car(name_auto = "BMW", rent_price = 7, transmission = True, description = '2,5 литра', img_url = 'static\assets\images\auto\bmw.jpg')

db.session.add(name)

db.session.commit()