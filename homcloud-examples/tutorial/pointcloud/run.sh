#!/bin/sh

python3 -m homcloud.pc2diphacomplex -I -D -d 3 pointcloud.txt pointcloud.idiagram
python3 -m homcloud.plot_diagram -d 1 -l -x "[0:0.1]" -X 256 pointcloud.idiagram -o pointcloud-pd1.png
python3 -m homcloud.diagram_to_text -d 1 pointcloud.idiagram -o pointcloud-pd1.txt
python3 -m homcloud.diagram_to_text -d 1 -S yes pointcloud.idiagram -o pointcloud-pd1-bdsimplex.txt
