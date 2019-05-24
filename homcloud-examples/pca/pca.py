import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def main():
    data = []
    for i in range(100):
        data.append(np.loadtxt("vects/{:04d}.txt".format(i)))
    vects = np.array(data)

    pca = PCA(n_components=2)
    pca.fit(vects)
    np.savetxt("mean.txt", pca.mean_)
    np.savetxt("pc1.txt", pca.components_[0, :])
    np.savetxt("pc2.txt", pca.components_[1, :])
    np.savetxt("pca.txt", pca.transform(vects))
    print(pca.explained_variance_ratio_)
    
main()
