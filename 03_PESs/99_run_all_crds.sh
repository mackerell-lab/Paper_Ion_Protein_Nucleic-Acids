
#!/bin/bash
###########################################
####   By Yiling Nan, 09/2024  ############
###########################################


#export CHARM_EXEC="/opt/mackerell/apps/charmm/serial/charmm-c49b1-serial-ljpme"
export CHARM_EXEC=/home/ynan/charmm/charmm/serial/charmm

num_proc=2 # parallel run
data_store="tmp_data"
# Create a temporary directory for log files
temp_dir=$(mktemp -d)
trap 'rm -rf "$temp_dir"' EXIT

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Find directories and execute the CHARMM commands in parallel
find . -maxdepth 3 -type d -path "./all_crds/*/scan*"   | xargs -P $num_proc -I {} bash -c '
    dir="{}"
   
    echo "${dir}" 
    cd "$dir" || { echo -e "${RED}Failed to change directory to $dir${NC}"; exit 1; }

    # Remove existing *_new.surf files if they exist
    rm -f *_new.surf

    # Run CHARMM command and capture any errors
    if ! '"$CHARM_EXEC"' -i ener.inp -o ener.out; then
        echo -e "${RED}Error in directory $dir${NC}" >> '"$temp_dir"'/error_log.txt
    else
	# Extract the last folder name
          last_folder_name=$(basename "$(pwd)")	
        # Rename *.surf to *_new.surf
        for file in *.surf; do
            [ -e "$file" ] && mv "$file" "${file%.surf}_${last_folder_name}_new.surf"
        done

        echo -e "${GREEN}Job in directory $dir completed successfully${NC}"
        # Copy renamed files to destination
        cp *_new.surf ../../../tmp_data/ 2>/dev/null || echo -e "${RED}Failed to copy *_new.surf files from $dir${NC}" >> '"$temp_dir"'/error_log.txt
    fi

    cd - > /dev/null
'

