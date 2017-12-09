import unittest

from aoc.day08 import day08


class TestDay08(unittest.TestCase):

    def test_largest_register(self):
        with open('inputs/day08_test_input.txt') as file:
            day08_test_input = [line.split() for line in file.readlines()]
        self.assertEqual(day08.largest_register(day08_test_input), 1)

    def test_register_max(self):
        with open('inputs/day08_test_input.txt') as file:
            day08_test_input = [line.split() for line in file.readlines()]
        self.assertEqual(day08.register_max(day08_test_input), 10)


if __name__ == '__main__':
    unittest.main()