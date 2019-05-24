#!/bin/sh

python3 -m homcloud.pict.pixel_levelset_nd -m superlevel -T npy -D -I -o superlevel.idiagram input.npy
python3 -m homcloud.pict.pixel_levelset_nd -m sublevel -T npy -D -I -o sublevel.idiagram input.npy

python3 -m homcloud.plot_PD -d 0 -N -o superlevel.0.png -l superlevel.idiagram
python3 -m homcloud.plot_PD -d 1 -N -o superlevel.1.png -l superlevel.idiagram
python3 -m homcloud.plot_PD -d 2 -N -o superlevel.2.png -l superlevel.idiagram
python3 -m homcloud.plot_PD -d 0 -o sublevel.0.png -l sublevel.idiagram
python3 -m homcloud.plot_PD -d 1 -o sublevel.1.png -l sublevel.idiagram
python3 -m homcloud.plot_PD -d 2 -o sublevel.2.png -l sublevel.idiagram
