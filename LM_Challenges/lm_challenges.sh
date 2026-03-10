#!/usr/bin/env bash

# Detect OS and set Python command
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" || "$OS" == "Windows_NT" ]]; then
    python_cmd="py -3"
    FIND_EXEC="find"
else
    python_cmd="python3"
    FIND_EXEC="find"
fi

# Command
cmd=(java -jar ../Theano.jar)
BASE_RESOURCES_PATH="."

show_java_output=false

# Model Name
models_name=("FSM AP EB EUL NLG NN REG SWIM TSM TUI")

for model_name in $models_name; do
    cd "$model_name"

    system_name="${model_name}_v1"
    versions=("${model_name}_v2" "${model_name}_v3")

    for current_version in "${versions[@]}"; do  
        refinement_file_name=${current_version}_refinement

        # Files path
        ota_file_path="$BASE_RESOURCES_PATH/${current_version}.rt"

        if [ "$model_name" = "FSM" ] ; then
            composition_file_path="$BASE_RESOURCES_PATH/${current_version}_composition.rt"
            model_file_path="$BASE_RESOURCES_PATH/${current_version}.rt"
            ota_file_path="$composition_file_path"

            echo -e "\nRunning composition for ${current_version}..."

            if [ "$show_java_output" = false ] ; then
                "${cmd[@]}" -i "$model_file_path" -o "$composition_file_path" -e BeUfFs -t composition -b 6 -a > /dev/null 2>&1
            else
                "${cmd[@]}" -i "$model_file_path" -o "$composition_file_path" -e BeUfFs -t composition -b 6 -a
            fi
        fi

        # Refinement
        refinement_file_path="$BASE_RESOURCES_PATH/${refinement_file_name}.rt"
        ota_file_content=$(cat "$ota_file_path")
        system_file_content=$(cat "$BASE_RESOURCES_PATH/${system_name}.rt")

        # Building the refinement file
        {
        echo "table $system_name"
        echo "$system_file_content"
        echo
        echo "endtable"
        echo "table $current_version"
        echo "$ota_file_content"
        echo
        echo "endtable"
        } > "$refinement_file_path"

        refinement_script_path="$BASE_RESOURCES_PATH/${refinement_file_name}.py"

        # Refinement check
        echo -e "\nDoes ${current_version} refine ${system_name}?"
        if [ "$show_java_output" = false ] ; then
            "${cmd[@]}" -i "$refinement_file_path" -o "$refinement_script_path" -t refinement > /dev/null 2>&1
        else
            "${cmd[@]}" -i "$refinement_file_path" -o "$refinement_script_path" -t refinement
        fi

        # Run Python script
        $python_cmd "$refinement_script_path"
        
    done

    cd ..
done

# Cleanup
cleanup_files() {
    $FIND_EXEC "$BASE_RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} \;
    $FIND_EXEC "$BASE_RESOURCES_PATH" -type f -name "*.bak" -exec rm -f {} \;
}

cleanup_files

echo
echo "Done"
