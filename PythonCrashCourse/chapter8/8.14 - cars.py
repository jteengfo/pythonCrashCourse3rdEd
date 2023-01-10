'''
Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:


car = make_car('subaru', 'outback', color='blue', tow_package=True)


Print the dictionary that’s returned to make sure all the information was
stored correctly.
'''

def make_car(manufacturer, model_name, **details):

    # make a car dict

    car_dict = {
        'manufacturer' : manufacturer,
        'model name': model_name,
    }

    for detail, value in details.items():
        car_dict[detail] = value

    return car_dict


car1 = make_car('tesla', 'model 3', color = 'olive', fsd_package = True, range_type = 'long range')
print(car1)