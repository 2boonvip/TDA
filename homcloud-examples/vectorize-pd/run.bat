homcloud-pc2diphacomplex -d 3 --no-square -I input.txt input.icomplex
homcloud-dipha input.icomplex output.idiagram
homcloud-plot-PD -d 1 -l -x "0:0.5" -X 64 -o pd.png output.idiagram
homcloud-vectorize-PD -d 1 -x "0:0.5" -X 64 -D 0.008 -C 30 -p 3.0 -H histoinfo.json -o vector.txt output.idiagram
homcloud-view-vectorized-PD vector.txt histoinfo.json -o vectorized-pd.png
