def look_and_say(num):
    len_num = len(num)
    num_index = 0
    output = ''
    while num_index < len_num:

        current_num = num[num_index]
        current_count = 1
        while num_index + 1 < len_num and num[num_index + 1] == current_num:
            current_count += 1
            num_index += 1

        output += str(current_count) + str(current_num)
        num_index += 1
    return output


def repeat(answer, func, repeat_count):
    for r in xrange(repeat_count):
        answer = func(answer)
    return answer


import unittest


class Test(unittest.TestCase):
    def test_look_and_say(self):
        self.assertEqual(look_and_say('111'), '31')
        self.assertEqual(look_and_say('111221'), '312211')

    def test_repeat(self):
        self.assertEqual(repeat('1', look_and_say, 5), '312211')

# unittest.main()
puzzle_input = '1113122113'
print len(repeat(puzzle_input, look_and_say, 50))
