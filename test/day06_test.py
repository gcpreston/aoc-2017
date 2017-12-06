import unittest

from aoc.day06 import day06


class TestDay06(unittest.TestCase):

    def test_repeated_redist(self):
        self.assertEqual(day06.repeated_redist([0, 2, 7, 0]), (5, 4))


if __name__ == '__main__':
    unittest.main()