#!/bin/sh

python3 -m homcloud.pc_alpha -d 3 --no-square -I -D input.txt output.idiagram
python3 -m homcloud.plot_PD -d 1 -x "[0:0.5]" -X 256 -l -U "no unit" -t "PD_1" -m 100 output.idiagram -o output.1.png
python3 -m homcloud.plot_PD -d 2 -x "[0:0.5]" -X 256 -l -U "no unit" -t "PD_2" -m 100 output.idiagram -o output.2.png
python3 -m homcloud.dump_diagram -d 1 output.idiagram > output.1.txt
python3 -m homcloud.dump_diagram -d 2 output.idiagram > output.2.txt
python3 -m homcloud.full_ph_tree -d 2 output.idiagram output.2.pht -j output-tree.2.json
python3 -m homcloud.query_full_ph_tree -c "draw-volumes-in-rectangle 0.21 0.25 0.28 0.35 voids.vtk" output.2.pht -B yes -D yes
python3 -m homcloud.query_full_ph_tree -c "write-volume-points-in-rectangle 0.21 0.25 0.28 0.35 volume-points.txt" output.2.pht
python3 -m homcloud.query_full_ph_tree -c "write-volume-simplices-in-rectangle 0.21 0.25 0.28 0.35 volume-tetrahderons.txt" output.2.pht
python3 -m homcloud.plot_PD_slice -d 1 -l 0.1 -r 0.2 -b 50 0.1 0.1 0.1 0.2 0.02 output.idiagram -o output.1.slice1.png
python3 -m homcloud.plot_PD_slice -d 1 -l 0.1 -r 0.2 -b 50 0.1 0.2 0.2 0.2 0.02 output.idiagram -o output.1.slice2.png
python3 -m homcloud.optimal_volume -d 1 -X 0.2:0.25 -Y 0.35:0.4 -j optimal-volumes.json -c 1.0 -n 3 output.idiagram
