import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplication(self):
        assert self.calc.multiplication(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction(self):
        assert self.calc.subtraction(self,10,5) == 5

    def test_addition(self):
        assert self.calc.addition(self,5,5) == 10

