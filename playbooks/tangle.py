#!/usr/bin/env python3

import os
import re
import sys

def extract_tangle_file(org_file):
    """
    Extract the tangle file name from the :tangle property in the Org file.
    """
    tangle_file = None
    with open(org_file, 'r') as f:
        for line in f:
            if ':tangle' in line:
                match = re.search(r':tangle\s+([^\s]+)', line)
                if match:
                    tangle_file = match.group(1)
                    break
    return tangle_file

def tangle_org_to_yml(org_file):
    """
    Tangle YAML code blocks from an Org file into a specified YAML file.
    """
    # Extract the tangle file name from the :tangle property
    yml_file = extract_tangle_file(org_file)
    
    if not yml_file:
        print(f"No :tangle property found in {org_file}. Skipping.")
        return

    yaml_blocks = []
    in_yaml_block = False
    with open(org_file, 'r') as f:
        for line in f:
            # Detect the start of a YAML code block
            if line.strip().startswith('#+begin_src yaml'):
                # Skip blocks with ":tangle no"
                if 'tangle no' in line:
                    in_yaml_block = False
                else:
                    in_yaml_block = True
                continue
            # Detect the end of a YAML code block
            elif line.strip().startswith('#+end_src'):
                in_yaml_block = False
                continue
            
            # Collect lines inside a YAML block
            if in_yaml_block:
                yaml_blocks.append(line)

    # Write the YAML content to the output file if there are any blocks
    if yaml_blocks:
        with open(yml_file, 'w') as f:
            f.writelines(yaml_blocks)
        print(f"Tangled {org_file} to {yml_file}")
    else:
        print(f"No YAML blocks found to tangle in {org_file}")

def main():
    """
    Main function to loop through all .org files and tangle them.
    """
    org_files = [f for f in os.listdir('.') if f.endswith('.org')]
    
    if not org_files:
        print("No .org files found in the current directory.")
        sys.exit(1)
    
    for org_file in org_files:
        tangle_org_to_yml(org_file)
    
    print("Tangling complete.")

if __name__ == "__main__":
    main()
