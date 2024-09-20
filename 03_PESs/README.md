This folder contains input files to calculate potential energy surfaces (PESs) using CHARMM and the corresponding cost functions against quantum mechanical (QM) data in support of the manuscript.
Folder Structure:

    all_crds:
        Contains all ion-model compound .crd files required by CHARMM.
        To run with a different force field, provide the appropriate foppar file and modify toppar.str accordingly.
        Run ./99_run_all_crds.sh to execute simulations. The script supports parallel execution.
        In the bash script, you can adjust the number of processors for the parallel run and set the folder to save MM PES results.

    pes_datas:
        Contains all PES data from both the original and new parameters, as well as QM data.
        Use read_data.py to read and combine these files into a single output file, which will be saved as Data_Report.

    Data_Report:
        Contains the combined data from tmp_data along with analysis scripts.
        01_analysis_data.py calculates cost functions and generates a report. Output files include:
            Output_PES_cost_functions.csv
            Output_data_summary_report.txt
        02_make_pes_figure.py generates figures for all combinations and saves them in the ./figures directory.
            The make_pdf.py script in the figures directory combines all figures into a single PDF, with one figure per page.

    03_view_cost_function.py:
        Visualizes the cost function for each ion and model compound.


