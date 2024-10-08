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

   C1  0.82150 -3.85163  0.00000
   C2 -0.42521 -3.00377  0.00000
   N3 -1.60166 -3.65170  0.00000
   H4 -2.46579 -3.12321  0.00000
   H5 -1.64618 -4.66198  0.00000
   O6 -0.38519 -1.75106  0.00000
   H7  1.70453 -3.20520  0.00000
   H8  0.83890 -4.49617  0.89080
   H9  0.83890 -4.49617 -0.89080
   LI10 -0.00000  0.00000  0.00000
--
0 1
   O11 LI10   R       O6   180.00000 N3  0.00000
   C12 O11  1.25335 LI10 169.42391 N3  0.00000
   N13 C12  1.34307 O11 120.67387 N3 180.00000
   H14 N13  1.01293 C12 119.70670 O11  0.00000
   H15 H14  1.74344 C12 65.30837 O11 180.00000
   C16 C12  1.50770 O11 122.38868 N13 180.00000
   H17 C16  1.09436 C12 109.57530 N13 180.00000
   H18 C16  1.09967 C12 110.04119 N13 59.57322
   H19 C16  1.09967 C12 110.04119 N13 -59.57322

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

