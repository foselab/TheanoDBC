package requirements2Z3.rqt;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ComposedRQTable extends RQTable {
	
	private ArrayList<RQTable> contracts; // all contracts parsed by the grammar available for the composition
	private ArrayList<RQTable> chosenContracts; // chosen contracts for the composition

	public ComposedRQTable() {
		super(null, null, null); // init empty RQTable

		this.contracts = new ArrayList<RQTable>();
		this.chosenContracts = new ArrayList<RQTable>();
	}
	
	public ArrayList<RQTable> getContracts(){
		return this.contracts;
	}
	
	public ArrayList<RQTable> getChosenContracts(){
		return this.chosenContracts;
	}
	
	// add a contract to available contracts for the composition
	public void add(RQTable r) {
		this.contracts.add(r);
	}
	
	public void compose(boolean all) throws Exception{
		// Print the names of the RQTables
        System.out.print("Available tables: ");
        this.printContracts();
        		
        // Selection of the contracts
        this.contractsSelection(all);
        
        // Composition of the chosen contracts
        this.composeContracts();
        
        // Print chosen contracts
        System.out.print("Processing composition between tables: ");
        this.printChosenContracts();
	}
	
	// the user can choose which contract will be part of the composition
	private void contractsSelection(boolean all) {
		
		// every contracts will be selected for composition
		if(all) {
			this.chosenContracts = this.contracts;
			return;
		}
		
		// ask the user to specify which table will be part of the composition
        Scanner scanner = new Scanner(System.in);
        boolean done = false;
        
    	while(!done && chosenContracts.size()<contracts.size()) {    
	        System.out.print("Please enter the name of the table to compose: ");
	        
	        String tableName = scanner.nextLine().trim();
	        boolean found = this.chooseContract(tableName);
	        
	        if (found)
	        	System.out.println("Table added successfully");
	        else
	        	System.out.println("Table not found");  
	        
	        if(chosenContracts.size()>=2 && chosenContracts.size()<contracts.size()) {
	        	boolean correctAnswer = false;
	        	while(!correctAnswer) {
	        		System.out.print("Do you want to choose other tables? [Y/N] ");
		        	String answer = scanner.nextLine().trim().toLowerCase();
		        	if (answer.equals("n")) {done=true;correctAnswer=true;}
		        	else if (answer.toLowerCase().equals("y")) correctAnswer=true;
		        	else System.out.println("Please choose between [Y/N] ");
	        	}
	        }
        }
        scanner.close();
	}
		
	// if the name of the contract is available move the contract from contracts to chosenContract
	// return true if available, false otherwise
	private boolean chooseContract(String tableName) {
		boolean found = false;
		for (RQTable rt: this.contracts) {
        	if (rt.getName().equals(tableName) & !this.chosenContracts.contains(rt)) {
        		this.chosenContracts.add(rt);
        		found = true;
        		break;
        	}
        }
		return found;
	}
	
	// compose the chosen contracts
	private void composeContracts() throws Exception {		
		if (this.chosenContracts.size()<2)
			throw new Exception("composition command must be used at least on two tables");

		// composition of the first two tables
		RQTable first = this.chosenContracts.get(0);
		RQTable second = this.chosenContracts.get(1);
		
		this.setVariables(getVariables(first, second));
		this.setRequirements(getRequirements(first, second));
		
		if (chosenContracts.size()==2) return;
		
		// compose every remaining table with the previous one
		for(int i=2; i<chosenContracts.size(); i++) {
			this.setVariables(getVariables(this, chosenContracts.get(i)));
			this.setRequirements(getRequirements(this, chosenContracts.get(i)));
		}
	}
	
	// get all the variables from the two contracts
	// TODO do not allow duplicates
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
		
	// print all contracts available for the composition
	private void printContracts() {		
		System.out.println(getContracts().stream().map(RQTable::getName).collect(Collectors.joining(", ")));
	}
	
	// print all chosen contracts for the composition
	private void printChosenContracts() {
		System.out.println(getChosenContracts().stream().map(RQTable::getName).collect(Collectors.joining(", ")));
	}

}
