from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation # Store the operation function

    @staticmethod
    def insert_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        '''perform the calculation stored'''
        try:
            return self.operation(self.a, self.b)
        except ZeroDivisionError: # Throw exception for divide by zero and test that the exception is thrown
            return None
        # return self.operation(self.a, self.b)
    
    def __repr__(self):
        '''return a representation of the calculation'''
        return f'calculation({self.a}, {self.b}, {self.operation.__name__})'

    '''def get_result(self) :
        # Call the stored operation with a and b
        return self.operation(self.a, self. b)'''