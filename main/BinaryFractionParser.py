from main.BinaryFraction import BinaryFraction


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
