

class Point(object):
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def distance_to(self, point):
        pass


class Intersection(object):
    def __init__(self, index, location):
        '''

        :param index:
        :param location is an instance of Point:
        '''
        self.index = index
        self.location = location


class Map(object):
    def __init__(self, input_file):
        self.nodes = {}

    def load_input(self, input_file):
        '''
        Loads the intersections from the input file to a list 
        :param input_file: path to the input file 
        :return: 
        '''
        file = open('data/input6.txt', 'r')

        value = file.readline().strip().split(' ')

        no_of_nodes = int(value[0])
        no_of_edges = int(value[1])

        file.readline()
        intersections_list = []

        #Create instances of an instersection and add to a list of intersections
        for line in file:
            if len(line) == 1:
                break
            coordinates = line.strip().split()
            # Read all coordinates
            index = coordinates[0]
            x_coord = coordinates[1]
            y_coord = coordinates[2]

            point = map.Point(x_coord, y_coord)
            intersection = map.Intersection(index, point)
            intersections_list.append(intersection)



    def addNodes(self, index):
        pass

    def get_connected_intersections_to(self, intersection):
        pass

    def get_intersections(self):
        pass