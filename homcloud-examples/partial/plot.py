import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

def main():
    data = np.loadtxt("data.txt")
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    delaunay(data[:, 0:2])
    plot(data[data[:, 2] == 0.0, :], "b")
    plot(data[data[:, 2] == 1.0, :], "r")
    plt.savefig("pointcloud.png")

def plot(data, color):
    plt.scatter(data[:, 0], data[:, 1], c=color, s=50, zorder=10)

def delaunay(data):
    tri = Delaunay(data)
    plt.triplot(data[:, 0], data[:, 1], tri.simplices, c="black")


if __name__ == "__main__":
    main()
