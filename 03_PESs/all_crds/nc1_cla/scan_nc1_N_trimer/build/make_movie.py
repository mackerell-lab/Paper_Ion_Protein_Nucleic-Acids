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
   N1 -0.68352  0.63392  2.72822
   C2 -1.09919  1.35970  3.96440
   H3 -1.35329  0.67956  1.94732
   H4 -0.52079 -0.36674  2.87937
   H5  0.17984  0.98199  2.28932
   H6 -0.30791  1.25880  4.71423
   H7 -2.03084  0.91945  4.33405
   H8 -1.25133  2.41405  3.71276
   CL9  0.00000  0.00000  0.00000
--
1 1

   N10 CL9  R        N1 180.00000 C2 180.00000
   C11 N10  1.49254 CL9 163.07620 C2 180.00000
   H12 N10  1.02980 C11 115.17485 CL9 56.16813
   H13 N10  1.02501 C11 113.37823 CL9 177.11034
   H14 N10  1.02917 C11 114.98541 CL9 -61.97283
   H15 C11  1.09478 N10 108.73337 H12 178.94513
   H16 C11  1.09473 N10 108.73058 H12 -60.94651
   H17 C11  1.09459 N10 108.46283 H12 58.99920

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

