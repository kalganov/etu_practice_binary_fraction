from __future__ import annotations

from dataclasses import dataclass

from Converter import converter


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
    print(converter.to_decimal_fraction(fr))
    print(converter)
