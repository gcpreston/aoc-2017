import unittest

from aoc.day12 import day12


class TestDay12(unittest.TestCase):

    def test_part1(self):
        contents = []
        with open('inputs/day12_test_input.txt') as file:
            for line in file.readlines():
                fixed_line = line.replace('<->', '').replace(',', '')
                contents.append([int(n) for n in fixed_line.split()])

        day12_test_input = {}
        for line in contents:
            day12_test_input[line[0]] = line[1:]

        self.assertEqual(len(day12.connected(0, day12_test_input)), 6)

    def test_part2(self):
        contents = []
        with open('inputs/day12_test_input.txt') as file:
            for line in file.readlines():
                fixed_line = line.replace('<->', '').replace(',', '')
                contents.append([int(n) for n in fixed_line.split()])

        day12_test_input = {}
        for line in contents:
            day12_test_input[line[0]] = line[1:]

        self.assertEqual(len(day12.get_groups(day12_test_input)), 2)


if __name__ == '__main__':
    unittest.main()