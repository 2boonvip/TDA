homcloud-pc-alpha -d 3 --no-square -I -D input.txt output.idiagram
homcloud-plot-PD -d 1 -x "[0:0.5]" -X 256 -l -U "no unit" -t "PD_1" -m 100 output.idiagram -o output.1.png
homcloud-plot-PD -d 2 -x "[0:0.5]" -X 256 -l -U "no unit" -t "PD_2" -m 100 output.idiagram -o output.2.png
homcloud-dump-diagram -d 1 output.idiagram > output.1.txt
homcloud-dump-diagram -d 2 output.idiagram > output.2.txt
homcloud-full-ph-tree -d 2 output.idiagram output.2.pht
homcloud-query-full-ph-tree -c "draw-volumes-in-rectangle 0.21 0.25 0.28 0.35 voids.vtk" output.2.pht -B yes -D yes
