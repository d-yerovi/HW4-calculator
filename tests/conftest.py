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
    # Add a command-line option to specify the number of records to generate
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of records to generate")

@pytest.fixture
def num_records_to_generate(request):
    """Return the number of records to generate"""
    # Get the number of records to generate from the pytest command-line option
    return request.config.getoption("--num_records")

@pytest.fixture
def records(num_records_to_generate):
    """Generate records for testing calculation operations"""
    result = []
    for _ in range(num_records_to_generate):
        # Generate two random decimal numbers
        a = Decimal(str(fake.pydecimal(left_digits=5, right_digits=2)))
        b = Decimal(str(fake.pydecimal(left_digits=5, right_digits=2)))
        operation = fake.random_element(elements=(add, subtract, multiply, divide))
        if operation == 'divide' and b == (0):
            b = Decimal('1')
        # Calculate the expected result based on the selected operation
        expected = {
            add: lambda a, b: a + b,
            subtract: lambda a, b: a - b,
            multiply: lambda a, b: a * b,
            divide: lambda a, b: a / b if b != 0 else float('inf'),
        }[operation](a, b)
        # Append the generated record to the result list
        result.append((a, b, operation, expected))
    return result


def test_calculation_operations(records):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    """
    for record in records:
        # Unpack the calculation record
        a, b, operation, expected = record
        # Create a Calculation instance with the provided operands and operation.
        calc = Calculation(a, b, operation)
        # Perform the operation and assert that the result matches the expected value.
        assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"
