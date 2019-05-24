#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    data = np.loadtxt("3d.txt")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    mask = data[:,2] > 0.01
    ax.scatter(data[:,0][mask], data[:,1][mask], data[:,2][mask])
    plt.show()

main()
