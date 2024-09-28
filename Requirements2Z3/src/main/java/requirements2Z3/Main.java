package requirements2Z3;

import java.io.FileReader;
import java.io.Reader;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

import generated.matlabLexer;
import generated.matlabParser;
import requirements2Z3.consistency.BoundedCompletenessTranslator;
import requirements2Z3.consistency.BoundedConsistencyTranslator;
import requirements2Z3.consistency.Functionality;
import requirements2Z3.consistency.UnboundedCompletenessTranslator;
import requirements2Z3.consistency.UnboundedConsistencyTranslator;
import requirements2Z3.rqt.ComposedRQTable;
import requirements2Z3.rqt.RQTable;
import requirements2Z3.visitors.translators.Table2Z3Visitor;

public class Main {

	public static void main(String[] args) throws Exception {
		CommandLine cmd = parseArguments(args);
        if (cmd == null) return;
        
        try {
            executeCommand(cmd);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }   
	}
	
	// try to parse arguments insert by the user
	private static CommandLine parseArguments(String[] args) {
		Options options = createOptions();
        
		CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();

        try {
            return parser.parse(options, args);
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("Theano", options);
            return null;
        }
    }
	
	// available terminal options
    private static Options createOptions() {
        Options options = new Options();

		// input file is always a .rt file
        options.addOption(Option.builder("i").longOpt("inputFile").desc("input file path").hasArg().required().build());
        
		// output file can be a .rt file (composition) or a python file
        options.addOption(Option.builder("o").longOpt("outputFile").desc("output file path").hasArg().required().build());
        
        options.addOption(Option.builder("t").longOpt("type").desc("consistency | completeness | composition | refinement").hasArg().required().build());
        options.addOption(Option.builder("e").longOpt("encoding").desc("encoding one among BeArFs | BeArVs | BeUfFs | BeUfVs | UeArFs | UeArVs | UeUfFs | UeUfVs").hasArg().build());
        options.addOption(Option.builder("b").longOpt("bound").desc("the bound").hasArg().build());
        options.addOption(Option.builder("a").longOpt("all").desc("compose all tables").hasArg(false).build());
        
        return options;
    }

    // execute the command insert by the user
    private static void executeCommand(CommandLine cmd) throws Exception {
    	// Parse the options
    	String inputFilePath = cmd.getOptionValue("i");
    	String outputFilePath = cmd.getOptionValue("o");
    	
    	if (inputFilePath.equals(outputFilePath)) {
    	    throw new Exception("Input and output file paths must be different.");
    	}
    	
        String encoding = cmd.getOptionValue("e", "BeUfFs"); // BeUfFs used as default for refinement
        String typeInput = cmd.getOptionValue("t");
        boolean all = cmd.hasOption("a");
        String boundValue = cmd.getOptionValue("b");
        int bound = (boundValue != null) ? Integer.parseInt(boundValue) + 2 : -1;

        // Parse the input file, it can be a single table or a list
        Reader reader = new FileReader(inputFilePath);
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(reader));
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        matlabParser rqParser = new matlabParser(tokens);
        rqParser.setBuildParseTree(true);
        RQTable rqTable = rqParser.g().rqt;
        
        if (rqTable instanceof ComposedRQTable) {
            handleComposedRQTable(cmd, (ComposedRQTable) rqTable, typeInput, inputFilePath, outputFilePath, encoding, all);
        } else {
            handleSingleTable(cmd, rqTable, typeInput, inputFilePath, outputFilePath, encoding, bound);
        }

        System.out.println("File: " + outputFilePath + " correctly generated");
        if (!typeInput.equals("composition")) {
            System.out.println("Run \"python3 " + outputFilePath + "\" to check for " + typeInput);
        }
    }
    
    private static void handleComposedRQTable(CommandLine cmd, ComposedRQTable composedTable, String typeInput, String inputFilePath, String outputFilePath, String encoding, boolean all) throws Exception {
        if (composedTable.getContracts().stream().anyMatch(table -> table.getName() == null || table.getName().isEmpty())) {
            throw new Exception("Every RQTable must have a name");
        }

        switch (typeInput) {
            case "composition":
                composedTable.compose(all);
                composedTable.writeToFile(outputFilePath);
                break;

            case "refinement":
                if (composedTable.getContracts().size() != 2) {
                    throw new Exception("Refinement command must be used on two tables");
                }
                Encodings.translate(inputFilePath, outputFilePath, encoding, 2, new BoundedConsistencyTranslator(), -1.0)
                        .refinementCheck(composedTable.getContracts().get(0), composedTable.getContracts().get(1));
                break;
            default:
                throw new IllegalArgumentException("Type: " + typeInput + " is not supported for this file.");
        }

		return;
    }
    
    private static void handleSingleTable(CommandLine cmd, RQTable rqTable, String typeInput, String inputFilePath, String outputFilePath, String encoding, int bound) throws Exception {
        double ts = (rqTable.getTd() != null) ? rqTable.getTd().getConstant() : -1;

        switch (typeInput) {
            case "consistency":
                if(bound != -1)
                	translate(inputFilePath, outputFilePath, encoding, bound, new BoundedConsistencyTranslator(), ts);
                else
                	translate(inputFilePath, outputFilePath, encoding, bound, new UnboundedConsistencyTranslator(), ts);
                break;
            case "completeness":
                if(bound != -1)
                	translate(inputFilePath, outputFilePath, encoding, bound, new BoundedCompletenessTranslator(), ts);
                else
                	translate(inputFilePath, outputFilePath, encoding, bound, new UnboundedCompletenessTranslator(), ts);
                break;
            default:
                throw new IllegalArgumentException("Type: " + typeInput + " is not supported.");
        }
    }

    private static <T extends Table2Z3Visitor> void translate(String inputFilePath, String outputFilePath,
			String encoding, int bound, Functionality<T> functionality, double ts) throws Exception {
		
		Encodings.translate(inputFilePath, outputFilePath, encoding, bound, functionality,ts).translate();
	}
}
