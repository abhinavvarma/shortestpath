import map
from pathfinder import ShortestPathFinder
from visualizepoints import visualize_route

file = 'data/usa.txt'

map_instance = map.Map()
map_instance.load_input(file)
result = ShortestPathFinder(map_instance).get_shortest_path( map_instance.get_intersection(0),
                                                             map_instance.get_intersection(5),)


visualize_route(map_instance.intersection_list,result[1])
