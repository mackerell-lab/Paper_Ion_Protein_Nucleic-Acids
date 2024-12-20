# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \



0 1
   C1 -2.38333 -4.56495  0.00000
   H2 -3.15505 -5.32716  0.00000
   C3 -2.46130 -3.18304  0.00000
   H4 -3.32318 -2.52462  0.00000
   N5 -1.03750 -4.86991  0.00000
   H6 -0.64137 -5.80448  0.00000
   N7 -1.17138 -2.70690  0.00000
   H8 -0.84599 -1.69271  0.00000
   C9 -0.31074 -3.73095  0.00000
   H10  0.77067 -3.65277  0.00000
   CL11 -0.00000  0.00000  0.00000
--
1 1
   N12 CL11   R        N7 180.00000 C3 180.0000
   H13 N12  1.06512 CL11  5.61155 C3 180.00000
   C14 N12  1.33767 H13 122.16675 CL11  0.00000
   H15 C14  1.08423 N12 125.90984 H13  0.00000
   N16 C14  1.35108 N12 107.41388 H15 180.00000
   H17 N16  1.01505 C14 124.48832 N12 180.00000
   C18 N16  1.37995 C14 109.77384 N12  0.00000
   H19 C18  1.08467 N16 122.58782 C14 180.00000
   C20 N12  1.37498 C14 109.78433 N16  0.00000
   H21 H19  2.80758 N12 40.56064 C18 180.00000

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

