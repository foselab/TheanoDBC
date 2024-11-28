#!/bin/bash

# Set the classpath
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

# Set the resources path
RESOURCES_PATH="../src/main/resources/evaluation"

# Set the command based on dev variable
cmd="java $JVM_OPTS -classpath \"$CLASSPATH\" $MAIN_CLASS"

# Tables to be checked
TABLES=("paper" "fsm")

show_java_output=false

redirect_output=""
if [ "$show_java_output" = false ]; then
    redirect_output="> /dev/null 2>&1"
fi

for table in "${TABLES[@]}"; do
    # Composition for each table
    echo -e "\n\n$table\n"
    echo -e "***********************************************"
    echo -e "Composition"
    echo -e "***********************************************"

    file_path="$RESOURCES_PATH/$table/$table.rt"
    composition_file_path="$RESOURCES_PATH/$table/$table-composition.rt"
    refinement_file_path="$RESOURCES_PATH/$table/$table-refinement.rt"
    refinement_python_file="$RESOURCES_PATH/$table/${table}_refinement.py"

    eval $cmd -i "$file_path" -o "$composition_file_path" -e BeUfFs -t composition -b 6 -a
    sleep 1
    
    composition_file_content=$(cat "$composition_file_path")
    system_table=$(awk '/table/, /endtable/' "$refinement_file_path")
    composition_table=$(echo "$composition_file_content" | awk '/table Composition/, /endtable/')
    refinement_file_content="${system_table}${composition_table}"
    echo "$refinement_file_content" > "$refinement_file_path"

    # Check refinement for each table
    echo -e "\n\n***********************************************"
    echo -e "Refinement check"
    echo -e "***********************************************"

    eval $cmd -i "$refinement_file_path" -o "$refinement_python_file" -t refinement $redirect_output
    sleep 1

    timeout 10 python "$refinement_python_file"
done

# Remove python files if any checks were run
find "$RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} +
