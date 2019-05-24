import numpy as np
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split

def main():
    xs = np.loadtxt("data-3-result/vectors.txt")
    ys = np.loadtxt("data-3/ys.txt").reshape(600, 1)

    xs_train, xs_test, ys_train, ys_test = train_test_split(
        xs, ys, test_size=0.1,
    )

    model = lm.RidgeCV(alphas=[0.1, 1.0, 10.0])
    model.fit(xs_train, ys_train)
    print("intercept:", model.intercept_[0])
    print("alpha:", model.alpha_)
    print("score on test set:", model.score(xs_test, ys_test))
    np.savetxt("data-3-result/linreg-coef.txt", np.ravel(model.coef_))

if __name__ == "__main__":
    main()
