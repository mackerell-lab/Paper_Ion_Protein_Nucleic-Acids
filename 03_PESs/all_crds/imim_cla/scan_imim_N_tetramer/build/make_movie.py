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
   C1 -2.07288 -4.01550  0.00000
   H2 -2.70552 -4.89588  0.00000
   C3 -2.38036 -2.66415  0.00000
   H4 -3.33876 -2.15789  0.00000
   N5 -0.69338 -4.08819  0.00000
   H6 -0.14348 -4.93835  0.00000
   N7 -1.19104 -1.98672  0.00000
   H8 -0.99570 -0.96381  0.00000
   C9 -0.17161 -2.83878  0.00000
   H10  0.87338 -2.55413  0.00000
   CL11  0.00000  0.00000  1.86618
   CL12  0.00000  0.00000 -1.86618
   X13  0.00000  0.00000  0.00000
--
1 1

   N14 X13   R       N7 180.00000 C3 180.00000
   H15 N14  1.04140 X13 20.13107 C3 180.00000
   C16 N14  1.32862 H15 119.07768 X13  0.00000
   H17 C16  1.08307 N14 124.87316 H15  0.00000
   N18 C16  1.35398 N14 107.22333 H17 180.00000
   H19 N18  1.01251 C16 124.43848 N14 180.00000
   C20 N18  1.38141 C16 109.65000 N14  0.00000
   H21 C20  1.08411 N18 122.68519 C16 180.00000
   C22 N14  1.36872 C16 110.44482 N18  0.00000
   H23 H21  2.81026 N14 40.52338 C20 180.0000

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

