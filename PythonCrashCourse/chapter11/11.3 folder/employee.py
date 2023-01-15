'''Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.'''

class Employee:
    '''A instance of an object employee'''

    def __init__(self, first_name, last_name, annual_salary):
        ''' Store all attirbutes of an employee. '''
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, salary_raise=5000):
        ''' Increases an employee's salary by $5_000 or by a certain amount.'''
        self.annual_salary += salary_raise
        

