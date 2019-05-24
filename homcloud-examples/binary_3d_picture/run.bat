homcloud-pict-binarize3d -m white-base -s -t 128 -I -o input.icomplex pict_01.png pict_02.png pict_03.png pict_04.png
homcloud-dipha input.icomplex output.idiagram
homcloud-plot-PD -x "[-10.5:10.5]" -X 21 -d 0 -o output.0.png output.idiagram
homcloud-plot-PD -x "[-10.5:10.5]" -X 21 -d 1 -o output.1.png output.idiagram
homcloud-plot-PD -x "[-10.5:10.5]" -X 21 -d 2 -o output.2.png output.idiagram
homcloud-dump-diagram -d 0 -o output.0.txt output.idiagram
homcloud-dump-diagram -d 1 -o output.1.txt output.idiagram
homcloud-dump-diagram -d 2 -o output.1.txt output.idiagram

homcloud-pict-binarize3d -m white-base -t 128 -I -o input_noerosion.icomplex pict_01.png pict_02.png pict_03.png pict_04.png
homcloud-dipha input_noerosion.icomplex output_noerosion.idiagram
homcloud-plot-PD -x "[-10.5:10.5]" -X 21 -d 1 -o output_noerosion.1.png output_noerosion.idiagram
homcloud-plot-PD -x "[-10.5:10.5]" -X 21 -d 2 -o output_noerosion.2.png output_noerosion.idiagram
homcloud-dump-diagram -d 1 -o output_noerosion.1.txt output_noerosion.idiagram
homcloud-dump-diagram -d 2 -o output_noerosion.2.txt output_noerosion.idiagram
