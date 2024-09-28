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
		// available terminal options
		Options options = new Options();

		// input file is always a .rt file
		Option input = new Option("i", "inputFile", true, "input file path");
		input.setRequired(true);
		options.addOption(input);

		// output file can be a .rt file (composition) or python file
		Option output = new Option("o", "outputFile", true, "output file path");
		output.setRequired(true);
		options.addOption(output);

		Option type = new Option("t", "type", true, "consistency | completeness | composition | refinement");
		type.setRequired(true);
		options.addOption(type);

		Option bound = new Option("b", "bound", true, "the bound");
		bound.setRequired(false);
		options.addOption(bound);

		Option encoding = new Option("e", "encoding", true,
				"encoding one among BeArFs | BeArVs | BeUfFs | BeUfVs | UeArFs | UeArVs | UeUfFs | UeUfVs");
		encoding.setRequired(false);
		options.addOption(encoding);
		
		// compose every tables in the file if this option is true
		Option all = new Option("a", "all", false, "all tables");
		all.setRequired(false);
		options.addOption(all);

		CommandLineParser parser = new DefaultParser();
		HelpFormatter formatter = new HelpFormatter();
		CommandLine cmd = null;// not a good practice, it serves it purpose

		try {
			cmd = parser.parse(options, args);
		} catch (ParseException e) {
			System.out.println(e.getMessage());
			formatter.printHelp("utility-name", options);

			System.exit(1);
		}

		String inputFilePath = cmd.getOptionValue("i") != null ? cmd.getOptionValue("i") : cmd.getOptionValue("input");
		String outputFilePath = cmd.getOptionValue("o") != null ? cmd.getOptionValue("o")
				: cmd.getOptionValue("output");
		String selectedEncoding = cmd.getOptionValue("e") != null ? cmd.getOptionValue("e")
				: cmd.getOptionValue("encoding");

		String boundVal = cmd.getOptionValue("b") != null ? cmd.getOptionValue("b") : cmd.getOptionValue("bound");

		int boundparam = boundVal != null ? Integer.parseInt(boundVal)+2 : -1;

		String typeInput = cmd.getOptionValue("t") != null ? cmd.getOptionValue("t") : cmd.getOptionValue("type");

		
		Reader sc=new FileReader(inputFilePath);
		matlabLexer lexer = new matlabLexer(new ANTLRInputStream(sc));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		matlabParser rqParser = new matlabParser(tokens);
		rqParser.setBuildParseTree(true);

		// parse .rt file
		// it can be a single table or a list
		RQTable RQTable = rqParser.g().rqt;
		
		// only composition or refinement can be used with more than one table
		if (RQTable instanceof ComposedRQTable) {
		    ComposedRQTable composedTable = (ComposedRQTable) RQTable;
		    
			if (composedTable.getContracts().stream().anyMatch(table -> table.getName() == null || table.getName().isEmpty()))
			    throw new Exception("Every RQTable must have a name");
			
			switch (typeInput) {
				case "composition":
					if(inputFilePath.compareTo(outputFilePath)==0)
						throw new Exception("Composition requires different input and output files");

					composedTable.compose(cmd.hasOption("a"));
					composedTable.writeToFile(outputFilePath);
					break;
					
				case "refinement":
					if (composedTable.getContracts().size()!=2)
						throw new Exception(typeInput + " command must be used on two tables");
					
					Encodings.translate(inputFilePath, outputFilePath, selectedEncoding, 2, new UnboundedConsistencyTranslator(),-1.0).refinementCheck(composedTable.getContracts().get(0), composedTable.getContracts().get(1));
					break;
					
				default:
					throw new IllegalArgumentException("Type: " + typeInput + " is not supported for this file. ");
			}
			
			System.out.println("File: " + outputFilePath + " correctly generated");
			if(typeInput.equals("refinement"))
				System.out.println("Run \"python3 " + outputFilePath + "\" to check for " + typeInput);

			return;
		}
				
		double ts=(RQTable.getTd()!=null) ? RQTable.getTd().getConstant() :-1;
		
		switch (typeInput) {
		case "consistency":
			if (cmd.getOptionValue("b") != null) {
				translate(inputFilePath, outputFilePath, selectedEncoding, boundparam,
						new BoundedConsistencyTranslator(),ts);
			} else {
				translate(inputFilePath, outputFilePath, selectedEncoding, boundparam,
						new UnboundedConsistencyTranslator(),ts);
			}
			break;

		case "completeness":
			if (cmd.getOptionValue("b") != null) {
				translate(inputFilePath, outputFilePath, selectedEncoding, boundparam,
						new BoundedCompletenessTranslator(),ts);
			} else {
				translate(inputFilePath, outputFilePath, selectedEncoding, boundparam,
						new UnboundedCompletenessTranslator(),ts);
			}
			break;

		default:
			throw new IllegalArgumentException("Type: " + typeInput + " is not supported. ");

		}
		System.out.println("File: " + outputFilePath + " correctly generated");
		System.out.println("Run \"python3 " + outputFilePath + "\" to check for " + typeInput);

	}

	private static <T extends Table2Z3Visitor> void translate(String inputFilePath, String outputFilePath,
			String selectedEncoding, int bound, Functionality<T> functionality, double ts) throws Exception {
		
		Encodings.translate(inputFilePath, outputFilePath, selectedEncoding, bound, functionality,ts).translate();
	}
}
