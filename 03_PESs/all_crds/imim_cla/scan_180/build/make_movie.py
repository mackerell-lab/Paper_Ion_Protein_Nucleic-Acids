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
 C1   -0.979859   -0.691537    0.000000
 H2   -1.800116   -1.403835    0.000000
 C3   -0.979859    0.691537    0.000000
 H4   -1.800116    1.403835    0.000000
 N5    0.346175   -1.079120    0.000000
 H6    0.681994   -2.040550    0.000000
 N7    0.346175    1.079120    0.000000
 H8    0.681994    2.040550    0.000000
 C9    1.151709    0.000000    0.000000
 H10   2.237838    0.000000    0.000000
--
-1 1
 cl   H6   R   N5   180.0   C1   0.0

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

