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
 C1      0.000000    0.513942    0.000000
 N2      0.628754    1.703580    0.000000
 H3      0.109407    2.571793    0.000000
 H4      1.638743    1.762759    0.000000
 N5     -1.342220    0.473050    0.000000
 H6     -1.890262    1.323784    0.000000
 H7     -1.839824   -0.407373    0.000000
 N8      0.700723   -0.623756    0.000000
 H9      1.712010   -0.555355    0.000000
 C10     0.085273   -1.957243    0.000000
 H11     0.892679   -2.697454    0.000000
 H12    -0.522596   -2.104233    0.905528
 H13    -0.522596   -2.104233   -0.905528
--
-1 1
 cl   H3   R   N2   180.0   C1   0.0

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

