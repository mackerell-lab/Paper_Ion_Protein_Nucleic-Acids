# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \
1 1
   C1  1.80347  2.51900  0.00000
   O2  2.20972  1.13163  0.00000
   H3  3.17511  1.08759  0.00000
   H4  0.70355  2.51106  0.00000
   H5  2.14906  3.03744  0.90354
   H6  2.14906  3.03744 -0.90354
   K7  0.00000 -0.00000  0.00000
--
0 1
   O8 K7  DISTANCE O2 180.00000 C1   0.00000
   C9 O8  1.44563 K7 100.79665 C1 180.00000
   H10 O8  0.96639 C9 108.93310 O2 180.00000
   H11 C9  1.09995 O8 105.90721 H10 180.00000
   H12 C9  1.09754 O8 111.39745 H10 62.15190
   H13 C9  1.09754 O8 111.39745 H10 -62.15190
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.1, 0.1))
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
