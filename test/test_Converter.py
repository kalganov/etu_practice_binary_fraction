from unittest import TestCase

from main.Converter import Converter


class TestConverter(TestCase):

    def setUp(self) -> None:
        self.converter = Converter()

    def test_binary_to_decimal(self):
        self.assertEqual(self.converter.binary_to_decimal("101"), 5)
