homcloud-pict-pixel-levelset -m sublevel -I input.png sublevel.icomplex
homcloud-dipha sublevel.icomplex sublevel.idiagram
homcloud-dump-diagram -d 0 sublevel.idiagram -o sublevel.0.txt
homcloud-dump-diagram -d 1 sublevel.idiagram -o sublevel.1.txt
homcloud-plot-PD -d 0 -x "[-0.5:255.5]" -X 256 -l -o sublevel.0.png sublevel.idiagram
homcloud-plot-PD -d 1 -x "[-0.5:255.5]" -X 256 -l -o sublevel.1.png sublevel.idiagram
homcloud-view-index-pict -d 0 -o sublevel.0.birth.png -B -L -s 5 -f "lifetime > 20" input.png sublevel.idiagram
homcloud-view-index-pict -d 1 -o sublevel.1.death.png -D -L -s 5 -f "lifetime > 30" input.png sublevel.idiagram

homcloud-pict-pixel-levelset -m superlevel -I input.png superlevel.icomplex
homcloud-dipha superlevel.icomplex superlevel.idiagram
homcloud-dump-diagram -d 0 superlevel.idiagram -o superlevel.0.txt
homcloud-dump-diagram -d 1 superlevel.idiagram -o superlevel.1.txt
homcloud-plot-PD -d 0 -x "[-0.5:255.5]" -X 256 -N -l -o superlevel.0.png superlevel.idiagram
homcloud-plot-PD -d 1 -x "[-0.5:255.5]" -X 256 -N -l -o superlevel.1.png superlevel.idiagram
homcloud-view-index-pict -d 0 -o superlevel.0.birth.png -N -B -L -s 5 -f "lifetime < -30" input.png superlevel.idiagram
homcloud-view-index-pict -d 1 -o superlevel.1.death.png -N -D -L -s 5 -f "lifetime < -20" input.png superlevel.idiagram
