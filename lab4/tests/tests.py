import unittest

from logics.get_data import get_data
from logics.main import get_number_of_possible_ways


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.first_dataset = get_data(1)
        self.first_width = self.first_dataset['width']
        self.first_height = self.first_dataset['height']
        self.first_matrix = self.first_dataset['matrix']
        self.first_chars = self.first_dataset['chars']
        self.first_exits = (0, self.first_height - 1)

        self.second_dataset = get_data(2)
        self.second_width = self.second_dataset['width']
        self.second_height = self.second_dataset['height']
        self.second_matrix = self.second_dataset['matrix']
        self.second_chars = self.second_dataset['chars']
        self.second_exits = (0, self.second_height - 1)

        self.third_dataset = get_data(3)
        self.third_width = self.third_dataset['width']
        self.third_height = self.third_dataset['height']
        self.third_matrix = self.third_dataset['matrix']
        self.third_chars = self.third_dataset['chars']
        self.third_exits = (0, self.third_height - 1)

    def test_first_case(self):
        self.assertEqual(
            get_number_of_possible_ways(
                width=self.first_width,
                height=self.first_height,
                matrix=self.first_matrix,
                exits=self.first_exits,
                chars=self.first_chars
            ), 2)

    def test_second_case(self):
        self.assertEqual(
            get_number_of_possible_ways(
                width=self.second_width,
                height=self.second_height,
                matrix=self.second_matrix,
                exits=self.second_exits,
                chars=self.second_chars
            ), 2)

    def test_third_case(self):
        self.assertEqual(
            get_number_of_possible_ways(
                width=self.third_width,
                height=self.third_height,
                matrix=self.third_matrix,
                exits=self.third_exits,
                chars=self.third_chars
            ), 201684)