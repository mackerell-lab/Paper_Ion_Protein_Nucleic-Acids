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

   C1  3.71755  1.26656  0.00000
   H2  2.96469  2.06129  0.00000
   H3  4.35375  1.36922  0.89102
   H4  4.35375  1.36922 -0.89102
   C5  3.02992 -0.07682  0.00000
   O6  1.77650 -0.19076  0.00000
   N7  3.80784 -1.16679  0.00000
   H8  4.81243 -1.03678  0.00000
   C9  3.25661 -2.52130  0.00000
   H10  2.64089 -2.67967  0.89518
   H11  2.64089 -2.67967 -0.89518
   H12  4.08898 -3.23269  0.00000
   LI13  0.00000  0.00000  0.00000
--
0 1

   O14 LI13 DISTANCE O6 180.00000 N7    0.00000
   C15 O14  1.25859 LI13 168.67732 N7  0.00000
   C16 C15  1.50914 O14 122.30026 N7  0.00000
   H17 C16  1.09471 C15 109.44361 O14  0.00000
   H18 C16  1.09964 C15 110.28702 O14 -120.24610
   H19 C16  1.09964 C15 110.28702 O14 120.24610
   N20 O14  2.25366 C15 30.85760 C16 180.00000
   H21 N20  1.01297 O14 146.96224 C15  0.00000
   C22 N20  1.46238 O14 93.51949 C15 180.00000
   H23 C22  1.09797 N20 110.18023 H21 -119.70066
   H24 C22  1.09797 N20 110.18023 H21 119.70066
   H25 C22  1.09494 N20 108.37475 H21  0.00000



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
