#import homcloud.interface as hc  # HomCloudのインターフェス
#import homcloud.paraview_interface as pv  # 3次元可視化用
import numpy as np
#import matplotlib.pyplot as plt


pointcloud = np.loadtxt("pointcloud.txt")

#hc.PDList.from_alpha_filtration(pointcloud, 
#                                save_to="pointcloud.idiagram",
#                                save_boundary_map=True)
#
#
#pdlist = hc.PDList("pointcloud.idiagram")
#
#pd = pdlist.dth_diagram(1)
#
#pd.histogram((0, 0.1), 256).plot(colorbar={"type": "log"})
#plt.savefig("pointcloud-pd1.png")
#
#
#print("helo")
