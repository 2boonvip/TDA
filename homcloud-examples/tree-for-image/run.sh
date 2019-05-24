#!/bin/sh

# python3 -m homcloud.pict.merge_tree_levelset -o output.pmt -T picture2d input.png -t msgpack
# python3 -m homcloud.plot_PD -d 0 -l -x "[-0.5:90]" -X 91 -o output.0.png output.pmt
# python3 -m homcloud.dump_diagram -d 0 -o output.0.txt output.pmt
python3 show_volume.py
