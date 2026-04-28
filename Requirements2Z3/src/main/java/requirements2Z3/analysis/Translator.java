package requirements2Z3.analysis;

import java.io.Reader;
import java.io.Writer;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import generated.matlabLexer;
import generated.matlabParser;
import requirements2Z3.consistency.Functionality;
import requirements2Z3.encodings.Encoder;
import requirements2Z3.rqt.RQTable;
import requirements2Z3.rqt.Requirement;
import requirements2Z3.rqt.Variables;
import requirements2Z3.visitors.DefineVariablesVisitor;
import requirements2Z3.visitors.translators.Table2Z3Visitor;
import requirements2Z3.z3formulae.Z3Formula;

public class Translator<T extends Table2Z3Visitor> {

	private Encoder encoder;
	private T z3visitor;
	private Reader sc;
	private Writer wt;
	private Functionality<T> functionality;

	public Encoder getEncoder() {
		return this.encoder;
	}

	public Translator(T z3visitor, Functionality<T> functionality, Reader scanner, Writer writer) {
		this.z3visitor = z3visitor;
		this.encoder = z3visitor.getEncoder();
		this.functionality = functionality;
		this.sc = scanner;
		this.wt = writer;
	}

	public void translate() throws Exception {

		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser parser = new matlabParser(tokens);
		parser.setBuildParseTree(true);

		RQTable tree=parser.primaryExpression().rqt;
				
		// creates the Z3 solver
		wt.write("from z3 import *;\n");

		wt.write("# Defines the Z3 solver\n");
		wt.write("solver = Solver()\n");

		// Define the types I and R that are used to define variables
		wt.write("# Define I and R\n");
		wt.write("I = IntSort()\n");
		wt.write("R = RealSort()\n");

		// visits the requirements table and creates a String that defines the variables
		// to be used in the encoding
		wt.write("# Signal variables definition\n");

		wt.write(new DefineVariablesVisitor().visit(tree) + "\n");
		
		if (tree.getTd()!=null) {
			 wt.write(tree.getTd().accept(z3visitor).toString());
		}


		// defines the quantification variables
		wt.write("# Quantification variables\n");

		wt.write("j = Int('j')\n");
		wt.write("i = Int('i')\n");
		wt.write("k = Int('k')\n");

		// define the timestamp array
		wt.write("# Timestamp structure\n");
		wt.write(this.encoder.defineTraceVariable());

		// add the monotonicity constraint to the timestamp structure
		wt.write("# Timestamp structure monotonicity\n");
		wt.write("solver.add(" + this.encoder.getMonotonicityConstraint() + ")\n");
		
		// add the encoding of the requirements table
		wt.write("# Requirements Table\n");
		wt.write("solver.add(" +this.functionality.getEncodingActivity(z3visitor, tree)+")\n");

		wt.write("# Processing the result\n");
		wt.write(this.processResult());

		sc.close();
		wt.close();
	}
	
