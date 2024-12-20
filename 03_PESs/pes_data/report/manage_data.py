import pandas as pd
import numpy as np
import os

# Data folder

data_folder = '../'

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
          'guab': ['n5_perp', 'n7_poav', 'n3_120', 'n3_perp', 'n13_120', 'n13_perp', 'n1_perp', 'o11_bi', 'o11_120', 'guab_N_trimer', 'guab_N_tetramer'],
          'cytb': ['o5_bi', 'o5_120', 'n1_perp', 'n6_perp', 'n6_120', 'n8_poav', 'cytb_N_trimer', 'cytb_N_tetramer'],
          'thyb': ['n1_perp', 'o5_120', 'o5_bi', 'o9_120', 'o9_bi'],
          'urab': ['n1_perp', 'o5_120', 'o5_bi', 'o9_120', 'o9_bi', 'urab_O_trimer', 'urab_O_tetramer', 'urab_O2_trimer', 'urab_O2_tetramer'],
          }

# Create a MultiIndex with three levels (index1, index2, index3)
multi_index = pd.MultiIndex.from_tuples([(i1, i2, i3) for i1 in index1 for i2 in index2 for i3 in index3[i1]],
                                        names=['Index1', 'Index2', 'Index3'])

# Create an empty DataFrame
df = pd.DataFrame(index=multi_index, columns=['Value1', 'Value2'])

# Loop through index1, index2, and index3 values and populate the DataFrame
for i1, i2, i3 in multi_index:
    # Generate file name based on index values
    file_name = os.path.join(data_folder, f"{i1}_{i2}_qm_qm_qm_scan_{i3}.xvg")
    
    try:
        # Read data from the file
        data = np.loadtxt(file_name)
        
        # Check if the file is empty
        if data.size == 0:
            print(f"File '{file_name}' is empty.")
        else:
            # Assign the data to the DataFrame columns individually
            df.at[(i1, i2, i3), 'Value1'] = data[:,0]
            df.at[(i1, i2, i3), 'Value2'] = data[:,1]

    except Exception as e:
        print(f"Reminding : {e}")

df.to_csv('data2.csv', index=True)  # Save with index
#df.to_excel('data.xlsx', index=True)  # Save with index

# Make a report
# Calculate sizes of each data entry and generate a text report

report_text = []

#for i1 in index1:
for i1 in index1:
    for i2 in index2:
        for i3 in index3[i1]:
            specific_row = df.loc[(i1, i2, i3)]
            value1 = specific_row['Value1']
            
            # Calculate min and max values
            if isinstance(value1, (list, np.ndarray)):
                min_value = np.min(value1)
                max_value = np.max(value1)
            else:
                min_value = 0
                max_value = 0
            
            value1_length = len(value1) if isinstance(value1, (list, np.ndarray)) else 0
            
            report_text.append(f" {i1: <8}  {i2: <4}  {i3: <20}  "
                               f" {value1_length: <6}  {min_value: <10.4f}  {max_value: <10.4f}")

# Write the report text to a text file
report_file = 'data_summary_report.txt'
with open(report_file, 'w') as f:
    f.write("Data Summary Report\n")
    f.write("=" * 80 + "\n")
    f.write("{: <7} {: <7} {: <24} {: <5} {: <10} {: <10}\n".format("Index1", "Index2", "Index3", "Size", "Min", "Max"))
    f.write("-" * 80 + "\n")
    f.write("\n".join(report_text))

print(f"Text report '{report_file}' generated.")

import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Define a custon color scale
custom_color_scale = ["rgb(31, 119, 180)", "rgb(255, 127, 14)", "rgb(44, 160, 44)",
                      "rgb(214, 39, 40)", "rgb(148, 103, 189)", "rgb(140, 86, 75)",
                      "rgb(60, 183, 12)", "rgb(240, 2, 146)" ,  "rgb(250, 249, 40)",
                      "rgb(255, 142, 0)", "rgb(0,   0,   0)" ,  "rgb(233, 184, 176)",
                      "rgb(255, 173, 1)", "rgb(43,  61,  39)" ,  "rgb(18,  78, 120)"]

