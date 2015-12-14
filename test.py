import unittest
# assembly = __import__("7 - Some Assembly Required")
# from assembly import *
execfile("7 - Some Assembly Required.py")

class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = '''123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i
        '''
        self.wire_signals = {
            'd': 72,
            'e': 507,
            'f': 492,
            'g': 114,
            'h': 65412,
            'i': 65079,
            'x': 123,
            'y': 456
        }

    def test_parse_input(self):
        self.assertEqual(parse_input(self.input_file), self.wire_signals)
