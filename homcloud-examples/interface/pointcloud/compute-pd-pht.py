import numpy as np
import homcloud.interface as hc


pds = hc.PDs.from_alpha_filtration(np.loadtxt("input.txt"),
                                   no_squared=True, save_to="output.idiagram")
pds[2].phtrees(save_to="output.2.pht")
