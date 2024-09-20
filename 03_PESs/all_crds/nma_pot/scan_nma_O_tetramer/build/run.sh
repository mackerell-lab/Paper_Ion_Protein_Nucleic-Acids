#!/bin/bash

rm *.pdb
rm *.crd
rm *.xyz

mkdir -p ../init_crd
mkdir -p ../init_pdb

rm ../init_crd/*.crd
rm ../init_pdb/*.pdb

python make_movie.py
./replace.sh

cp remove_float.sh ../init_crd
cd ../init_crd
./remove_float.sh

