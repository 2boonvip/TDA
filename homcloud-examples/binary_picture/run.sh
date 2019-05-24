#!/bin/sh

python3 -m homcloud.pict.binarize -m black-base -I -s -t 128 input.png input.icomplex
python3 -m homcloud.dipha input.icomplex output.idiagram
python3 -m homcloud.dump_diagram -d 0 output.idiagram -o output.0.txt
python3 -m homcloud.dump_diagram -d 1 output.idiagram -o output.1.txt
python3 -m homcloud.plot_PD -d 0 -x "[-20.5:20.5]" -X 41 -l -o output.0.png output.idiagram
python3 -m homcloud.plot_PD -d 1 -x "[-20.5:20.5]" -X 41 -l -o output.1.png output.idiagram
python3 -m homcloud.view_index_pict -d 0 -o output.death.0.png -D -s 5 -f "birth == -5" -f "death == -4" input.png output.idiagram
python3 -m homcloud.view_index_pict -d 1 -o output.birth.1.png -B -s 5 -f "birth == 6" -f "death == 7" input.png output.idiagram
python3 use_tree.py
