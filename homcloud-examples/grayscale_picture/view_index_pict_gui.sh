#!/bin/sh

D=$1
SUB_SUPER=$2

python3 -m homcloud.view_index_pict_gui -d $1 input.png $2.idiagram
