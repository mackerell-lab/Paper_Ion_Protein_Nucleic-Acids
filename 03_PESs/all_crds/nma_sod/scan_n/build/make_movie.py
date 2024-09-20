# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \
0 1
 C1     1.098175     1.565263     0.000000
 H2     0.631555     2.557430     0.000000
 H3     1.735324     1.460846     0.892506
 H4     1.735324     1.460846    -0.892506
 C5     0.000000     0.514178     0.000000
 O6    -1.206163     0.792232     0.000000
 N7     0.430929    -0.785971     0.000000
 H8     1.423106    -0.979872     0.000000
 C9    -0.527406    -1.884499     0.000000
 H10   -1.171471    -1.836020     0.890708
 H11   -1.171471    -1.836020    -0.890708
 H12    0.025820    -2.832924     0.000000

--
1 1
 na   N7 DISTANCE   C5   90.0   O6   90.0
'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 10.1, 0.1))
    #long_range_distances = list(np.arange(6.0, 11.0, 1.0))
    distances = short_range_distances # + long_range_distances
    
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
