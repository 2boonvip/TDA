import numpy as np
import scipy.misc


pict = np.loadtxt("grayscale.txt")
scipy.misc.imsave("grayscale.png", pict)
