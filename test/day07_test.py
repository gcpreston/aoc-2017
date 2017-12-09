import unittest

from aoc.day07 import day07


class TestDay07(unittest.TestCase):

    def test_parent(self):
        with open('inputs/day07_test_input.txt') as file:
            day07_test_input = [day07.Program(line) for line in file.readlines()]
        self.assertEqual(day07.parent('pbga', day07_test_input).name, 'padx')

    def test_total_weight(self):
        with open('inputs/day07_test_input.txt') as file:
            day07_test_input = [day07.Program(line) for line in file.readlines()]
        self.assertEqual(day07.total_weight(day07.Program('ugml (68) -> gyxo, ebii, jptl'), day07_test_input), 251)


if __name__ == '__main__':
    unittest.main()
