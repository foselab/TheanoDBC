#!/bin/bash

# Command
cmd="java -jar Theano.jar"

# Functions
cleanup_files() {
    find "$BASE_RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} +
    find "$BASE_RESOURCES_PATH" -type f -name "*.bak" -exec rm -f {} +
}

show_java_output=false
redirect_output=""
if [ "$show_java_output" = false ]; then
    redirect_output="> /dev/null 2>&1"
fi

# Paths
BASE_RESOURCES_PATH="."
CONTROLLED_VEHICLE_PATH="$BASE_RESOURCES_PATH/controlled_vehicle.rt"

# First refinement
CC1_PATH="$BASE_RESOURCES_PATH/first/cc.rt"
VE1_PATH="$BASE_RESOURCES_PATH/first/we.rt"
CC1VE1_PATH="$BASE_RESOURCES_PATH/first/temp.rt"
CC1VE1_COMPOSITION_PATH="$BASE_RESOURCES_PATH/first/composition.rt"
REFINEMENT_FILE_PATH_1="$BASE_RESOURCES_PATH/first/refinement.rt"
REFINEMENT_SCRIPT_PATH="$BASE_RESOURCES_PATH/first/script.py"

{
  echo "table CruiseController"
  cat "$CC1_PATH"
  echo -e "\nendtable"
  echo "table Vehicle"
  cat "$VE1_PATH"
  echo -e "\nendtable"
} > "$CC1VE1_PATH"

echo -e "\nFIRST CONFIGURATION"

# Composition
echo -e "\nRunning composition..."
eval $cmd -i "$CC1VE1_PATH" -o "$CC1VE1_COMPOSITION_PATH." -e BeUfFs -t composition -b 6 -a

rm -f $CC1VE1_PATH

# Refinement
composition_file_content=$(cat "$CC1VE1_COMPOSITION_PATH")
system_table=$(cat "$CONTROLLED_VEHICLE_PATH")

{
    echo "table ControlledVehicle"
    echo "$system_table"
    echo "endtable"
    echo "table Composition"
    echo "$composition_file_content"
    echo "endtable"
} > "$REFINEMENT_FILE_PATH_1"

echo -e "\nRunning refinement..."
eval $cmd -i "$REFINEMENT_FILE_PATH_1" -o "$REFINEMENT_SCRIPT_PATH" -t refinement $redirect_output
timeout 10 python "$REFINEMENT_SCRIPT_PATH"

# Second refinement
CC2_PATH="$BASE_RESOURCES_PATH/second/cc.rt"
VE2_PATH="$BASE_RESOURCES_PATH/second/we.rt"
CC2VE2_PATH="$BASE_RESOURCES_PATH/second/temp.rt"
CC2VE2_COMPOSITION_PATH="$BASE_RESOURCES_PATH/second/composition.rt"
REFINEMENT_FILE_PATH_2="$BASE_RESOURCES_PATH/second/refinement.rt"
REFINEMENT_SCRIPT_PATH="$BASE_RESOURCES_PATH/second/script.py"

{
  echo "table CruiseController"
  cat "$CC2_PATH"
  echo -e "\nendtable"
  echo "table Vehicle"
  cat "$VE2_PATH"
  echo -e "\nendtable"
} > "$CC2VE2_PATH"

echo -e "\nSECOND CONFIGURATION"

# Composition
echo -e "\nRunning composition..."
eval $cmd -i "$CC2VE2_PATH" -o "$CC2VE2_COMPOSITION_PATH." -e BeUfFs -t composition -b 6 -a

rm -f $CC2VE2_PATH

# Refinement
composition_file_content=$(cat "$CC2VE2_COMPOSITION_PATH")
system_table=$(cat "$CONTROLLED_VEHICLE_PATH")

{
    echo "table ControlledVehicle"
    echo "$system_table"
    echo "endtable"
    echo "table Composition"
    echo "$composition_file_content"
    echo "endtable"
} > "$REFINEMENT_FILE_PATH_2"

echo -e "\nRunning refinement..."
eval $cmd -i "$REFINEMENT_FILE_PATH_2" -o "$REFINEMENT_SCRIPT_PATH" -t refinement $redirect_output
timeout 10 python "$REFINEMENT_SCRIPT_PATH"

# End script cleaning up
cleanup_files
echo -e "\nDone"

