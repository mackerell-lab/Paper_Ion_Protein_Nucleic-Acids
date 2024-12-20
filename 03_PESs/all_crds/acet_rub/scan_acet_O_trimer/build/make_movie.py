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
   C1  3.06096  1.68199  3.32978
   H2  3.19287  0.97489  4.15639
   H3  2.77949  2.66746  3.71486
   H4  4.00599  1.75653  2.77837
   C5  2.01528  1.15259  2.32191
   O6  1.30472  2.00043  1.68370
   O7  1.95377 -0.11108  2.13818
   RB8 -0.04387 -0.00054  0.03770
--
-1 1
   C9 RB8  R       C5 177.36022 O6 95.14456
   O10 C9  1.27857 RB8 61.50930 O6  4.27837
   O11 C9  1.27698 RB8 62.40202 O6 -174.38841
   C12 C9  1.54576 RB8 176.14526 C1 -8.97669
   H13 C12  1.09472 C9 111.40378 RB8 125.59464
   H14 C12  1.09665 C9 106.22348 RB8  5.99837
   H15 C12  1.09582 C9 110.53000 RB8 -111.45381
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

