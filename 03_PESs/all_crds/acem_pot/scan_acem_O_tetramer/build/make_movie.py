# Imports
# -------

import psi4
import numpy as np

# Configurations
# --------------

psi4.set_memory('1000mb')
psi4.core.set_num_threads(1)


zmatrix = ''' \

 
2 1

   C1  0.60340 -2.72902  0.00000
   C2 -0.87331 -2.38704  0.00000
   N3 -1.75020 -3.39301  0.00000
   H4 -2.74519 -3.18830  0.00000
   H5 -1.45752 -4.36366  0.00000
   O6 -1.24311 -1.17862  0.00000
   H7  1.20046 -1.80562  0.00000
   H8  0.87295 -3.32900  0.88330
   H9  0.87295 -3.32900 -0.88330
   K10  0.00000 -0.00000  1.91854
   K11  0.00000 -0.00000 -1.91854
--
0 1

   O12 O6   R       C2 116.45935 N3 180.00000
   C13 O12  1.26373 O6 116.45935 N3 180.00000
   N14 C13  1.33451 O12 121.90670 N3 180.00000
   H15 N14  1.01583 C13 119.45202 O12  0.00000
   H16 N14  1.01381 C13 122.14223 O12 180.00000
   C17 C13  1.51579 O12 120.05433 N14 180.00000
   H18 C17  1.09962 C13 109.84699 O12  0.00000
   H19 C17  1.10130 C13 111.18382 O12 -120.66299
   H20 C17  1.10130 C13 111.18382 O12 120.66299

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

