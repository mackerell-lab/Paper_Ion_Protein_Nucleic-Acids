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

   C1  3.88124  1.49545  0.00000
   H2  3.36582  2.46162  0.00000
   H3  4.52233  1.42183  0.89070
   H4  4.52233  1.42183 -0.89070
   C5  2.85175  0.40376  0.00000
   O6  1.60880  0.64949  0.00000
   N7  3.26020 -0.87657  0.00000
   H8  4.25477 -1.08123  0.00000
   C9  2.29907 -1.97673  0.00000
   H10  1.66133 -1.93710  0.89636
   H11  1.66133 -1.93710 -0.89636
   H12  2.84206 -2.92716  0.00000
   K13  0.00000  0.00000  1.80414
   K14  0.00000  0.00000 -1.80414
--
0 1

   O15 O6   DISTANCE  C5 146.83225 N7  0.00000
   C16 O15  1.26701 O6 146.83225 N7 180.00000
   C17 C16  1.50054 O15 122.13733 N7 180.00000
   H18 C17  1.09505 C16 108.60105 O15  0.00000
   H19 C17  1.09989 C16 110.56037 O15 -120.12882
   H20 C17  1.09989 C16 110.56037 O15 120.12882
   N21 O15  2.24855 C16 31.55788 C17 180.00000
   H22 N21  1.01541 O15 148.88677 C16  0.00000
   C23 N21  1.46087 O15 91.59964 C16 180.00000
   H24 C23  1.10079 N21 110.73518 H22 -119.46139
   H25 C23  1.10079 N21 110.73518 H22 119.46139
   H26 C23  1.09461 N21 109.11891 H22  0.00000


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
