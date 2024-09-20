Potential Energy Surface (PES) Calculations - Input Files

This directory contains input files for calculating potential energy surfaces (PESs) using CHARMM, alongside cost function computations against quantum mechanical (QM) data. These files support the accompanying manuscript.
Folder Structure:
all_crds/

    Description: Contains all .crd files for ion-model compounds needed by CHARMM.
    How to Use:
        To run simulations with a different force field, replace the foppar file and adjust toppar.str accordingly.
        Execute simulations by running ./99_run_all_crds.sh.
        The script supports parallel execution:
            You can modify the number of processors used for parallel execution within the script.
            Adjust the target folder where molecular mechanics (MM) PES results are saved.

pes_datas/

    Description: Contains all PES data from both the original and updated parameters, along with QM reference data.
    How to Use:
        Use the read_data.py script to combine these datasets into a single output file, which will be saved as Data_Report.

Data_Report/

    Description: Contains the combined data from tmp_data, as well as analysis scripts for generating reports and figures.
    Included Scripts:
        01_analysis_data.py:
            Calculates cost functions and generates a summary report.
            Output files:
                Output_PES_cost_functions.csv
                Output_data_summary_report.txt
        02_make_pes_figure.py:
            Generates figures for all ion-model compound combinations and saves them in the ./figures directory.
            Additionally, use the make_pdf.py script (in the figures/ directory) to combine all figures into a single PDF, with one figure per page.
        03_view_cost_function.py:
            Visualizes the cost functions for each ion and model compound.

PES_Nan_et_al_QM_MM.pdf

    Description: Contains PES plots saved as a PDF document.

zmatrices.csv

    Description: Provides Z-matrices for all systems involved in the PES calculations.
