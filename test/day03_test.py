import unittest

from aoc.day03 import day03


class TestDay03(unittest.TestCase):

    def test_steps(self):
        self.assertEqual(day03.steps(1), 0)
        self.assertEqual(day03.steps(12), 3)
        self.assertEqual(day03.steps(23), 2)
        self.assertEqual(day03.steps(1024), 31)


if __name__ == '__main__':
    unittest.main()