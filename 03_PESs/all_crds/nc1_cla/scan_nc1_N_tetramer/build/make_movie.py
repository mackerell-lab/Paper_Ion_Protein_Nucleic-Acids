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
   N1 -1.24229  0.65274  1.37137
   C2 -0.60103  0.85212  2.69440
   H3 -2.23518  0.88764  1.38229
   H4 -1.12119 -0.35753  1.07006
   H5 -0.74568  1.24761  0.64624
   H6  0.45411  0.57812  2.59095
   H7 -1.08073  0.20325  3.43565
   H8 -0.68254  1.90494  2.98632
   CL9  0.50326  2.15206 -0.56824
   CL10 -0.50326 -2.15206  0.56824
   X11  0.00000  0.00000  0.00000
--
1 1

   N12 X11   R     N1  180.00000 C2    0.00000
   C13 N12  1.48370 X11 113.22175 C2 -180.00000
   H14 N12  1.02036 C13 112.33903 X11 -179.98669
   H15 N12  1.06117 C13 109.37845 X11 -58.21926
   H16 N12  1.06128 C13 109.37211 X11 58.22307
   H17 C13  1.09503 N12 107.37311 H14 -179.99354
   H18 C13  1.09571 N12 109.53879 H14 -60.89179
   H19 C13  1.09558 N12 109.54716 H14 60.91967

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

