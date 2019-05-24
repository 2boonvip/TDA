import numpy as np

def main():
    pc1 = np.loadtxt("data-1-result/pca-pc1.txt")
    np.savetxt("data-1-result/pca-pc1-mask-positive.txt", pc1 > 0.05, fmt="%d")
    np.savetxt("data-1-result/pca-pc1-mask-negative.txt", pc1 < -0.03, fmt="%d")
    pc2 = np.loadtxt("data-1-result/pca-pc2.txt")
    np.savetxt("data-1-result/pca-pc2-mask-positive.txt", pc2 > 0.05, fmt="%d")
    np.savetxt("data-1-result/pca-pc2-mask-negative.txt", pc2 < -0.05, fmt="%d")

if __name__ == "__main__":
    main()
