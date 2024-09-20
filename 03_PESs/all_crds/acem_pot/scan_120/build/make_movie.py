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
 C1     1.099299   -0.880605    0.000000
 C2     0.000000    0.168255    0.000000
 N3    -1.279608   -0.335534    0.000000
 H4    -2.054281    0.315050    0.000000
 H5    -1.466279   -1.327585    0.000000
 O6     0.221592    1.381257    0.000000
 H7     2.069964   -0.371460    0.000000
 H8     1.019661   -1.521610    0.892247
 H9     1.019661   -1.521610   -0.892247
--
1 1
 K   O6   R   C2   120.0   C1   0.0
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

