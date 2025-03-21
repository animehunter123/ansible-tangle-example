#!/bin/bash

# Check if emacs is installed
command -v emacs >/dev/null 2>&1 || { echo >&2 "Emacs is required but not installed. Aborting."; exit 1; }

# Loop through all .org files in the current directory
for org_file in *.org; do
    # Check if the file exists (in case there are no .org files)
    if [ -f "$org_file" ]; then
        # Generate the output .yml filename
        yml_file="${org_file%.org}.yml"
        
        # Use emacs in batch mode to tangle the .org file
        emacs --batch --eval "(require 'org)" --eval "(org-babel-tangle-file \"$org_file\" \"$yml_file\" \"yaml\")"
        
        echo "Tangled $org_file to $yml_file"
    fi
done

echo "Tangling complete."
