import json

import matplotlib.pyplot as plt
import homcloud.interface as hc


def plot_histogram(pd, title):
    histo = pd.histogram((0, 0.5), 256)
    histo.plot(colorbar={"type": "log", "max": 100}, title=title, 
               aspect="equal")
    plt.savefig(title + ".png")


pds = hc.PDs("output.idiagram")
plot_histogram(pds[1], "PD1")
plot_histogram(pds[2], "PD2")
