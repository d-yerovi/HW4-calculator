'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''test addition'''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''test substraction'''
    assert Calculator.subtract(2,2) == 0

def test_multiplication():
    '''test multiplication'''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''test division'''
    assert Calculator.divide(2,2) == 1
