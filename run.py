import map
from pathfinder import DijkstraShortestPathFinder, AStarShortestPathFinder
from visualizer import Visualizer

# file = 'data/input6.txt'
file = 'data/usa.txt'

map_instance = map.Map()
map_instance.load_input(file)

source_index = raw_input("\nEnter the index of the source intersection. (Hit enter to choose the default value)")
if not source_index:
    source_index = 608

source = map_instance.get_intersection(source_index)
print "Selected Source:", str(source)

dest_index = raw_input("\nEnter the index of the destination intersection. (Hit enter to choose the default value)")
if not dest_index:
    dest_index = 76344

dest = map_instance.get_intersection(dest_index)
print "Destination:", str(dest)

algo_choice = raw_input("\nPlease choose the algorithm to run. \n1. A-Star Algorithm \n2. Dijkstra's Algorithm\n(Hit enter to choose the default algorithm)\n")
if (algo_choice==1):
    Algo = DijkstraShortestPathFinder
else:
    Algo = AStarShortestPathFinder

print "Selected Algorithm:", Algo
print "\nExecuting.."
result = Algo(map_instance).get_shortest_path(source,dest)
print "Done. Printing the shortest path"
for i in result[1]:
    print i

v = Visualizer()
v.draw(map_instance, result[1])