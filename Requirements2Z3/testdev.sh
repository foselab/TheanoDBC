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

echo -e "\n\n*************************"
echo -e "Consistency Check"
echo -e "*************************\n"

echo "Requirements Table1_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table1_5.rt -o src/main/resources/Table1_5.py -e BeUfFs -t consistency -b 33 > /dev/null 2>&1
timeout 15 python src/main/resources/Table1_5.py
sleep 2

echo "Requirements Table2_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table2_5.rt -o src/main/resources/Table2_5.py -e BeUfFs -t consistency -b 33 > /dev/null 2>&1
timeout 15 python src/main/resources/Table2_5.py
sleep 2

echo "Requirements Table3_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table3_5.rt -o src/main/resources/Table3_5.py -e BeUfFs -t consistency -b 33 > /dev/null 2>&1
timeout 15 python src/main/resources/Table3_5.py
sleep 2

echo "Requirements Table4_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table4_5.rt -o src/main/resources/Table4_5.py -e BeUfFs -t consistency -b 33 > /dev/null 2>&1
timeout 15 python src/main/resources/Table4_5.py
sleep 2

echo -e "\n\n*************************"
echo -e "Completeness Check"
echo -e "*************************\n"

echo "Requirements Table1_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table1_5.rt -o src/main/resources/Table1_5.py -e BeUfVs -t completeness -b 6 > /dev/null 2>&1
timeout 15 python src/main/resources/Table1_5.py
sleep 2

echo "Requirements Table2_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table2_5.rt -o src/main/resources/Table2_5.py -e BeUfVs -t completeness -b 6 > /dev/null 2>&1
timeout 15 python src/main/resources/Table2_5.py
sleep 2

echo "Requirements Table3_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table3_5.rt -o src/main/resources/Table3_5.py -e BeUfVs -t completeness -b 6 > /dev/null 2>&1
timeout 15 python src/main/resources/Table3_5.py
sleep 2

echo "Requirements Table4_5"
java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/Table4_5.rt -o src/main/resources/Table4_5.py -e BeUfVs -t completeness -b 6 > /dev/null 2>&1
timeout 15 python src/main/resources/Table4_5.py
sleep 2