from city_functions import city_country

# def test_city_country():
#     ''' Will the function accept Edmonton, Canada?'''
#     string = city_country('edmonton', 'canada')
#     assert string == 'Edmonton, Canada'

def test_city_country():
    '''Will the function accept Edmonton, Canada - population: 1 519 000'''

    string_yes_pop = city_country('edmonton', 'canada', 1_519_000)
    string_no_pop = city_country('calgary', 'canada')
    assert string_yes_pop == 'Edmonton, Canada - population: 1519000'
    assert string_no_pop == 'Calgary, Canada'