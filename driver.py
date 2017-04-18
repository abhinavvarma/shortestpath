import map
from pathfinder import ShortestPathFinder

file = 'data/input6.txt'

map_instance = map.Map()
map_instance.load_input(file)

result = ShortestPathFinder(map_instance).get_shortest_path(map_instance.get_intersection(0), map_instance.get_intersection(5))
print result