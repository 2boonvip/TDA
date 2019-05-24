#!/bin/sh

awk '{print($1, $2)}' < data.txt > data_nolabel.txt
awk '{ if($3 == 0){print($1, $2)}}' < data.txt > data_0.txt
awk '{ if($3 == 1){print($1, $2)}}' < data.txt > data_1.txt

python3 -m homcloud.pc2diphacomplex -D -d 2 data_nolabel.txt data_nolabel.diagram
python3 -m homcloud.pc2diphacomplex -D -d 2 data_0.txt data_0.diagram
python3 -m homcloud.pc2diphacomplex -D -d 2 data_1.txt data_1.diagram

python3 -m homcloud.dump_diagram -S no -d 1 data_nolabel.diagram > data_nolabel.1.txt
python3 -m homcloud.dump_diagram -S no -d 1 data_0.diagram > data_01.1.txt
python3 -m homcloud.dump_diagram -S no -d 1 data_1.diagram >> data_01.1.txt

sort -n data_nolabel.1.txt | awk '{printf("%8f %8f\n", $1, $2)}' > nl.txt
sort -n data_01.1.txt | awk '{printf("%8f %8f\n", $1, $2)}' > 01.txt
diff -u nl.txt 01.txt > diff.txt
