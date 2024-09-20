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
 C1    -0.046835    0.671162    0.000000
 O2    -0.046835   -0.763724    0.000000
 H3     0.872175   -1.060525    0.000000
 H4    -1.100154    0.979151    0.000000
 H5     0.441831    1.082095    0.899440
 H6     0.441831    1.082095   -0.899440
--
1 1
 CS   H3   DISTANCE   O2   180.0   C1   0.0

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.0, 6.1, 0.1))
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
