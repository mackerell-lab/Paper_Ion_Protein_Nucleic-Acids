# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \



-1 1
   C1  1.72131 -2.57822  0.00000
   N2  2.31512 -1.38709  0.00000
   H3  1.70457 -0.56169  0.00000
   H4  3.31839 -1.29450  0.00000
   N5  0.39501 -2.63345  0.00000
   H6 -0.10640 -1.73543  0.00000
   H7 -0.10297 -3.50865  0.00000
   N8  2.45537 -3.72110  0.00000
   H9  3.46052 -3.63471  0.00000
   C10  1.84991 -5.04257  0.00000
   H11  2.65237 -5.78827  0.00000
   H12  1.23440 -5.19843  0.89975
   H13  1.23440 -5.19843 -0.89975
   CL14  0.00000  0.00000  1.75669
   CL15  0.00000  0.00000 -1.75669
   X16  0.00000  0.00000  0.00000
--
1 1
   C17 X16   R     C1 180.00000 N2 180.00000
   N18 C17  1.33094 X16 60.22610 N2 180.00000
   H19 N18  1.02668 C17 117.01192 X16  0.00000
   H20 N18  1.00753 C17 121.77046 H19 180.00000
   N21 C17  1.32745 N18 118.88215 H19  0.00000
   H22 N21  1.02852 C17 116.79247 N18  0.00000
   H23 N21  1.00695 C17 122.02399 N18 180.00000
   N24 C17  1.35832 N21 120.32749 N18 180.00000
   H25 N24  1.00886 C17 117.79927 N18  0.00000
   C26 N24  1.45357 C17 122.67179 N18 180.00000
   H27 C26  1.09545 N24 108.28377 C17 180.00000
   H28 C26  1.10122 N24 111.19161 C17 61.19953
   H29 C26  1.10122 N24 111.19161 C17 -61.19953

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

