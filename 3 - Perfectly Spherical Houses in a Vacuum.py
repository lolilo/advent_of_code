def get_houses(s):
    current_location = [0, 0]
    set_locations = set([tuple(current_location)])
    for arrow in s:
        if arrow == '^':
            current_location[1] += 1
        elif arrow == '>':
            current_location[0] += 1
        elif arrow == 'v':
            current_location[1] -= 1
        elif arrow == '<':
            current_location[0] -= 1
        set_locations.add(tuple(current_location))
    return len(set_locations)


def get_houses_with_robo(s):
    current_location_santa = [0, 0]
    current_location_robo = [0, 0]
    current_locations = [current_location_santa, current_location_robo]
    set_locations = set([tuple([0, 0])])

    santa = True
    for arrow in s:
        if santa:
            mover = 0
        else:
            mover = 1

        if arrow == '^':
            current_locations[mover][1] += 1
        elif arrow == '>':
            current_locations[mover][0] += 1
        elif arrow == 'v':
            current_locations[mover][1] -= 1
        elif arrow == '<':
            current_locations[mover][0] -= 1
        set_locations.add(tuple(current_locations[mover]))
        santa = not santa

    return len(set_locations)


import unittest

class Test(unittest.TestCase):
    def test_get_houses(self):
        self.assertEqual(get_houses('^v^v^v^v^v'), 2)

    def test_get_houses_with_robo(self):
        self.assertEqual(get_houses_with_robo('^v^v^v^v^v'), 11)

# unittest.main()

f = open('input.txt', 'r')
# print get_houses(f.read())
print get_houses_with_robo(f.read())
