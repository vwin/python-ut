import pytest

from src.demo.calculator import Calculator


class TestCalculator():
    @pytest.mark.parametrize("num1, num2, total", [(3, 5, 8), (1, 2, 3), (2, 2, 4)])
    def test_add(self, num1, num2, total):
        c = Calculator()
        result = c.add(num1, num2)
        assert result == total

    @pytest.mark.parametrize("num1, num2, total", [
        pytest.param(5, 1, 4, marks=pytest.mark.passed),
        pytest.param(5, 2, 4, marks=pytest.mark.fail),
        (5, 4, 1)
    ])
    def test_sub(self, num1, num2, total):
        c = Calculator()
        result = c.sub(num1, num2)
        assert result == total


if __name__ == '__main__':
    pytest.main(['test_calculator_pytest_with_parameterize.py'])
