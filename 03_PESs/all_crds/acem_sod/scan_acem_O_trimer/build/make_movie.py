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

   C1  0.87890 -4.22280  0.00000
   C2 -0.36637 -3.36968  0.00000
   N3 -1.54305 -4.02803  0.00000
   H4 -2.40985 -3.50513  0.00000
   H5 -1.58283 -5.03813  0.00000
   O6 -0.32494 -2.12005  0.00000
   H7  1.76355 -3.57850  0.00000
   H8  0.89569 -4.86785  0.89047
   H9  0.89569 -4.86785 -0.89047
   NA10 -0.00000  0.00000  0.00000
--
0 1
   O11 NA10  R       O6 180.00000   N3  0.00000
   C12 O11  1.25032 NA10 173.18479 N3  0.00000
   N13 C12  1.34833 O11 121.12551 N3 180.00000
   H14 N13  1.01231 C12 119.67278 O11  0.00000
   H15 H14  1.74185 C12 65.44634 O11 180.00000
   C16 C12  1.50947 O11 122.51605 N13 180.00000
   H17 C16  1.09441 C12 109.51910 N13 180.00000
   H18 C16  1.09969 C12 110.12811 N13 59.58918
   H19 C16  1.09969 C12 110.12811 N13 -59.58918

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

