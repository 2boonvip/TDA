import numpy as np
from scipy.ndimage import gaussian_filter

def main():
    data = np.zeros((100, 100, 100))
    for _ in range(3000):
        x, y, z = np.random.randint(100, size=(3,))
        data[z, y, x] = np.random.rand()

    np.save("input.npy", gaussian_filter(data, sigma=2.0))

if __name__ == "__main__":
    main()
