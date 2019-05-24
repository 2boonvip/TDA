#!/bin/sh

python3 -m homcloud.pict.pixel_levelset_nd -m superlevel -T text2d -I -D grayscale.txt -o grayscale.idiagram
python3 -m homcloud.plot_diagram -d 0 -l grayscale.idiagram -o grayscale-superlevel-0.png
python3 -m homcloud.diagram_to_text -d 0 grayscale.idiagram -o grayscale-superlevel-0.txt
python3 -m homcloud.diagram_to_text -d 0 -S yes grayscale.idiagram -o grayscale-bdpixels.txt
python3 plot_birth_pixel.py grayscale-bdpixels.txt grayscale.txt grayscale-birth-pixels.png
