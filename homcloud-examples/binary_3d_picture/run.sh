#!/bin/sh

python3 -m homcloud.pict.binarize3d -m white-base -s -t 128 -I -o input.icomplex pict_??.png
python3 -m homcloud.dipha input.icomplex output.idiagram
python3 -m homcloud.plot_PD -x "[-10.5:10.5]" -X 21 -d 0 -o output.0.png output.idiagram
python3 -m homcloud.plot_PD -x "[-10.5:10.5]" -X 21 -d 1 -o output.1.png output.idiagram
python3 -m homcloud.plot_PD -x "[-10.5:10.5]" -X 21 -d 2 -o output.2.png output.idiagram
python3 -m homcloud.dump_diagram -d 0 -o output.0.txt output.idiagram
python3 -m homcloud.dump_diagram -d 1 -o output.1.txt output.idiagram
python3 -m homcloud.dump_diagram -d 2 -o output.2.txt output.idiagram

python3 -m homcloud.pict.binarize3d -m white-base -t 128 -I -o input_noerosion.icomplex pict_??.png
python3 -m homcloud.dipha input_noerosion.icomplex output_noerosion.idiagram
python3 -m homcloud.plot_PD -x "[-10.5:10.5]" -X 21 -d 1 -o output_noerosion.1.png output_noerosion.idiagram
python3 -m homcloud.plot_PD -x "[-10.5:10.5]" -X 21 -d 2 -o output_noerosion.2.png output_noerosion.idiagram
python3 -m homcloud.dump_diagram -d 1 -o output_noerosion.1.txt output_noerosion.idiagram
python3 -m homcloud.dump_diagram -d 2 -o output_noerosion.2.txt output_noerosion.idiagram
