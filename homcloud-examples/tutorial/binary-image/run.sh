#!/bin/sh

python3 -m homcloud.pict.binarize_nd -T picture2d -m black-base -t 128 -I -D -s -o binary-image.idiagram binary-image.png
python3 -m homcloud.plot_diagram -d 0 -l -x "[-20.5:7.5]" -X 28 binary-image.idiagram -o binary-image-pd0.png
python3 -m homcloud.diagram_to_text -d 0 binary-image.idiagram -o binary-image-pd0.txt
python3 -m homcloud.diagram_to_text -d 0 -S yes binary-image.idiagram -o binary-image-bdpixels.txt
python3 plot_birth_pixel.py -5 -4 binary-image-bdpixels.txt binary-image.png binary-image-birth-pixels.png