	public void refinementCheck(RQTable first, RQTable second) throws Exception {
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser parser = new matlabParser(tokens);
		parser.setBuildParseTree(true);

		String tableName = first.getName();
		String newTableName = second.getName();
		
		Variables variables = first.getVariables();
		variables.addAll(second.getVariables());
		
		// get combined requirement for the two tables
		Requirement R1 = first.getTableRequirement();
		Requirement R2 = second.getTableRequirement();
		
		// convert requirements to z3formula
		Z3Formula A1 = R1.getPrecondition().accept(z3visitor);
		Z3Formula G1 = R1.getPostcondition().accept(z3visitor);
		Z3Formula A2 = R2.getPrecondition().accept(z3visitor);
		Z3Formula G2 = R2.getPostcondition().accept(z3visitor);
				
//		String A1inA2 = Z3Formula.getImplies(A1, A2).toString(); // A1 ⇒ A2
//		String G2inG1 = Z3Formula.getImplies(G2, G1).toString(); // G2 ⇒ G1
		
		// import libraries
		wt.write("from z3 import *;\n\n");
		
		// get tables names
		wt.write("# Tables names\n");
		wt.write("RQTableName=\""+tableName+"\"\n");
		wt.write("NewRQTableName=\""+newTableName+"\"\n\n");

		// creates the Z3 solver
		wt.write("# Defines the Z3 solver\n");
		wt.write("solver = Solver()\n");
		wt.write("solver.set(\"timeout\", 10000) # 10 sec\n\n");
		
		// Define the types I and R that are used to define variables
		wt.write("# Define I and R\n");
		wt.write("I = IntSort()\n");
		wt.write("R = RealSort()\n\n");
		
		// visits the requirements table and creates a String that defines the variables
		// to be used in the encoding
		wt.write("# Signal variables definition\n");
		wt.write(new DefineVariablesVisitor().visit(variables) + "\n");

		// Function to print the counter example
		// wt.write("# Utility function\n");
        // wt.write("def print_counterexample(model):\n");
        // wt.write("\tprint(\"-\" * 40)\n");
        // wt.write("\tprint(\"Counterexample\")\n");
        // wt.write("\tprint(\"-\" * 40)\n");
        // wt.write("\tfor v in model:\n");
        // wt.write("\t\tif v.name() != \"tau\":\n");
        // wt.write("\t\t\tprint(str(v) + \" = \" + str(model[v]))\n");
        // wt.write("\tprint(\"\")\n\n");
        
        // Function to evaluate conditions using a model
        // wt.write("# Function to evaluate conditions using a model\n");
        // wt.write("def evaluate_condition(condition, model, name):\n");
        // wt.write("\t# Dynamically extract variable-value pairs from the model, excluding 'tau'\n");
        // wt.write("\tvariable_values = {d.name(): model[d] for d in model if d.name()!='tau' and d.name()!='div0' and d.name()!='mod0' and d.name()[0].isalnum()}\n");
        // // wt.write("\tprint(\"Variable values:\", variable_values)\n\n");
        // wt.write("\t# Substitute values dynamically\n");
        // wt.write("\tsubstituted_condition = substitute(\n");
        // wt.write("\t\tcondition,\n");
        // wt.write("\t\t*[(eval(var_name), variable_values[var_name]) for var_name in variable_values]\n");
        // wt.write("\t)\n\n");
        // //wt.write("\tprint(f\"{name} = {substituted_condition}\")\n");
        // wt.write("\t# Simplified condition\n");
        // wt.write("\tsimplified_condition = simplify(substituted_condition)\n");
        // wt.write("\t# Evaluate the condition\n");
        // wt.write("\tcondition_result = is_true(simplified_condition)\n");
        // wt.write("\tprint(f\"{name} = {condition_result}\")\n\n");
        // wt.write("\treturn variable_values, condition_result\n\n");
        
        // Contradictions check
        // wt.write("# Function to find contradictions\n");
        // wt.write("def contradictions(condition, name, details=False):\n");
        // wt.write("\tglobal solver\n");
        // wt.write("\tsolver.push()\n");
        // wt.write("\tsolver.add(condition)\n");
        // wt.write("\tres = solver.check()\n");
        // wt.write("\tif details:\n");
        // wt.write("\t\tif res == sat: \n");
        // wt.write("\t\t\tprint(f\"{name} has no contradictions.\")\n");
        // wt.write("\t\telif res == unsat:\n");
        // wt.write("\t\t\tprint(f\"{name} has contradictions.\")\n");
        // wt.write("\t\telse:\n");
        // wt.write("\t\t\tprint(f\"{name}: unknown.\")\n");
        // wt.write("\tsolver.pop()\n");
        // wt.write("\treturn res == unsat\n\n");
        
        // Missing assertions
        // wt.write("# Function to find missing elements in a refinement condition\n");
        // wt.write("def fix_refinement_condition(source, target, name):\n");
        // wt.write("\tsolver = Solver()\n");
        // wt.write("\tupdated_target = target  # Start with the original target\n\n");
        // wt.write("\twhile True:\n");
        // wt.write("\t\tsolver.push()\n");
        // wt.write("\t\tsolver.add(source, Not(updated_target))  # Check source => target\n");
        // wt.write("\t\tif solver.check() == sat:\n");
        // wt.write("\t\t\tmodel = solver.model()\n");
        // wt.write("\t\t\tprint(f\"Refinement failed for {name}, finding missing terms...\")\n\n");
        // wt.write("\t\t\t# Find missing terms in the source that were true in the counterexample\n");
        // wt.write("\t\t\tmissing_terms = []\n");
        // wt.write("\t\t\tfor term in source.children():\n");
        // wt.write("\t\t\t\tif model.evaluate(term):\n");
        // wt.write("\t\t\t\t\tmissing_terms.append(term)\n\n");
        // wt.write("\t\t\tif not missing_terms:\n");
        // wt.write("\t\t\t\tprint(f\"No missing terms found for {name}, something is wrong.\")\n");
        // wt.write("\t\t\t\tbreak\n\n");
        // wt.write("\t\t\t# Add missing terms to the target\n");
        // wt.write("\t\t\tupdated_target = Or(updated_target, Or(*missing_terms))\n");
        // wt.write("\t\t\tprint(f\"Missing this assertion or part of it: {missing_terms}.\")\n");
        // wt.write("\t\telse:\n");
        // //wt.write("\t\t\tprint(f\"{name} is now valid!\")\n");
        // wt.write("\t\t\tbreak\n");
        // wt.write("\t\tsolver.pop()\n\n");
        // wt.write("\treturn updated_target\n\n");

        // Contracts
        wt.write("# Contracts\n");
        wt.write("A1="+A1.toString()+"\n");
        wt.write("A2="+A2.toString()+"\n");
        wt.write("G1="+G1.toString()+"\n");
        wt.write("G2="+G2.toString()+"\n\n");
        
        // Check if the conditions have contradictions
        // wt.write("# Check contradictions on requirements \n");
        // //wt.write("print(\"Checking contradictions in the requirements...\")\n");
        // wt.write("A1_sat=contradictions(A1, \"A1\", False)\n");
        // wt.write("A2_sat=contradictions(A2, \"A2\", False)\n");
        // wt.write("G1_sat=contradictions(G1, \"G1\", False)\n");
        // wt.write("G2_sat=contradictions(G2, \"G2\", False)\n\n");
        
        // Useless testing refinement if the conditions have contradictions
        // wt.write("if(A1_sat or A2_sat or G1_sat or G2_sat):\n");
        // wt.write("\tprint(\"contradictions\")\n");
        // wt.write("\texit()\n\n");
        // //wt.write("print(\"Couldn't find contradictions.\")\n\n");
        
        // Refinement conditions
        wt.write("# Refinement conditions \n");
        wt.write("refinement_A=Implies(A1,A2)\n");
        wt.write("refinement_G=Implies(G2,G1)\n\n");
        
        // Constraints
        wt.write("# Constraint \n");
        wt.write("solver.add(A1)\n\n");
        
        // Check refinement condition on assumptions
        wt.write("# Check refinement condition on assumptions\n");
        wt.write("solver.push()\n\n");
        wt.write("solver.add(Not(refinement_A))\n");
        wt.write("res = solver.check()\n");
        wt.write("if res == sat:\n");
        //wt.write("\tprint(f\"Assumptions violated.\")\n");
        //wt.write("\tmodel = solver.model()\n");
        //wt.write("\tevaluate_condition(A1, model, \"A1\")\n");
        //wt.write("\tevaluate_condition(A2, model, \"A2\")\n");
        //wt.write("\tprint_counterexample(model)\n");
        //wt.write("\tmissing_A = fix_refinement_condition(A1, A2, \"A2\")\n");
        wt.write("\tprint(f\"unsafe\")\n");
        wt.write("\tsolver.pop()\n");
        wt.write("\texit()\n");
        wt.write("elif res == unknown: \n");
        wt.write("\tprint(f\"unknown\")\n");
        wt.write("\tsolver.pop()\n");
        wt.write("\texit()\n\n");

        //wt.write("else:\n");
        //wt.write("\tprint(f\"Assumptions: unknown.\")\n");
        wt.write("solver.pop()\n\n");
                
        // Check refinement condition on guarantees
        wt.write("# Check refinement condition on guarantees\n");
        wt.write("solver.push()\n\n");
        wt.write("solver.add(Not(refinement_G))\n");
        wt.write("res = solver.check()\n");
        wt.write("if res == sat:\n");
        //wt.write("\tprint(f\"Guarantees violated.\")\n");
        //wt.write("\tmodel = solver.model()\n");
        //wt.write("\tevaluate_condition(G1, model, \"G1\")\n");
        //wt.write("\tevaluate_condition(G2, model, \"G2\")\n");
        //wt.write("\tprint_counterexample(model)\n");
        wt.write("\tprint(f\"unsafe\")\n");
        wt.write("\tsolver.pop()\n");
        wt.write("\texit()\n");
        wt.write("elif res == unknown: \n");
        wt.write("\tprint(f\"unknown\")\n");
        wt.write("\tsolver.pop()\n");
        wt.write("\texit()\n\n");
        //wt.write("else:\n");
        //wt.write("\tprint(f\"Guarantees: unknown.\")\n");
        
        wt.write("solver.pop()\n\n");
        wt.write("print(f\"safe\")\n");

		sc.close();
		wt.close();
	}
	
