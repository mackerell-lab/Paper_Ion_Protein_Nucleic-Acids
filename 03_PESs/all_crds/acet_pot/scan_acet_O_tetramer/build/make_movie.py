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

    C1            2.405213718881     1.371913930476     2.872040067154
    H2            2.587697311034     0.601296337318     3.631922248613
    H3            1.995010064423     2.283563748693     3.324966176091
    H4            3.371388117991     1.627623367128     2.409497123266
    C5            1.475034989468     0.846142648621     1.787678152316
    O6            0.738578643149     1.681031734938     1.155034365690
    O7            1.480900731668    -0.408480479089     1.531645395139
    K8            1.184847401852     0.224490587762    -1.089470350497
    K9           -1.191086683870    -0.225905759631     1.095321297355
--
-1 1

    C10    C5   DISTANCE   K9     33.41   K8   0.0
    O11    C10  1.28143   C5     64.43   O6   0.0
    O12    C10  1.28143   C5     64.43   O6   180.0
    C13    C10  1.51632   C5    180.00   C1   180.00
    H14    C13  1.09695   C10   110.43487  K9 298.44172
    H15    C13  1.09695   C10   108.26511  K9 180.22677
    H16    C13  1.09695   C10   110.44284  K9 61.97356
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.0, 0.1))
    long_range_distances = list(np.arange(6.0, 10.1, 0.1))
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
