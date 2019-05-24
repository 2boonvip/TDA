import numpy as np
import matplotlib.pyplot as plt

def main():
    pict = np.loadtxt("grayscale.txt")
    print("max: ", np.max(pict))
    print("min: ", np.min(pict))
    print("mean: ", np.mean(pict))
    print("std: ", np.std(pict))
    plt.hist(pict, range=(-4.0, 4.0))
    plt.savefig("grayscale-hist.png")

main()
