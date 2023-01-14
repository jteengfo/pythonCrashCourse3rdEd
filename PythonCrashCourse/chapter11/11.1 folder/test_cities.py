from city_functions import city_country

def test_city_country():
    ''' Will the function accept Edmonton, Canada?'''
    string = city_country('edmonton', 'canada')
    assert string == 'Edmonton, Canada'