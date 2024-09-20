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
    C1            2.189333951208     1.247913196112     2.609780230495
    H2            2.371126854863     0.476137922689     3.367249094663
    H3            1.777669286343     2.158744940137     3.060682842529
    H4            3.152242562000     1.501940068836     2.141182172117
    C5            1.263966235131     0.725923275796     1.536815102554
    O6            0.511024597069     1.530070292048     0.880415351539
    O7            1.239837415145    -0.524028521231     1.251277485861
    LI8           0.747714657264     0.141383309210    -0.687390647662
    LI9          -0.760133621399    -0.144040546371     0.698962760699
--
-1 1
    C10    C5   DISTANCE   LI9    26.02   LI8  0.0
    O11    C10  1.28143   C5     59.55   O6   0.0
    O12    C10  1.28143   C5     59.55   O6   180.0
    C13    C10  1.51632   C5    180.00   C1   180.00
    H14    C13  1.09695   C10   110.43487  LI9 298.41249
    H15    C13  1.09695   C10   108.26511  LI9 180.18103
    H16    C13  1.09695   C10   110.44284  LI9 61.92233

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
