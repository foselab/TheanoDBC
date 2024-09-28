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
