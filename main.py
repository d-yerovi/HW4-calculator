import sys
# Import the sys module to access command-line arguments
from calculator import Calculator
# Import the Calculator class from the calculator module
from decimal import Decimal, InvalidOperation
# Import the Decimal class and InvalidOperation exception from the decimal module

def calculate_and_print(a, b, operation_name):
    """
    Calculate the result of a mathematical operation and print the result.

    Args:
        a (str): The first number as a string
        b (str): The second number as a string
        operation_name (str): The name of the operation to perform (add, subtract, multiply, divide)
    """
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }
    # Map operation names to their corresponding Calculator class methods

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        # Convert input strings to Decimal objects
        result = operation_mappings.get(operation_name) 
        # Get the Calculator method corresponding to the operation name
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
            # Perform the operation and print the result
        else:
            print(f"Unknown operation: {operation_name}")
            # Handle unknown operations
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        # Handle invalid number inputs
    except ZeroDivisionError:
        print("Error: Division by zero.")
        # Handle division by zero errors
    except Exception as e: 
        # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    """
    The main entry point of the program.
    """
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        # Print usage instructions if the command-line arguments are invalid
        sys.exit(1)
        # Exit the program with a non-zero status code
    
    _, a, b, operation = sys.argv
    # Unpack the command-line arguments
    calculate_and_print(a, b, operation)
    # Call the calculate_and_print function with the command-line arguments

if __name__ == '__main__':
    # Guard clause to ensure the main function is only executed when the script is run directly
    main()