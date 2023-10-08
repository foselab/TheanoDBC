package requirements2Z3.checkers;

import java.io.IOException;
import java.io.Writer;
import java.util.Scanner;

import org.antlr.v4.runtime.tree.ParseTree;

import requirements2Z3.RTBoundedFunctionality;
import requirements2Z3.visitors.BeUfFs;

public class BeUfFsChecker extends BoundedChecker {

	private final float ts;
	private RTBoundedFunctionality boundedFunctionality;

	public BeUfFsChecker(String inputFile, String outputFile, RTBoundedFunctionality functionality, float ts, int bound)
			throws Exception {
		super(inputFile, outputFile, functionality, bound);
		this.ts = ts;
		this.boundedFunctionality=functionality;
	}

	public float getTs() {
		return ts;
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
		return tree.accept(new BeUfFs(this.boundedFunctionality.getCurrentIndexI(),this.ts));
	}

	@Override
	public String getMonotonicityConstraint() {
		StringBuilder bulder = new StringBuilder();

		float currentTs = 0;
		bulder.append("And(");
		for (int i = 0; i < this.getBound(); i++) {
			if (i != 0) {
				bulder.append(",");
			}
			bulder.append("tau(" + i + ")==" + currentTs);
			currentTs = currentTs + this.getTs();
		}
		bulder.append(")");

		return bulder.toString();
	}

	@Override
	public void writeTimestampConstraint(Writer wt) throws IOException {
		wt.write("s.add(Ts==" + this.getTs() + ")\n");
	}

	@Override
	public void processRequirements(Scanner sc, Writer wt) throws Exception {
		this.functionality.processRequirements(sc, wt, this);
	}
}
