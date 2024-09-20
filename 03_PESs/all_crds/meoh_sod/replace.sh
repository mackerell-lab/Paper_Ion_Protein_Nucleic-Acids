#!/bin/bash


original="drude_toppar_2019\/toppar.str"
replace="toppar.str"

for scan_dir in scan_*; do
    # Check if the item is a directory
    ener_file="$scan_dir/ener.inp"

    if [ -f "$ener_file" ]; then
        # Replace the specified line in ener.inp
        sed -i "s/${original}/${replace}/g"  $ener_file
        echo "Replaced line in $ener_file"
    else
            echo "ener.inp not found in $scan_dir"
    fi
done
