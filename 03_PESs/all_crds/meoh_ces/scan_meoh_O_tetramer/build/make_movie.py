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
   C1  2.58093  2.91276  0.00000
   O2  2.05467  1.51844  0.00000
   H3  2.86215  0.99065  0.00000
   H4  1.72633  3.59320  0.00000
   H5  3.24169  3.05077  0.86892
   H6  3.24169  3.05077 -0.86892
   CS7  0.00000  0.00000 -2.34379
   CS8  0.00000  0.00000  2.34379
--
0 1
   O9 O2  DISTANCE CS7 42.53268 C1 136.30644
   C10 O9  1.49033 O2 147.14302 C1 180.00000
   H11 O9  0.96467 C10 102.49174 O2 180.00000
   H12 C10  1.09241 O9 107.84897 H11 180.00000
   H13 C10  1.10030 O9 109.23239 H11 56.76086
   H14 C10  1.10030 O9 109.23239 H11 -56.76086

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(0.5, 6.1, 0.1))
    long_range_distances = list(np.arange(6.0, 11.0, 1.0))
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
