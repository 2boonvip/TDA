#!/bin/sh
D=$1
python3 -m homcloud.plot_PD_gui -d $D -x "[-20.5:20.5]" -X 41 output.idiagram

