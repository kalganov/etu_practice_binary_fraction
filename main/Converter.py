from fractions import Fraction

from main import BinaryFraction


class Converter:
    ZERO_FRACTION = Fraction(0, 1)

    def __init__(self):
        self.__cache = {}

    @staticmethod
    def binary_to_decimal(num):
        k = len(num)
        return sum(map(lambda i: int(num[i]) * (2 ** (k - i - 1)), range(k)))

    def to_decimal_fraction(self, binary_fraction: BinaryFraction):
        if binary_fraction in self.__cache:
            return self.__cache[binary_fraction]

        decimal_fraction = self.__binary_periodical_part_to_decimal(
            binary_fraction) + self.__binary_non_periodical_part_to_decimal(
            binary_fraction) + self.__binary_int_part_to_decimal(binary_fraction)

        self.__cache[binary_fraction] = decimal_fraction

        return decimal_fraction

    def __binary_int_part_to_decimal(self, binary_fraction: BinaryFraction):
        if binary_fraction.int_part is None:
            return Converter.ZERO_FRACTION
        int_part_len = len(binary_fraction.int_part)
        a = 0
        for i, el in enumerate(binary_fraction.int_part):
            a += int(el) * 2 ** (int_part_len - 1 - i)
        return Fraction(a)

    def __binary_non_periodical_part_to_decimal(self, binary_fraction: BinaryFraction):
        if binary_fraction.non_periodical_part is None:
            return Converter.ZERO_FRACTION
        k = len(binary_fraction.non_periodical_part)
        a = self.binary_to_decimal(binary_fraction.non_periodical_part)
        b = 2 ** k
        return Fraction(a, b)

    def __binary_periodical_part_to_decimal(self, binary_fraction: BinaryFraction):
        if binary_fraction.periodical_part is None:
            return Converter.ZERO_FRACTION
        k = len(binary_fraction.periodical_part)
        a = self.binary_to_decimal(binary_fraction.periodical_part)
        b = (2 ** k - 1) * 2 ** len(binary_fraction.periodical_part)
        return Fraction(a, b)


converter = Converter()