	public void generateSmtLibFormula(RQTable first, RQTable second) throws Exception {
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser parser = new matlabParser(tokens);
		parser.setBuildParseTree(true);

		String tableName = first.getName();
		String newTableName = second.getName();
		
		Variables variables = first.getVariables();
		variables.addAll(second.getVariables());
		
		// get combined requirement for the two tables
		Requirement R1 = first.getTableRequirement();
		Requirement R2 = second.getTableRequirement();
		
		// convert requirements to z3formula
		Z3Formula A1 = R1.getPrecondition().accept(z3visitor);
		Z3Formula G1 = R1.getPostcondition().accept(z3visitor);
		Z3Formula A2 = R2.getPrecondition().accept(z3visitor);
		Z3Formula G2 = R2.getPostcondition().accept(z3visitor);
						
		// import libraries
		wt.write("from z3 import *;\n\n");
		
		// get tables names
		wt.write("# Tables names\n");
		wt.write("RQTableName=\""+tableName+"\"\n");
		wt.write("NewRQTableName=\""+newTableName+"\"\n\n");

		// creates the Z3 solver
		wt.write("# Defines the Z3 solver\n");
		wt.write("solver = Solver()\n");
		wt.write("solver.set(\"timeout\", 10000) # 10 sec\n\n");
		
		// Define the types I and R that are used to define variables
		wt.write("# Define I and R\n");
		wt.write("I = IntSort()\n");
		wt.write("R = RealSort()\n\n");
		
		// visits the requirements table and creates a String that defines the variables
		// to be used in the encoding
		wt.write("# Signal variables definition\n");
		wt.write(new DefineVariablesVisitor().visit(variables) + "\n");

        // Contracts
        wt.write("# Contracts\n");
        wt.write("A1="+A1.toString()+"\n");
        wt.write("A2="+A2.toString()+"\n");
        wt.write("G1="+G1.toString()+"\n");
        wt.write("G2="+G2.toString()+"\n\n");
        
        // Refinement conditions
        wt.write("# Refinement conditions \n");
        wt.write("refinement_A=Implies(A1,A2)\n");
        wt.write("refinement_G=Implies(G2,G1)\n\n");
        
        wt.write("solver.push()\n\n");

        // Constraints
        wt.write("# Constraint \n");
        wt.write("solver.add(A1)\n");
        wt.write("solver.add(Not(And(refinement_A,refinement_G)))\n\n");

        // Print smtlib formula
        wt.write("# Generate smtlib formula \n");
		wt.write("print('(set-logic ALL)')\n");
		//wt.write("print('(set-option :timeout 10000)')\n");
		wt.write("print(solver.sexpr())\n");
		wt.write("print('(check-sat)')\n\n");
        wt.write("solver.pop()\n");
        
		sc.close();
		wt.close();
	}
	
