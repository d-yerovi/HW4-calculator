from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0: raise ZeroDivisionError("Error, cannot divide number by zero") # Throw exception for divide by zero and test that the exception is thrown
    return a / b