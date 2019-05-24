import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def main():
    xs = np.loadtxt("data-1-result/vectors.txt")
    pca = PCA(n_components=2)
    pca.fit(xs)
    np.savetxt("data-1-result/pca-mean.txt", pca.mean_)
    np.savetxt("data-1-result/pca-pc1.txt", pca.components_[0, :])
    np.savetxt("data-1-result/pca-pc2.txt", pca.components_[1, :])
    np.savetxt("data-1-result/pca.txt", pca.transform(xs))
    print("explained variance ratio: ", pca.explained_variance_ratio_)

if __name__ == "__main__":
    main()
