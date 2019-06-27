import pandas
import glob

files = glob.glob("./EMG_data_for_gestures-master/*")

count = 0
for f in files:
    text_files = glob.glob(f+"/*")
    for t in text_files:
        data_table = pandas.read_table(t)
        for i in range(6):
            count += 1
            data = data_table[data_table['class'] == i+1]
            data.to_csv("./EMG_data_for_gestures-master/status{0}/dataset{1}.csv".format(i+1,count))
            