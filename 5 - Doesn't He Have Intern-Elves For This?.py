def is_nice(s):
    len_s = len(s)
    return has_at_least_three_vowels(s) and contains_two_letters_in_a_row(s, len_s) and does_not_have_blacklisted_strings(s, len_s)


def has_at_least_three_vowels(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
        if vowel_count > 2:
            return True
    return False


def contains_two_letters_in_a_row(s, len_s):
    for i in xrange(len_s - 1):
        if s[i] == s[i+1]:
            return True
    return False


def does_not_have_blacklisted_strings(s, len_s):
    blacklist = set(['ab', 'cd', 'pq', 'xy'])
    for i in xrange(len_s - 1):
        current_pair = s[i:i+2]
        if current_pair in blacklist:
            return False
    return True


def is_nice2(s):
    len_s = len(s)
    return twice_without_overlap(s, len_s) and repeat_letter_with_one_char_inbetween(s, len_s)


def twice_without_overlap(s, len_s):
    pair_hash = {}
    for i in xrange(len_s - 1):
        pair = s[i:i+2]
        if pair_hash.get(pair):
            for hash_i in pair_hash[pair]:
                if abs(hash_i - i) > 1:
                    return True
        else:
            pair_hash[pair] = [i]
    return False


def repeat_letter_with_one_char_inbetween(s, len_s):
    for i in xrange(len_s - 2):
        if s[i] == s[i+2]:
            return True
    return False

import unittest


class Test(unittest.TestCase):
    def test_is_nice(self):
        self.assertEqual(is_nice('ugknbfddgicrmopn'), True)
        self.assertEqual(is_nice('aaa'), True)
        self.assertEqual(is_nice('haegwjzuvuyypxyu'), False)
        self.assertEqual(is_nice('dvszwmarrgswjxmb'), False)

    def test_twice_without_overlap(self):
        self.assertEqual(twice_without_overlap('aabcdefgaa', len('aabcdefgaa')), True)
        self.assertEqual(twice_without_overlap('aaa', len('aaa')), False)
        self.assertEqual(twice_without_overlap('xyxy', len('xyxy')), True)

    def test_is_nice2(self):
        self.assertEqual(is_nice2('ieodomkazucvgmuy'), False)
        self.assertEqual(is_nice2('uurcxstgmygtbstg'), False)
        self.assertEqual(is_nice2('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(is_nice2('xxyxx'), True)


# unittest.main()
f = open('input.txt', 'r')
strings = f.read().split()
nice_count = 0
for string in strings:
    if is_nice2(string):
        nice_count += 1
print nice_count
