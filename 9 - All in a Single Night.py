def make_graph(s):
    graph = {}
    for line in s.split('\n'):
        city1, _, city2, _, distance = line.split()
        graph = add_to_graph(city1, city2, distance, graph)
        graph = add_to_graph(city2, city1, distance, graph)
    return graph


def add_to_graph(city1, city2, distance, graph):
    if graph.get(city1):
        graph[city1][city2] = int(distance)
    else:
        graph[city1] = { city2: int(distance) }
    return graph


def dfs(graph, starting_city, visited=None):
    if visited is None:
        visited = set()
    visited.add(starting_city)
    for next_city in set(graph[starting_city].keys()) - visited:
        dfs(graph, next_city, visited)
    return visited


def my_permutations(l):
    if len(l) < 2:
        return [l]
    permutations = []
    for item in l:
        remaining_items = l[:]
        remaining_items.remove(item)
        rest = my_permutations(remaining_items)
        permuations_starting_with_this_item = [[item] + x for x in rest]
        permutations.extend(permuations_starting_with_this_item)
    return permutations


# https://mchouza.wordpress.com/2010/11/21/solving-the-travelling-salesman-problem/
from itertools import permutations


def tour_len(path, graph):
    distance = 0
    for city_index in xrange(len(path) - 1): 
        city1 = path[city_index]
        city2 = path[city_index + 1]
        distance += graph[city1][city2]
    return distance


def tsp_naive_solve(graph):
    shortest_distance, best_tour = min((tour_len(t, graph), t) for t in permutations(graph.keys()))
    return shortest_distance, best_tour


def tsp_naive_solve_get_shortest_distance_only(graph):
    shortest_distance = min((tour_len(t, graph)) for t in my_permutations(graph.keys()))
    return shortest_distance


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = '''London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141'''

        self.graph = {
            'Belfast': {'Dublin': 141, 'London': 518},
            'Dublin': {'Belfast': 141, 'London': 464},
            'London': {'Belfast': 518, 'Dublin': 464}
        }

    def test_make_graph(self):
        self.assertEqual(make_graph(self.s), self.graph)

    def test_dsf(self):
        self.assertEqual(dfs(self.graph, 'Dublin'), set(['Dublin', 'London', 'Belfast']))

    def test_tsp_naive_solve(self):
        self.assertEqual(tsp_naive_solve(self.graph), (605, ('Belfast', 'Dublin', 'London')))

    def test_my_permutations(self):
        self.assertEqual(my_permutations(self.graph.keys()), [list(l) for l in permutations(self.graph.keys())])

    def test_tsp_naive_solve_get_shortest_distance_only(self):
        self.assertEqual(tsp_naive_solve_get_shortest_distance_only(self.graph), 605)


unittest.main()

# s = open('input.txt', 'r').read()
# graph = make_graph(s)

# from pprint import pprint
# pprint(graph)

# print tsp_naive_solve(graph)
