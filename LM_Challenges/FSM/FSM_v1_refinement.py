from z3 import *;

# Tables names
RQTableName="FSM_system"
NewRQTableName="FSM_v1"

# Defines the Z3 solver
solver = Solver()
solver.set("timeout", 10000) # 10 sec

# Define I and R
I = IntSort()
R = RealSort()

# Signal variables definition
standby=Bool('standby')
apfail=Bool('apfail')
supported=Bool('supported')
limits=Bool('limits')
pullup=Bool('pullup')
good=Bool('good')
ap_transition=Bool('ap_transition')
ap_nominal=Bool('ap_nominal')
ap_maneuver=Bool('ap_maneuver')
ap_standby=Bool('ap_standby')
mode=Bool('mode')
request=Bool('request')
sen_nominal=Bool('sen_nominal')
sen_transition=Bool('sen_transition')
sen_fault=Bool('sen_fault')
ap_transition_out=Bool('ap_transition_out')
ap_nominal_out=Bool('ap_nominal_out')
ap_maneuver_out=Bool('ap_maneuver_out')
ap_standby_out=Bool('ap_standby_out')
sen_nominal_out=Bool('sen_nominal_out')
sen_transition_out=Bool('sen_transition_out')
sen_fault_out=Bool('sen_fault_out')

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
A1=And(limits,Not(standby),Not(apfail),supported)
A2=Or(And(Or(And(standby,ap_transition),And(ap_transition,good,supported,Not(standby)),And(ap_nominal,Not(good),Not(standby)),And(ap_nominal,standby),And(ap_maneuver,standby,good),And(ap_maneuver,supported,good,Not(standby)),And(ap_standby,Not(standby),Not(apfail)),And(ap_standby,apfail),And(Not(standby),Not(apfail),supported)),Or(limits,And(sen_nominal,Not(request),Not(limits)),And(sen_fault,Not(request),Not(limits)),And(sen_transition,request,mode))),Not(And(Implies(And(standby,ap_transition),ap_standby_out),Implies(And(ap_transition,good,supported,Not(standby)),ap_nominal_out),Implies(And(ap_nominal,Not(good),Not(standby)),ap_maneuver_out),Implies(And(ap_nominal,standby),ap_standby_out),Implies(And(ap_maneuver,standby,good),ap_standby_out),Implies(And(ap_maneuver,supported,good,Not(standby)),ap_transition_out),Implies(And(ap_standby,Not(standby),Not(apfail)),ap_transition_out),Implies(And(ap_standby,apfail),ap_maneuver_out),Implies(And(Not(standby),Not(apfail),supported),pullup),And(Implies(limits,And(sen_fault_out,Not(good))),Implies(And(sen_nominal,Not(request),Not(limits)),sen_transition_out),Implies(And(sen_fault,Not(request),Not(limits)),sen_transition_out),Implies(And(sen_transition,request,mode),sen_nominal_out)))))
G1=pullup
G2=And(Implies(And(standby,ap_transition),ap_standby_out),Implies(And(ap_transition,good,supported,Not(standby)),ap_nominal_out),Implies(And(ap_nominal,Not(good),Not(standby)),ap_maneuver_out),Implies(And(ap_nominal,standby),ap_standby_out),Implies(And(ap_maneuver,standby,good),ap_standby_out),Implies(And(ap_maneuver,supported,good,Not(standby)),ap_transition_out),Implies(And(ap_standby,Not(standby),Not(apfail)),ap_transition_out),Implies(And(ap_standby,apfail),ap_maneuver_out),Implies(And(Not(standby),Not(apfail),supported),pullup),And(Implies(limits,And(sen_fault_out,Not(good))),Implies(And(sen_nominal,Not(request),Not(limits)),sen_transition_out),Implies(And(sen_fault,Not(request),Not(limits)),sen_transition_out),Implies(And(sen_transition,request,mode),sen_nominal_out)))

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
