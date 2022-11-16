from unittest import TestCase

from main.BinaryFraction import BinaryFraction
from main.BinaryFractionParser import BinaryFractionParser


class TestBinaryFractionParser(TestCase):

    def test_parse_binary_fraction_with_all_parts(self):
        self.assertEqual(BinaryFraction("0", "101", "0"), BinaryFractionParser.parse_binary_fraction("0.0(101)"))

    def test_parse_binary_fraction_with_only_int(self):
        self.assertEqual(BinaryFraction("101", None, None), BinaryFractionParser.parse_binary_fraction("101"))
