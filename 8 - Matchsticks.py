def part1(strings):
    code_char_count = 0
    char_value_count = 0
    for string in strings:
        len_string = len(string)
        code_char_count += len_string
        char_index = 0
        while char_index < len_string:
            if string[char_index] == '\"': # beginning and ending string quotes for every line
                char_index += 1
            elif string[char_index] == '\\':
                char_value_count += 1
                if string[char_index + 1] == 'x':
                    char_index += 4 
                else:
                    char_index += 2
            else: # char value
                char_value_count += 1
                char_index += 1
    return code_char_count - char_value_count


def part2(strings):
    additional_chars_for_encoding_count = 0
    for string in strings:
        additional_chars_for_encoding_count += 4 # for starting/ending quotes /"
        len_string = len(string)
        char_index = 1
        while char_index < len_string - 1:
            if string[char_index: char_index + 2] == '\\x':
                additional_chars_for_encoding_count += 1
                char_index += 4
            elif string[char_index] == '\\':
                additional_chars_for_encoding_count += 2
                char_index += 2
            else:
                char_index += 1
    return additional_chars_for_encoding_count


f = open('input.txt', 'r')
s = f.read()
strings = s.split()
# escape_chars = set(['\\', '\"', '\\x'])

test_input = '''""
"abc"
"aaa\\"aaa"
"\\x27"
'''

# strings = test_input.split()
# print strings
print part1(strings)
print part2(strings)