# Create a figure for each combination of index1
#for i1 in index1:
for i1 in ['nma','acem']:
    # Create subplots for each index2
    fig = make_subplots(rows=3, cols=2,
            subplot_titles=[f"<b>{i1} - {i2}</b>".upper() for i2 in index2],
                        shared_xaxes=True, shared_yaxes=False,
                        vertical_spacing=0.1, horizontal_spacing=0.15
                        )

    # Create a dictionary to store color mappings for each index3
    index3_colors = {}

    for i2_index, i2 in enumerate(index2, start=1):
        # Create a subset of the DataFrame for the specific combination of index1, index2, and index3
        subset = df.loc[(i1, i2), :]
        min_values = np.zeros(len(index3[i1])) # Get Min values
        row_i2 = (i2_index - 1) // 2 + 1  # Integer division
        col_i2 = (i2_index - 1) % 2 + 1 

        # Check if there is data for this combination
        if not subset.empty:
            # Add lines for each index3
            for i3_index, i3 in enumerate(index3[i1]):
                specific_row = df.loc[(i1, i2, i3)]
                value1 = specific_row['Value1']
                value2 = specific_row['Value2']

                if isinstance(value1, (list, np.ndarray)) and len(value1) > 0:
                    min_values[i3_index-1]=np.min(value2)

                    color = index3_colors.get(i3, None)
                    if color is None:
                        color = index3_colors.get(i3, custom_color_scale[i3_index])
                        index3_colors[i3] = color

                    fig.add_trace(go.Scatter(x=value1, 
                                             y=value2,
                                             name=i3,
                                             mode='lines',
                                             line=dict(
                                                 width=4.5,
                                                 color=color)
                                              ),
                                            row=row_i2, 
                                            col=col_i2)
        # Get Min Value to adjust plot range
        #print(min_values)
        global_min = np.min(min_values)
        multi = int(global_min / 50)
        rounded_min_value = 50 * (multi -1 )
        #print(global_min, multi, rounded_min_value)

        # Update Subplot title

        for i in fig['layout','annotations']:
            i['font'] = dict(family='Helvetica',color='black',size=36)

        # Update x-axis properties for the subplot

        fig.update_xaxes(
            row=row_i2,
            col=col_i2,
            range=[1, 8],
            ticks="outside",
            #tickvals = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
            tickcolor='black',
            tick0=0,
            dtick=2.0,
            tickfont=dict(family='Helvetica', color='black', size=30),
            title_font=dict(family='Helvetica',color='black',size=30),
            title_text='<b> Distance, A <b>',
            mirror=True, linecolor='black', linewidth=4.5,
            #showline=True,
            showgrid=False,
            tickwidth=4.5,
            ticklen=24,
            minor=dict(
                ticklen=12,
                tickwidth=3.0,
                tickcolor="black",
                dtick=0.5
            )
        )

        # Update y-axis properties for the subplot
        fig.update_yaxes(
            row=row_i2,
            col=col_i2,
            range=[rounded_min_value, 80],
            ticks="outside",
            tick0=0,
            dtick=50,
            #tickvals = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
            tickcolor='black',
            title_text='<b> Energy, kcal/mol <b>',
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
                dtick=10
                )
            )
    # Create a title dictionary for each subplot
    #subplot_titles = {f"Line Plot - {i1} - {i2}": dict(textfont=dict(family='Helvetica', size=18))
    #                  for i2 in index2}
    
    #print(min_values)
    #global_min = np.min(min_values)
    #rounded_min_value = min_value - (min_value % 50)
    # Update subplot layout
    fig.update_layout(title_text=f"<b> QM Summaries of {i1} <b> ".upper(),
                      title_x = 0.5, # Center the main title
                      title_font=dict(family='Helvetica',color='black',size=36),
                      paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
                      plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot background
                      width=1600,  # Adjust the width of the figure
                      height=1800,  # Adjust the height of the figure
                      #legend=dict(
                      #    x=0.5,
                      #    y=1.05,
                      #    font=dict(family='Helvetica', color='black', size=24)
                      #  )
                      )
    
    # Show the figure
    fig.show()
    figure_folder = './figures' # f"{i1}_{i2}_qm_qm_qm_scan_{i3}.xvg"
    output_path = os.path.join(figure_folder, f"{i1}.png")
    fig.write_image(output_path)
