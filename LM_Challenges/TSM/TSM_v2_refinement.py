from z3 import *;

# Tables names
RQTableName="TSM_v1"
NewRQTableName="TSM_v2"

# Defines the Z3 solver
solver = Solver()
solver.set("timeout", 10000) # 10 sec

# Define I and R
I = IntSort()
R = RealSort()

# Signal variables definition
ia=Array('ia',I,R)
ib=Array('ib',I,R)
ic=Array('ic',I,R)
T_Level=Array('T_Level',I,R)
PC_Limit=Array('PC_Limit',I,R)
PC=Array('PC',I,R)
FC=Bool('FC')
FC_1=Bool('FC_1')
FC_2=Bool('FC_2')
FC_4=Bool('FC_4')
set_val=Array('set_val',I,R)
MVS=Array('MVS',I,R)
GCA=Array('GCA',I,R)

# Utility function
def print_counterexample(model):
	print("-" * 40)
	print("Counterexample")
	print("-" * 40)
	for v in model:
		if v.name() != "tau":
			print(str(v) + " = " + str(model[v]))
	print("")

# Function to evaluate conditions using a model
def evaluate_condition(condition, model, name):
	# Dynamically extract variable-value pairs from the model, excluding 'tau'
	variable_values = {d.name(): model[d] for d in model if d.name() != 'tau'}
	# Substitute values dynamically
	substituted_condition = substitute(
		condition,
		*[(eval(var_name), variable_values[var_name]) for var_name in variable_values]
	)

	# Simplified condition
	simplified_condition = simplify(substituted_condition)
	# Evaluate the condition
	condition_result = is_true(simplified_condition)
	print(f"{name} = {condition_result}")

	return variable_values, condition_result

# Function to find contradictions
def contradictions(condition, name, details=False):
	global solver
	solver.push()
	solver.add(condition)
	res = solver.check()
	if details:
		if res == sat: 
			print(f"{name} has no contradictions.")
		elif res == unsat:
			print(f"{name} has contradictions.")
		else:
			print(f"{name}: unknown.")
	solver.pop()
	return res == unsat

# Function to find missing elements in a refinement condition
def fix_refinement_condition(source, target, name):
	solver = Solver()
	updated_target = target  # Start with the original target

	while True:
		solver.push()
		solver.add(source, Not(updated_target))  # Check source => target
		if solver.check() == sat:
			model = solver.model()
			print(f"Refinement failed for {name}, finding missing terms...")

			# Find missing terms in the source that were true in the counterexample
			missing_terms = []
			for term in source.children():
				if model.evaluate(term):
					missing_terms.append(term)

			if not missing_terms:
				print(f"No missing terms found for {name}, something is wrong.")
				break

			# Add missing terms to the target
			updated_target = Or(updated_target, Or(*missing_terms))
			print(f"Missing this assertion or part of it: {missing_terms}.")
		else:
			break
		solver.pop()

	return updated_target

