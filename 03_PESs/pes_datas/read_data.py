import pandas as pd
import numpy as np
import os
import re

# Define the folder containing the files
folder_path = './'

# Create an empty DataFrame to hold all the data
all_data = pd.DataFrame()

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.surf'):
        # Extract indices from filename
        match = re.match(r'(lit|sod|pot|rub|ces|cla)_(.*)_drude_(.*)_(qm|new|original)\.surf', filename)
        if match:
            index1, index2, index3, index4 = match.groups()
            
            # Read the file with two columns of floats
            file_path = os.path.join(folder_path, filename)
            try:
                df = pd.read_csv(file_path, sep='\s+', header=None, names=['Column1', 'Column2'])
            except pd.errors.EmptyDataError:
                print(f"Warning: {filename} is empty.")
                continue
            except pd.errors.ParserError:
                print(f"Error: {filename} could not be parsed.")
                continue
            
            # Add indices to the DataFrame
            df['Index1'] = index1
            df['Index2'] = index2
            df['Index3'] = index3
            df['Index4'] = index4
            
            # Append to the all_data DataFrame
            all_data = pd.concat([all_data, df], ignore_index=True)

# Group data by Index1, Index2, Index3, and Index4
grouped = all_data.groupby(['Index1', 'Index2', 'Index3', 'Index4'])

# Prepare lists to hold the arrays and their indices
indices = []
col1_arrays = []
col2_arrays = []

# Iterate over each group
for (index1, index2, index3, index4), group in grouped:
    col1_array = group['Column1'].to_numpy()
    col2_array = group['Column2'].to_numpy()
    
    # Convert arrays to strings for storage
    col1_array_str = np.array2string(col1_array, separator=',', formatter={'float_kind':lambda x: f'{x:.6f}'})
    col2_array_str = np.array2string(col2_array, separator=',', formatter={'float_kind':lambda x: f'{x:.6f}'})
    
    # Append indices and arrays to the lists
    indices.append([index1, index2, index3, index4])
    col1_arrays.append(col1_array_str)
    col2_arrays.append(col2_array_str)

# Create a DataFrame with the arrays and indices
output_df = pd.DataFrame({
    'Index1': [i[0] for i in indices],
    'Index2': [i[1] for i in indices],
    'Index3': [i[2] for i in indices],
    'Index4': [i[3] for i in indices],
    'Column1_Array': col1_arrays,
    'Column2_Array': col2_arrays,
})

# Save the consolidated data to data.csv
output_df.to_csv('../Data_report/data_qm_orignal_new.csv', index=False)
print("All data has been saved to ../Data_report/data_qm_orignal_new.csv.")

