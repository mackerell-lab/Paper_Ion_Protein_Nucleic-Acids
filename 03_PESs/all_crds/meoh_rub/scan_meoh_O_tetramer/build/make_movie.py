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
   C1  1.58005  2.27505  0.00000
   O2  1.41259  0.82982  0.00000
   H3  2.25656  0.35050  0.00000
   H4  0.56052  2.67579  0.00000
   H5  2.10652  2.60105  0.90414
   H6  2.10652  2.60105 -0.90414
   RB7  0.00000 -0.00000 -2.16842
   RB8  0.00000 -0.00000  2.16842
--
0 1
   O9  O2  DISTANCE RB7 52.92801 C1 121.05415
   C10 O9  1.45490 O2 127.04133 C1 180.00000
   H11 O9  0.97058 C10 112.98474 O2 180.00000
   H12 C10  1.09546 O9 104.84827 H11 180.00000
   H13 C10  1.09586 O9 110.53598 H11 61.76805
   H14 C10  1.09586 O9 110.53598 H11 -61.76805

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
