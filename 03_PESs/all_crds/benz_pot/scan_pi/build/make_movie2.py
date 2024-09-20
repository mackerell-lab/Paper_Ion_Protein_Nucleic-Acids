# Imports
# -------

import psi4
import numpy as np
import math

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \

0 1
 C1     0.000000    0.703980    1.219329
 H2     0.000000    1.251078    2.166931
 C3     0.000000   -0.703980    1.219329
 H4     0.000000   -1.251078    2.166931
 C5     0.000000    1.407959    0.000000
 H6     0.000000    2.502156   -0.000001
 C7     0.000000   -1.407959    0.000000
 H8     0.000000   -2.502156   -0.000001
 C9     0.000000    0.703979   -1.219329
 H10    0.000000    1.251078   -2.166930
 C11    0.000000   -0.703979   -1.219329
 H12    0.000000   -1.251078   -2.166930
--
1 1
 K   C11   R   C1   A   C7   90.0

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.2, 10.1, 0.1))
    distances = short_range_distances 
    
    print (distances)
#    import sys
#    sys.exit(0)

    for x in distances:

        R = math.sqrt(x**2+ 1.4**2 )

        print(R)
        ang = math.atan(x/1.4)
        A = math.degrees(ang)
        print(A)

        distance_zmatrix = zmatrix.replace(' R ', str(R)).replace(' A ', str(A))

        
        print(distance_zmatrix)
        universe = psi4.geometry(distance_zmatrix)
        universe.update_geometry()
        universe.print_out()

        universe.save_xyz_file('%.1f.xyz' % x, False)

        counter += 1

