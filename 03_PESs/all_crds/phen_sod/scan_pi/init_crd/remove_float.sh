#!/bin/bash

cation="sod"
anion="phen"
for i in {2..10}
do
mv ${cation}_${anion}_${i}.*0.crd ${cation}_${anion}_${i}.crd 
done
