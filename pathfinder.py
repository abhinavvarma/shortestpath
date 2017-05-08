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

    def enqueue(self, node, distance):
        self._node_manager.store(node)
        PriorityQueue.put(self, (distance, node.id))

    def dequeue(self):
        item = super(NodeQueue, self).get(block=True, timeout=None)
        return self._node_manager.get_node(item[1])


class ShortestPathFinder(object):
    def __init__(self, map):
        self.map = map
        self._reached_nodes = {}

    def get_cost(self, current_node, destination_node):
        raise NotImplementedError()


    def is_done(self, queue, source=None, destination=None):
        return queue.empty()

    def _compute_single_source_shortest_path(self, source, destination=None):
        node_manager = NodeManager()
        queue = NodeQueue(node_manager)
        source_node = node_manager.to_node(source)
        destination_node = node_manager.to_node(destination)
        source_node.distance = 0
        queue.enqueue(source_node, self.get_cost(source_node, destination_node))

        while not self.is_done(queue, source, destination):
            current = queue.dequeue()
            current.visited = True
            adjacent_intersections = self.map.get_connected_intersections_to(current.intersection)

            for adjacent_intersection in adjacent_intersections:
                adjacent_node = node_manager.to_node(adjacent_intersection)
                if adjacent_node.visited:
                    continue
                queue.enqueue(adjacent_node, self.get_cost(adjacent_node, destination_node))
                distance = current.distance + adjacent_node.distance_to(current)

                if adjacent_node.distance > distance:
                    adjacent_node.distance = distance
                    adjacent_node.parent = current
                    self.get_reached_nodes(source_node.intersection)[adjacent_node.id] = adjacent_node

    def get_reached_nodes(self, source):
        if source.index not in self._reached_nodes:
            self._reached_nodes[source.index] = {}
        return self._reached_nodes[source.index]

    def get_shortest_path(self, source, destination):
        cached_paths = self.get_reached_nodes(source)

        if not cached_paths:
            self._compute_single_source_shortest_path(source, destination)
            cached_paths = self.get_reached_nodes(source)

        if destination.index not in cached_paths:
            return -1, []

        destination_node = cached_paths[destination.index]
        path = []

        current = destination_node
        while current != None:
            path.insert(0, current.intersection)
            current = current.parent

        return destination_node.distance, path


class DijkstraShortestPathFinder(ShortestPathFinder):
    def get_cost(self, current_node, destination_node):
        return current_node.distance


class AStarShortestPathFinder(ShortestPathFinder):
    def get_cost(self, current_node, destination_node):
        return destination_node.intersection.location.distance_to(current_node.intersection.location) + destination_node.distance

    def is_done(self, queue, source=None, destination=None):
        return queue.empty() or destination.index in self.get_reached_nodes(source)