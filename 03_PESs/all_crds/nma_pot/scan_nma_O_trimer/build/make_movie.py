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


   C1  4.39436  1.33599  0.00000
   H2  3.66180  2.14952  0.00000
   H3  5.03342  1.42000  0.89092
   H4  5.03342  1.42000 -0.89092
   C5  3.65690  0.01968  0.00000
   O6  2.40721 -0.04997  0.00000
   N7  4.39853 -1.10393  0.00000
   H8  5.40767 -1.02665  0.00000
   C9  3.77023 -2.42047  0.00000
   H10  3.14428 -2.54302  0.89479
   H11  3.14428 -2.54302 -0.89479
   H12  4.55503 -3.18436  0.00000
   K13  0.00000  0.00000  0.00000
--
0 1

   O14 K13  DISTANCE O6  180.00000 N7  0.00000
   C15 O14  1.25163 K13 175.62101 N7  0.00000
   C16 C15  1.50881 O14 122.44939 N7  0.00000
   H17 C16  1.09474 C15 108.73850 O14  0.00000
   H18 C16  1.09963 C15 110.53006 O14 -120.10080
   H19 C16  1.09963 C15 110.53006 O14 120.10080
   N20 O14  2.25304 C15 31.08123 C16 180.00000
   H21 N20  1.01210 O14 147.72924 C15  0.00000
   C22 N20  1.45878 O14 92.37927 C15 180.00000
   H23 C22  1.09886 N20 110.24273 H21 -119.78470
   H24 C22  1.09886 N20 110.24273 H21 119.78470
   H25 C22  1.09519 N20 108.71454 H21  0.00000


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
