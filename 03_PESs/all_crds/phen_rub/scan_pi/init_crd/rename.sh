#!/bin/bash

for filename in * ; do
  # Check if the filename contains "XX"
  if [[ "$filename" == *lit* ]]; then
    # Replace "XX" with "BB" in the filename
    new_filename="${filename/lit/rub}"
    
    # Rename the file
    sed -i 's/LIT/RUB/g' "$filename"
    mv "$filename" "$new_filename"
    
    echo "Renamed: $filename -> $new_filename"
  fi
done

