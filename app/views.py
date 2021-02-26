from app import app, db
from app.models import Car, Journal
from flask import render_template, request
from datetime import datetime


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    car_list = Car.query.all()

    context = {'car_list':car_list}

    return render_template('index.html', **context)

   

@app.route('/auto_detail/<int:car_id>', methods=['GET', 'POST'])
def auto_detail(car_id):
    
    car = Car.query.get(car_id)

    list_jornal = car.pr

    list_jornals = []

    for jornal in list_jornal:
        id = jornal.id
        car_id = jornal.car_id
        time_begin = jornal.time_begin.strftime("%d.%m.%Y %H:%M:%S")
        time_end = jornal.time_end.strftime("%d.%m.%Y %H:%M:%S")
        total_cost = jornal.total_cost
    
        list_jornals.append({'id':id, 'car_id':car_id, 'time_begin':time_begin, 'time_end':time_end, 'total_cost':total_cost})

    
    return render_template('auto_detail.html', car=car, list_jornals=list_jornals)


@app.route('/rent_car/<int:car_id>', methods=['GET', 'POST'])
def rent_car(car_id):

    car = Car.query.get(car_id)

    journal = Journal.query.all()
    
    if request.method == 'POST':

        
        car.availability = False if car.availability else True
        
        if car.availability == False:
            car.created = datetime.now() 
            time_begin = datetime.now()
            time_end = None
            car.num_book += 1
            db.session.add(Journal(car_id=car_id, time_begin=time_begin, time_end=time_end))
            db.session.commit()
        db.session.commit()
        

    age_seconds = (datetime.now() - car.created).seconds
    car.total_time += age_seconds
    car.total_rent = car.total_time * car.rent_price / 60
    db.session.commit()

    if car.availability == True:
        journal[-1].time_end = datetime.now()
        journal[-1].total_cost = (journal[-1].time_end - car.created).seconds * car.rent_price/60
    
    db.session.commit()

    return render_template('auto_detail.html', car=car)



@app.route('/create_auto', methods=['POST', 'GET'])
def create_auto():
    
    context = None

    if request.method == 'POST':
        
        name_auto = request.form['name']
        rent_price = request.form['price']
        description = request.form['description']
        transmission = True if request.form['transmission'] == " ДА " else False
        img_url = request.form['img_url']
        img_url2 = request.form['img_url2']
        img_url3 = request.form['img_url3']
        img_url4 = request.form['img_url4']

        db.session.add(Car(name_auto = name_auto, rent_price = rent_price, description = description,
         transmission = transmission, img_url = img_url, img_url2 = img_url2, img_url3 = img_url3, img_url4 = img_url4))
        db.session.commit()

        context = {'method': 'POST', 
                'name': name_auto,
                'price': rent_price, 
                'description': description,
                'transmission': transmission,
                'img_url': img_url,
                'img_url2': img_url2,
                'img_url3': img_url3,
                'img_url4': img_url4,
                }
        
    

    elif request.method == 'GET':

        context = {
            'method': 'GET',
        }

    
    return render_template('create_auto.html', **context)


@app.route('/rental_log', methods=['GET', 'POST'])
def rental_log():
    
    car_list = Car.query.all()
    context = {'car_list':car_list}
    
    return render_template('rental_log.html', **context)


@app.route('/del_auto/<int:car_id>', methods = ['POST'])
def del_auto(car_id):
    
    car = Car.query.get(car_id)

    db.session.delete(car)
    db.session.commit()

    return render_template('del_auto.html', car=car)


@app.route('/change_auto/<int:car_id>', methods = ['POST', 'GET'])
def change_auto(car_id):

    car = Car.query.get(car_id)


    if request.method == 'POST':

        new_name = request.form['new_name']
        new_price = request.form['new_price']
        new_description = request.form['new_description']
        new_transmission = True if request.form['new_transmission'] == " ДА " else False
        new_img_url = request.form['new_img_url']
        new_img_url2 = request.form['new_img_url2']
        new_img_url3 = request.form['new_img_url3']
        new_img_url4 = request.form['new_img_url4']

        if new_name:
            car.name_auto = request.form['new_name']
        if new_price:
            car.rent_price = request.form['new_price']
        if new_description:
            car.description = request.form['new_description']
        if new_transmission:
            car.transmission = request.form['new_transmission']
        if new_img_url:
            car.img_url = request.form['new_img_url']
        if new_img_url2:
            car.img_url2 = request.form['new_img_url2']
        if new_img_url3:
            car.img_url3 = request.form['new_img_url3']
        if new_img_url4:
            car.img_url4 = request.form['new_img_url4']
        

        db.session.commit()

    return render_template('change_auto.html', car=car)