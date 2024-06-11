import pytest
import sys
from io import StringIO
import main

# This test function uses parameterization to run multiple tests with different inputs
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8\n"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8\n"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20\n"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5\n"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero\n"),
    ("9", "3", 'unknown', "Unknown operation: unknown\n"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number.\n"),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.\n")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    # Set the command line arguments for the main function
    sys.argv = ['', a_string, b_string, operation_string]
    
    # Call the main function
    main.main()
    
    # Capture the output of the main function
    captured = capsys.readouterr()
    
    # Assert that the captured output matches the expected output
    assert captured.out == expected_string