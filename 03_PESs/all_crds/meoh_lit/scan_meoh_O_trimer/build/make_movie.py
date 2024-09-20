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
   C1  1.57786  2.56609  0.00000
   O2  1.49407  1.10531  0.00000
   H3  2.39965  0.76429  0.00000
   H4  0.54955  2.94172  0.00000
   H5  2.09835  2.90827  0.90215
   H6  2.09835  2.90827 -0.90215
   LI7  0.00000 -0.00000  0.00000
--
0 1
   O8 LI7 DISTANCE  O2 180.00000 C1   0.00000
   C9 O8  1.46318  LI7 129.77685 C1 180.00000
   H10 O8  0.96766 C9 107.35217 O2 180.00000
   H11 C9  1.09478 O8 106.78377 H10 180.00000
   H12 C9  1.09630 O8 109.80380 H10 61.00166
   H13 C9  1.09630 O8 109.80380 H10 -61.00166

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
