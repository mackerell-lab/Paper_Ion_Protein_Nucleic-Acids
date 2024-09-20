#!/bin/bash

for filename in * ; do
  # Check if the filename contains "XX"
  if [[ "$filename" == *sod* ]]; then
    # Replace "XX" with "BB" in the filename
    new_filename="${filename/sod/ces}"
    
    # Rename the file
    sed -i 's/SOD/CES/g' "$filename"
    mv "$filename" "$new_filename"
    
    echo "Renamed: $filename -> $new_filename"
  fi
done

