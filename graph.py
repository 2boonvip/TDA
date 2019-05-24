import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def data_processing(path): 
    data = pd.read_table(path)
            
    return data

path = "1_raw_data_13-12_22.03.16.txt"

data = data_processing(path)
plt.figure(figsize=(10,4))
plt.title("Ch1")
plt.xlabel("Time [ms]")
plt.ylabel("Amplitude [×10^2 V]")
plt.plot(data.loc[:,"channel1"])

plt.show()