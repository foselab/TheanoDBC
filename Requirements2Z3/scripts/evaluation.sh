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
BASE_RESOURCES_PATH="../src/main/resources/evaluation"
FSM_RESOURCES_PATH="$BASE_RESOURCES_PATH/FSM"
TUSTIN_RESOURCES_PATH="$BASE_RESOURCES_PATH/TUI"
RESULT_PATH="$BASE_RESOURCES_PATH/results"
mkdir -p "$RESULT_PATH"

# Command
cmd="java $JVM_OPTS -classpath \"$CLASSPATH\" $MAIN_CLASS"

# Functions
run_with_timer() {
    local start_time=$(date +%s.%N)
    eval "$@" > /dev/null 2>&1
    local end_time=$(date +%s.%N)
    python3 -c "print($end_time - $start_time)"
}

cleanup_files() {
    find "$BASE_RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} +
    find "$BASE_RESOURCES_PATH" -type f -name "*.bak" -exec rm -f {} +
}

show_java_output=true
redirect_output=""
if [ "$show_java_output" = false ]; then
    redirect_output="> /dev/null 2>&1"
fi

trap "echo -e '\nCtrl+C detected. Exiting...'; cleanup_python_files; exit 0" SIGINT

# Iteration Count
ITERATIONS=50

# FSM Composition
composition_time_file="$RESULT_PATH/E1.txt"
[ -f "$composition_time_file" ] && mv "$composition_time_file" "${composition_time_file}.bak"
> "$composition_time_file"

for ((i = 1; i <= ITERATIONS; i++)); do
    echo "Running FSM composition iteration $i..."
    elapsed_time=$(run_with_timer "$cmd -i \"$FSM_RESOURCES_PATH/FSM.rt\" -o \"$FSM_RESOURCES_PATH/FSM_composition.rt\" -e BeUfFs -t composition -b 6 -a" $redirect_output)
    echo "$elapsed_time" >> "$composition_time_file"
done

# Refinement FSM
refinement_file_path="$FSM_RESOURCES_PATH/FSM_refinement.rt"
composition_file_content=$(cat "$FSM_RESOURCES_PATH/FSM_composition.rt")
system_table=$(sed '/endtable/ q' "$refinement_file_path")
{
    echo "$system_table"
    echo "table Composition"
    echo "$composition_file_content"
    echo "endtable"
} > "$refinement_file_path"

refinement_time_file="$RESULT_PATH/E2.txt"
[ -f "$refinement_time_file" ] && mv "$refinement_time_file" "${refinement_time_file}.bak"
> "$refinement_time_file"

for ((i = 1; i <= ITERATIONS; i++)); do
    echo "Running FSM refinement iteration $i..."
    elapsed_time=$(run_with_timer "$cmd -i \"$refinement_file_path\" -o \"$FSM_RESOURCES_PATH/FSM_refinement.py\" -t refinement" $redirect_output)
    if ! timeout 10 python "$FSM_RESOURCES_PATH/FSM_refinement.py"; then
        echo "Python script timed out or failed on iteration $i" >> "$refinement_time_file"
    fi
    echo "$elapsed_time" >> "$refinement_time_file"
done

# TUI Refinement
e=3
TABLES=("TUI_v2" "TUI_v3")
for table in "${TABLES[@]}"; do
    echo "Processing TUI table: $table"
    refinement_time_file="$RESULT_PATH/E${e}.txt"
    ((e++))
    [ -f "$refinement_time_file" ] && mv "$refinement_time_file" "${refinement_time_file}.bak"
    > "$refinement_time_file"
    
    for ((i = 1; i <= ITERATIONS; i++)); do
        echo "Running refinement for table $table, iteration $i..."
        refinement_file_path="$TUSTIN_RESOURCES_PATH/${table}.rt"
        refinement_python_file="$TUSTIN_RESOURCES_PATH/${table}_refinement.py"
        
        elapsed_time=$(run_with_timer "$cmd -i \"$refinement_file_path\" -o \"$refinement_python_file\" -t refinement" $redirect_output)
        if ! timeout 10 python "$refinement_python_file"; then
            echo "Python script timed out or failed on iteration $i" >> "$refinement_time_file"
        fi
        echo "$elapsed_time" >> "$refinement_time_file"
    done
done

cleanup_files
echo -e "\nDone"
