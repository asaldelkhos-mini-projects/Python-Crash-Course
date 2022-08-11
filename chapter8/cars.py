# exercise 8-14

def car_info(manufacturer, model, **extra_info):
    car['manufacturer'] = manufacturer
    car['model_name'] = model
    return car

car_form = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car_form)    
