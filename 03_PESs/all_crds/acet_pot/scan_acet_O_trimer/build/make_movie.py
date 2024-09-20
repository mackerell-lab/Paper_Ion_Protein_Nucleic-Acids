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
   C1  2.71045  1.51952  3.12927
   H2  2.72633  0.84373  3.99637
   H3  2.43977  2.53887  3.43821
   H4  3.72514  1.54086  2.70052
   C5  1.74023  0.99533  2.06445
   O6  1.08202  1.86334  1.40122
   O7  1.68818 -0.27052  1.91350
   K8 -0.04468 -0.00165  0.03762
--
-1 1

   C9 K8   R       C5 177.34116 O6 91.89560
   O10 C9  1.27552 K8 63.14347 O6  4.91658
   O11 C9  1.27557 K8 63.18104 O6 -175.26717
   C12 C9  1.53309 K8 179.01315 C1 -21.39068
   H13 C12  1.09877 C9 110.95454 K8 134.07612
   H14 C12  1.10172 C9 108.67751 K8 14.39843
   H15 C12  1.09975 C9 110.09227 K8 -103.25660

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
