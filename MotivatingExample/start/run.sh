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
  echo -e "\nendtable"
  echo "table WE_v0"
  cat "$WE_PATH"
  echo -e "\nendtable"
} > "$SCC_WE_PATH"

# Composition
echo -e "\nRunning composition..."
eval $cmd -i "$SCC_WE_PATH" -o "$SCC_WE_COMPOSITION." -e BeUfFs -t composition -b 6 -a

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
