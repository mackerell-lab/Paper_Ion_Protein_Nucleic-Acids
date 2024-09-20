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

   C1  0.78826 -4.54519  0.00000
   C2 -0.42398 -3.64810  0.00000
   N3 -1.62691 -4.26172  0.00000
   H4 -2.46681 -3.69766  0.00000
   H5 -1.71229 -5.26867  0.00000
   O6 -0.33576 -2.40386  0.00000
   H7  1.69069 -3.92615  0.00000
   H8  0.78499 -5.19099  0.89014
   H9  0.78499 -5.19099 -0.89014
   K10  0.00000  0.00000  0.00000
--
0 1
   O11 K10  R        O6 180.00000 N3  0.00000
   C12 O11  1.24736 K10 176.10465 N3  0.00000
   N13 C12  1.35040 O11 121.08224 N3 180.00000
   H14 N13  1.01172 C12 119.08885 O11  0.00000
   H15 H14  1.74280 C12 65.73602 O11 180.00000
   C16 C12  1.50808 O11 122.44677 N13 180.00000
   H17 C16  1.09434 C12 109.04830 N13 180.00000
   H18 C16  1.09973 C12 110.29963 N13 59.65680
   H19 C16  1.09973 C12 110.29963 N13 -59.65680

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

