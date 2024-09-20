########################################
#  Analysis Cost function based PESs   #
#     Yiling Nan 09/24                 #
########################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
from itertools import product

def minim(Distance, Energy, points, Ion, Compound, Direction):

    import numpy as np
    from scipy import interpolate

    xmin_read = min(Distance)
    xmax_read = max(Distance)
    #print("Data in {:s} range is {:8.5f} {:8.5f}".format(Direction, xmin_read, xmax_read) )

    f = interpolate.interp1d(Distance, Energy)
    xnew = np.linspace(xmin_read, xmax_read, num=points, endpoint=False)
    ynew = f(xnew)

    min_energy = min(ynew)
    min_index  = np.where( ynew == min_energy)
    min_x = np.sum(xnew[min_index])


    """
    if xmin_read == min_x:
        print("Warning!! Minimum Point is First Point {:s} {:s} {:s}".format(Ion, Compound, Direction))
        print("Data in range is {:8.5f} {:8.5f}".format(xmin_read, xmax_read))

    if xmax_read == min_x:
        print("Warning!! Maximum Point is Last Point {:s} {:s} {:s}".format(Ion, Compound, Direction))
        print("Data in range is {:8.5f} {:8.5f}".format(Direction, xmin_read, xmax_read))

    """

    return min_x, min_energy, xmin_read, xmax_read


def error_function2(Distance_qm, Energy_qm, Distance_mm, Energy_mm, min_x, max_x, points):

    import numpy as np
    from scipy import interpolate
    import math

    f_mm = interpolate.interp1d(Distance_mm,Energy_mm)
    xnew_mm = np.linspace(min_x,max_x,num=points, endpoint=False)
    ynew_mm = f_mm(xnew_mm)

    f_qm = interpolate.interp1d(Distance_qm,Energy_qm)
    xnew_qm = np.linspace(min_x,max_x,num=points, endpoint=False)
    ynew_qm = f_qm(xnew_qm)

    #error = (ynew_mm - ynew_qm) * ynew_qm
    weight = np.exp((ynew_qm - ynew_mm))
    comp  = np.ones(len(weight))
    weight = np.maximum(weight,comp)
    weight = np.matrix(weight)
    weight_sum = np.sum(weight)

    error = ynew_qm - ynew_mm
    error = np.matrix(error)

    error_w = np.multiply(error,weight)
    error_square = np.multiply(error_w,error)
    error_sum = np.sum(error_square)

    #result = math.sqrt( error_sum / weight_sum )

    result = math.sqrt( error_sum / points )
    #result = np.sum(result)

    return result


def Get_Error(Distance_qm, Energy_qm, Distance_mm, Energy_mm, Ion, Compound, Direction):
    

    min_x_qm, min_energy_qm, x_range_l_qm, x_range_h_qm = minim(Distance_qm,Energy_qm,200, Ion, Compound, Direction)

    # Get Local Minium From MM data
    min_x_mm, min_energy_mm, x_range_l_mm, x_range_h_mm = minim(Distance_mm,Energy_mm,200, Ion, Compound, Direction)

    # Calculate Error Function,
    # Define Fitting Range in x, min_x_qm : max_x_qm
    # If min_x_qm == x_range_h_qm, fitt from 3.0 A
    # chose smaller value from qm, mm to set larger boundary
    
    if (x_range_h_qm - min_x_qm) < 0.1:
       min_x_qm = 3
       min_x_mm = 3
       min_energy_qm = 0
       min_energy_mm = 0

    max_x_qm = min(x_range_h_qm, x_range_h_mm)
    points = int((max_x_qm - min_x_qm)/0.02)

    #print("CALC range:[{:8.5f} : {:8.5f}] {:s} {:s} {:s}".format(min_x_qm, max_x_qm, Ion, Compound, Direction))

    Error_new = error_function2(Distance_qm, Energy_qm, Distance_mm, Energy_mm, min_x_qm, max_x_qm, points)
    Error_new = np.sum(Error_new)

    #consider min_x and min_energy in error function
    Error_x =  ( min_x_qm - min_x_mm ) * 5
    Error_energy = (min_energy_qm - min_energy_mm ) * 0.5
    Error_minimum_point = abs(Error_x) + abs(Error_energy)
    Error_new_raw = Error_new + Error_minimum_point

    if Direction.endswith("trimer"):
        Error_new_w = Error_new_raw * 5 
    elif Direction.endswith("tetramer"):
        Error_new_w = Error_new_raw * 10
    else:
        Error_new_w = Error_new_raw

    Error_new = format(Error_new_w, '.3f')

    return Error_new
    

