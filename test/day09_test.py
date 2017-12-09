import unittest

from aoc.day09 import day09


class TestDay09(unittest.TestCase):

    def test_score(self):
        self.assertEqual(day09.score('{}'), 1)
        self.assertEqual(day09.score('{{{}}}'), 6)
        self.assertEqual(day09.score('{{},{}}'), 5)
        self.assertEqual(day09.score('{{{},{},{{}}}}'), 16)
        self.assertEqual(day09.score('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(day09.score('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(day09.score('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(day09.score('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)


if __name__ == '__main__':
    unittest.main()