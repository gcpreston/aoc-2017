import unittest

from aoc.day02 import day02


class TestDay02(unittest.TestCase):

    def test_checksum(self):
        spreadsheet = [[5, 1, 9, 5],
                       [7, 5, 3],
                       [2, 4, 6, 8]]
        self.assertEqual(day02.checksum(spreadsheet), 18)

    def test_div_sum(self):
        spreadsheet = [[5, 9, 2, 8],
                       [9, 4, 7, 3],
                       [3, 8, 6, 5]]
        self.assertEqual(day02.div_sum(spreadsheet), 9)


if __name__ == '__main__':
    unittest.main()