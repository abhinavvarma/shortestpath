import map
from pathfinder import ShortestPathFinder
from visualizepoints import plot_points

file = 'data/input6.txt'

map_instance = map.Map()
map_instance.load_input(file)

result = ShortestPathFinder(map_instance).get_shortest_path(
    map_instance.get_connected_intersections_to(0),
    map_instance.get_connected_intersections_to(5),
)
plot_points(map_instance.intersection_list)
