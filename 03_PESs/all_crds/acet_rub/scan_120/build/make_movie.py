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
 C1     0.041766   -1.351919    0.000000
 H2     1.077266   -1.728007    0.000000
 H3    -0.491434   -1.732622    0.888337
 H4    -0.491434   -1.732622   -0.888337
 C5     0.000000    0.204165    0.000000
 O6    -1.167196    0.710388    0.000000
 O7     1.124071    0.799583    0.000000
--
1 1
 RB   O6   R   C5   120.0   C1   0.0
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

