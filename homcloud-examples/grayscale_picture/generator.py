import numpy as np
import scipy.misc
from scipy.ndimage import gaussian_filter

ary = np.zeros((128, 128), dtype=float)

for i in range(1000):
    x = np.random.randint(128)
    y = np.random.randint(128)
    ary[y, x] = np.random.rand()

ary = gaussian_filter(ary, sigma=2.0)
scipy.misc.imsave("input.png", ary)
