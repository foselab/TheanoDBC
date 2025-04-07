#!/bin/bash

# Command
cmd="java -jar ../Theano.jar"
BASE_RESOURCES_PATH="."

show_java_output=false
redirect_output=""
if [ "$show_java_output" = false ]; then
    redirect_output="> /dev/null 2>&1"
fi

# Paths
NEW_CONTRACT_PATH="we_v1.rt"
NEW="WE_v1"
OLD_CONTRACT_PATH="$BASE_RESOURCES_PATH/../start/we_v0.rt"
OLD="WE_v0"
REFINEMENT_FILE_PATH="refinement.rt"
REFINEMENT_SCRIPT_PATH="script.py"

# Logging
echo -e "\nOTA $NEW"

# Building the refinement file
{
  echo "table $OLD"
  cat "$OLD_CONTRACT_PATH"
  echo -e "\nendtable"
  echo "table $NEW"
  cat "$NEW_CONTRACT_PATH"
  echo -e "\nendtable"
} > "$REFINEMENT_FILE_PATH"

# Refinement check
echo -e "\nChecking if $NEW refines $OLD..."
eval $cmd -i "$REFINEMENT_FILE_PATH" -o "$REFINEMENT_SCRIPT_PATH" -t refinement $redirect_output
timeout 10 python "$REFINEMENT_SCRIPT_PATH"

# End script cleaning up
cleanup_files() {
    find "$BASE_RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} +
    find "$BASE_RESOURCES_PATH" -type f -name "*.bak" -exec rm -f {} +
}

cleanup_files
echo -e "\nDone"
