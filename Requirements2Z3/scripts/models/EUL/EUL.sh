#!/bin/bash

# Configuration
CLASSPATH="../../../target/classes:\
$HOME/.m2/repository/org/antlr/antlr4/4.5/antlr4-4.5.jar:\
$HOME/.m2/repository/org/antlr/antlr4-runtime/4.5/antlr4-runtime-4.5.jar:\
$HOME/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.jar:\
$HOME/.m2/repository/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar:\
$HOME/.m2/repository/org/antlr/ST4/4.0.8/ST4-4.0.8.jar:\
$HOME/.m2/repository/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.jar:\
$HOME/.m2/repository/commons-cli/commons-cli/1.5.0/commons-cli-1.5.0.jar"

# Set JVM options
JVM_OPTS="-Dfile.encoding=UTF-8 \
-Dstdout.encoding=UTF-8 \
-Dstderr.encoding=UTF-8 \
-XX:+ShowCodeDetailsInExceptionMessages"

# Set the main class
MAIN_CLASS="requirements2Z3.Main"

# Paths
BASE_RESOURCES_PATH="."

# Command
cmd="java $JVM_OPTS -classpath \"$CLASSPATH\" $MAIN_CLASS"

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

#trap "echo -e '\nCtrl+C detected. Exiting...'; cleanup_files; exit 0" SIGINT

# Model Name
model_name="EUL"
system_name="EUL_v1"
versions=("EUL_v2")

for current_version in "${versions[@]}"; do    
    refinement_file_name=${current_version}_refinement

    # Files path
    model_file_path="$BASE_RESOURCES_PATH/${current_version}.rt"
    ota_file_path="$BASE_RESOURCES_PATH/${current_version}.rt"

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
    python "$refinement_script_path"

done

#cleanup_files
echo -e "\nDone"

while true; do
    sleep 1
done