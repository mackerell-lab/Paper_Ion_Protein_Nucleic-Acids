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
   C1  2.31292  1.29210  3.16063
   H2  2.14282  0.53280  3.93798
   H3  1.95971  2.26122  3.53045
   H4  3.39950  1.33498  3.02472
   C5  1.53631  0.86832  1.92046
   O6  0.82614  1.74561  1.33670
   O7  1.63784 -0.35730  1.59404
   RB8 -0.98587 -0.64845  1.09508
   RB9  1.01963  0.67347 -1.13401
--
-1 1
   C10 C5   DISTANCE   RB9 32.82632 RB8 -0.04985
   O11 C10  1.27070 C5 64.09892 O6 -0.01518
   O12 C10  1.27239 C5 62.42498 O6 174.69903
   C13 C10  1.52338 C5 172.57596 C1 -0.13867
   H14 C13  1.09989 C10 107.70994 RB9 149.31601
   H15 C13  1.09589 C10 114.55391 RB9 32.23870
   H16 C13  1.09577 C10 110.88201 RB9 -91.74491

'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.0, 0.1))
    long_range_distances = list(np.arange(6.0, 8.5, 0.1))
    distances = short_range_distances + long_range_distances
    
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
