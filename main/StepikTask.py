from main.BinaryFractionParser import BinaryFractionParser
from main.Converter import converter


class StepikTask:

    @staticmethod
    def solve_task():
        source = input()
        binary_fraction = BinaryFractionParser.parse_binary_fraction(source)
        decimal_fraction = converter.to_decimal_fraction(binary_fraction)
        print(decimal_fraction.numerator, decimal_fraction.denominator)
