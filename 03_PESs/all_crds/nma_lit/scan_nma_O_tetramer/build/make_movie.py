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


   C1  3.33593  1.23237  0.00000
   H2  2.58149  2.02619  0.00000
   H3  3.97556  1.34045  0.88882
   H4  3.97556  1.34045 -0.88882
   C5  2.66580 -0.11455  0.00000
   O6  1.37352 -0.22161  0.00000
   N7  3.41379 -1.20099  0.00000
   H8  4.42295 -1.06967  0.00000
   C9  2.88359 -2.57182  0.00000
   H10  2.27798 -2.73987  0.89928
   H11  2.27798 -2.73987 -0.89928
   H12  3.73126 -3.26392  0.00000
   LI13 -0.00000  0.00000  1.27199
   LI14 -0.00000  0.00000 -1.27199
--
0 1

   O15 O6   DISTANCE C5 166.09911 N7 180.00000
   C16 O15  1.29670 O6 166.09911 N7  0.00000
   C17 C16  1.50442 O15 121.18749 N7  0.00000
   H18 C17  1.09514 C16 110.00513 O15  0.00000
   H19 C17  1.10036 C16 110.29591 O15 -120.54609
   H20 C17  1.10036 C16 110.29591 O15 120.54609
   N21 O15  2.26315 C16 30.37794 C17 180.00000
   H22 N21  1.01767 O15 146.94390 C16  0.00000
   C23 N21  1.46979 O15 94.49712 C16 180.00000
   H24 C23  1.09714 N21 109.99726 H22 -119.27856
   H25 C23  1.09714 N21 109.99726 H22 119.27856
   H26 C23  1.09432 N21 108.08540 H22  0.00000


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
