import pandas as pd
import numpy as np
import os

# Data folder


# Sample index values
index1 = ['acet', 'aceh', 'acem', 'benz', 'dmds', 'dmpl', 'dms', 'imid', 'indo', 'mam1', 'mas', 'meet', 'meoh', 'mes', 'mesh', 'nma','phen', 'phet', 'adeb', 'guab', 'cytb', 'thyb', 'urab']
index2 = ['LI', 'NA', 'K', 'RB', 'CS']
index3 = {'acet': ['bisector', '120', '180', 'perp', 'acet_O_trimer', 'acet_O_tetramer'], 
          'aceh': ['o1_lp', 'o1_120', 'o1_oh', 'o2_180', 'o2_120', 'o2_perp', 'aceh_O2_trimer', 'aceh_O2_tetramer', 'aceh_O6_trimer', 'aceh_O6_tetramer'],
          'acem': ['120', '180', 'perp', 'nsp2', 'acem_O_trimer', 'acem_O_tetramer'],
          'benz': ['pi', 'benz_center_trimer', 'benz_center_tetramer'],
          'dmds': ['lp', 'bisector', 'dmds_S_trimer', 'dmds_S_tetramer'],
          'dmpl': ['o13_bisector', 'o13_perp', 'o13_180', 'o13_120', 'o11_lp', 'o11_120', 'dmpl_O11_trimer', 'dmpl_O11_tetramer', 'dmpl_O13_trimer', 'dmpl_O13_tetramer'],
          'dms' : ['120', 'lp', 'dms_S_trimer', 'dms_S_tetramer'],
          'imid': ['perp_nd1', 'perp_ne2', 'lp_ne2', 'pi', 'imid_N_trimer', 'imid_N_tetramer'],
          'indo': ['perp_n', 'pi'],
          'mam1': ['lp','hn', 'mam1_N_trimer'],
          'mas' : ['om_lp', 'om_120', 'oc_120', 'oc_180', 'oc_perp', 'mas_OC_trimer', 'mas_OC_tetramer'],
          'meet': ['lp', '120', 'meet_O_trimer', 'meet_O_tetramer'],
          'meoh': ['bisector', 'lp', 'oh', 'meoh_O_trimer', 'meoh_O_tetramer'],
          'mes' : ['120', '180', 'mes_S_trimer', 'mes_S_tetramer'],
          'mesh': ['bisector', 'lp', 'sh', 'mesh_S_trimer', 'mesh_S_tetramer'],
          'nma' : ['120', '180', 'perp', 'n', 'nma_O_trimer', 'nma_O_tetramer'],
          'phen': ['lp', '120', 'oh', 'pi', 'phen_O_trimer', 'phen_O_tetramer'],
          'phet': ['120', '180', 'pi', 'phet_O_trimer', 'phet_O_tetramer'],
          'adeb': ['n6_120', 'n6_perp', 'n3_120', 'n3_perp', 'n8_poav', 'n12_120', 'n12_perp', 'n1_perp'],
          'guab': ['n5_perp', 'n7_poav', 'n3_120', 'n3_perp', 'n13_120', 'n13_perp', 'n1_perp', 'o11_bi', 'o11_120', 'guan_N_trimer', 'guab_N_tetramer'],
          'cytb': ['o5_bi', 'o5_120', 'n1_perp', 'n6_perp', 'n6_120', 'n8_poav', 'cytb_N_trimer', 'cytb_N_tetramer'],
          'thyb': ['n1_perp', 'o5_120', 'o5_bi', 'o9_120', 'o9_bi'],
          'urab': ['n1_perp', 'o5_120', 'o5_bi', 'o9_120', 'o9_bi', 'urab_O_trimer', 'urab_O_tetramer', 'urab_O2_trimer', 'urab_O2_tetramer'],
          }

# Create a MultiIndex with three levels (index1, index2, index3)
multi_index = pd.MultiIndex.from_tuples([(i1, i2, i3) for i1 in index1 for i2 in index2 for i3 in index3[i1]],
                                        names=['Index1', 'Index2', 'Index3'])

# Create an empty DataFrame
df = pd.read_csv('data.csv', index_col=['Index1', 'Index2', 'Index3'])


index2_mapping = {
    'lit': 'LI',
    'sod': 'NA',
    'pot': 'K',
    'rub': 'RB',
    'ces': 'CS'
}

# Specify the index values you want to retrieve
target_index1 = 'acet'
target_index2 = 'sod'
target_index3 = '120'


# Use the updated index2 name
target_index2_updated = index2_mapping.get(target_index2,target_index2)

# Use loc to retrieve the specific row
specific_row = df.loc[(target_index1, target_index2_updated, target_index3)]

# Get the values for Value1 and Value2 columns
value1 = specific_row['Value1']
value2 = specific_row['Value2']

print("Value1:", value1)
print("Value2:", value2)
