class LightGrid(object):
    def __init__(self, n, operation_map):
        self.size = n
        self.grid = self.make_grid(n)
        self.operations = operation_map

    def __repr__(self):
        s = [[str(e) for e in row] for row in self.grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return '\n'.join(table)

    def make_grid(self, n):
        return [[0] * n for i in xrange(n)]

    def parse_and_execute(self, s):
        command, coord1, coord2 = self.parse_instruction(s)
        self.perform_instruction(command, coord1, coord2)

    def parse_instruction(self, s):
        words = s.split()
        if words[0] == 'toggle':
            command = self.operations['toggle']
            first_coord = self.parse_coord(words[1])
            second_coord = self.parse_coord(words[3])
        else:
            command = self.operations[words[1]]
            first_coord = self.parse_coord(words[2])
            second_coord = self.parse_coord(words[4])
        return command, first_coord, second_coord

    def parse_coord(self, s):
        x, y = [int(x) for x in s.split(',')]
        return (x, y)

    def perform_instruction(self, command, coord1, coord2):
        for y in xrange(coord1[1], coord2[1] + 1):
            for x in xrange(coord1[0], coord2[0] + 1):
                self.grid[y][x] = command(self.grid[y][x])

    def get_lit_light_count(self):
        light_count = 0
        for row in self.grid:
            light_count += sum(row)
        return light_count


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.operations = {
            'toggle': lambda x: 0 if x else 1,
            'on': lambda x: 1,
            'off': lambda x: 0
        }
        self.test_grid = LightGrid(10, self.operations)
        self.maxDiff = None

    def test_toggle(self):
        self.test_grid.perform_instruction(self.operations['toggle'], (0, 0), (9, 0))
        self.assertEqual(self.test_grid.grid[0], [1] * 10)
        self.test_grid.perform_instruction(self.operations['toggle'], (0, 0), (9, 0))
        self.assertEqual(self.test_grid.grid[0], [0] * 10)
        self.test_grid.perform_instruction(self.operations['toggle'], (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)

    def test_turn_on(self):
        self.test_grid.perform_instruction(self.operations['on'], (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)
        self.test_grid.perform_instruction(self.operations['on'], (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[1] * 10] * 10)

    def test_turn_off(self):
        self.test_grid.perform_instruction(self.operations['off'], (0, 0), (9, 9))
        self.assertEqual(self.test_grid.grid, [[0] * 10] * 10)


unittest.main()

operations1 = {
    'toggle': lambda x: 0 if x else 1,
    'on': lambda x: 1,
    'off': lambda x: 0
}

operations2 = {
    'toggle': lambda x: x + 2,
    'on': lambda x: x + 1,
    'off': lambda x: max(x - 1, 0)
}

grid1 = LightGrid(1000, operations1)
grid2 = LightGrid(1000, operations2)
f = open('input.txt', 'r')
for line in f.read().split('\n'):
    grid1.parse_and_execute(line)
    grid2.parse_and_execute(line)
print grid1.get_lit_light_count()
print grid2.get_lit_light_count()
# 543903
# 14687245
