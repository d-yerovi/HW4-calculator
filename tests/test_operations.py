'''Testing Operations''' 
from decimal import Decimal
# import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

""""""
def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation (Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation (Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation (Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''test division operation'''
    calculation = Calculation(Decimal("10"), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Division operation failed"
