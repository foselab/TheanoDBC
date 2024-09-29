package requirements2Z3.rqt;

import java.util.Objects;

import requirements2Z3.visitors.RQTableVisitor;

public class Variable {

	private final String name;

	private final String type;

	private final String inputOutput;

	public Variable(String name, String type, String inputOutput) {
		this.name = name;
		this.type = type;
		this.inputOutput = inputOutput;
	}

	public String getName() {
		return name;
	}

	public String getType() {
		return type;
	}

	public String getInputOutput() {
		return inputOutput;
	}
	
	@Override
    public boolean equals(Object obj) {
		if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Variable other = (Variable) obj;

        return Objects.equals(this.name, other.name) &&
               Objects.equals(this.type, other.type) &&
               Objects.equals(this.inputOutput, other.inputOutput);
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.name, this.type, this.inputOutput);
    }

	public <T> T accept(RQTableVisitor<T> visitor) {
		return visitor.visit(this);
	}

}
