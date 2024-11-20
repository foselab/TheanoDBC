package requirements2Z3.rqt;

import java.util.LinkedHashSet;
import java.util.Set;

import requirements2Z3.visitors.RQTableVisitor;

public class Variables {

	private Set<Variable> vars;
	
	
	public Variables() {
		vars=new LinkedHashSet<Variable>();
	}
			
	public void add(Variable v) {
		this.vars.add(v);	
	}
	
	public void addAll(Variables vars) {
		this.vars.addAll(vars.getVariables());
	}
		
	public Set<Variable> getVariables(){
		return this.vars;
	}
	
	public Variables getInputVariables() {
	    return filterVariablesByType("input");
	}

	public Variables getOutputVariables() {
	    return filterVariablesByType("output");
	}

	private Variables filterVariablesByType(String type) {
	    Variables filteredVariables = new Variables();
	    for (Variable variable : getVariables()) {
	        if (type.equals(variable.getInputOutput())) {
	            filteredVariables.add(variable);
	        }
	    }
	    return filteredVariables;
	}
		
	public <T> T accept(RQTableVisitor<T> visitor) {
		return visitor.visit(this);
	}
}
