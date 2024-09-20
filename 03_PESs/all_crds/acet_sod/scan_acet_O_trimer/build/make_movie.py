# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \

0 1
   C1  2.49392  1.44488  3.02259
   H2  2.64829  0.68060  3.79745
   H3  2.09318  2.36919  3.46118
   H4  3.47370  1.67072  2.57144
   C5  1.56483  0.91398  1.92368
   O6  0.79526  1.75413  1.35193
   O7  1.64680 -0.32768  1.64605
   NA8 -0.00386 -0.00107  0.00376
--
-1 1
   C9 NA8  R        C5 179.89731 O6 0.00000
   O10 C9  1.27498 NA8 62.78182 O6  0.000000
   O11 C9  1.27478 NA8 62.87813 O6 -169.95831
   C12 C9  1.53396 NA8 179.03772 C1 -12.61893
   H13 C12  1.09872 C9 110.87696 NA8 125.86411
   H14 C12  1.10206 C9 108.42892 NA8  6.98379
   H15 C12  1.09924 C9 110.44935 NA8 -110.95718

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.2, 10.1, 0.1))
    distances = short_range_distances 
    
    print (distances)
#    import sys
#    sys.exit(0)

    for distance in distances:

        distance_zmatrix = zmatrix.replace(' R ', str(distance))

        universe = psi4.geometry(distance_zmatrix)
        universe.update_geometry()
        universe.print_out()

        universe.save_xyz_file('%.1f.xyz' % distance, False)

        counter += 1

