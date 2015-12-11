def get_one(s):
    l, w, h = [int(x) for x in s.split('x')]
    sides = [l*w, w*h, h*l]
    return 2 * sum(sides) + min(sides)


def get_total(s):
    size_list = s.split()
    return sum([get_one(size) for size in size_list])


def get_one_ribbon(s):
    l, w, h = [int(x) for x in s.split('x')]
    first, second = get_mins([l, w, h])
    return 2 * (first + second) + l * w * h


def get_mins(l):
    max_item = max(l)
    l.remove(max_item)
    return l


def get_total_ribbon(s):
    size_list = s.split()
    return sum([get_one_ribbon(size) for size in size_list])


import unittest


class Test(unittest.TestCase):

    def test_get_total(self):
        self.assertEqual(get_total('1x1x10\n2x3x4'), 58 + 43)

    def test_get_one(self):
        self.assertEqual(get_one('2x3x4'), 58)
        self.assertEqual(get_one('1x1x10'), 43)

    def test_get_one(self):
        self.assertEqual(get_one_ribbon('2x3x4'), 34)
        self.assertEqual(get_one_ribbon('1x1x10'), 14)

unittest.main()
