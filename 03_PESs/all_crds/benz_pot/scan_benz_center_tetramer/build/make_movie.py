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

   C1  3.26334  1.53931  0.70532
   H2  3.82338  2.30155  1.25270
   C3  3.26334  1.53931 -0.70532
   H4  3.82338  2.30155 -1.25270
   C5  2.61851  0.50430  1.41361
   H6  2.68921  0.45600  2.50300
   C7  2.61851  0.50430 -1.41361
   H8  2.68921  0.45600 -2.50300
   C9  2.00241 -0.54825  0.70633
   H10  1.62466 -1.40687  1.26933
   C11  2.00241 -0.54825 -0.70633
   H12  1.62466 -1.40687 -1.26933
   X13 -1.14096 -1.39675  0.04106
   X14 -0.49613 -0.36174  0.74638
   K15  0.49740  1.97836  0.00000
   K16 -0.49740 -1.97836  0.00000
--
0 1

   X17 X13  R       X14 91.36743 C9 -163.68160
   C18 X17  1.40873 X13 91.36743 X14  180.0000
   H19 C18  1.09283 X17 176.20755 X13 -179.48138
   C20 X17  1.40873 X13 90.00287 X14 -119.91983
   H21 C20  1.09283 X17 176.20755 X13 177.12191
   C22 X17  1.41361 X13 91.36272 X14 120.02597
   H23 C22  1.09276 X17 175.50601 X13 -176.79377
   C24 X17  1.41361 X13 88.63728 X14 -59.97403
   H25 C24  1.09276 X17 175.50601 X13 176.79377
   C26 X17  1.40938 X13 91.36681 X14 60.08439
   H27 C26  1.09402 X17 174.25011 X13 170.17005
   C28 X17  1.40938 X13 90.00091 X14 -0.06060
   H29 C28  1.09402 X17 174.25011 X13 -167.81136

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

