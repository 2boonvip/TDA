homcloud-pict-binarize -m black-base -I -s -t 128 input.png input.icomplex
homcloud-dipha input.icomplex output.idiagram
homcloud-dump-diagram -d 0 output.idiagram -o output.0.txt
homcloud-dump-diagram -d 1 output.idiagram -o output.1.txt
homcloud-plot-PD -d 0 -x "[-20.5:20.5]" -X 41 -l -o output.0.png output.idiagram
homcloud-plot-PD -d 1 -x "[-20.5:20.5]" -X 41 -l -o output.1.png output.idiagram
homcloud-view-index-pict -d 0 -o output.death.0.png -D -s 5 -f "birth == -5" -f "death == -4" input.png output.idiagram
homcloud-view-index-pict -d 1 -o output.birth.1.png -B -s 5 -f "birth == 6" -f "death == 7" input.png output.idiagram
