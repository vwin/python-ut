import unittest
from unittest import mock

from src.demo.calculator import Calculator


def multiple(a, b):
    return a * b


def is_error(a, b):
    try:
        return multiple(a, b)
    except Exception as e:
        return -1


class TestCalculator(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        mock_return = 10
        c.add = mock.Mock(return_value=mock_return)

        result = c.add(3, 5)

        self.assertEqual(result, mock_return)

    def test_add_with_side_effect(self):
        c = Calculator()
        mock_return = 10
        # 传递side_effect关键字参数, 会覆盖return_value参数值, 使用真实的add方法测试
        c.add = mock.Mock(return_value=mock_return, side_effect=c.add)

        result = c.add(3, 5)

        self.assertEqual(result, 8)

    @mock.patch.object(Calculator, 'add')
    def test_add_with_annotation(self, mock_add):
        c = Calculator()
        mock_return = 10
        mock_add.return_value = mock_return

        result = c.add(3, 5)

        self.assertEqual(result, mock_return)

    @mock.patch.object(Calculator, 'add')
    def test_add_with_different_return(self, mock_add):
        c = Calculator()
        mock_return = [10, 8]
        mock_add.side_effect = mock_return

        result1 = c.add(3, 5)
        result2 = c.add(3, 5)

        self.assertEqual(result1, mock_return[0])
        self.assertEqual(result2, mock_return[1])

    @mock.patch('test_calculator_mock.multiple')
    def test_function_multiple(self, mock_multiple):
        mock_return = 1
        mock_multiple.return_value = mock_return

        result = multiple(3, 5)

        self.assertEqual(result, mock_return)

    @mock.patch('test_calculator_mock.multiple')
    def test_function_multiple_exception(self, mock_multiple):
        mock_multiple.side_effect = Exception

        result = is_error(3, 5)

        self.assertEqual(result, -1)

    @mock.patch.object(Calculator, 'add')
    @mock.patch('test_calculator_mock.multiple')
    def test_both(self, mock_multiple, mock_add):
        c = Calculator()
        mock_add.return_value = 1
        mock_multiple.return_value = 2

        self.assertEqual(c.add(3, 5), 1)
        self.assertEqual(multiple(3, 5), 2)


if __name__ == '__main__':
    unittest.main()
