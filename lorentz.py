import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorentz方程式のパラメータ
p, gamma, b = 10, 28, 8/3

# 時間パラメータ
dt = 0.01 # 刻み幅
t_0 = 0 #　初期時刻
t_n = 50 # 終了時刻

# 位置パラメータ
X_0 = np.array([1, 1, 1]) # 質点の初期位置


# ルンゲクッタ法に関する関数
def RungeKutta(t, X):
  k_1 = LorenzEquation(t, X)
  k_2 = LorenzEquation(t + dt/2, X + k_1*dt/2)
  k_3 = LorenzEquation(t + dt/2, X + k_2*dt/2)
  k_4 = LorenzEquation(t + dt, X + k_3*dt)

  return X + dt/6*(k_1 + 2*k_2 + 2*k_3 + k_4)

def LorenzEquation(t, X):
  x, y, z = X[0],  X[1],  X[2]

  return np.array([-p*x + p*y, -x*z + gamma*x - y, x*y - b*z])


if __name__ == '__main__':
    t = t_0
    X = X_0
    data = np.r_[X]

    while t < t_n:
      X = RungeKutta(t, X)
      t += dt
      data = np.c_[data, X]

    print(data)
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.plot(data[0,:], data[1,:], data[2,:])
    plt.show()

    np.savetxt('input.txt', data.T, fmt='%.18e', delimiter=' ')
    
    open('test.txt','r')