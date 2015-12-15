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
        graph[city1] = {city2: int(distance)}
    return graph


# not relevant? 
def find_minimum_distance(city1, city2, graph, current_distance=0):
    next_cities = graph[city1].keys()
    if city2 in next_cities:
        return current_distance + graph[city1][city2]


def get_one_path_distance(starting_city, visited, distance, graph):
    print ''
    print starting_city
    visited.add(starting_city)
    more_cities_to_visit = set(graph[starting_city].keys()) - visited
    print more_cities_to_visit

    if more_cities_to_visit == set([]):
        print 'YO', starting_city
        return 0

    # for city in more_cities_to_visit:
        # print distance
    city = list(more_cities_to_visit)[0]
    print graph[city][starting_city]
    distance += graph[city][starting_city]
    print 'ditance: ', distance
    distance += get_one_path_distance(city, visited, distance, graph)
    print 'ditance: ', distance


    return distance



# def get_min_distance_to_reach_all_cities(graph, visited):
#     if len(visited) == len(graph.keys()):
#         return 0

#     path_distances = []
#     all_cities = set(graph.keys())
#     for city in all_cities - visited:
#         min_for_this_city = get_min_distance_to_reach_all_cities(graph, visited.add(city))
#         path_distances.append(min_for_this_city)
#     return min(path_distances)


def dfs(graph, starting_city, visited=None):
    if visited is None:
        visited = set()
    visited.add(starting_city)
    for next_city in set(graph[starting_city].keys()) - visited:
        dfs(graph, next_city, visited)
    return visited


graph = {'Belfast': {'Dublin': 141, 'London': 518},
            'Dublin': {'Belfast': 141, 'London': 464},
            'London': {'Belfast': 518, 'Dublin': 464}}


print dfs(graph, 'Belfast')




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

# print tsp_naive_solve(graph)







import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = '''London to Dublin = 464
            London to Belfast = 518
            Dublin to Belfast = 141'''

        self.graph = {'Belfast': {'Dublin': 141, 'London': 518},
            'Dublin': {'Belfast': 141, 'London': 464},
            'London': {'Belfast': 518, 'Dublin': 464}}

    def test_make_graph(self):
        self.assertEqual(make_graph(self.s), self.graph)

    def test_find_minimum_distance(self):
        self.assertEqual(get_min_distance_to_reach_all_cities(self.graph, set([])), 141)

    def test_get_one_path_distance(self):
        self.assertEqual(get_one_path_distance('Belfast', set([]), 0, self.graph), 35)

# unittest.main()
s = open('input.txt', 'r').read()

# s = '''London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141'''

graph = make_graph(s)

# from pprint import pprint
# pprint(graph)

print tsp_naive_solve(graph)
