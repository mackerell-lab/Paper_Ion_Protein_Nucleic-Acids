#!/bin/bash

# Define the directory containing the files
directory="./"


# Change to the target directory
cd "$directory" || exit

# Loop through each file matching the pattern
for file in *_qm_qm_qm_*.xvg; do
  # Extract parts of the filename
  a=$(echo "$file" | cut -d'_' -f1)
  b=$(echo "$file" | cut -d'_' -f2)
  c=$(echo "$file" | sed -r 's/.*_qm_qm_qm_(.*)\.xvg/\1/')

  # Replace occurrences in ${b}
  case "$b" in
    LI) b="lit" ;;
    NA) b="sod" ;;
    K) b="pot" ;;
    RB) b="rub" ;;
    CS) b="ces" ;;
    CL) b="cla" ;;
    *) echo "Unrecognized value for ${b}. Skipping file: ${file}"; continue ;;
  esac

  # Construct the new filename
  new_filename="${b}_${a}_drude_${c}_qm.surf"
  #echo "$new_filename"
  # Rename the file
  mv "$file" "$new_filename"
done

