
########################################
#  Cost Function Visualization         #
#       Yiling Nan 09/24               #
########################################


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Read the file, ignoring the first 4 lines
#file_path = 'Output_cost_function_report.txt'
file_path = 'Output_cost_function_report.txt'
df = pd.read_csv(file_path, sep='\s+', skiprows=4, header=None)


# Extract necessary columns
x_col = df[1]  # 2nd column for x-axis
y_col = df[0]  # 1st column for y-axis
method_col = df[2]  # 3rd column represents different methods
color_value = df[3]  # 4th column represents the value for the colormap

# Desired order for the y-axis
y_order = ['lit', 'sod', 'pot', 'rub', 'ces', 'cla']

# Define your custom colors
#colors = ['#ded9f6','#c3b4e5','#a083c9','#8058ac', '#592986']  # Purple 
#colors = ['#FFFFFF','#f3def5', '#cbaad8', '#9e72c3', '#924dbf', '#4d01a6']  # Purple 
colors = ['#FFFFFF', '#FFFFFF', '#f3def5', '#cbaad8', '#9e72c3', '#924dbf', '#4d01a6']  # Purple 
#colors = ['#f3def5', '#9e72c3','#924dbf','#7338a0' ,'#4e008c']  
#colors = ['#f6e7f1','#e5c8e5','#b583c9','#9358ac','#782986', '#592986']  

# Create the colormap
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

# Map the y-values to the order specified
df[0] = pd.Categorical(df[0], categories=y_order, ordered=True)
df = df.sort_values(by=[0, 1])  # Sort the DataFrame by the custom y-order and x-values

# Get unique methods from the 3rd column for creating subplots
unique_methods = method_col.unique()

# Filter out "QM" method
filtered_methods = [method for method in unique_methods if method != 'qm']

# Create subplots: one for each method, stacked vertically
num_plots = len(filtered_methods)
fig, axs = plt.subplots(num_plots, 1, figsize=(20, 6 * num_plots), sharex=True, sharey=True)  # Vertical stack

# Loop through each method and plot the colormap
for i, method in enumerate(filtered_methods):
    ax = axs[i] if num_plots > 1 else axs  # Adjust for a single subplot
    subset_df = df[df[2] == method]  # Filter data for the current method

    # Create a pivot table to transform the data into a matrix form suitable for plotting
    pivot_table = subset_df.pivot(index=0, columns=1, values=3)  # 1st col as y, 2nd col as x, 4th col as value
    
    # Plot the 2D colormap using imshow, set color range from 0 to 30
    cax = ax.imshow(pivot_table, aspect='auto', origin='lower', cmap=cmap, vmin=0, vmax=700)

    # Customize subplot
    ax.set_title(f'Method: {method}')
    ax.set_xlabel('Compound' if i == num_plots - 1 else '')  # X-label only on last subplot
    ax.set_ylabel('Ion')
    
    # Set y-ticks in the specified order
    ax.set_yticks(np.arange(len(y_order)))
    ax.set_yticklabels(y_order)

    # Set x-ticks based on pivot table's columns
    ax.set_xticks(np.arange(len(pivot_table.columns)))
    ax.set_xticklabels(pivot_table.columns)

# Create color bar outside the figure
cbar = fig.colorbar(cax, ax=axs, orientation='vertical', fraction=0.02, pad=0.04)
cbar.set_label('Cost Function (Color)')

# Move the color bar outside the figure
cbar.ax.set_position([0.92, 0.15, 0.02, 0.7])  # Adjust as needed

# Adjust layout
plt.savefig("Output_costfunction_ion_compound.png", dpi=200) 
#plt.show()
