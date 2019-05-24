import scipy.misc
import numpy as np

def main():
    for n in range(600):
        pict = scipy.misc.imread("data-3/{:04d}.png".format(n)) > 128
        print(np.sum(pict))


main()
