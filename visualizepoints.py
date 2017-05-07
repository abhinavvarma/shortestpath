import matplotlib.pyplot as plt

x_route = []
y_route = []
x_all = []
y_all = []


def visualize_route(visited_intersections, route):
    '''
    Visualize the visited points and route in a scatter plot
    :param all_intersections: list of intersections that are visited
    :param route: list of intersections that form the route
    '''



    for route_intersection in route:
        x_route.append(route_intersection.location.x_coord)
        y_route.append(route_intersection.location.y_coord)


    for intersection in visited_intersections:
        x_all.append(intersection.location.x_coord)
        y_all.append(intersection.location.y_coord)

    plt.plot(x_route, y_route)
    plt.scatter(x_all, y_all)
    plt.show()

