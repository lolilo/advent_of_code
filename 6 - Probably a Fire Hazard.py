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
        for row in self.grid:
            light_count += sum(row)
        return light_count

    def perform_instruction(self, command, coord1, coord2):
        if command < 2:
            for y in xrange(coord1[1], coord2[1] + 1):
                for x in xrange(coord1[0], coord2[0] + 1):
                    self.grid[y][x] = command
        else:
            for y in xrange(coord1[1], coord2[1] + 1):
                for x in xrange(coord1[0], coord2[0] + 1):
                    self.grid[y][x] = 0 if self.grid[y][x] else 1

    def parse_instruction(self, s):
        words = s.split()
        if words[0] == 'toggle':
            command = 2
            first_coord = self.parse_coord(words[1])
            second_coord = self.parse_coord(words[3])
        else:
            command = 1 if words[1] == 'on' else 0
            first_coord = self.parse_coord(words[2])
            second_coord = self.parse_coord(words[4])
        return command, first_coord, second_coord

    def parse_coord(self, s):
        x, y = [int(x) for x in s.split(',')]
        return (x, y)


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.test_grid = LightGrid(10)
        self.maxDiff = None

    def test_toggle(self):
        self.test_grid.perform_instruction(2, (0, 0), (9, 0))
        self.assertEqual(self.test_grid.grid[0], [1] * 10)
        self.test_grid.perform_instruction(2, (0, 0), (9, 0))
        self.assertEqual(self.test_grid.grid[0], [0] * 10)
        self.test_grid.perform_instruction(2, (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)

    def test_turn_on_or_off(self):
        self.test_grid.perform_instruction(1, (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)
        self.test_grid.perform_instruction(1, (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)
        self.test_grid.perform_instruction(0, (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[0] * 10] * 10)


# unittest.main()

grid = LightGrid(1000)
f = open('input.txt', 'r')
for line in f.read().split('\n'):
    command, coord1, coord2 = grid.parse_instruction(line)
    grid.perform_instruction(command, coord1, coord2)
print grid.get_lit_light_count()
# 543903
