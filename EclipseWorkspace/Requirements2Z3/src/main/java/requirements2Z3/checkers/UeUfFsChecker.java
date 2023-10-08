package requirements2Z3.checkers;

import java.io.IOException;
import java.io.Writer;
import java.util.Scanner;

import org.antlr.v4.runtime.tree.ParseTree;

import requirements2Z3.Checker;
import requirements2Z3.RTFunctionality;
import requirements2Z3.visitors.UeUfFs;

public class UeUfFsChecker extends Checker {

	private float ts;

	public UeUfFsChecker(String inputFile, String outputFile,RTFunctionality functionality, float ts) throws Exception {
		super(inputFile, outputFile,functionality);
		this.ts = ts;
	}

	public void processVariableDefinitions(Scanner sc, Writer wt) throws IOException, Exception {
		super.processVariableDefinitions(sc, wt);

		
		wt.write("Ts = Real('Ts')\n");

	}
	
	

	@Override
	public void defineTau(Scanner sc, Writer wt) throws Exception {
		wt.write("tau = Function('tau', IntSort(), RealSort())\n");
	}

	@Override
	public String visitTree(ParseTree tree) {
		return tree.accept(new UeUfFs());
	}

	@Override
	public String getMonotonicityConstraint() {
		return "And(ForAll(j,Implies(j>=0,(tau(j+1)-tau(j)==" + ts + "))),tau(0)==0)";
	}

	@Override
	public void writeTimestampConstraint(Writer wt) throws IOException {
		wt.write("s.add(Ts==" + ts + ")\n");
	}
	@Override
	public void processRequirements(Scanner sc, Writer wt) throws Exception {
		this.functionality.processRequirements(sc, wt, this);
	}
}
