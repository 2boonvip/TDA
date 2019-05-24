#!/bin/sh

python3 -m homcloud.pc2diphacomplex -d 3 --no-square -I input.txt input.icomplex
python3 -m homcloud.dipha input.icomplex output.idiagram
python3 -m homcloud.plot_PD -d 1 -l -x "0:0.5" -X 64 -o pd.png output.idiagram
python3 -m homcloud.vectorize_PD -d 1 -x "0:0.5" -X 64 -D 0.008 -C 30 -p 3.0 -H histoinfo.json -o vector.txt output.idiagram
python3 -m homcloud.view_vectorized_PD vector.txt histoinfo.json -o vectorized-pd.png