# Convert array strings back to numpy arrays
def parse_array(array_str):
    try:
        # Convert string representation of array to a list of floats
        array_list = ast.literal_eval(array_str)
        return np.array(array_list)
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing array: {e}")
        return np.array([])  # Return an empty array on error

###########################################################################
# Calculation #############################################################
###########################################################################


# Define the CSV file path
csv_file_path = 'data_qm_orignal_new.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Create a list of unique (Index1, Index2, Index3) combinations
unique_combinations = df.groupby(['Index1', 'Index2', 'Index3']).size().reset_index()[['Index1', 'Index2', 'Index3']]

data_dict = {}

# Process each unique combination
for _, row in unique_combinations.iterrows():
    index1 = row['Index1']
    index2 = row['Index2']
    index3 = row['Index3']

    # Filter data for each Index4 type
    data_dict[(index1, index2, index3, 'qm')] = {}
    data_dict[(index1, index2, index3, 'original')] = {}
    data_dict[(index1, index2, index3, 'new')] = {}

    for index4 in ['qm', 'original', 'new']:
        filtered_df = df[(df['Index1'] == index1) & (df['Index2'] == index2) & (df['Index3'] == index3) & (df['Index4'] == index4)]
        if not filtered_df.empty:
            data = filtered_df.iloc[0]
            distance_array = parse_array(data['Column1_Array'])
            energy_array = parse_array(data['Column2_Array'])
            
            if len(distance_array) > 0 and len(energy_array) > 0:
                data_dict[(index1, index2, index3, index4)] = {'distance': distance_array, 'energy': energy_array}

                #print(data_dict[(index1, index2, index3, index4)]['distance'])

# Calculate RMS differences
Cost_functions = []

#print(data_dict.items())

for (index1, index2, index3, index4), data in data_dict.items():
    # Access the datasets
    if index4 == 'qm' :

        qm_data = data_dict.get((index1, index2, index3, 'qm'), {})
        original_data = data_dict.get((index1, index2, index3, 'original'), {})
        new_data = data_dict.get((index1, index2, index3, 'new'), {})

        if (qm_data and 'distance' in qm_data and 'energy' in qm_data and
        original_data and 'distance' in original_data and 'energy' in original_data and
        new_data and 'distance' in new_data and 'energy' in new_data):
            

            # Calculate Cost Function
            qm_cost_function      = 0
            original_cost_function = Get_Error(qm_data['distance'], qm_data['energy'], original_data['distance'], original_data['energy'],index1,index2,index3)
            new_cost_function     = Get_Error(qm_data['distance'], qm_data['energy'], new_data['distance'], new_data['energy'],index1,index2,index3)

    # Determine which cost function to store based on the value of index4
    if index4 == 'qm':
        cost_function = qm_cost_function
    elif index4 == 'original':
        cost_function = original_cost_function
    elif index4 == 'new':
        cost_function = new_cost_function
    else:
        cost_function = None

    Cost_functions.append({
        'Ion': index1,
        'Compound': index2,
        'Direction': index3,
        'Method': index4,
        'Distance': data_dict.get((index1, index2, index3, index4), {}).get('distance',[]),
        'Energy': data_dict.get((index1, index2, index3, index4), {}).get('energy',[]),
        'Cost_function': cost_function 
                    })

# Convert the results to a DataFrame
results_df = pd.DataFrame(Cost_functions)

