#!/bin/bash

theano="Theano.jar"

# true -> run from source 
# false ->  java -jar Theano.jar
dev=true

# Set the classpath (replace backslashes with forward slashes)
CLASSPATH="target/classes:\
$HOME/.m2/repository/org/antlr/antlr4/4.5/antlr4-4.5.jar:\
$HOME/.m2/repository/org/antlr/antlr4-runtime/4.5/antlr4-runtime-4.5.jar:\
$HOME/.m2/repository/org/abego/treelayout/org.abego.treelayout.core/1.0.1/org.abego.treelayout.core-1.0.1.jar:\
$HOME/.m2/repository/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar:\
$HOME/.m2/repository/org/antlr/ST4/4.0.8/ST4-4.0.8.jar:\
$HOME/.m2/repository/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.jar:\
$HOME/.m2/repository/commons-cli/commons-cli/1.5.0/commons-cli-1.5.0.jar"

# Set any JVM options
JVM_OPTS="-Dfile.encoding=UTF-8 \
-Dstdout.encoding=UTF-8 \
-Dstderr.encoding=UTF-8 \
-XX:+ShowCodeDetailsInExceptionMessages"

# Set the main class
MAIN_CLASS="requirements2Z3.Main"

# Set the resources path (adjust the path to the correct location)
RESOURCES_PATH="src/main/resources"

# Set the command based on dev variable
if [ "$dev" = false ]; then
    cmd="java -jar $theano"
else
    cmd="java $JVM_OPTS -classpath \"$CLASSPATH\" $MAIN_CLASS"
fi

# Tables to be checked
TABLES=()
PAPER_TABLES=("TableCar_v1" "TableCar_v2" "TableCar_v3" "TableController_v1") # demonstration paper examples, check completeness and consistency
COMPOSITION_TABLES=("System") # composition examples
REFINEMENT_TABLES=("ABS_v1" "ABS_v2" "ABS_v3" "ABS_v4" "ABS_v5") # refinement examples

# Initialize flags for completeness, consistency, and refinement
run_completeness=false
run_consistency=false
run_refinement=false
run_composition=false

show_java_output=false
redirect_output=""

if [ "$show_java_output" = false ]; then
    redirect_output="> /dev/null 2>&1"
fi

# Manual argument parsing for long options
for arg in "$@"; do
  case $arg in
    -refinement)
      run_refinement=true
      shift
      ;;
    -completeness)
      run_completeness=true
      shift
      ;;
    -consistency)
      run_consistency=true
      shift
      ;;
    -composition)
      run_composition=true
      shift
      ;;
    *)
      echo "Invalid option: $arg"
      ;;
  esac
done

# If no options are provided, display a message and enter an infinite loop
if [ "$run_completeness" = false ] && [ "$run_consistency" = false ] && [ "$run_refinement" = false ] && [ "$run_composition" = false ]; then
    echo -e "Please run the script with one of the following options:\n \t[-refinement]\n \t[-completeness]\n \t[-consistency]\n \t[-composition]\n"
    echo "Press [Ctrl+C] to exit."
    while true; do
        sleep 1
    done
fi

# Check composition for each table
if [ "$run_composition" = true ]; then
    echo -e "\n\n***********************************************"
    echo -e "Composition"
    echo -e "***********************************************"
    RESOURCES_PATH="src/main/resources/composition_examples"
    TABLES=("${COMPOSITION_TABLES[@]}")

    for table in "${TABLES[@]}"; do
        echo -e "\n$table"

        eval $cmd -i "$RESOURCES_PATH/$table.rt" -o "$RESOURCES_PATH/${table}-composed.rt" -e BeUfFs -t composition -b 6 -a
        sleep 2
    done
fi

# Check refinement for each table
if [ "$run_refinement" = true ]; then
    echo -e "\n\n***********************************************"
    echo -e "Refinement check"
    echo -e "***********************************************"
    RESOURCES_PATH="src/main/resources/refinement_examples"
    TABLES=("${REFINEMENT_TABLES[@]}")
    
    for table in "${TABLES[@]}"; do
        echo -e "\n$table"

        eval $cmd -i "$RESOURCES_PATH/$table.rt" -o "$RESOURCES_PATH/${table}_refinement.py" -t refinement $redirect_output
        timeout 10 python "$RESOURCES_PATH/${table}_refinement.py"
        sleep 2
    done
fi

# Check completeness and consistency for each table
if [[ "$run_completeness" = true || "$run_consistency" = true ]]; then
    echo -e "\n\n***********************************************"
    echo -e "Completeness/Consistency check"
    echo -e "***********************************************"
    RESOURCES_PATH="src/main/resources/paper_examples"
    TABLES=("${PAPER_TABLES[@]}")
    
    for table in "${TABLES[@]}"; do
        echo -e "\n$table"

        if [ "$run_completeness" = true ]; then
            eval $cmd -i "$RESOURCES_PATH/$table.rt" -o "$RESOURCES_PATH/${table}_completeness.py" -e BeUfFs -t completeness -b 6 $redirect_output
            timeout 10 python "$RESOURCES_PATH/${table}_completeness.py"
            sleep 2
        fi

        if [ "$run_consistency" = true ]; then
            eval $cmd -i "$RESOURCES_PATH/$table.rt" -o "$RESOURCES_PATH/${table}_consistency.py" -e BeUfFs -t consistency -b 6 $redirect_output
            timeout 10 python "$RESOURCES_PATH/${table}_consistency.py"
            sleep 2
        fi
    done
fi

# Remove python files if any checks were run
if [ "$run_completeness" = true ] || [ "$run_consistency" = true ] || [ "$run_refinement" = true ]; then
    find "$RESOURCES_PATH" -type f -name "*.py" -exec rm -f {} +
fi
