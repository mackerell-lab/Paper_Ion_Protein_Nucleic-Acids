# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \

2 1
   C1  1.45371  2.20526  0.00000
   O2  1.23892  0.71451  0.00000
   H3  2.13386  0.32572  0.00000
   H4  0.45452  2.65548  0.00000
   H5  2.00774  2.48177  0.90345
   H6  2.00774  2.48177 -0.90345
   LI7 -0.00000  0.00000 -1.43155
   LI8 -0.00000  0.00000  1.43155

--
0 1
   O9  O2  DISTANCE       LI7 45.02710 C1 119.08010
   C10 O9  1.50615 O2 128.17181 C1 180.00000
   H11 O9  0.97574 C10 105.28278 O2 180.00000
   H12 C10  1.09594 O9 106.05661 H11 180.00000
   H13 C10  1.09527 O9 108.78478 H11 60.60659
   H14 C10  1.09527 O9 108.78478 H11 -60.60659

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(0.5, 6.1, 0.1))
    long_range_distances = list(np.arange(6.0, 11.0, 0.1))
    distances = short_range_distances + long_range_distances
    
    print (distances)
#    import sys
#    sys.exit(0)

    for distance in distances:

        distance_zmatrix = zmatrix.replace('DISTANCE', str(distance))

        universe = psi4.geometry(distance_zmatrix)
        universe.update_geometry()
        universe.print_out()

        universe.save_xyz_file('%.1f.xyz' % distance, False)

        counter += 1
