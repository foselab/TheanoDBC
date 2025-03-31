from z3 import *;

# Tables names
RQTableName="AP_v1"
NewRQTableName="AP_v2"

# Defines the Z3 solver
solver = Solver()
solver.set("timeout", 10000) # 10 sec

# Define I and R
I = IntSort()
R = RealSort()

# Signal variables definition
roll_angle=Array('roll_angle',I,R)
TurnKnob=Array('TurnKnob',I,R)
HDGmode=Bool('HDGmode')
autopilot_engaged=Bool('autopilot_engaged')
hdg_hold_mode_cmd=Array('hdg_hold_mode_cmd',I,R)
roll_actuator_command=Array('roll_actuator_command',I,R)
roll_cmd=Array('roll_cmd',I,R)
roll_hold_reference=Array('roll_hold_reference',I,R)
no_other_lateral_mode=Bool('no_other_lateral_mode')
abs_roll_angle=Array('abs_roll_angle',I,R)
sign_roll_angle=Array('sign_roll_angle',I,R)
abs_roll_actuator_command=Array('abs_roll_actuator_command',I,R)
Cb=Bool('Cb')
Cc=Bool('Cc')
Cd=Bool('Cd')

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
A1=True
A2=True
G1=And(Implies(Not(autopilot_engaged),roll_actuator_command[0]==0.0),Implies(And(no_other_lateral_mode,autopilot_engaged),roll_cmd[0]==roll_hold_reference[0]),Implies(And(Or(TurnKnob[0]>=3.0,TurnKnob[0]<=(-3.0)),Or(TurnKnob[0]<=30.0,TurnKnob[0]>=(-30.0))),roll_hold_reference[0]==TurnKnob[0]),Implies(abs_roll_angle[0]>=30.0,roll_hold_reference[0]==30.0*sign_roll_angle[0]),Implies(And(roll_angle[0]<6.0,roll_angle[0]>(-6.0)),roll_hold_reference[0]==0.0),Implies(Not(Or(Cb,Cc,Cd)),roll_hold_reference[0]==roll_angle[0]),Implies(HDGmode,roll_cmd[0]==hdg_hold_mode_cmd[0]),abs_roll_actuator_command[0]<=15.0)
G2=And(Implies(Not(autopilot_engaged),roll_actuator_command[0]==0.0),Implies(And(no_other_lateral_mode,autopilot_engaged),roll_cmd[0]==roll_hold_reference[0]),Implies(Or(TurnKnob[0]<=30.0,TurnKnob[0]>=(-30.0)),roll_hold_reference[0]==TurnKnob[0]),Implies(abs_roll_angle[0]>=30.0,roll_hold_reference[0]==30.0*sign_roll_angle[0]),Implies(And(roll_angle[0]<6.0,roll_angle[0]>(-6.0)),roll_hold_reference[0]==0.0),Implies(Not(Or(Cb,Cc,Cd)),roll_hold_reference[0]==roll_angle[0]),Implies(HDGmode,roll_cmd[0]==hdg_hold_mode_cmd[0]),abs_roll_actuator_command[0]<=15.0)

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
