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
   C1  1.94569  2.73184  0.00000
   O2  1.82653  1.27923  0.00000
   H3  2.72571  0.92339  0.00000
   H4  0.92627  3.13292  0.00000
   H5  2.47167  3.07049  0.90119
   H6  2.47167  3.07049 -0.90119
   NA7 -0.00000  0.00000  0.00000

--
0 1
   O8 NA7  DISTANCE O2 180.00000 C1  0.0000
   C9 O8  1.45749 NA7 129.69516 C1 180.0000
   H10 O8  0.96703 C9 106.90148 O2 180.00000
   H11 C9  1.09548 O8 106.78769 H10 180.00000
   H12 C9  1.09704 O8 110.29539 H10 61.14625
   H13 C9  1.09704 O8 110.29539 H10 -61.14625

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
