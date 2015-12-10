def get_floor(s):
    opening_paren_count = 0
    closing_paren_count = 0
    for token in s:
        if token == '(':
            opening_paren_count += 1
        else:
            closing_paren_count += 1
    difference = opening_paren_count - closing_paren_count
    return difference


import unittest

class Test(unittest.TestCase):

    def test_get_floor(self):
        self.assertEqual(get_floor('(())'), 0)
        self.assertEqual(get_floor('()()'), 0)
        self.assertEqual(get_floor('))((((('), 3)
        self.assertEqual(get_floor('(()(()('), 3)
        self.assertEqual(get_floor(''), 0)
        self.assertEqual(get_floor(')))'), -3)
