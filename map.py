from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def distance_to(self, point):
        return sqrt((point.y_coord-self.y_coord)**2+(point.x_coord-self.x_coord)**2)

    def __str__(self):
        return "(%s, %s)" % (self.x_coord, self.y_coord)


class Intersection(object):
    def __init__(self, index, location):
        '''
        :param index:
        :param location is an instance of Point:
        '''
        self.index = index
        self.location = location

    def __str__(self):
        return "%s@%s" % (self.index, self.location)


class Map(object):
    def __init__(self):
        self.routes = {}
        self.intersection_list = []

    def get_intersection(self, index):
        return self.intersection_list[index]

    def load_input(self, input_file_path):
        '''
        Loads the intersections from the input file to a list 
        :param input_file_path: path to the input file
        :return: 
        '''
        input_file = open(input_file_path, 'r')

        value = input_file.readline().strip().split(' ')

        no_of_nodes = int(value[0])
        no_of_edges = int(value[1])

        input_file.readline()
        intersections_list = []

        #Create instances of an instersection and add to a list of intersections
        while True:
            line = input_file.readline()
            if len(line) == 1:
                break
            coordinates = line.strip().split()
            # Read all coordinates
            index = int(coordinates[0])
            x_coord = int(coordinates[1])
            y_coord = int(coordinates[2])


            #add intersection to the intersection list
            self.add_intersection(index, x_coord, y_coord)



        line = input_file.readline()

        #reading the route between the points
        connected_intersections = line.strip().split()

        while connected_intersections != []:
            self.add_route(int(connected_intersections[0]), int(connected_intersections[1]))
            connected_intersections = input_file.readline().strip().split()



    def add_intersection(self, index, x_coord, y_coord):
        '''
        Create a new intersection, point instance and add to a list of instances
        :param index: index of the location 
        :param x_coord: x coordinate of location
        :param y_coord: y coordinate of location
        :return: None
        '''
        #initialize the route dict for each index
        self.routes[index] = []

        #create a new point instance
        new_point = Point(int(x_coord), int(y_coord))

        #create a new intersectio instance
        new_intersection = Intersection(index, new_point)

        #append the instance of the intersection to a list
        #list index represents index of the location
        self.intersection_list.append(new_intersection)



    def add_route(self, start, end, bidirectional=True):
        '''
        Add a route from start to ending index, the routes are stored as a dictionary
        :param start: index of starting location 
        :param end: index of ending location
        :return: 
        '''
        if end not in self.routes[start]:
            self.routes[start].append(end)
        if bidirectional and (start not in self.routes[end]):
            self.routes[end].append(start)




    def get_connected_intersections_to(self, intersection):
        '''
        Return the instance of intersections as a list
        :param intersection: integer value of the intersection
        :return: list of instances 
        '''
        #read list of connected intersections for an index location
        connected_indexes = self.routes[intersection.index]
        intersection_instance_list = []
        for index in connected_indexes:
            intersection_instance_list.append(self.intersection_list[int(index)])

        return intersection_instance_list


