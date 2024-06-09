from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add calculation to the history"""
        cls.history.append(calculation) 
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Retrieve entire history of calculations'''
        return cls.history 
    
    @classmethod
    def clear_history(cls):
        '''Clear the historv of calculations'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''get the latest calculation or return none if there is no history'''
        cls._latest = cls.history[-1]
        if cls._latest: return cls._latest 
        else: return None

    @classmethod
    def get_all_calculations(self):
        '''Returns a list of all Calculation objects in the history.'''
        return self.history

    @classmethod 
    def search_operation(cls, operation_name: str) -> List[Calculation]:
        '''seach for calculation by operation name'''
        return [calc for calc in cls.history if calc.operation_name == operation_name]