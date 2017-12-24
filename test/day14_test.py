import unittest

from aoc.day14 import day14


class TestDay14(unittest.TestCase):

    def test_square_count(self):
        self.assertEqual(day14.square_count('flqrgnkx'), 8108)

    def test_region_count(self):
        self.assertEqual(day14.region_count('flqrgnkx'), 1242)


if __name__ == '__main__':
    unittest.main()