import unittest

from aoc.day05 import day05


class TestDay05(unittest.TestCase):

    def test_steps_to_exit_v1(self):
        self.assertEqual(day05.steps_to_exit_v1([0, 3, 0, 1, -3]), 5)

    def test_steps_to_exit_v2(self):
        self.assertEqual(day05.steps_to_exit_v2([0, 3, 0, 1, -3]), 10)


if __name__ == '__main__':
    unittest.main()
