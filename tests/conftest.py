# tests/conftest.py
"""
Conftest module for calculator tests
"""
from decimal import Decimal
from faker import Faker
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

fake = Faker()  # Create a Faker instance

def pytest_addoption(parser):
    """Add a pytest option to specify the number of records to generate"""
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of records to generate")

@pytest.fixture
def num_records_to_generate(request):
    """Return the number of records to generate"""
    return request.config.getoption("--num_records")

@pytest.fixture(params=range(1))
def records(request):
    """Generate records for testing calculation operations"""
    num_records = num_records_to_generate(request)
    for _ in range(num_records):
        a = Decimal(str(fake.pydecimal(left_digits=5, right_digits=2)))
        b = Decimal(str(fake.pydecimal(left_digits=5, right_digits=2)))
        operation = fake.random_element(elements=(add, subtract, multiply, divide))
        if operation == 'divide' and b == (0):
            b = Decimal('1')
        expected = {
            add: lambda a, b: a + b,
            subtract: lambda a, b: a - b,
            multiply: lambda a, b: a * b,
            divide: lambda a, b: a / b if b != 0 else float('inf'),
        }[operation](a, b)
        yield a, b, operation, expected


def test_calculation_operations(calculation_records):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        records (tuple): 
        A tuple containing the operands 'a' and 'b', the operation, and the expected result.
    """
    a, b, operation, expected = calculation_records
    # Create a Calculation instance with the provided operands and operation.
    calc = Calculation(a, b, operation)
    # Perform the operation and assert that the result matches the expected value.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"
