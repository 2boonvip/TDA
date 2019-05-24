import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import homcloud.interface as hc  # HomCloudのインターフェス
import homcloud.paraview_interface as pv  # 3次元可視化用


def data_processing(path): 
    data = pd.read_table(path)
    data *= 10000
    return data
            
def delay(data,channel):
    line = data.loc[:,channel]
    pointcloud = np.array([0,0,0])
    for i in range(2287,4401):
        tmp = np.array([line[i],line[i+1],line[i+2]]) 
        pointcloud = np.c_[pointcloud,tmp]
    for i in (33733,35397):
        tmp = np.array([line[i],line[i+1],line[i+2]]) 
        pointcloud = np.c_[pointcloud,tmp]
    return pointcloud.T

path = "1_raw_data_13-12_22.03.16.txt"

data = data_processing(path)

pointcloud = delay(data,'channel1')

#fig = plt.figure()
#ax = Axes3D(fig)
#
#ax.plot(pointcloud[0,:], pointcloud[1,:], pointcloud[2,:])
#plt.show()
plt.plot(data.loc[:,"channel1"])
plt.show()


hc.PDList.from_alpha_filtration(pointcloud, 
                                save_to="pointcloud.idiagram",
                                save_boundary_map=True)


pdlist = hc.PDList("pointcloud.idiagram")

pd = pdlist.dth_diagram(1)

pd.histogram((0.012, 0.013), 256).plot(colorbar={"type": "log"})
plt.savefig("pointcloudA.png")


print("helo")
    
    
        

    
