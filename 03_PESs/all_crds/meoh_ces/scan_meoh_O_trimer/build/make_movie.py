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
   C1  2.43819  3.59419  0.00000
   O2  2.48676  2.12173  0.00000
   H3  3.43815  1.94420  0.00000
   H4  1.35996  3.79567  0.00000
   H5  2.91037  3.99744  0.90679
   H6  2.91037  3.99744 -0.90679
   CS7  0.00000  0.00000  0.00000
--
0 1
   O8 CS7 DISTANCE  O2 180.00000 C1   0.00000
   C9 O8  1.47326 CS7 128.58171 C1 180.00000
   H10 O8  0.96781 C9 102.45922 O2 180.00000
   H11 C9  1.09689 O8 102.47355 H10 180.00000
   H12 C9  1.09901 O8 110.64380 H10 61.84887
   H13 C9  1.09901 O8 110.64380 H10 -61.84887
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
