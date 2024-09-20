#!/bin/bash

for filename in * ; do
  # Check if the filename contains "XX"
  if [[ "$filename" == *ces* ]]; then
    # Replace "XX" with "BB" in the filename
    new_filename="${filename/ces/rub}"
    
    # Rename the file
    sed -i 's/CES/RUB/g' "$filename"
    mv "$filename" "$new_filename"
    
    echo "Renamed: $filename -> $new_filename"
  fi
done