# Specify the output file path
output_file_path = 'Output_PES_cost_functions.csv'

# Save the DataFrame to a CSV file
results_df.to_csv(output_file_path, index=False)

# Print confirmation message
print(f'Results have been saved to {output_file_path}')

# Convert Distance and Cost_function to numeric if necessary
results_df['Distance'] = results_df['Distance']
results_df['Cost_function'] = pd.to_numeric(results_df['Cost_function'], errors='coerce')

#print(results_df['Distance'])
#print(results_df['Cost_function'])
# Get unique values for each relevant column
ions = results_df['Ion'].unique()
compounds = results_df['Compound'].unique()
directions = results_df['Direction'].unique()
methods = results_df['Method'].unique()

# Create all combinations of the relevant columns
combinations = product(ions, compounds, directions, methods)
# Prepare to collect report data
report_text = []

# Loop through each combination
for ion, compound, direction, method in combinations:
    # Filter the DataFrame for the current combination
    filtered_df = results_df[
        (results_df['Ion'] == ion) &
        (results_df['Compound'] == compound) &
        (results_df['Direction'] == direction) &
        (results_df['Method'] == method)
    ]
    #print(filtered_df)
    if not filtered_df.empty:
        # Calculate min and max distances and mean cost function
        try:
            min_distance = np.min(filtered_df['Distance'].min())
            max_distance = np.max(filtered_df['Distance'].max())
            mean_cost_function = filtered_df['Cost_function'].mean()
            #print(min_distance)        
            # Append the result to report text
        except Exception as e:
            min_distance = 0
            max_distance = 0
            print(f"Warning analysis Ion: {ion}, Compound: {compound} Direction: {direction} Method: {method}. Error: {e}")

        report_text.append(f"{ion: <10}  {compound: <10}  {direction: <25}  {method: <10}  "
                           f"{min_distance: <10.4f}  {max_distance: <10.4f}  {mean_cost_function: <10.4f}")

        
#print(report_text)
# Write the report text to a text file
report_file = 'Output_data_summary_report.txt'
with open(report_file, 'w') as f:
    f.write("Data Summary Report\n")
    f.write("=" * 80 + "\n")
    f.write('{: <10}" "{: <10}" "{: <10}" "{: <10}" "{: <10}" "{: <10}" "{: <10}"\n'.format("Ion", "Compound", "Direction", "Method", "Min Distance", "Max Distance", "Cost_function"))
    f.write("-" * 80 + "\n")
    f.write("\n".join(report_text))

print(f"Text report '{report_file}' generated.")


# Cost function 

# Create all combinations of the relevant columns
combinations2 = product(ions, compounds, methods)
# Prepare to collect report data
report_text2 = []

# Loop through each combination
for ion, compound, method in combinations2:
    # Filter the DataFrame for the current combination
    filtered_df = results_df[
        (results_df['Ion'] == ion) &
        (results_df['Compound'] == compound) &
        (results_df['Method'] == method)
    ]
    if not filtered_df.empty:
        # Calculate min and max distances and mean cost function
        try:
            sum_cost_function = np.sum(filtered_df['Cost_function'])
            #print(min_distance)        
            # Append the result to report text
        except Exception as e:
            print(f"Warning analysis sum of cost function Ion: {ion}, Compound: {compound} Method: {method}. Error: {e}")

        report_text2.append(f"{ion: <10}  {compound: <10} {method: <10} {sum_cost_function: <10.4f} ")

# Write the report text to a text file
report_file2 = 'Output_cost_function_report.txt'
with open(report_file2, 'w') as f:
    f.write("Cost Function Report\n")
    f.write("=" * 80 + "\n")
    f.write('{: <10}" "{: <10}" "{: <10}" "{: <10}"\n'.format("Ion", "Compound", "Method", "Sum_Cost_function"))
    f.write("-" * 80 + "\n")
    f.write("\n".join(report_text2))

print(f"Text report '{report_file2}' generated.")

