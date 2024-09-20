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
   C1  4.13912  1.15194  0.00000
   H2  3.42832  1.98458  0.00000
   H3  4.78020  1.22248  0.89074
   H4  4.78020  1.22248 -0.89074
   C5  3.38179 -0.15535  0.00000
   O6  2.12759 -0.20762  0.00000
   N7  4.11670 -1.28083  0.00000
   H8  5.12562 -1.19519  0.00000
   C9  3.50828 -2.60866  0.00000
   H10  2.88631 -2.74357  0.89511
   H11  2.88631 -2.74357 -0.89511
   H12  4.30860 -3.35619  0.00000
   NA13  0.00000  0.00000  0.00000

--
0 1

   O14 NA13 DISTANCE   O6 180.00000 N7   0.00000
   C15 O14  1.25529 NA13 172.04035 N7  0.00000
   C16 C15  1.51081 O14 122.47046 N7  0.00000
   H17 C16  1.09477 C15 109.42941 O14  0.00000
   H18 C16  1.09972 C15 110.34810 O14 -120.24525
   H19 C16  1.09972 C15 110.34810 O14 120.24525
   N20 O14  2.26016 C15 30.73496 C16 180.00000
   H21 N20  1.01255 O14 146.79955 C15  0.00000
   C22 N20  1.46059 O14 93.73139 C15 180.00000
   H23 C22  1.09831 N20 110.33844 H21 -119.63601
   H24 C22  1.09831 N20 110.33844 H21 119.63601
   H25 C22  1.09513 N20 108.42907 H21  0.00000


'''


if __name__ == '__main__':

    counter = 1

    short_range_distances = list(np.arange(1.5, 10.1, 0.1))
    #long_range_distances = list(np.arange(6.0, 11.0, 1.0))
    distances = short_range_distances # + long_range_distances
    
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
