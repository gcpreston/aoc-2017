import unittest

from aoc.day13 import day13


class TestDay13(unittest.TestCase):

    def test_severity(self):
        with open('inputs/day13_test_input.txt') as file:
            lines = file.readlines()
            deepest = int(lines[-1].split(': ')[0])
            day13_test_input = [0 for _ in range(deepest + 1)]
            for line in lines:
                data = [int(n) for n in line.split(': ')]
                day13_test_input[data[0]] = data[1]

        self.assertEqual(day13.severity(day13_test_input), 24)

    def test_delay(self):
        with open('inputs/day13_test_input.txt') as file:
            lines = file.readlines()
            deepest = int(lines[-1].split(': ')[0])
            day13_test_input = [0 for _ in range(deepest + 1)]
            for line in lines:
                data = [int(n) for n in line.split(': ')]
                day13_test_input[data[0]] = data[1]

        self.assertEqual(day13.delay(day13_test_input), 10)


if __name__ == '__main__':
    unittest.main()