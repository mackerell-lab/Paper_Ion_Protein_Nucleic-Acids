# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \
-1 1
 C1     -0.7757109984        0.0000000000        0.0000000000
 H2     -1.1729651115        0.0000407474        1.0197552121
 H3     -1.1392598432       -0.8828635382       -0.5390025931
 H4     -1.1392598432        0.8828204604       -0.5390731463
 C5      0.7757109984       -0.0000000000        0.0000000000
 O6      1.3427562678        0.0000454496        1.1374341864
 O7      1.3108656256       -0.0000460872       -1.1533921718
--
1 1
 na   O6 DISTANCE   C5   180.0   C1   0.0
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(XXXXX, XXXXX, XXXXX))
    #long_range_distances = list(np.arange(6.0, 11.0, 1.0))
    distances = short_range_distances #+ long_range_distances
    
    print (distances)
#    import sys
#    sys.exit(0)

    for distance in distances:

        distance_zmatrix = zmatrix.replace('DISTANCE', str(distance))

        universe = psi4.geometry(distance_zmatrix)
        universe.update_geometry()
        universe.print_out()

        universe.save_xyz_file('%.Xf.xyz' % distance, False)

        counter += 1
