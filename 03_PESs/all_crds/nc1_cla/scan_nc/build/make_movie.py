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
 N1     0.187573   -0.292076   -0.619553
 C2    -0.211689    0.329627    0.699207
 H3    -0.547004   -0.175354   -1.328361
 H4     0.363317   -1.299732   -0.522691
 H5     1.044612    0.134516   -0.992572
 H6     0.607295    0.173330    1.409599
 H7    -1.126662   -0.164252    1.043780
 H8    -0.384438    1.398262    0.531876
--
-1 1
 cl   N1   R   C2   180.0   H3   0.0

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

