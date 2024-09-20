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
   C1  2.30269  1.33313  2.77617
   H2  2.51981  0.55008  3.51602
   H3  1.87544  2.22152  3.26107
   H4  3.25187  1.61991  2.29593
   C5  1.35775  0.79833  1.69748
   O6  0.52797  1.60730  1.16638
   O7  1.46647 -0.42708  1.36136
   LI8 -0.01504 -0.00365  0.01385
--
-1 1
   C9 LI8  R       C5 179.51096 O6 95.54293
   O10 C9  1.27527 LI8 61.73644 O6  8.89332
   O11 C9  1.27486 LI8 62.01430 O6 -170.55886
   C12 C9  1.53047 LI8 178.08526 C1 -7.87602
   H13 C12  1.09849 C9 110.67865 LI8 123.20262
   H14 C12  1.10169 C9 108.40649 LI8  4.32869
   H15 C12  1.09897 C9 110.35227 LI8 -113.71445

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

