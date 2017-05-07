import sys
from Queue import PriorityQueue


class Node(object):
    def __init__(self, intersection):
        self.intersection = intersection
        self.distance = sys.maxint
        self.visited = False
        self.parent = None

    @property
    def id(self):
        return self.intersection.index

    def distance_to(self, node):
        return node.intersection.location.distance_to(self.intersection.location)

    def __str__(self):
        return "%s, d:%s, v:%s" % (self.intersection , self.distance , self.visited)


class NodeManager(object):
    def __init__(self):
        self.__cache = {}

    def store(self, node):
        self.__cache[node.id] = node

    def to_node(self, intersection):
        if intersection.index not in self.__cache:
            self.store(Node(intersection))
        return self.get_node(intersection.index)

    def get_node(self, index):
        return self.__cache.get(index)

class NodeQueue(object, PriorityQueue):
    def __init__(self, node_manager):
        self._node_manager = node_manager
        PriorityQueue.__init__(self)

    def put(self, node, block=True, timeout=None):
        self._node_manager.store(node)
        PriorityQueue.put(self, (node.distance, node.id), block=True, timeout=None)

    def get(self, block=True, timeout=None):
        item = super(NodeQueue, self).get(block=True, timeout=None)
        return self._node_manager.get_node(item[1])


class ShortestPathFinder(object):
    def __init__(self, map):
        self.map = map
        self._cached_paths = {}

    def _compute_single_source_shortest_path(self, source):
        node_manager = NodeManager()
        queue = NodeQueue(node_manager)
        source_node = node_manager.to_node(source)
        source_node.distance = 0
        queue.put(source_node)

        while not queue.empty():
            current = queue.get()
            current.visited = True
            adjacent_intersections = self.map.get_connected_intersections_to(current.intersection)

            for adjacent_intersection in adjacent_intersections:
                adjacent_node = node_manager.to_node(adjacent_intersection)
                if adjacent_node.visited:
                    continue
                queue.put(adjacent_node)
                distance = current.distance + adjacent_node.distance_to(current)

                if adjacent_node.distance > distance:
                    adjacent_node.distance = distance
                    adjacent_node.parent = current
                    self.get_cached_paths(source_node.intersection)[adjacent_node.id] = adjacent_node

    def get_cached_paths(self, source):
        if source.index not in self._cached_paths:
            self._cached_paths[source.index] = {}
        return self._cached_paths[source.index]

    def get_shortest_path(self, source, destination):
        cached_paths = self.get_cached_paths(source)

        if not cached_paths:
            self._compute_single_source_shortest_path(source)
            cached_paths = self.get_cached_paths(source)

        if destination.index not in cached_paths:
            return -1, []

        destination_node = cached_paths[destination.index]
        path = []

        current = destination_node
        while current.parent != None:
            path.insert(0, current.intersection)
            current = current.parent

        return destination_node.distance, path