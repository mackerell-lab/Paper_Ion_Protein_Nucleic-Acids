#!/bin/bash

cation="pot"
anion="acem"

for i in $(seq 1.5 0.1 10.0) 
do
original1="2.xyz"
replace1="${i}.xyz"

original2="2.pdb"
replace2="${i}.pdb"

cp readxyz2pdb_cp.c readxyz2pdb.c

sed -i "s/${original1}/${replace1}/g" readxyz2pdb.c

sed -i "s/${original2}/${replace2}/g" readxyz2pdb.c

gcc readxyz2pdb.c -o readxyz2pdb -lm
./readxyz2pdb

cp ${replace2} ../init_pdb/${cation}_${anion}_${i}.pdb

echo "I generate the pdb file ${i}"

original3="2.crd"
replace3="${i}.crd"

cp readxyz2crd_cp.c readxyz2crd.c

sed -i "s/${original1}/${replace1}/g" readxyz2crd.c

sed -i "s/${original3}/${replace3}/g" readxyz2crd.c

gcc readxyz2crd.c -o readxyz2crd -lm
./readxyz2crd

cp ${replace3} ../init_crd/${cation}_${anion}_${i}.crd

echo "I generate the crd file ${i}"


done


