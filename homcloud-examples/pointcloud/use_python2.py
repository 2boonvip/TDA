import matplotlib.pyplot as plt
import numpy as np

from homcloud.alpha_filtration import create_alpha_shape
from homcloud.dipha import get_diagram
from homcloud.plot_PD import PDColorHistogramPlotter, ZSpec, AuxPlotInfo
from homcloud.diagram import Ruler, PDHistogram

def main():
    pointcloud = np.loadtxt("input.txt")
    filtration = create_alpha_shape(pointcloud, 3).create_filtration(no_square=True)
    filtration.indexize()
    diagrams = get_diagram(filtration)
    for degree in [1, 2]:
        print("degree: {}".format(degree))
        print_birthdeath_pairs(diagrams[degree])

    for degree in [1, 2]:
        show_diagram(diagrams[degree], "degree: {}".format(degree))

def print_birthdeath_pairs(diagram):
    for (birth, death) in zip(diagram.births, diagram.deaths):
        print(birth, " ", death)

def show_diagram(diagram, title):
    plt.clf()
    x_ruler = y_ruler = Ruler(minmax=(0, 1), bins=256)
    PDColorHistogramPlotter(
        PDHistogram(diagram, x_ruler, y_ruler),
        ZSpec.Log(),
        AuxPlotInfo(title=title, unit_name="")
    ).plot(*plt.subplots())
    # If you want to save figure instead of showing, please use plt.savefig()
    plt.show()

main()
