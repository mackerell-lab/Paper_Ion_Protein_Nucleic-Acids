#!/bin/csh
#

# Generated by CHARMM-GUI (http://www.charmm-gui.org)

# This folder contains a pre-optimized PDB structure and OpenMM inputs.
# All input files were optimized for OpenMM v7.3 or above, so lower version of OpenMM can cause some errors.
# You can get the latest development version of OpenMM at the git repository:
# https://github.com/pandegroup/openmm


# Equilibration

set init = step3_charmm2omm
set istep = step4_equilibration

~/miniconda3/envs/simulation/bin/python -u openmm_run.py -i ${istep}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -b ${init}.str -orst ${istep}.rst -odcd ${istep}.dcd > ${istep}.out



