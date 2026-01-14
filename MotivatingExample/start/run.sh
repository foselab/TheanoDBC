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
CONTROLLED_VEHICLE_PATH="$BASE_RESOURCES_PATH/../controller.rt"

SCC_PATH="scc_v0.rt"
WE_PATH="we_v0.rt"
SCC_WE_PATH="temp.rt"
SCC_WE_COMPOSITION="composition.rt"
REFINEMENT_FILE_PATH="refinement.rt"
REFINEMENT_SCRIPT_PATH="script.py"

{
  echo "table SCC_v0"
  cat "$SCC_PATH"
  echo
  echo "endtable"
  echo "table WE_v0"
  cat "$WE_PATH"
  echo
  echo "endtable"
} > "$SCC_WE_PATH"

# Composition
echo "Running composition..."
"${cmd[@]}" -i "$SCC_WE_PATH" -o "$SCC_WE_COMPOSITION" -e BeUfFs -t composition -b 6 -a

rm -f $SCC_WE_PATH

# Refinement
composition_file_content=$(cat "$SCC_WE_COMPOSITION")
system_table=$(cat "$CONTROLLED_VEHICLE_PATH")
NEW="Composition"
OLD="Controller"

{
    echo "table $OLD"
    echo "$system_table"
    echo "endtable"
    echo "table $NEW"
    echo "$composition_file_content"
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
