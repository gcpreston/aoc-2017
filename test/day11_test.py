import unittest

from aoc.day11 import day11


class TestDay11(unittest.TestCase):

    def test_cancel_diagonals(self):
        self.assertEqual(day11.cancel_steps({'nw': 2, 'n': 0, 'ne': 0, 'sw': 0, 's': 0, 'se': 2}),
                         {'nw': 0, 'n': 0, 'ne': 0, 'sw': 0, 's': 0, 'se': 0})
        self.assertEqual(day11.cancel_steps({'nw': 1, 'n': 0, 'ne': 3, 'sw': 2, 's': 0, 'se': 0}),
                         {'nw': 1, 'n': 0, 'ne': 1, 'sw': 0, 's': 0, 'se': 0})

    def test_convert_diagonals(self):
        self.assertEqual(day11.convert_steps({'nw': 2, 'n': 0, 'ne': 2, 'sw': 0, 's': 0, 'se': 0}),
                         {'nw': 0, 'n': 2, 'ne': 0, 'sw': 0, 's': 0, 'se': 0})
        self.assertEqual(day11.convert_steps({'nw': 0, 'n': 0, 'ne': 0, 'sw': 3, 's': 0, 'se': 2}),
                         {'nw': 0, 'n': 0, 'ne': 0, 'sw': 1, 's': 2, 'se': 0})

    def test_steps_away(self):
        self.assertEqual(day11.steps_away(['ne', 'ne', 'ne']), 3)
        self.assertEqual(day11.steps_away(['ne', 'ne', 'sw', 'sw']), 0)
        self.assertEqual(day11.steps_away(['ne', 'ne', 's', 's']), 2)
        self.assertEqual(day11.steps_away(['se', 'sw', 'se', 'sw', 'sw']), 3)


if __name__ == '__main__':
    unittest.main()
