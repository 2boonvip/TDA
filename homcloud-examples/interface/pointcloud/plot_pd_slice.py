import matplotlib.pyplot as plt
import homcloud.interface as hc


def plot_slice():
    pds = hc.PDs("output.idiagram")
    hist = pds[1].slice_histogram(0.1, 0.1, 0.1, 0.2, 0.02, bins=50)
    print("slice histogram PD1 (0.1, 0.1) - (0.1, 0.2):")
    print(hist.values)
    hist.plot(left_label="0.1", right_label="0.2")
    plt.title("PD1, slice, (0.1, 0.1) - (0.1, 0.2)")
    plt.savefig("output.1.slice1.png")


plot_slice()
