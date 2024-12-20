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

   C1  2.59227  1.16988  0.70489
   H2  2.68574  2.11233  1.25000
   C3  2.59227  1.16988 -0.70489
   H4  2.68574  2.11233 -1.25000
   C5  2.56230 -0.05065  1.40980
   H6  2.63195 -0.05205  2.50030
   C7  2.56230 -0.05065 -1.40980
   H8  2.63195 -0.05205 -2.50030
   C9  2.53203 -1.27124  0.70491
   H10  2.57819 -2.21700  1.25030
   C11  2.53203 -1.27124 -0.70491
   H12  2.57819 -2.21700 -1.25030
   K13  0.00000 -0.00000  0.00000
--
0 1

   X14 K13  R        C5 151.18480 C7 180.00000
   C15 X14  1.40978 K13 90.23746 C11 -0.00028
   H16 C15  1.09275 C11 93.92545 K13 179.99887
   C17 X14  1.40978 K13 90.23746 C9  0.00028
   H18 C17  1.09275 C9 93.92545 K13 -179.99887
   C19 X14  1.40980 K13 90.00000 C7  0.00000
   H20 C19  1.09273 C7 93.65531 K13 179.99900
   C21 X14  1.40980 K13 90.00000 C5  0.00000
   H22 C21  1.09273 C5 93.65531 K13 -179.99900
   C23 X14  1.40984 K13 89.75067 C3 -0.00028
   H24 C23  1.09272 C3 93.40253 K13 179.99918
   C25 X14  1.40984 K13 89.75067 C1  0.00028
   H26 C25  1.09272 C1 93.40253 K13 -179.99918

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

