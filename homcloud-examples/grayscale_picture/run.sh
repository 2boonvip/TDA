#!/bin/sh

python3 -m homcloud.pict.pixel_levelset -m sublevel -I input.png sublevel.icomplex
python3 -m homcloud.dipha sublevel.icomplex sublevel.idiagram
python3 -m homcloud.dump_diagram -d 0 sublevel.idiagram -o sublevel.0.txt
python3 -m homcloud.dump_diagram -d 1 sublevel.idiagram -o sublevel.1.txt
python3 -m homcloud.plot_PD -d 0 -x "[-0.5:255.5]" -X 256 -l -o sublevel.0.png sublevel.idiagram
python3 -m homcloud.plot_PD -d 1 -x "[-0.5:255.5]" -X 256 -l -o sublevel.1.png sublevel.idiagram
python3 -m homcloud.view_index_pict -d 0 -o sublevel.0.birth.png -B -L -s 5 -f "lifetime > 20" input.png sublevel.idiagram
python3 -m homcloud.view_index_pict -d 1 -o sublevel.1.death.png -D -L -s 5 -f "lifetime > 30" input.png sublevel.idiagram

python3 -m homcloud.pict.pixel_levelset -m superlevel -I input.png superlevel.icomplex
python3 -m homcloud.dipha superlevel.icomplex superlevel.idiagram
python3 -m homcloud.dump_diagram -d 0 superlevel.idiagram -o superlevel.0.txt
python3 -m homcloud.dump_diagram -d 1 superlevel.idiagram -o superlevel.1.txt
python3 -m homcloud.plot_PD -d 0 -x "[-0.5:255.5]" -X 256 -N -l -o superlevel.0.png superlevel.idiagram
python3 -m homcloud.plot_PD -d 1 -x "[-0.5:255.5]" -X 256 -N -l -o superlevel.1.png superlevel.idiagram
python3 -m homcloud.view_index_pict -d 0 -o superlevel.0.birth.png -N -B -L -s 5 -f "lifetime < -30" input.png superlevel.idiagram
python3 -m homcloud.view_index_pict -d 1 -o superlevel.1.death.png -N -D -L -s 5 -f "lifetime < -20" input.png superlevel.idiagram
