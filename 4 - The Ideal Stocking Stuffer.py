import hashlib


def get_lowest_positive_number(secret_key):
    i = 1
    while i > 0:
        test_string = secret_key + str(i)
        m = hashlib.md5()
        m.update(test_string)
        digest = m.digest()

        if has_five_starting_zeros(digest):
            return i
        i += 1


def has_five_starting_zeros(digest):
    for index in xrange(2):
        if digest[index] != '\x00':
            return False
    if digest[2] > '\x0f':
        return False
    return True


import unittest

class Test(unittest.TestCase):
    def test_get_lowest_positive_number(self):
        self.assertEqual(get_lowest_positive_number('abcdef'), 609043)

# unittest.main()
print get_lowest_positive_number('ckczppom')
