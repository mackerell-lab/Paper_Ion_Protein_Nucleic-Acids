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
   C1  1.25192  1.82652  0.00000
   O2  1.52687  0.39328  0.00000
   H3  2.48953  0.26614  0.00000
   H4  0.15610  1.92752  0.00000
   H5  1.66375  2.31777  0.89281
   H6  1.66375  2.31777 -0.89281
   K7  0.00000 -0.00000 -2.17679
   K8  0.00000 -0.00000  2.17679
--
0 1

   O9  O2  DISTANCE K7 54.08312 C1 92.90431
   C10 O9  1.45937 O2 93.58454 C1 180.00000
   H11 O9  0.97102 C10 108.38339 O2 180.00000
   H12 C10  1.10047 O9 106.12535 H11 180.00000
   H13 C10  1.09911 O9 111.61406 H11 60.89632
   H14 C10  1.09911 O9 111.61406 H11 -60.89632
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(0.5, 6.1, 0.1))
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
