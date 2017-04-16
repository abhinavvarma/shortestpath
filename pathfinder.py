import sys


class Node(object):
    def __init__(self, intersection):
        self.intersection = intersection
        self.distance = sys.maxint

    @property
    def id(self):
        return self.intersection.index



class ShortestPathFinder(object):
    def __init__(self, map):
        self.map = map

    def _compute_single_source_shortest_path(self, source):
        visited = {}
        source_node = Node(source)
        current = source_node
        adjacent_nodes = self.map.get_connected_nodes_to(current)

        for adjacent_node in adjacent_nodes:
            if adjacent_node.id in visited:
                pass

    def get_cached_paths(self, source):
        return {}

    def get_shortest_path(self, source, destination):
        cached_paths = self.get_cached_paths(source)
        if not cached_paths:
            self._compute_single_source_shortest_path(source)
            cached_paths = self.get_cached_paths(source)

        return cached_paths[destination]
