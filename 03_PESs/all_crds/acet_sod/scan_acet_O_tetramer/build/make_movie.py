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
    C1            2.303471137364     1.318101872284     2.774085170019
    H2            2.479761882992     0.544904502943     3.531957190048
    H3            1.886910813277     2.227001221350     3.225317079269
    H4            3.273184459631     1.577218967472     2.322078259724
    C5            1.388195404996     0.796522155222     1.683460161039
    O6            0.651175577516     1.625834182889     1.042298275634
    O7            1.390840125185    -0.457127316946     1.417990108354
    NA8          -0.929101153887    -0.176194209842     0.854409943738
    NA9           0.926510645283     0.175437589492    -0.851940290700
--
-1 1
    C10    C5   DISTANCE  NA9    28.81   NA8  0.0
    O11    C10  1.28143   C5     61.03   O6   0.0
    O12    C10  1.28143   C5     61.03   O6   180.0
    C13    C10  1.51632   C5    180.00   C1   180.00
    H14    C13  1.09695   C10   110.57905  NA9 298.41405
    H15    C13  1.09695   C10   108.50357  NA9 180.21057
    H16    C13  1.09695   C10   110.57905  NA9 61.97309
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.0, 0.1))
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
