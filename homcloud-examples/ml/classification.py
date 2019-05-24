import numpy as np

from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split

def main():
    xs = np.loadtxt("data-1-result/vectors.txt")
    labels = np.loadtxt("data-1/labels.txt")

    data_train, data_test, label_train, label_test = train_test_split(
        xs, labels, test_size=0.1
    )
    model = LogisticRegressionCV(penalty="l2")
    model.fit(data_train, label_train)

    print("intercept: {}".format(model.intercept_[0]))
    print("C: {}".format(model.C_[0]))
    print("score on test set: {}".format(model.score(data_test, label_test)))

    np.savetxt("data-1-result/logreg-coef.txt", np.ravel(model.coef_))

if __name__ == "__main__":
    main()
