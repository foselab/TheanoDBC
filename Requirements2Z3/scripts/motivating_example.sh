#!/bin/bash

# Configuration
CLASSPATH="../target/classes:\
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
BASE_RESOURCES_PATH="../src/main/resources/motivating_example"

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

trap "echo -e '\nCtrl+C detected. Exiting...'; cleanup_python_files; exit 0" SIGINT

# Composition
echo -e "\nRunning composition..."
eval $cmd -i "$BASE_RESOURCES_PATH/motivating_example.rt" -o "$BASE_RESOURCES_PATH/motivating_example_composition.rt" -e BeUfFs -t composition -b 6 -a

# Refinement FSM
refinement_file_path="$BASE_RESOURCES_PATH/motivating_example_refinement.rt"
composition_file_content=$(cat "$BASE_RESOURCES_PATH/motivating_example_composition.rt")
system_table=$(sed '/endtable/ q' "$refinement_file_path")
{
    echo "$system_table"
    echo "table Composition"
    echo "$composition_file_content"
    echo "endtable"
} > "$refinement_file_path"

echo -e "\nRunning refinement..."
eval $cmd -i "$refinement_file_path" -o "$BASE_RESOURCES_PATH/motivating_example_refinement.py" -t refinement $redirect_output
timeout 10 python "$BASE_RESOURCES_PATH/motivating_example_refinement.py"

cleanup_files
echo -e "\nDone"

while true; do
    sleep 1
done