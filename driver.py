import map
from pathfinder import ShortestPathFinder

file = 'data/usa.txt'

map_instance = map.Map()
map_instance.load_input(file)

result = ShortestPathFinder(map_instance).get_shortest_path(map_instance.get_intersection(608), map_instance.get_intersection(990))
print result