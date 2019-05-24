@echo off
@setlocal enabledelayedexpansion
cd %~dp0
set padding=4
mkdir diagrams vects

for /l %%i in (0, 1, 99) do (
    set NUM=%%i
    set N=0000!NUM!
    set N=!N:~-4!
    echo !N! 
    homcloud-pict-binarize -t 128 -m white-base -I -D picts/!N!.png diagrams/!N!.idiagram
    homcloud-vectorize-PD -x "[-40.5:10.5]" -X 51 -y "[-30.5:20.5]" -Y 51 -D 2.0 -C 0.5 -p 1.0 -d 0 -H histoinfo.json -o vects/!N!.txt diagrams/!N!.idiagram
)

