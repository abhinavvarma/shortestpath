import networkx as nx
import matplotlib.pyplot as plt


class Visualizer():
    def __init__(self):
        self.g = nx.Graph()

    def plot_intersection(self, intersection, color="w"):
        self.g.add_node(intersection.index, pos=(intersection.location.x_coord, intersection.location.y_coord), node_color=color)

    def plot_edge(self, source_intersection_id, destination_intersection_id, color="c"):
        self.g.add_edge(source_intersection_id, destination_intersection_id, {"edge_color":color})

    def draw(self, map, path):
        # if len(path) == 0:
        #     return
        self.plot_map(map, path)
        pos = nx.get_node_attributes(self.g, 'pos')
        node_colors = []
        edge_colors = []
        for edge in self.g.edges(data=True):
            edge_colors.append(edge[2]['edge_color'])
        for node, attributes in self.g.node.items():
            node_colors.append(attributes['node_color'])
        nx.draw(self.g, pos, node_size=10, edge_color=edge_colors, node_color=node_colors, width=5)
        plt.show()

    def plot_map(self, map, path):
        for intersection in map.intersection_list:
            self.plot_intersection(intersection)

        for source_index, adjacent_nodes in map.routes.items():
            for adjacent_intersection_index in adjacent_nodes:
                self.plot_edge(source_index, adjacent_intersection_index)

        if len(path) > 0:
            prv = path[0]
            for i in xrange(1, len(path)):
                current_node = path[i]
                self.plot_edge(prv.index, current_node.index, color='r')
                prv = current_node