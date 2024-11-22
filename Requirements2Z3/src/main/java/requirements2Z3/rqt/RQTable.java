package requirements2Z3.rqt;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import requirements2Z3.visitors.RQTableToStringVisitor;
import requirements2Z3.visitors.RQTableVisitor;

public class RQTable {

	private final TimestampDefinition td;
	private Requirements requirements;
	private Variables variables;
	private String name = null;
	
	public RQTable(TimestampDefinition td, Variables variables, Requirements requirements) {
		this.td=td;
		this.requirements=requirements;
		this.variables=variables;
	}
	
	public <T> T accept(RQTableVisitor<T> visitor) {
		return visitor.visit(this);
	}

	public Requirements getRequirements() {
		return requirements;
	}
	
	public Requirement getTableRequirement() {
		int n_req = this.getRequirements().getRequirements().size();
		
		if (n_req < 2)
			return this.getRequirements().getRequirement(0);
		
		Requirement fst_req = this.getRequirements().getRequirement(0);
		Requirement snd_req = this.getRequirements().getRequirement(1);

		PFormula precondition = new OrFormula(fst_req.getPrecondition(), snd_req.getPrecondition());

		for(int i=2; i<n_req; i++) {
			precondition = new OrFormula(precondition, this.getRequirements().getRequirement(i).getPrecondition());
		}

		PFormula postcondition = new ImpliesFormula(fst_req.getPrecondition(), fst_req.getPostcondition());

		for(int i=1; i<n_req; i++) {
			Requirement current = this.getRequirements().getRequirement(i);
			postcondition = new AndFormula(postcondition, new ImpliesFormula(current.getPrecondition(), current.getPostcondition()));
		}

		return new Requirement(precondition, postcondition);
	}
	
	public void setRequirements(Requirements req) {
		this.requirements = req;
	}

	public Variables getVariables() {
		return variables;
	}
	
	public void setVariables(Variables var) {
		this.variables = var;
	}

	public TimestampDefinition getTd() {
		return td;
	}
	
	public void setName(String name) {
		if (name != null && !name.equals("<missing IDENTIFIER>"))
			this.name = name;
	}
	
	public String getName() {
		return name;
	}
	
	public void writeToFile(String outputFilePath) throws Exception {
		String content = this.accept(new RQTableToStringVisitor());

        try {
            Files.write(Paths.get(outputFilePath), content.getBytes());
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
	}
}
