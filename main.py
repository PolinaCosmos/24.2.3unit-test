import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 99,1) == 100


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
         self.calculator.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода')




