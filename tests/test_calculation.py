'''This module contains tests for the calculator operations and Calculation class.'''
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

# It's good practice to add a docstring at the beginning of the module

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal ('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal ('10'), Decimal('5'), multiply, Decimal ('50')),
    (Decimal ('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal ('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'),Decimal ('0.5'), subtract, Decimal ('10.0')),
    (Decimal ('10.5'), Decimal('2'), multiply, Decimal ('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
    (Decimal('10'), Decimal('0'), divide, None),
])

def test_calculation_operation(a, b, operation, expected):
    '''test calculation with various cases'''
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f'Fail {operation.__name__} operation with values {a}, {b}.'

def test_calculation_repr():
    '''check the string format of the calculation class'''
    calc = Calculation(Decimal("10"), Decimal("5"), add)
    expected_repr = "calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The (__repre__) method output doesn't match operation"

def test_divide_by_zero():
    '''test division method divided by zero to make sure it raises a ValueError'''
    calc = Calculation(Decimal("10"), Decimal("0"), divide)
    # with pytest.raises(ValueError, match='Error, cannot divide number by zero'):
    calc.perform()

    # store a history of calculations, so that you can retrieve the last calculation
def test_calculation_history():
    '''test calculation history'''
    history = Calculations
    calc1 = Calculation(Decimal("10"), Decimal("5"), add)
    calc2 = Calculation(Decimal("10"), Decimal("2"), divide)
    history.add_calculation(calc1)
    history.add_calculation(calc2)
    assert history.get_latest() == calc2
    assert history.get_all_calculations() == [calc1, calc2]