	public void singleRefinementCheck(RQTable first, RQTable second) throws Exception {
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser parser = new matlabParser(tokens);
		parser.setBuildParseTree(true);

		String tableName = first.getName();
		String newTableName = second.getName();
		
		Variables variables = first.getVariables();
		variables.addAll(second.getVariables());
		
		// get combined requirement for the two tables
		Requirement R1 = first.getTableRequirement();
		Requirement R2 = second.getTableRequirement();
		
		// convert requirements to z3formula
		Z3Formula A1 = R1.getPrecondition().accept(z3visitor);
		Z3Formula G1 = R1.getPostcondition().accept(z3visitor);
		Z3Formula A2 = R2.getPrecondition().accept(z3visitor);
		Z3Formula G2 = R2.getPostcondition().accept(z3visitor);
						
		// import libraries
		wt.write("from z3 import *;\n\n");
		
		// get tables names
		wt.write("# Tables names\n");
		wt.write("RQTableName=\""+tableName+"\"\n");
		wt.write("NewRQTableName=\""+newTableName+"\"\n\n");

		// creates the Z3 solver
		wt.write("# Defines the Z3 solver\n");
		wt.write("solver = Solver()\n");
		wt.write("solver.set(\"timeout\", 10000) # 10 sec\n\n");
		
		// Define the types I and R that are used to define variables
		wt.write("# Define I and R\n");
		wt.write("I = IntSort()\n");
		wt.write("R = RealSort()\n\n");
		
		// visits the requirements table and creates a String that defines the variables
		// to be used in the encoding
		wt.write("# Signal variables definition\n");
		wt.write(new DefineVariablesVisitor().visit(variables) + "\n");

        // Contracts
        wt.write("# Contracts\n");
        wt.write("A1="+A1.toString()+"\n");
        wt.write("A2="+A2.toString()+"\n");
        wt.write("G1="+G1.toString()+"\n");
        wt.write("G2="+G2.toString()+"\n\n");
        
        // Refinement conditions
        wt.write("# Refinement conditions \n");
        wt.write("refinement_A=Implies(A1,A2)\n");
        wt.write("refinement_G=Implies(G2,G1)\n\n");
        
        wt.write("solver.push()\n\n");

        // Constraints
        wt.write("# Constraint \n");
        wt.write("solver.add(A1)\n");
        wt.write("solver.add(Not(And(refinement_A,refinement_G)))\n\n");
        
        // Check refinement condition
        wt.write("# Check refinement condition\n");
        wt.write("res = solver.check()\n");
        wt.write("if res == sat:\n");
        wt.write("\tprint(f\"unsafe\")\n");
        wt.write("elif res == unsat: \n");
        wt.write("\tprint(f\"safe\")\n");
        wt.write("else: \n");
        wt.write("\tprint(f\"unknown\")\n\n");

        wt.write("solver.pop()\n");

		sc.close();
		wt.close();
	}
	

	/**
	 * this function adds a part that checks whether the result is sat or unsat, and
	 * the corresponding result based on the functionality (consistency or
	 * completeness)
	 * 
	 * @param sc
	 * @param wt
	 * @throws Exception
	 */
	private String processResult() throws Exception {

		StringBuilder b = new StringBuilder();

		b.append("res=solver.check()\n");
		b.append("if (res.r ==  Z3_L_FALSE):\n");

		b.append(this.functionality.printPositiveResult());

		b.append("\t sys.exit(1)\n");
		b.append("else:\n");
		b.append("\t if (res.r == Z3_L_TRUE):\n");

		b.append(this.functionality.printNegativeResult());
		b.append("\t\t sys.exit(-1)\n");
		b.append("\t else:\n");
		b.append("\t\t print('unknown')\n");
		b.append("#\t\t print(solver.reason_unknown())\n");
		b.append("\t\t sys.exit(0)\n");

		return b.toString();
	}

	public Z3Formula visitTree(RQTable tree) {
		return tree.accept(z3visitor);
	}
}