import numpy as np
import scipy.ndimage
import scipy.misc


def main():
    pict = np.zeros((200, 200))
    for _ in range(40):
        pict[np.random.randint(200), np.random.randint(200)] = 1.0 + np.random.normal(scale=0.1)
    pict = scipy.ndimage.gaussian_filter(pict, 20.0)
    for _ in range(1000):
        pict[np.random.randint(200), np.random.randint(200)] += np.random.normal(scale=0.001)
    pict = scipy.ndimage.gaussian_filter(pict, 2.0)

    #scipy.misc.imshow(pict)
    #np.savetxt("grayscale.txt", (pict - np.mean(pict))/np.std(pict))


main()
