import unittest

from aoc.day04 import day04


class TestDay04(unittest.TestCase):

    def test_valid_passphrase_v1(self):
        self.assertEqual(day04.valid_passphrase_v1('aa bb cc dd ee'), True)
        self.assertEqual(day04.valid_passphrase_v1('aa bb cc dd aa'), False)
        self.assertEqual(day04.valid_passphrase_v1('aa bb cc dd aaa'), True)

    def test_valid_passphrase_v2(self):
        self.assertEqual(day04.valid_passphrase_v2('abcde fghij'), True)
        self.assertEqual(day04.valid_passphrase_v2('abcde xyz ecdab'), False)
        self.assertEqual(day04.valid_passphrase_v2('a ab abc abd abf abj'), True)
        self.assertEqual(day04.valid_passphrase_v2('iiii oiii ooii oooi oooo'), True)
        self.assertEqual(day04.valid_passphrase_v2('oiii ioii iioi iiio'), False)


if __name__ == '__main__':
    unittest.main()
