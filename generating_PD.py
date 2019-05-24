import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
import homcloud.interface as hc  # HomCloudのインターフェス
import homcloud.paraview_interface as pv  # 3次元可視化用

path = "1_raw_data_13-12_22.03.16.txt" #対象データファイル名を指定
channels = ['channel1','channel2']#対象チャンネル名
picture_names = ['channel1_output.png','channel1_output.png'] #出力画像ファイル名
output_text_name = ['text1.txt','text2.txt']


#対象データ成型
def data_processing(path): 
    data = pandas.read_table(path)
    data *= 10000#値の大きさを調整
    return data

#3次元遅れ座標生成           
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


#３次元遅れ座標の表示
def display_3D(pointcloud):
    fig = plt.figure()
    ax = Axes3D(fig)
    
    ax.plot(pointcloud[0,:], pointcloud[1,:], pointcloud[2,:])
    plt.show()
    plt.plot(data.loc[:,"channel1"])
    plt.show()
    
    
def output_picture(pd):
    pd.histogram((0, 0.1), 256).plot(colorbar={"type": "log"})#Birthの表示範囲を指定
    plt.savefig(pic_name)#出力ファイル名
    
def output_text(pd):
    with open(txt_name,'w') as f:
        f.write('birth death\n')
            
    for birth,death in zip(pd.births,pd.deaths):
        with open(txt_name,'a') as f:
            f.write('{0},{1}\n'.format(birth,death))
    



#以下実行部
for channel,pic_name,txt_name in zip(channels,picture_names,output_text_name):
    
    data = data_processing(path)
    
    pointcloud = delay(data,channel)

    #PD生成・保存
    hc.PDList.from_alpha_filtration(pointcloud, 
                                    save_to="pointcloud.idiagram",
                                    save_boundary_map=True)
    
    pdlist = hc.PDList("pointcloud.idiagram")
    
    pd = pdlist.dth_diagram(1)
    
    output_picture(pd)
    output_text(pd)
    

print("Done")