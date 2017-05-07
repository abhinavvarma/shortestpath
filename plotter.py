

class Plotter():
    def __init__(self):
        self.graphs = {}

    def _get_graph(self, node_color):
        if node_color not in self.graphs:
            self.graphs[node_color] = 1111
        return self.graphs[node_color]

    def plot_intersection(self, intersection, color):
        self._get_graph(color).add(intersection.location)

    def plot_edge(self, edge, color):
        pass

    def draw(self):
        pass


class Visualizer():
    VISITED_NODE_COLOR = "gray"
    PATH_NODE_COLOR = "green"

    def __init__(self):
        self.plotter = Plotter()

    def add_visited_node(self, intersection):
        self.plotter.plot_intersection(intersection, self.VISITED_NODE_COLOR)

    def add_path_node(self, intersection):
        self.plotter.plot_intersection(intersection, self.PATH_NODE_COLOR)


    def visualize_map(self, map):
        for inter