import map
from pathfinder import DijkstraShortestPathFinder, AStarShortestPathFinder
from visualizer import Visualizer

# file = 'data/input6.txt'
file = 'data/usa.txt'

map_instance = map.Map()
map_instance.load_input(file)
# result = AStarShortestPathFinder(map_instance).get_shortest_path( map_instance.get_intersection(0),
#                                                              map_instance.get_intersection(5),)
result = DijkstraShortestPathFinder(map_instance).get_shortest_path( map_instance.get_intersection(608),
                                                             map_instance.get_intersection(76344),)


v = Visualizer()
v.draw(map_instance, result[1])