class LightGrid(object):
    def __init__(self, n):
        self.size = n
        self.grid = self.make_grid(n)

    def __repr__(self):
        s = [[str(e) for e in row] for row in self.grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def make_grid(self, n):
        grid = []
        for i in xrange(n):
            grid.append([0] * n)
        return grid

    def get_lit_light_count(self):
        light_count = 0
        for row in xrange(self.size):
            for column in xrange(self.size):
                if self.grid[row][column]:
                    light_count += 1
        return light_count

    def toggle(self, coord1, coord2):
        for y in xrange(coord1[1], coord2[1] + 1):
            for x in xrange(coord1[0], coord2[0] + 1):
                self.grid[y][x] = 0 if self.grid[y][x] else 1

    def turn_on_or_off(self, command, coord1, coord2):
        final_state = 1 if command == 'on' else 0
        for y in xrange(coord1[1], coord2[1] + 1):
            for x in xrange(coord1[0], coord2[0] + 1):
                self.grid[y][x] = final_state

    def perform_instruction(self, s):
        words = s.split()
        if words[0] == 'toggle':
            self.toggle(self.get_coord(words[1]), self.get_coord(words[3]))
        else:
            self.turn_on_or_off(words[1], self.get_coord(words[2]), self.get_coord(words[4]))

    def get_coord(self, s):
        x, y = [int(x) for x in s.split(',')]
        return (x, y)


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.test_grid = LightGrid(10)
        self.maxDiff = None

    def test_toggle(self):
        self.test_grid.toggle(self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,0'))
        self.assertEqual(self.test_grid.grid[0], [1] * 10)
        self.test_grid.toggle(self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,0'))
        self.assertEqual(self.test_grid.grid[0], [0] * 10)
        self.test_grid.toggle(self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,9'))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)

    def test_turn_on_or_off(self):
        self.test_grid.turn_on_or_off('on', self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,9'))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)
        self.test_grid.turn_on_or_off('on', self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,9'))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)
        self.test_grid.turn_on_or_off('off', self.test_grid.get_coord('0,0'), self.test_grid.get_coord('9,9'))
        self.assertEqual(self.test_grid.grid, [[0] * 10] * 10)


unittest.main()

grid = LightGrid(1000)
f = open('input.txt', 'r')
for line in f.read().split('\n'):
    grid.perform_instruction(line)
print grid.get_lit_light_count()
