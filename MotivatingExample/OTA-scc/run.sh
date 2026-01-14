#!/usr/bin/env bash

# Detect OS and set Python command
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OS" == "Windows_NT" ]]; then
    PYTHON_CMD="py -3"
    FIND_EXEC="find"
else
    PYTHON_CMD="python3"
    FIND_EXEC="find"
fi

# Command
cmd=(java -jar ../Theano.jar)
BASE_RESOURCES_PATH="."

show_java_output=false

# Paths
NEW_CONTRACT_PATH="scc_v1.rt"
NEW="SCC_v1"
OLD_CONTRACT_PATH="$BASE_RESOURCES_PATH/../start/scc_v0.rt"
OLD="SCC_v0"
REFINEMENT_FILE_PATH="refinement.rt"
REFINEMENT_SCRIPT_PATH="script.py"

# Logging
echo "OTA $NEW"

# Building the refinement file
{
  echo "table $OLD"
  cat "$OLD_CONTRACT_PATH"
  echo
  echo "endtable"
  echo "table $NEW"
  cat "$NEW_CONTRACT_PATH"
  echo
  echo "endtable"
} > "$REFINEMENT_FILE_PATH"

# Refinement check
echo "Checking if $NEW refines $OLD..."
if [ "$show_java_output" = false ] ; then
    "${cmd[@]}" -i "$REFINEMENT_FILE_PATH" -o "$REFINEMENT_SCRIPT_PATH" -t refinement > /dev/null 2>&1
else
    "${cmd[@]}" -i "$REFINEMENT_FILE_PATH" -o "$REFINEMENT_SCRIPT_PATH" -t refinement
fi

# Run Python script
$PYTHON_CMD "$REFINEMENT_SCRIPT_PATH"

# Cleanup
cleanup_files() {
    $FIND_EXEC "$BASE_RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} \;
    $FIND_EXEC "$BASE_RESOURCES_PATH" -type f -name "*.bak" -exec rm -f {} \;
}

cleanup_files
echo "Done"
