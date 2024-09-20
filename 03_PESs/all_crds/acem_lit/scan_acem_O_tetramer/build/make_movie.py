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

   C1  0.90913 -3.46113  0.00000
   C2 -0.34882 -2.64175  0.00000
   N3 -1.51465 -3.26456  0.00000
   H4 -2.38556 -2.74102  0.00000
   H5 -1.56533 -4.27946  0.00000
   O6 -0.30838 -1.35098  0.00000
   H7  1.78574 -2.80560  0.00000
   H8  0.93596 -4.11062  0.88819
   H9  0.93596 -4.11062 -0.88819
   LI10 -0.00000  0.00000  1.28320
   LI11 -0.00000  0.00000 -1.28320
--
0 1

   O12 O6   R       C2 168.93638 N3 180.00000
   C13 O12  1.29139 O6 168.93638 N3  0.00000
   N14 C13  1.32176 O12 119.90682 N3 180.00000
   H15 N14  1.01616 C13 120.87625 O12  0.00000
   H16 N14  1.01617 C13 120.97085 O12 180.00000
   C17 C13  1.50128 O12 121.28417 N14 180.00000
   H18 C17  1.09461 C13 110.13192 O12  0.00000
   H19 C17  1.10065 C13 110.02842 O12 -120.80499
   H20 C17  1.10065 C13 110.02842 O12 120.80499

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

