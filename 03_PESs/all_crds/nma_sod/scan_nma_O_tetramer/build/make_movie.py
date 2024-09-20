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

   C1  3.51777  1.28756  0.00000
   H2  2.76764  2.08548  0.00000
   H3  4.15834  1.39248  0.88812
   H4  4.15834  1.39248 -0.88812
   C5  2.83381 -0.05619  0.00000
   O6  1.55627 -0.16130  0.00000
   N7  3.59894 -1.14304  0.00000
   H8  4.60635 -1.01128  0.00000
   C9  3.06601 -2.50833  0.00000
   H10  2.45580 -2.67816  0.89653
   H11  2.45580 -2.67816 -0.89653
   H12  3.90826 -3.20711  0.00000
   NA13 -0.00000  0.00000  1.65254
   NA14 -0.00000  0.00000 -1.65254

--
0 1

   O15 O6   DISTANCE  C5 169.37914 N7 180.00000
   C16 O15  1.28186 O6 169.37914 N7  0.00000
   C17 C16  1.50780 O15 121.67938 N7  0.00000
   H18 C17  1.09515 C16 109.79255 O15  0.00000
   H19 C17  1.10005 C16 110.43524 O15 -120.50671
   H20 C17  1.10005 C16 110.43524 O15 120.50671
   N21 O15  2.26634 C16 30.37337 C17 180.00000
   H22 N21  1.01600 O15 146.87872 C16  0.00000
   C23 N21  1.46561 O15 94.34713 C16 180.00000
   H24 C23  1.09771 N21 110.25899 H22 -119.47380
   H25 C23  1.09771 N21 110.25899 H22 119.47380
   H26 C23  1.09439 N21 108.35849 H22  0.00000


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
