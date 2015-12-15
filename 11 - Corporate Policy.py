alphabet = 'abcdefghijklmnopqrstuvwxyz'
blacklist = set(['i', 'o', 'l'])


def make_alphabet_dict():
    index = 1
    d = {}
    for char in alphabet:
        d[char] = index
        index += 1
    return d


def one_increasing_straight(s):
    len_s = len(s)
    for char_index in xrange(len_s - 2):
        if s[char_index: char_index + 3] in alphabet:
            return True
    return False


def contains_letter_in_blacklist(s):
    for char in s:
        if char in blacklist:
            return True
    return False


def contains_two_different_nonoverlapping_pairs(s):
    pairs = 0
    char_index = 0
    while char_index < len(s) - 1:
        if s[char_index] == s[char_index + 1]:
            pairs += 1
            char_index += 2
            if pairs > 1:
                return True
        else:
            char_index += 1
    return False


def passes_all_rules(s):
    return one_increasing_straight(s) and not contains_letter_in_blacklist(s) and contains_two_different_nonoverlapping_pairs(s)


def increment_password(s, alphabet_dict):
    new_password = [ alphabet_dict[x] for x in s ]
    changed = False
    index = -1
    while not changed:
        if new_password[index] < 26:
            new_password[index] += 1
            for i in xrange(index + 1, 0):
                new_password[i] = 1
            changed = True
        else:
            index -= 1
    return ''.join([ alphabet[x - 1] for x in new_password ])


def find_next_password(original_password):
    alphabet_dict = make_alphabet_dict()
    next_password = increment_password(original_password, alphabet_dict)
    while not passes_all_rules(next_password):
        next_password = increment_password(next_password, alphabet_dict)
    return next_password


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.alphabet_dict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}

    def test_one_increasing_straight(self):
        self.assertEqual(one_increasing_straight('abc'), True)
        self.assertEqual(one_increasing_straight(''), False)
        self.assertEqual(one_increasing_straight('acsabcdf'), True)
        self.assertEqual(one_increasing_straight('ghjaabcc'), True)

    def test_contains_letter_in_blacklist(self):
        self.assertEqual(contains_letter_in_blacklist(''), False)
        self.assertEqual(contains_letter_in_blacklist('sdflskjdf'), True)
        self.assertEqual(contains_letter_in_blacklist('abcdffaa'), False)
        self.assertEqual(contains_letter_in_blacklist('ghjaabcc'), False)

    def test_contains_two_different_nonoverlapping_pairs(self):
        self.assertEqual(contains_two_different_nonoverlapping_pairs(''), False)
        self.assertEqual(contains_two_different_nonoverlapping_pairs('sdflskjdf'), False)
        self.assertEqual(contains_two_different_nonoverlapping_pairs('abcdffaa'), True)
        self.assertEqual(contains_two_different_nonoverlapping_pairs('ghjaabcc'), True)

    def test_passes_all_rules(self):
        self.assertEqual(passes_all_rules('hijklmmn'), False)
        self.assertEqual(passes_all_rules('abcdffaa'), True)
        self.assertEqual(passes_all_rules('ghjaabcc'), True)

    def test_increment_password(self):
        self.assertEqual(increment_password('xx', self.alphabet_dict), 'xy')
        self.assertEqual(increment_password('xz', self.alphabet_dict), 'ya')

    def test_find_next_password(self):
        self.assertEqual(find_next_password('abcdefgh'), 'abcdffaa')

unittest.main()
print find_next_password('cqjxjnds')
print find_next_password('cqjxxyzz')
