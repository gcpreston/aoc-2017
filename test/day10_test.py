import unittest

from aoc.day10 import day10


class TestDay10(unittest.TestCase):

    def test_part1(self):
        part1_data = day10.solve_part1([3, 4, 1, 5], 0, 0, list(range(5)), n=5)
        self.assertEqual(part1_data[0][0] * part1_data[0][1], 12)

    def test_xor_map(self):
        self.assertEqual(day10.xor_map([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), 64)

    def test_part2(self):
        self.assertEqual(day10.solve_part2(''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(day10.solve_part2('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(day10.solve_part2('1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(day10.solve_part2('1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')


if __name__ == '__main__':
    unittest.main()