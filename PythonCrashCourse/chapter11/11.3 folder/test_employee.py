'''Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.'''

import pytest
from employee import Employee

def test_give_default_raise():
    '''Test that the employee's annual salary will be raised by 5000'''
    employee = Employee('John', 'Doe', 34_000)
    employee.give_raise()
    assert employee.annual_salary == 39_000

def test_give_custom_raise():
    ''' Test that the employee's annual salary will be raised by a custom amount.'''
    employee = Employee('John', 'Doe', 34_000)
    employee.give_raise(10_000)
    assert employee.annual_salary == 44_000

'''
Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass.'''

@pytest.fixture
def employee():
    ''' An instance of an employee'''

    employee = Employee('John', 'Doe', 34_000)
    return employee

def test_give_default_raise(employee):
    '''Test that the employee's annual salary will be raised by 5000'''
    employee.give_raise()
    assert employee.annual_salary == 39_000

def test_give_custom_raise(employee):
    ''' Test that the employee's annual salary will be raised by a custom amount.'''
    employee.give_raise(10_000)
    assert employee.annual_salary == 44_000