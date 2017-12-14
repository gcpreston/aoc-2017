import unittest

from aoc.day09 import day09


class TestDay09(unittest.TestCase):

    def test_score(self):
        self.assertEqual(day09.solve('{}'), (1, 0))
        self.assertEqual(day09.solve('{{{}}}'), (6, 0))
        self.assertEqual(day09.solve('{{},{}}'), (5, 0))
        self.assertEqual(day09.solve('{{{},{},{{}}}}'), (16, 0))
        self.assertEqual(day09.solve('{<a>,<a>,<a>,<a>}'), (1, 4))
        self.assertEqual(day09.solve('{{<ab>},{<ab>},{<ab>},{<ab>}}'), (9, 8))
        self.assertEqual(day09.solve('{{<!!>},{<!!>},{<!!>},{<!!>}}'), (9, 0))
        self.assertEqual(day09.solve('{{<a!>},{<a!>},{<a!>},{<ab>}}'), (3, 17))


if __name__ == '__main__':
    unittest.main()