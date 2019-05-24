import os
import sys
import numpy as np

import homcloud.vectorize_PD as vectorize_PD
from homcloud.diagram import PD, Ruler, PDHistogram

# configure following 4 functions
def weight_function():
    return vectorize_PD.atan_weight_function(c=0.5, p=2.0)

def load_diagram(path):
    return PD.load_from_indexed_diphafile(path, d=0)

def xy_rulers():
    return (Ruler(minmax=(-40.5, 10.5), bins=51),
            Ruler(minmax=(-30.5, 20.5), bins=51))

def apply_gaussian(histogram):
    histogram.apply_gaussian_filter(sigma=2.0)

def main():
    vectors = []
    for n in range(100):
        print(n, file=sys.stderr)
        diagrampath = "data-1-pd/{:04d}.idiagram".format(n)

        diagram = load_diagram(diagrampath)
        histogram = PDHistogram(diagram, *xy_rulers())
        histogram.apply_weight(weight_function())
        apply_gaussian(histogram)
        vectors.append(histogram.vectorize())

        if n == 0:
            vectorize_PD.save_histogram_information("data-1-pd/histoinfo.json", histogram)

    os.makedirs("data-1-result", exist_ok=True)
    np.savetxt("data-1-result/vectors.txt", np.vstack(vectors))

if __name__ == "__main__":
    main()
