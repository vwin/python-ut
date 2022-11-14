import pytest

from src.demo.calculator import Calculator


@pytest.fixture()
def set_up():
    print("[pytest with fixture] start")
    yield
    print("[pytest with fixture] end")


class TestCalculator():
    def test_add(self, set_up):
        c = Calculator()
        result = c.add(3, 5)
        assert result == 8

    def test_sub(self, set_up):
        c = Calculator()
        result = c.sub(10, 5)
        assert result == 5

    @pytest.mark.usefixtures("set_up")
    def test_mul(self):
        c = Calculator()
        result = c.mul(5, 7)
        assert result == 35

    @pytest.mark.usefixtures("set_up")
    def test_div(self):
        c = Calculator()
        result = c.div(10, 5)
        assert result == 2


if __name__ == '__main__':
    pytest.main(['-s', 'test_calculator_pytest_with_fixture.py'])