# Contracts
A1=Or(And(ib[0]<=ia[0],ia[0]<=ic[0]),And(ic[0]<=ia[0],ia[0]<=ib[0]),Or(And(ia[0]<=ib[0],ib[0]<=ic[0]),And(ic[0]<=ib[0],ib[0]<=ia[0])),Or(And(ia[0]<=ic[0],ic[0]<=ib[0]),And(ib[0]<=ic[0],ic[0]<=ia[0])),FC_1,FC_2,FC_4,Or(FC_1,FC_2,FC_4),And(Not(FC),Or(ia[0]-ib[0]>T_Level[0],ia[0]-ib[0]>(-T_Level[0]),ia[0]-ic[0]>T_Level[0],ia[0]-ic[0]>(-T_Level[0]),ib[0]-ic[0]>T_Level[0],ib[0]-ic[0]>(-T_Level[0])),PC[0]>PC_Limit[0]),Not(FC),FC)
A2=Or(And(ib[0]<=ia[0],ia[0]<=ic[0]),And(ic[0]<=ia[0],ia[0]<=ib[0]),Or(And(ia[0]<=ib[0],ib[0]<=ic[0]),And(ic[0]<=ib[0],ib[0]<=ia[0])),Or(And(ia[0]<=ic[0],ic[0]<=ib[0]),And(ib[0]<=ic[0],ic[0]<=ia[0])),FC_1,FC_2,FC_4,Or(FC_1,FC_2,FC_4),And(Not(FC),Or(ia[0]-ib[0]>T_Level[0],ia[0]-ib[0]>(-T_Level[0]),ia[0]-ic[0]>T_Level[0],ia[0]-ic[0]>(-T_Level[0]),ib[0]-ic[0]>T_Level[0],ib[0]-ic[0]>(-T_Level[0]))),Not(FC),FC)
G1=And(Implies(Or(And(ib[0]<=ia[0],ia[0]<=ic[0]),And(ic[0]<=ia[0],ia[0]<=ib[0])),MVS[0]==ia[0]),Implies(Or(And(ia[0]<=ib[0],ib[0]<=ic[0]),And(ic[0]<=ib[0],ib[0]<=ia[0])),MVS[0]==ib[0]),Implies(Or(And(ia[0]<=ic[0],ic[0]<=ib[0]),And(ib[0]<=ic[0],ic[0]<=ia[0])),MVS[0]==ic[0]),Implies(FC_1,GCA[0]==ib[0]+ic[0]*0.5),Implies(FC_2,GCA[0]==ia[0]+ic[0]*0.5),Implies(FC_4,GCA[0]==ia[0]+ib[0]*0.5),Implies(Or(FC_1,FC_2,FC_4),FC),Implies(And(Not(FC),Or(ia[0]-ib[0]>T_Level[0],ia[0]-ib[0]>(-T_Level[0]),ia[0]-ic[0]>T_Level[0],ia[0]-ic[0]>(-T_Level[0]),ib[0]-ic[0]>T_Level[0],ib[0]-ic[0]>(-T_Level[0])),PC[0]>PC_Limit[0]),FC),Implies(Not(FC),set_val[0]==MVS[0]),Implies(FC,set_val[0]==GCA[0]))
G2=And(Implies(Or(And(ib[0]<=ia[0],ia[0]<=ic[0]),And(ic[0]<=ia[0],ia[0]<=ib[0])),MVS[0]==ia[0]),Implies(Or(And(ia[0]<=ib[0],ib[0]<=ic[0]),And(ic[0]<=ib[0],ib[0]<=ia[0])),MVS[0]==ib[0]),Implies(Or(And(ia[0]<=ic[0],ic[0]<=ib[0]),And(ib[0]<=ic[0],ic[0]<=ia[0])),MVS[0]==ic[0]),Implies(FC_1,GCA[0]==ib[0]+ic[0]*0.5),Implies(FC_2,GCA[0]==ia[0]+ic[0]*0.5),Implies(FC_4,GCA[0]==ia[0]+ib[0]*0.5),Implies(Or(FC_1,FC_2,FC_4),FC),Implies(And(Not(FC),Or(ia[0]-ib[0]>T_Level[0],ia[0]-ib[0]>(-T_Level[0]),ia[0]-ic[0]>T_Level[0],ia[0]-ic[0]>(-T_Level[0]),ib[0]-ic[0]>T_Level[0],ib[0]-ic[0]>(-T_Level[0]))),FC),Implies(Not(FC),set_val[0]==MVS[0]),Implies(FC,set_val[0]==GCA[0]))

# Check contradictions on requirements 
print("Checking contradictions in the requirements...")
A1_sat=contradictions(A1, "A1", False)
A2_sat=contradictions(A2, "A2", False)
G1_sat=contradictions(G1, "G1", False)
G2_sat=contradictions(G2, "G2", False)

if(A1_sat or A2_sat or G1_sat or G2_sat):
	print("Contradictions found. Fix the requirements before testing the refinement.")
	exit()
print("Couldn't find contradictions.")

# Refinement conditions 
refinement_A=Implies(A1,A2)
refinement_G=Implies(G2,G1)

# Constraint 
solver.add(A1==True)

# Check refinement condition on assumptions
solver.push()
solver.add(Not(refinement_A))
res = solver.check()
if res == sat:
	print(f"Assumptions violated.")
	model = solver.model()
	evaluate_condition(A1, model, "A1")
	evaluate_condition(A2, model, "A2")
	print_counterexample(model)
	print(f"{NewRQTableName} does NOT refine {RQTableName} (update NOT recommended).")
	exit()
elif res == unsat: 
	print(f"Assumptions holds.") # the condition is always true
else:
	print(f"Assumptions: unknown.")
solver.pop()

# Check refinement condition on guarantees
solver.push()
solver.add(Not(refinement_G))
res = solver.check()
if res == sat:
	print(f"Guarantees violated.")
	model = solver.model()
	evaluate_condition(G1, model, "G1")
	evaluate_condition(G2, model, "G2")
	print_counterexample(model)
	print(f"{NewRQTableName} does NOT refine {RQTableName} (update NOT recommended).")
	exit()
elif res == unsat: 
	print(f"Guarantees holds.") # the condition is always true
else:
	print(f"Guarantees: unknown.")
solver.pop()

print(f"{NewRQTableName} refines {RQTableName} (compatible update).")
