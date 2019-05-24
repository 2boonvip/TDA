# About this example

This example computes a persistence diagram for a given 
point cloud and optimal cycles.

# Input data

input.txt 

5000 points in 3D are contained in the file.
These points are randomly generated.

# How to run the example

Type:

    sh run.sh
    
and the following files are generated.
* output.idiagram - This file contains all persistence data.
* output.1.png - The 1st persistence diagram 
* output.1.txt - The list of all 1st birth-death pairs
* output.2.png - The 2nd persistence diagram 
* output.2.txt - The list of all 2nd birth-death pairs

# How to use GUI

After `sh run.sh`, please type as follows:

    python3 -m homcloud.plot_PD_gui -d $D output.idiagram
    
where `$D` is the degree of the persistent homology.
Probably, using log-scale is better in many cases. If you want to do so,
please click `log` radiobutton and click `Replot` button.

If you want to compute the volume optimal cycle of a clicked birth-death pair,
please add `--optimal-cycle on` option. To compute the volume optimal cycles
interactively from GUI, you should adjust the parameters in right-top panel.
Please switch `Query volume optimal cycle` checkbox on and
change `cutoff-radius` to `0.5`. After that, click a birth-death pair
in the diagram and optimal cycle is shown in the `paraview` window.
