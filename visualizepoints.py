import matplotlib.pyplot as plt

x = []
y = []

def plot_points(intersection_points):
    for point in intersection_points:
       x.append(point.location.x_coord)
       y.append(point.location.y_coord)


    plt.scatter(x,y)
    plt.plot(x,y)

    plt.show()