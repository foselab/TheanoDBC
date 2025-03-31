#!/bin/bash

# Paths
BASE_RESOURCES_PATH="."

# Command
cmd="java -jar ../Theano.jar"

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

# Model Name
model_name="FSM"
system_name="FSM_system"
versions=("FSM_v0" "FSM_v1") # FSM_v0 or FSM_v1

for current_version in "${versions[@]}"; do    
    refinement_file_name=${current_version}_refinement

    # Files path
    composition_file_path="$BASE_RESOURCES_PATH/${current_version}_composition.rt"

    model_file_path="$BASE_RESOURCES_PATH/${current_version}.rt"
    ota_file_path="$composition_file_path"

    # Composition
    echo -e "\nRunning composition..."
    eval $cmd -i "$model_file_path" -o "$composition_file_path" -e BeUfFs -t composition -b 6 -a

    # Refinement
    refinement_file_path="$BASE_RESOURCES_PATH/${refinement_file_name}.rt"
    ota_file_content=$(cat "$ota_file_path")
    system_file_content=$(cat "$BASE_RESOURCES_PATH/${system_name}.rt")

    echo "table ${system_name}" > "$refinement_file_path"
    echo "$system_file_content" >> "$refinement_file_path"
    echo "endtable" >> "$refinement_file_path"

    echo "table ${current_version}" >> "$refinement_file_path"
    echo "$ota_file_content" >> "$refinement_file_path"
    echo "endtable" >> "$refinement_file_path"

    echo -e "\nDoes ${current_version} refine ${system_name}?"

    refinement_script_path="$BASE_RESOURCES_PATH/${refinement_file_name}.py"

    eval $cmd -i "$refinement_file_path" -o "$refinement_script_path" -t refinement $redirect_output
    timeout 10 python "$refinement_script_path"

done

#cleanup_files
echo -e "\nDone"
