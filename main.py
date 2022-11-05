from fractions import Fraction


class BinaryFraction:

    def __init__(self, source: str):
        self.__int_part = None
        self.__periodical = None
        self.__non_periodical = None

        if '.' in source:
            self.__int_part, fraction_part = source.split('.')
            if '(' in fraction_part:
                self.__non_periodical, periodical = fraction_part.split("(")
                self.__periodical = periodical[:-1]
            else:
                self.__non_periodical = fraction_part
        else:
            self.__int_part = source

    def __repr__(self):
        return f"{self.__int_part}.{self.__non_periodical}({self.__periodical})"

    @staticmethod
    def binary_to_decimal(num):
        k = len(num)
        return sum(map(lambda i: int(num[i]) * (2 ** (k - i - 1)), range(k)))

    def to_decimal_fraction(self):
        return self.__periodical_part_to_decimal() + \
               self.__non_periodical_part_to_decimal() + \
               self.__int_part_to_decimal()

    def __int_part_to_decimal(self):
        if self.__int_part is None:
            return Fraction(0, 1)
        int_part_len = len(self.__int_part)
        a = 0
        for i, el in enumerate(self.__int_part):
            a += int(el) * 2 ** (int_part_len - 1 - i)
        return Fraction(a)

    def __non_periodical_part_to_decimal(self):
        if self.__non_periodical is None:
            return Fraction(0, 1)
        k = len(self.__non_periodical)
        a = self.binary_to_decimal(self.__non_periodical)
        b = 2 ** k
        return Fraction(a, b)

    def __periodical_part_to_decimal(self):
        if self.__periodical is None:
            return Fraction(0, 1)
        k = len(self.__periodical)
        a = self.binary_to_decimal(self.__periodical)
        b = (2 ** k - 1) * 2 ** len(self.__non_periodical)
        return Fraction(a, b)


if __name__ == '__main__':
    res = BinaryFraction("1.001").to_decimal_fraction()
    if res.denominator == 1:
        print(res.numerator)
    else:
        print(res.numerator / res.denominator)
