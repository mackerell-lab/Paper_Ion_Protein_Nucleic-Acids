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
   C1  2.85474  1.66494  3.52758
   H2  2.92820  0.86915  4.27554
   H3  2.32981  2.51631  3.97277
   H4  3.83347  1.94470  3.11321
   C5  1.99850  1.13206  2.34551
   O6  1.27619  1.96098  1.72575
   O7  2.02889 -0.11050  2.11449
   CS8 -1.30577 -0.24797  1.21361
   CS9  1.30414  0.24571 -1.21215
--
-1 1
   C10 C5  DISTANCE CS9 28.32180 CS8 -0.01130
   O11 C10  1.26224 C5 63.86187 O6 -0.00046
   O12 C10  1.26426 C5 60.67954 O6 179.29907
   C13 C10  1.55450 C5 176.08285 C1 -16.17353
   H14 C13  1.09514 C10 109.58281 CS9 121.99076
   H15 C13  1.09899 C10 107.02600 CS9 -0.46566
   H16 C13  1.09417 C10 106.50982 CS9 -120.70227


'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 6.0, 0.1))
    long_range_distances = list(np.arange(6.0, 10.1, 0.1))
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
