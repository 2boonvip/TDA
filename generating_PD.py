import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
import scipy.stats
import math
import homcloud.interface as hc  # HomCloudのインターフェス
import homcloud.paraview_interface as pv  # 3次元可視化用

betti_sequence_range = 0.05 #betti系列を生成する際のデータ間隔

data_ranges = [(2287,4401),(6423,8217),(12534,14521),(17995,19729),(23545,25402),
               (28883,30840),(33733,35397),(37023,38752),(42750,44576),(48325,50030),
               (53862,55616),(59786,61578)]
path = "1_raw_data_13-12_22.03.16.txt" #対象データファイル名を指定
channels = ['channel1']#対象チャンネル名
picture_names = ['1_1output.png','2_1output.png','3_1output.png','4_1output.png',
                 '5_1output.png','6_1output.png','1_2output.png','2_2output.png',
                 '3_2output.png','4_2output.png','5_2output.png','6_2output.png',] 
#picture_names = ['2_1output.png','3_1output.png','6_1output.png','2_2output.png','3_2output.png','6_2output.png']#出力画像ファイル名
output_text_name = ['']


#対象データ成型
def data_processing(path): 
    data = pandas.read_table(path)
    return data

#3次元遅れ座標生成           
def delay(data,channel,data_range):
    line = data.loc[:,channel]
    pointcloud = np.array([0,0,0])
    
    for i in range(data_range[0],data_range[1]):
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
    
    
def output_picture(pd,pic_name):
    pd.histogram((0, 1), 256).plot(colorbar={"type": "log"})#Birthの表示範囲を指定
    plt.savefig(pic_name)#出力ファイル名
    
def output_text(pd):
    with open(txt_name,'w') as f:
        f.write('birth death\n')
            
    for birth,death in zip(pd.births,pd.deaths):
        with open(txt_name,'a') as f:
            f.write('{0},{1}\n'.format(birth,death))
   
#データを0-1区間で正規化
def normalization(pd):
    for j in range(len(pd)):
        lengths = [math.sqrt(pd[j].deaths[i] ** 2 + pd[j].births[i] ** 2 ) for i in range(len(pd[j].deaths))]
        length_maximum = max(lengths)
        
        for i in range(len(pd[j].deaths)):
            pd[j].births[i] = math.sqrt(2) * pd[j].births[i] / length_maximum
            pd[j].deaths[i] = math.sqrt(2) * pd[j].deaths[i] / length_maximum
        
    return pd
          
            
def calc_death_birth(pd,death_birth,index):
    tmp = 0
    sum_death_birth  = sum (pd.deaths - pd.births)
    death_birth.append((index,sum_death_birth))
    
    return death_birth
    

#betti系列の生成
def generating_betti_sequence(pd):
    betti_sequence = []
    for i in range(len(pd)):
        for j in range(int(1/betti_sequence_range)):
            tmp = 0
            for k in range(len(pd[i].deaths)):
                if pd[i].births[k] <= betti_sequence_range*j and pd[i].deaths[k] >= betti_sequence_range*j:
                    tmp += 1
            betti_sequence.append(tmp)
            
    return betti_sequence

#以下実行部
          
data = data_processing(path)
death_birth = []


for i in range(len(data_ranges)):
#    for channel,pic_name,txt_name in zip(channels,picture_names,output_text_name):

#        data = data_processing(path)
        
        pointcloud = delay(data,'channel1',data_ranges[i])
    
        #PD生成・保存
        hc.PDList.from_alpha_filtration(pointcloud, 
                                        save_to="pointcloud.idiagram",
                                        save_boundary_map=True)
        
        pdlist = hc.PDList("pointcloud.idiagram")
        
        pd = [pdlist.dth_diagram(i) for i in range(3)] #0~2次元のPDを生成
        pd = normalization(pd)#データの正規化
        betti_sequence = generating_betti_sequence(pd)
        
        print(betti_sequence)
        plt.xlim([0,1])
        plt.plot([i * betti_sequence_range for i in range(len(betti_sequence))],betti_sequence)
        
        plt.savefig("bitti_test{0}.png".format(i+1))
        
#        death_birth = calc_death_birth(pd,death_birth,i)
#        output_picture(pd,picture_names[i])
#        output_text(pd)
        
print("Done")