package requirements2Z3.rqt;

public class ComposedRQTable extends RQTable {
	private RQTable first;
	private RQTable second;
	
	public ComposedRQTable(RQTable first, RQTable second) {
		super(null, getVariables(first, second), getRequirements(first, second));

		this.first = first;
		this.second = second;
	}

	public RQTable getFirst() {
		return first;
	}

	public RQTable getSecond() {
		return second;
	}
	
	private static Variables getVariables(RQTable first, RQTable second) {
		Variables vars = first.getVariables();
		vars.addAll(second.getVariables());
		return vars;
	}
	
	private static Requirements getRequirements(RQTable first, RQTable second) {
		Requirement fst = first.getRequirements().getRequirement(0);
		Requirement snd = second.getRequirements().getRequirement(0);
		
		PFormula A1 = fst.getPrecondition();
		PFormula G1 = fst.getPostcondition();
		PFormula A2 = snd.getPrecondition();
		PFormula G2 = snd.getPostcondition(); 
		
		AndFormula post = new AndFormula(G1, G2);
		OrFormula pre = new OrFormula(new AndFormula(A1, A2), new NegationFormula(post));
		
		Requirements req = new Requirements();
		req.add(new Requirement(pre, post));
		return req;
	}
}
