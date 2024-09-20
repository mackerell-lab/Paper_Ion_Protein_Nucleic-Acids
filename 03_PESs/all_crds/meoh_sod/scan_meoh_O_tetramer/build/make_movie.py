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
   C1  1.54912  2.27077  0.00000
   O2  1.36880  0.79736  0.00000
   H3  2.26650  0.42290  0.00000
   H4  0.54211  2.70404  0.00000
   H5  2.09541  2.58023  0.89871
   H6  2.09541  2.58023 -0.89871
   NA7 0.00000  0.00000 -1.82543
   NA8 0.00000  0.00000  1.82543

--
0 1
   O9 O2   DISTANCE  NA7 49.04846 C1 119.82377
   C10 O9  1.48440 O2 127.19903 C1 180.00000
   H11 O9  0.97267 C10 105.66513 O2 180.0000
   H12 C10  1.09627 O9 106.30282 H11 180.00000
   H13 C10  1.09630 O9 109.92040 H11 60.68462
   H14 C10  1.09630 O9 109.92040 H11 -60.68462


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
