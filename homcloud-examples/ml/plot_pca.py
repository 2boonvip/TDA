import numpy as np
import matplotlib.pyplot as plt

def main():
    pca = np.loadtxt("data-1-result/pca.txt")
    labels = np.loadtxt("data-1/labels.txt", dtype=int)

    # plt.xlim(-3, 3)
    # plt.ylim(-3, 3)
    plt.axes().set_aspect('equal')
    plot(pca[labels == 0, :], "r")
    plot(pca[labels == 1, :], "b")
    plt.show()

def plot(data, color):
    plt.scatter(data[:, 0], data[:, 1], c=color)

main()
