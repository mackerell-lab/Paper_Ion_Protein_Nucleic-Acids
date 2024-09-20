########################################
#      Make PES Figures                #
#       Yiling Nan 09/24               #
########################################



import pandas as pd
#import matplotlib.pyplot as plt
import itertools
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import os
import sys


# Load the CSV file (adjust filepath as necessary)
file_path = "Output_PES_cost_functions.csv"
data = pd.read_csv(file_path)

# Helper function to convert string of numbers to a numpy array of floats
def parse_array(string):
    # Remove brackets and split by whitespace or commas
    clean_string = string.strip("[]").replace('\n', ' ').replace(',', ' ')
    return np.array([float(x) for x in clean_string.split()])

# Parse the 'Distance' and 'Energy' columns into numeric arrays
data['Distance'] = data['Distance'].apply(parse_array)
data['Energy'] = data['Energy'].apply(parse_array)

# Generate all unique combinations of Index1, Index2
combinations = data[['Ion', 'Compound']].drop_duplicates()

# Function to plot distance and energy for each combination of indices
def plot_combination(Ion, Compound):
    try:

        # Filter data for the current combination
        subset = data[(data['Ion'] == Ion) & (data['Compound'] == Compound)]
        Directions = subset['Direction'].unique()
        num_directions = len(Directions)

        # Create a subplot figure 

        num_figures = (len(Directions) + 5) // 6  # Calculate number of figures needed
        num_directions_per_figure = min(len(Directions), 6)
        min_values = np.zeros((len(Directions),3)) # Get Min values

        min_energy_values = []

        for direction in Directions:
            direction_subset = subset[subset['Direction'] == direction]

            # Loop through rows in the subset and extract distances, energies, etc.
            for _, row in direction_subset.iterrows():
                distances = row['Distance']
                energies = row['Energy']
                methods = row['Method']
                cost_functions = row['Cost_function']

                # Calculate and store the minimum Energy value for this Index3
                min_energy_values.append(energies.min())

                #print(min_energy_values)

            global_min = min(min_energy_values) if min_energy_values else None
            multi = int(global_min / 50)
            rounded_min_value = 50 * (multi -1 )


        for figure_num in range(num_figures):
            start_idx = figure_num * 6
            num_directions_per_figure = 6
            if start_idx + 6 > len(Directions):
                    num_directions_per_figure = len(Directions) - start_idx
            end_idx = start_idx + num_directions_per_figure

            # Create a subplot figure for the current figure
            rows = int((num_directions_per_figure + 1) / 2)
            cols = 2
            rows = 3
            fig_name = f"fig{figure_num + 1}"

            #print(rows, cols)
            globals()[fig_name] = make_subplots(rows=rows, cols=cols,
                                     #shared_xaxes='all', shared_yaxes= 'all', vertical_spacing=0.05, horizontal_spacing= 0.01,
                                     vertical_spacing=0.1, horizontal_spacing= 0.1,
                                     x_title='<b> Distance, Å </b>',
                                     y_title='<b> Energy, kcal/mol <b>',
                                    subplot_titles=[f"Direction: {Directions[x]}" for x in range(start_idx, end_idx)])

            for i, Direction in enumerate(Directions[start_idx:end_idx], start=1):
                # Filter data based on selected direction
                direction_subset = subset[subset['Direction'] == Direction]
                row_i2 = (i - 1) // 2 + 1  # Integer division
                col_i2 = (i - 1) % 2 + 1
                #print(row_i2, col_i2)

                methods = ['qm', 'original', 'new']

                for method in methods:
                    method_subset = direction_subset[direction_subset['Method'] == method]
                    x_plot = np.array(method_subset['Distance'].values[0]).tolist()
                    y_plot = np.array(method_subset['Energy'].values[0]).tolist()
                    error  = np.sum(method_subset['Cost_function'].values)
                    #print(type(y_plot))
                    if method == 'qm':
                        color = '#000000'
                        line_style = 'dot'
                        text=' '
                        x_position = col_i2 / 2 - 0.4 #
                        y_position = row_i2 /3 - 0.4 #
                    elif method == 'original':
                        color = 'rgba(0,141,0,1.0)'
                        line_style = 'solid'
                        text=f'Cost_fun: {error:.3f}'
                        x_position = 0.97  #  col_i2 / 2 - 0.5
                        y_position = 0.95 #  row_i2 /3 -0.4
                    else:
                        color = 'rgba(229,8,106,1.0)'
                        line_style = 'solid'
                        text=f'Cost_fun: {error:.3f}'
                        x_position = 0.97 #col_i2 / 2 - 0.5
                        y_position =  0.88 #row_i2 /3 -0.42


                    #print(x_plot)
                    # Add trace to subplot
                    trace = go.Scatter(x=x_plot, y=y_plot,
                                          mode='lines',
                                          #name=f'Parameter: {selected_value}',
                                          #text=[f'Error: {value3:.2f}' ],
                                          showlegend=False,
                                          line=dict(color=color, dash=line_style, width=4.5) )
                    globals()[fig_name].add_trace(trace, row=row_i2, col=col_i2)


                    # Calculate x, y index
                    x_ind = num_directions_per_figure
                    y_ind = num_directions_per_figure + 1

                    for idx, annotation in enumerate(globals()[fig_name]['layout']['annotations']):
                        if idx <= y_ind:
                            annotation['font'] = dict(family='Helvetica', color='black',size=36)
                            #print(annotation)
                            #print(idx, annotation)
                        if idx == x_ind:
                            annotation['yshift'] = -80

                        if idx == y_ind:
                            annotation['xshift'] = -100

                    globals()[fig_name].add_annotation(dict(x=x_position, y= y_position, xref="x domain", yref="y domain",
                                text=text , showarrow=False,font=dict(family="Helvetica",size=30,color=color)), row=row_i2, col=col_i2)


                globals()[fig_name].update_xaxes(
                      row=row_i2,
                      col=col_i2,
                      range=[1, 8],
                      ticks="inside",
                      #tickvals = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
                      tickcolor='black',
                      tick0=0,
                      dtick=2.0,
                      tickfont=dict(family='Helvetica', color='black', size=30),
                      title_font=dict(family='Helvetica',color='black',size=30),
                      mirror=True, linecolor='black', linewidth=4.5,
                      #showline=True,
                      showgrid=False,
                      tickwidth=4.5,
                      ticklen=24,
                      minor=dict(
                          ticklen=12,
                          tickwidth=3.0,
                          tickcolor="black",
                          dtick=0.5,
                          ticks="inside"
                           )
                      )

                # Update y-axis properties for the subplot
                globals()[fig_name].update_yaxes(
                        row=row_i2,
                        col=col_i2,
                        ticks="inside",
                        tick0=0,
                        dtick=50,
                        range=[rounded_min_value,30],
                        #tickvals = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
                        tickcolor='black',
                        #title_text='<b> Energy, kcal/mol <b>',
                        tickfont=dict(family='Helvetica', color='black', size=30),
                        title_font=dict(family='Helvetica',color='black',size=30),
                        mirror=True, linecolor='black', linewidth=4.5,
                        #showline=True,
                        showgrid=False,
                        tickwidth=4.5,
                        ticklen=24,
                        minor=dict(
                            ticklen=12,
                            tickwidth=3.0,
                            tickcolor="black",
                            dtick=10,
                            ticks="inside"
                            )
                        )



            globals()[fig_name].update_layout(
            title_text=f"<b> {Compound} {Ion} {figure_num + 1 }/{num_figures} <b> ".upper(),
            title_x = 0.5, # Center the main title
            title_font=dict(family='Helvetica',color='black',size=36),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_range=[1,8],
            yaxis_range=[rounded_min_value,30],
            #yaxis1_range= [rounded_min_value,80],
            #yaxis2_range= [rounded_min_value,80],
            #yaxis3_range= [rounded_min_value,80],
            #yaxis4_range= [rounded_min_value,80],
            #yaxis5_range= [rounded_min_value,80],
            #yaxis6_range= [rounded_min_value,80],
            #legend_title_text='Element',
            autosize=True,
            width=1600,
            height=1800,
            margin=dict(l=180,r=180,b=180,
                t=180,pad=0
                ),
            )

            # Show or save the Plotly figure
            #globals()[fig_name].show()
            figure_folder = './figures/' 
            output_path = os.path.join(figure_folder, f"{Compound}_{Ion}_{figure_num + 1}_{num_figures}.png")


            globals()[fig_name].write_image(output_path)

    except Exception as e:
        print(f"Error plotting combination Ion: {Ion}, Compound: {Compound}. Error: {e}")
# Iterate through all combinations and plot
for comb in combinations.itertuples(index=False):
    plot_combination(comb.Ion, comb.Compound)

# Plot Upon Selection
#plot_combination('sod','dmpl')
