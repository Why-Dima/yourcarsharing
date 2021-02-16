from app import app, db
from app.models import Car
from flask import render_template, request


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    car_list = Car.query.all()

    context = {'car_list':car_list}

    return render_template('index.html', **context)

   

@app.route('/auto_detail/<int:car_id>', methods=['GET', 'POST'])
def auto_detail(car_id):
    
    print('test')

    car = Car.query.get(car_id)

    #context = None

    

    #context = {'id': car.id,
     #           'transmission': car.transmission,
      #          'availability': car.availability,
       #         'name_auto': car.name_auto,
        #        'price': car.rent_price,
         #       'auto_description': car.description,
          #      }

    

    return render_template('auto_detail.html', car=car)


@app.route('/rent_car/<int:car_id>', methods=['POST','GET'])
def rent_car(car_id):

    print('test2')
    
    if request.method == 'POST':

        car = Car.query.get(car_id)
        car.availability = 'Свободно' if car.availability else 'Занято'
        print(car)
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

        db.session.add(Car(name_auto = name_auto, rent_price = rent_price, description = description, transmission = transmission))
        db.session.commit()

        context = {'method': 'POST', 
                'name': name_auto,
                'price': rent_price, 
                'description': description,
                'transmission': transmission
                }
        
    

    elif request.method == 'GET':

        context = {
            'method': 'GET',
        }

    
    return render_template('create_auto.html', **context)


@app.route('/rental_log')
def rental_log():
    
    car_list = Car.query.all()

    context = {'car_list': car_list}
    
    
    
    return render_template('/rental_log.html', **context)


@app.route('/del_auto/<int:car_id>', methods = ['POST'])
def del_auto(car_id):
    
    car = Car.query.get(car_id)

    print(car)

    db.session.delete(car)
    db.session.commit()

    return render_template('del_auto.html', car=car)


