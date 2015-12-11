def get_floor(s):
    floor_count = 0
    for token in s:
        if token == '(':
            floor_count += 1
        else:
            floor_count -= 1
    return floor_count


def get_basement_position(s):
    floor_count = 0
    for token_index in xrange(len(s)):
        if s[token_index] == '(':
            floor_count += 1
        else:
            floor_count -= 1
        if floor_count < 0:
            return token_index + 1


import unittest

class Test(unittest.TestCase):

    def test_get_floor(self):
        self.assertEqual(get_floor('(())'), 0)
        self.assertEqual(get_floor('()()'), 0)
        self.assertEqual(get_floor('))((((('), 3)
        self.assertEqual(get_floor('(()(()('), 3)
        self.assertEqual(get_floor(''), 0)
        self.assertEqual(get_floor(')))'), -3)

    def test_get_basement_position(self):
        self.assertEqual(get_basement_position(')'), 1)
        self.assertEqual(get_basement_position('()())'), 5)
        self.assertEqual(get_basement_position('((()'), None)

unittest.main()
