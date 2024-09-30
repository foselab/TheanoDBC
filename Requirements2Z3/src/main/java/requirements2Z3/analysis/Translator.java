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
	
	public void refinementCheck(RQTable RQTable, RQTable NewRQTable) throws Exception {
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser parser = new matlabParser(tokens);
		parser.setBuildParseTree(true);

		String tableName = RQTable.getName();
		String newTableName = NewRQTable.getName();
		
		// creates the Z3 solver
		wt.write("from z3 import *;\n\n");
		
		wt.write("# Tables names\n");
		wt.write("RQTableName=\""+tableName+"\"\n");
		wt.write("NewRQTableName=\""+newTableName+"\"\n\n");

		wt.write("# Defines the Z3 solver\n");
		wt.write("solver = Solver()\n\n");
		
		// Define the types I and R that are used to define variables
		wt.write("# Define I and R\n");
		wt.write("I = IntSort()\n");
		wt.write("R = RealSort()\n\n");
		
		// visits the requirements table and creates a String that defines the variables
		// to be used in the encoding
		wt.write("# Signal variables definition\n");
		wt.write(new DefineVariablesVisitor().visit(RQTable) + "\n");
		wt.write(new DefineVariablesVisitor().visit(NewRQTable) + "\n");
		
		if (RQTable.getTd()!=null) {
			 wt.write(RQTable.getTd().accept(z3visitor).toString());
		}

		if (NewRQTable.getTd()!=null) {
			 wt.write(NewRQTable.getTd().accept(z3visitor).toString());
		}

		// defines the quantification variables
		wt.write("# Quantification variables\n");

		wt.write("j = Int('j')\n");
		wt.write("i = Int('i')\n");
		wt.write("k = Int('k')\n\n");
		
		// define the timestamp array
		wt.write("# Timestamp structure\n");
		wt.write(this.encoder.defineTraceVariable() + "\n");

		// add the monotonicity constraint to the timestamp structure
		wt.write("# Timestamp structure monotonicity\n");
		wt.write("solver.add(" + this.encoder.getMonotonicityConstraint() + ")\n\n");
							
		// convert requirements to z3formula
		Z3Formula A1 = RQTable.getRequirements().getRequirement(0).getPrecondition().accept(z3visitor);
		Z3Formula G1 = RQTable.getRequirements().getRequirement(0).getPostcondition().accept(z3visitor);
		Z3Formula A2 = NewRQTable.getRequirements().getRequirement(0).getPrecondition().accept(z3visitor);
		Z3Formula G2 = NewRQTable.getRequirements().getRequirement(0).getPostcondition().accept(z3visitor);
		
		String A1inA2 = Z3Formula.getImplies(A1, A2).toString(); // A1 ⇒ A2
		String G2inG1 = Z3Formula.getImplies(G2, G1).toString(); // G2 ⇒ G1
		
		wt.write("# Refinement condition \n");
		wt.write("refinement_condition=And("+A1inA2+","+G2inG1+")\n");
		wt.write("solver.add(Not(refinement_condition))\n\n");
		wt.write("if solver.check() == unsat:\n");
		wt.write("\tprint(f\"{NewRQTableName} refines {RQTableName} (compatible update) \")\n");
		wt.write("else:\n");
		wt.write("\tprint(f\"{NewRQTableName} does NOT refine {RQTableName} (update NOT recommended)\")\n");
		wt.write("\tprint(\"Model example:\")\n");
		wt.write("\tprint(solver.model())");
		
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