import unittest

from aoc.day01 import day01


class TestDay01(unittest.TestCase):
    def test_captcha_solution_v1(self):
        self.assertEqual(day01.captcha_solution_v1('1122'), 3)
        self.assertEqual(day01.captcha_solution_v1('1111'), 4)
        self.assertEqual(day01.captcha_solution_v1('1234'), 0)
        self.assertEqual(day01.captcha_solution_v1('91212129'), 9)

    def test_captcha_solution_v2(self):
        self.assertEqual(day01.captcha_solution_v2('1212'), 6)
        self.assertEqual(day01.captcha_solution_v2('1221'), 0)
        self.assertEqual(day01.captcha_solution_v2('123425'), 4)
        self.assertEqual(day01.captcha_solution_v2('123123'), 12)
        self.assertEqual(day01.captcha_solution_v2('12131415'), 4)


if __name__ == '__main__':
    unittest.main()
