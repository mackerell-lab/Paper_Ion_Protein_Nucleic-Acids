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

   C1  0.92842 -3.64136  0.00000
   C2 -0.32716 -2.81049  0.00000
   N3 -1.49317 -3.45572  0.00000
   H4 -2.36764 -2.94103  0.00000
   H5 -1.53345 -4.46954  0.00000
   O6 -0.28835 -1.53429  0.00000
   H7  1.80776 -2.98915  0.00000
   H8  0.95391 -4.29108  0.88755
   H9  0.95391 -4.29108 -0.88755
   NA10  0.00000  0.00000  1.66905
   NA11  0.00000  0.00000 -1.66905
--
0 1

   O12 O6   R       C2 171.09768 N3 180.00000
   C13 O12  1.27680 O6 171.09768 N3  0.00000
   N14 C13  1.33263 O12 120.70019 N3 180.00000
   H15 N14  1.01469 C13 120.56151 O12  0.00000
   H16 N14  1.01461 C13 121.23378 O12 180.00000
   C17 C13  1.50559 O12 121.75246 N14 180.00000
   H18 C17  1.09481 C13 109.94171 O12  0.00000
   H19 C17  1.10024 C13 110.19460 O12 -120.73701
   H20 C17  1.10024 C13 110.19460 O12 120.73701

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

