#!/bin/bash

rm *.pdb
rm *.crd
rm *.xyz

rm ../init_crd/*.crd
rm ../init_pdb/*.pdb

python make_movie.py
./replace.sh

cp remove_float.sh ../init_crd

cd ../init_crd
./remove_float.sh

mkdir ../../drude/init_crd
mkdir ../../additive/init_crd

rm -rf ../../drude/init_crd/*.crd
rm -rf ../../additive/init_crd/*.crd

cp -rfp * ../../drude/init_crd
cp -rfp * ../../additive/init_crd

