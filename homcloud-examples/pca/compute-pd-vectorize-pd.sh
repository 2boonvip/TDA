#!/bin/sh

mkdir -p diagrams vects

for i in `seq -f %04g 0 99`; do
    echo $i
    python3 -m homcloud.pict.binarize -t 128 -m white-base -I -D picts/${i}.png diagrams/${i}.idiagram
    python3 -m homcloud.vectorize_PD -x "[-40.5:10.5]" -X 51 -y "[-30.5:20.5]" -Y 51 -D 2.0 -C 0.5 -p 1.0 -d 0 -H histoinfo.json -o vects/${i}.txt diagrams/${i}.idiagram
done
