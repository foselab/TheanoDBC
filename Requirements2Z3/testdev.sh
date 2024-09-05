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

# Remove python files
rm -f src/main/resources/*.py

echo -e "\nRequirements TableAM_01_Car"

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_01_Car.rt -o src/main/resources/TableAM_03_completeness.py -e BeUfFs -t completeness -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_03_completeness.py
sleep 2

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_01_Car.rt -o src/main/resources/TableAM_03_consistency.py -e BeUfFs -t consistency -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_03_consistency.py
sleep 2

echo -e "\nRequirements TableAM_02_Car"

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_02_Car.rt -o src/main/resources/TableAM_02_completeness.py -e BeUfFs -t completeness -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_02_completeness.py
sleep 2

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_02_Car.rt -o src/main/resources/TableAM_02_consistency.py -e BeUfFs -t consistency -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_02_consistency.py

echo -e "\nRequirements TableAM_03_Car"

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_03_Car.rt -o src/main/resources/TableAM_03_completeness.py -e BeUfFs -t completeness -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_03_completeness.py
sleep 2

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_03_Car.rt -o src/main/resources/TableAM_03_consistency.py -e BeUfFs -t consistency -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_03_consistency.py
sleep 2

echo -e "\nRequirements TableAM_03_Controller"

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_03_Controller.rt -o src/main/resources/TableAM_04_completeness.py -e BeUfFs -t completeness -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_04_completeness.py
sleep 2

java $JVM_OPTS -classpath "$CLASSPATH" $MAIN_CLASS -i src/main/resources/TableAM_03_Controller.rt -o src/main/resources/TableAM_04_consistency.py -e BeUfFs -t consistency -b 6 > /dev/null 2>&1
timeout 10 python src/main/resources/TableAM_04_consistency.py
sleep 2

# Remove python files
rm -f src/main/resources/*.py