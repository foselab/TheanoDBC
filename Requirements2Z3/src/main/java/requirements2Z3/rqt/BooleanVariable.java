package requirements2Z3.rqt;

import requirements2Z3.visitors.RQTableVisitor;

public class BooleanVariable extends PFormula {

	private final String id;
	private final boolean value;

	public BooleanVariable(String id, boolean value) {
		this.id = id;
		this.value = value;
	}
	
	public String getId() {
		return id;
	}

	public boolean getValue() {
		return value;
	}
	
	public <T> T accept(RQTableVisitor<T> visitor) {
		return visitor.visit(this);
	}
}
