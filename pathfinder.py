class ShortestPathFinder(object):
    def __init__(self, map):
        pass

    def _compute_single_source_shortest_path(self, source):
        pass

    def get_cached_paths(self, source):
        return {}

    def get_shortest_path(self, source, destination):
        cached_paths = self.get_cached_paths(source)
        if not cached_paths:
            self._compute_single_source_shortest_path(source)
            cached_paths = self.get_cached_paths(source)

        return cached_paths[destination]
