import matplotlib.pyplot as plt

x = []
y = []


x_all = []
y_all = []

def plot_points(all_instances, intersection_points):
    for point in intersection_points:
       x.append(point.location.x_coord)
       y.append(point.location.y_coord)

    for all_point in all_instances:
        x_all.append(all_point.location.x_coord)
        y_all.append(all_point.location.y_coord)


    plt.scatter(x_all,y_all)
    plt.scatter(x,y)
    plt.plot(x,y)

    plt.show()