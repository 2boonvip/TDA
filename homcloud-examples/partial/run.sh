#!/bin/sh

python3 plot.py
python3 -m homcloud.pc2diphacomplex -I -D -d 2 -P -A data.txt data.idiagram
python3 -m homcloud.plot_PD -d 1 data.idiagram -o data.1.png -x "0:0.03"
python3 -m homcloud.full_ph_tree -d 1 data.idiagram data.1.pht
