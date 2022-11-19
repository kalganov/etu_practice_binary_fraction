from fractions import Fraction
from unittest import TestCase, mock
from unittest.mock import call

from main.BinaryFraction import BinaryFraction
from main.BinaryFractionParser import BinaryFractionParser
from main.Converter import converter
from main.StepikTask import StepikTask


def mock_input_response(*args, **kwargs):
    # if not args[0] == BinaryFraction("0", "0", "0"):
    #     raise ValueError()
    return Fraction(4, 7)


class TestStepikTask(TestCase):

    def test_solve_task(self):
        mock_builtin_function = mock.patch('builtins.input', side_effect=["0.0(101)", "101"])
        # mock_method_on_object = mock.patch.object(converter, "to_decimal_fraction",
        #                                           side_effect=[Fraction(4, 7), Fraction(5, 1)])
        mock_method_on_object = mock.patch.object(converter, "to_decimal_fraction",
                                                  side_effect=mock_input_response)
        mock_static_method = mock.patch.object(BinaryFractionParser, "parse_binary_fraction",
                                               side_effect=[BinaryFraction("0", "101", "0"),
                                                            BinaryFraction("101", None, None)])

        mock_stdout_patch = mock.patch('builtins.print')

        with mock_builtin_function, mock_method_on_object, mock_static_method, mock_stdout_patch as mock_stdout:
            StepikTask.solve_task()

            self.assertIn(call(4, 7), mock_stdout.mock_calls)
