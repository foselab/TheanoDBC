#!/bin/bash

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
RESOURCES_PATH="src/main/resources/paper_examples"

# Tables to be checked
TABLES=("TableCar_v1" "TableCar_v2" "TableCar_v3" "TableController_v1")

# Check completeness and consistency for each table
for table in "${TABLES[@]}"; do
    echo -e "\n$table"

    java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i $RESOURCES_PATH/$table.rt -o $RESOURCES_PATH/${table}_completeness.py -e BeUfFs -t completeness -b 6 > /dev/null 2>&1
    timeout 10 python $RESOURCES_PATH/${table}_completeness.py
    sleep 2
   
    java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i $RESOURCES_PATH/$table.rt -o $RESOURCES_PATH/${table}_consistency.py -e BeUfFs -t consistency -b 6 > /dev/null 2>&1
    timeout 10 python $RESOURCES_PATH/${table}_consistency.py
    sleep 2
done

# Remove python files if any checks were run
rm -f $RESOURCES_PATH/*.py
