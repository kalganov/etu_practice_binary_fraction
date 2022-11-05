from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


class Converter:
    ZERO_FRACTION = Fraction(0, 1)

    @staticmethod
    def binary_to_decimal(num):
        k = len(num)
        return sum(map(lambda i: int(num[i]) * (2 ** (k - i - 1)), range(k)))

    def to_decimal_fraction(self, binary_fraction: BinaryFraction):
        decimal_fraction = self.__binary_periodical_part_to_decimal(
            binary_fraction) + self.__binary_non_periodical_part_to_decimal(
            binary_fraction) + self.__binary_int_part_to_decimal(binary_fraction)
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


class BinaryFractionParser:

    @staticmethod
    def parse_binary_fraction(source: str):
        int_part = None
        periodical_part = None
        non_periodical_part = None

        if '.' in source:
            int_part, fraction_part = source.split('.')
            if '(' in fraction_part:
                non_periodical_part, periodical = fraction_part.split("(")
                periodical_part = periodical[:-1]
            else:
                non_periodical_part = fraction_part
        else:
            int_part = source

        return BinaryFraction(int_part, periodical_part, non_periodical_part)


@dataclass(frozen=True)
class BinaryFraction:
    int_part: str | None
    periodical_part: str | None
    non_periodical_part: str | None


if __name__ == '__main__':
    fr = BinaryFractionParser.parse_binary_fraction("1.001(11)")
    converter = Converter()
    print(converter.to_decimal_fraction(fr))
    print(converter)
