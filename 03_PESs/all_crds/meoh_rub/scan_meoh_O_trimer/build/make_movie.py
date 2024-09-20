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
   C1  1.93916  2.67753  0.00000
   O2  2.22947  1.26938  0.00000
   H3  3.17717  1.08256  0.00000
   H4  0.83523  2.69360  0.00000
   H5  2.32421  3.16505  0.90424
   H6  2.32421  3.16505 -0.90424
   RB7  0.00000  0.00000  0.00000
--
0 1
   O8 RB7  DISTANCE  O2 180.00000 C1   0.00000
   C9  O8  1.43777 RB7 108.00668 C1 180.00000
   H10 O8  0.96594 C9 112.80087 O2 180.00000
   H11 C9  1.10405 O8 102.48284 H10 180.00000
   H12 C9  1.09708 O8 111.36814 H10 62.25946
   H13 C9  1.09708 O8 111.36814 H10 -62.25946
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.1, 0.1))
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
