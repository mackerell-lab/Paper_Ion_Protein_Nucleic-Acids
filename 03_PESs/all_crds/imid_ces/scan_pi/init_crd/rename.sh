#!/bin/bash

for filename in * ; do
  # Check if the filename contains "XX"
  if [[ "$filename" == *pot* ]]; then
    # Replace "XX" with "BB" in the filename
    new_filename="${filename/pot/ces}"
    
    # Rename the file
    sed -i 's/POT/CES/g' "$filename"
    mv "$filename" "$new_filename"
    
    echo "Renamed: $filename -> $new_filename"
  fi
done

