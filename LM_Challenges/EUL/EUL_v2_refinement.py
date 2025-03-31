from z3 import *;

# Tables names
RQTableName="EUL_v1"
NewRQTableName="EUL_v2"

# Defines the Z3 solver
solver = Solver()
solver.set("timeout", 10000) # 10 sec

# Define I and R
I = IntSort()
R = RealSort()

# Signal variables definition
theta=Array('theta',I,R)
Vi_1=Array('Vi_1',I,R)
Vi_2=Array('Vi_2',I,R)
Vi_3=Array('Vi_3',I,R)
DCM321_1_1=Array('DCM321_1_1',I,R)
DCM321_2_1=Array('DCM321_2_1',I,R)
DCM321_3_1=Array('DCM321_3_1',I,R)
DCM321_1_2=Array('DCM321_1_2',I,R)
DCM321_2_2=Array('DCM321_2_2',I,R)
DCM321_3_2=Array('DCM321_3_2',I,R)
DCM321_1_3=Array('DCM321_1_3',I,R)
DCM321_2_3=Array('DCM321_2_3',I,R)
DCM321_3_3=Array('DCM321_3_3',I,R)
DCM_det=Array('DCM_det',I,R)
Vb_1=Array('Vb_1',I,R)
Vb_2=Array('Vb_2',I,R)
Vb_3=Array('Vb_3',I,R)
r1xr1Transpose=Bool('r1xr1Transpose')
r2xr2Transpose=Bool('r2xr2Transpose')
r3xr3Transpose=Bool('r3xr3Transpose')
r1xr2Transpose=Bool('r1xr2Transpose')
r1xr3Transpose=Bool('r1xr3Transpose')
r2xr3Transpose=Bool('r2xr3Transpose')
c1xc1Transpose=Bool('c1xc1Transpose')
c2xc2Transpose=Bool('c2xc2Transpose')
c3xc3Transpose=Bool('c3xc3Transpose')
c1xc2Transpose=Bool('c1xc2Transpose')
c1xc3Transpose=Bool('c1xc3Transpose')
c2xc3Transpose=Bool('c2xc3Transpose')
r2xr1Transpose=Bool('r2xr1Transpose')
r3xr1Transpose=Bool('r3xr1Transpose')
r3xr2Transpose=Bool('r3xr2Transpose')

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
G1=And(Vb_1[0]==DCM321_1_1[0]*Vi_1[0]+DCM321_1_2[0]*Vi_2[0]+DCM321_1_3[0]*Vi_3[0],Vb_2[0]==DCM321_2_1[0]*Vi_1[0]+DCM321_2_2[0]*Vi_2[0]+DCM321_2_3[0]*Vi_3[0],Vb_3[0]==DCM321_3_1[0]*Vi_1[0]+DCM321_3_2[0]*Vi_2[0]+DCM321_3_3[0]*Vi_3[0],Vb_1[0]*Vb_1[0]+Vb_2[0]*Vb_2[0]+Vb_3[0]*Vb_3[0]==Vi_1[0]*Vi_1[0]+Vi_2[0]*Vi_2[0]+Vi_3[0]*Vi_3[0],Implies(theta[0]>=0.0,And(theta[0]!=3.1415926536/2.0,DCM_det[0]!=0.0)),Implies(theta[0]<0.0,And((-theta[0])!=3.1415926536/2.0,DCM_det[0]!=0.0)),DCM_det[0]==DCM321_1_1[0]*DCM321_2_2[0]*DCM321_3_3[0]-DCM321_2_3[0]*DCM321_3_2[0]+DCM321_1_2[0]*DCM321_2_3[0]*DCM321_3_1[0]-DCM321_2_1[0]*DCM321_3_3[0]+DCM321_1_3[0]*DCM321_2_1[0]*DCM321_3_2[0]-DCM321_3_1[0]*DCM321_2_2[0],And(r1xr1Transpose,r1xr2Transpose,r3xr3Transpose),And(r1xr2Transpose,r1xr3Transpose,r2xr3Transpose),And(c1xc1Transpose,c2xc2Transpose,c3xc3Transpose),And(c1xc2Transpose,c1xc3Transpose,c2xc3Transpose),And(r1xr1Transpose,r1xr2Transpose,r1xr3Transpose,r2xr1Transpose,r2xr2Transpose,r2xr3Transpose,r3xr1Transpose,r3xr2Transpose,r3xr3Transpose),DCM_det[0]==1.0,Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_1_2[0]*DCM321_1_2[0]+DCM321_1_3[0]*DCM321_1_3[0]==1.0,r1xr1Transpose),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_1_2[0]*DCM321_1_2[0]+DCM321_1_3[0]*DCM321_1_3[0]!=1.0,Not(r1xr1Transpose)),Implies(DCM321_2_1[0]*DCM321_2_1[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_2_3[0]*DCM321_2_3[0]==1.0,r2xr2Transpose),Implies(DCM321_2_1[0]*DCM321_2_1[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_2_3[0]*DCM321_2_3[0]!=1.0,Not(r2xr2Transpose)),Implies(DCM321_3_1[0]*DCM321_3_1[0]+DCM321_3_2[0]*DCM321_3_2[0]+DCM321_3_3[0]*DCM321_3_3[0]==1.0,r3xr3Transpose),Implies(DCM321_3_1[0]*DCM321_3_1[0]+DCM321_3_2[0]*DCM321_3_2[0]+DCM321_3_3[0]*DCM321_3_3[0]!=1.0,Not(r3xr3Transpose)),Implies(DCM321_1_1[0]*DCM321_2_1[0]+DCM321_1_2[0]*DCM321_2_2[0]+DCM321_1_3[0]*DCM321_2_3[0]==0.0,r1xr2Transpose),Implies(DCM321_1_1[0]*DCM321_2_1[0]+DCM321_1_2[0]*DCM321_2_2[0]+DCM321_1_3[0]*DCM321_2_3[0]!=0.0,Not(r1xr2Transpose)),Implies(DCM321_1_1[0]*DCM321_3_1[0]+DCM321_1_2[0]*DCM321_3_2[0]+DCM321_1_3[0]*DCM321_3_3[0]==0.0,r1xr3Transpose),Implies(DCM321_1_1[0]*DCM321_3_1[0]+DCM321_1_2[0]*DCM321_3_2[0]+DCM321_1_3[0]*DCM321_3_3[0]!=0.0,Not(r1xr3Transpose)),Implies(DCM321_2_1[0]*DCM321_3_1[0]+DCM321_2_2[0]*DCM321_3_2[0]+DCM321_2_3[0]*DCM321_3_3[0]==0.0,r2xr3Transpose),Implies(DCM321_2_1[0]*DCM321_3_1[0]+DCM321_2_2[0]*DCM321_3_2[0]+DCM321_2_3[0]*DCM321_3_3[0]!=0.0,Not(r2xr3Transpose)),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_2_1[0]*DCM321_2_1[0]+DCM321_3_1[0]*DCM321_3_1[0]==1.0,c1xc1Transpose),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_2_1[0]*DCM321_2_1[0]+DCM321_3_1[0]*DCM321_3_1[0]!=1.0,Not(c1xc1Transpose)),Implies(DCM321_1_2[0]*DCM321_1_2[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_3_2[0]*DCM321_3_2[0]==1.0,c2xc2Transpose),Implies(DCM321_1_2[0]*DCM321_1_2[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_3_2[0]*DCM321_3_2[0]!=1.0,Not(c2xc2Transpose)),Implies(DCM321_1_3[0]*DCM321_1_3[0]+DCM321_2_3[0]*DCM321_2_3[0]+DCM321_3_3[0]*DCM321_3_3[0]==1.0,c3xc3Transpose),Implies(DCM321_1_3[0]*DCM321_1_3[0]+DCM321_2_3[0]*DCM321_2_3[0]+DCM321_3_3[0]*DCM321_3_3[0]!=1.0,Not(c3xc3Transpose)),Implies(DCM321_1_1[0]*DCM321_1_2[0]+DCM321_2_1[0]*DCM321_2_2[0]+DCM321_3_1[0]*DCM321_3_2[0]==0.0,c1xc2Transpose),Implies(DCM321_1_1[0]*DCM321_1_2[0]+DCM321_2_1[0]*DCM321_2_2[0]+DCM321_3_1[0]*DCM321_3_2[0]!=0.0,Not(c1xc2Transpose)),Implies(DCM321_1_1[0]*DCM321_1_3[0]+DCM321_2_1[0]*DCM321_2_3[0]+DCM321_3_1[0]*DCM321_3_3[0]==0.0,c1xc3Transpose),Implies(DCM321_1_1[0]*DCM321_1_3[0]+DCM321_2_1[0]*DCM321_2_3[0]+DCM321_3_1[0]*DCM321_3_3[0]!=0.0,Not(c1xc3Transpose)),Implies(DCM321_1_2[0]*DCM321_1_3[0]+DCM321_2_2[0]*DCM321_2_3[0]+DCM321_3_2[0]*DCM321_3_3[0]==0.0,c2xc3Transpose),Implies(DCM321_1_2[0]*DCM321_1_3[0]+DCM321_2_2[0]*DCM321_2_3[0]+DCM321_3_2[0]*DCM321_3_3[0]!=0.0,Not(c2xc3Transpose)),Implies(DCM321_2_1[0]*DCM321_1_1[0]+DCM321_2_2[0]*DCM321_1_2[0]+DCM321_2_3[0]*DCM321_1_3[0]==0.0,r2xr1Transpose),Implies(DCM321_2_1[0]*DCM321_1_1[0]+DCM321_2_2[0]*DCM321_1_2[0]+DCM321_2_3[0]*DCM321_1_3[0]!=0.0,Not(r2xr1Transpose)),Implies(DCM321_3_1[0]*DCM321_1_1[0]+DCM321_3_2[0]*DCM321_1_2[0]+DCM321_3_3[0]*DCM321_1_3[0]==0.0,r3xr1Transpose),Implies(DCM321_3_1[0]*DCM321_1_1[0]+DCM321_3_2[0]*DCM321_1_2[0]+DCM321_3_3[0]*DCM321_1_3[0]!=0.0,Not(r3xr1Transpose)),Implies(DCM321_3_1[0]*DCM321_2_1[0]+DCM321_3_2[0]*DCM321_2_2[0]+DCM321_3_3[0]*DCM321_2_3[0]==0.0,r3xr2Transpose),Implies(DCM321_3_1[0]*DCM321_2_1[0]+DCM321_3_2[0]*DCM321_2_2[0]+DCM321_3_3[0]*DCM321_2_3[0]!=0.0,Not(r3xr2Transpose)))
G2=And(Vb_1[0]==DCM321_1_1[0]*Vi_1[0]+DCM321_1_2[0]*Vi_2[0]+DCM321_1_3[0]*Vi_3[0],Vb_2[0]==DCM321_2_1[0]*Vi_1[0]+DCM321_2_2[0]*Vi_2[0]+DCM321_2_3[0]*Vi_3[0],Vb_3[0]==DCM321_3_1[0]*Vi_1[0]+DCM321_3_2[0]*Vi_2[0]+DCM321_3_3[0]*Vi_3[0],Vb_1[0]*Vb_1[0]+Vb_2[0]*Vb_2[0]+Vb_3[0]*Vb_3[0]==Vi_1[0]*Vi_1[0]+Vi_2[0]*Vi_2[0]+Vi_3[0]*Vi_3[0],Implies(theta[0]>=0.0,And(theta[0]!=3.1415926536/3.0,DCM_det[0]!=0.0)),Implies(theta[0]<0.0,And((-theta[0])!=3.1415926536/3.0,DCM_det[0]!=0.0)),DCM_det[0]==DCM321_1_1[0]*DCM321_2_2[0]*DCM321_3_3[0]-DCM321_2_3[0]*DCM321_3_2[0]+DCM321_1_2[0]*DCM321_2_3[0]*DCM321_3_1[0]-DCM321_2_1[0]*DCM321_3_3[0]+DCM321_1_3[0]*DCM321_2_1[0]*DCM321_3_2[0]-DCM321_3_1[0]*DCM321_2_2[0],And(r1xr1Transpose,r1xr2Transpose,r3xr3Transpose),And(r1xr2Transpose,r1xr3Transpose,r2xr3Transpose),And(c1xc1Transpose,c2xc2Transpose,c3xc3Transpose),And(c1xc2Transpose,c1xc3Transpose,c2xc3Transpose),And(r1xr1Transpose,r1xr2Transpose,r1xr3Transpose,r2xr1Transpose,r2xr2Transpose,r2xr3Transpose,r3xr1Transpose,r3xr2Transpose,r3xr3Transpose),DCM_det[0]==1.0,Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_1_2[0]*DCM321_1_2[0]+DCM321_1_3[0]*DCM321_1_3[0]==1.0,r1xr1Transpose),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_1_2[0]*DCM321_1_2[0]+DCM321_1_3[0]*DCM321_1_3[0]!=1.0,Not(r1xr1Transpose)),Implies(DCM321_2_1[0]*DCM321_2_1[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_2_3[0]*DCM321_2_3[0]==1.0,r2xr2Transpose),Implies(DCM321_2_1[0]*DCM321_2_1[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_2_3[0]*DCM321_2_3[0]!=1.0,Not(r2xr2Transpose)),Implies(DCM321_3_1[0]*DCM321_3_1[0]+DCM321_3_2[0]*DCM321_3_2[0]+DCM321_3_3[0]*DCM321_3_3[0]==1.0,r3xr3Transpose),Implies(DCM321_3_1[0]*DCM321_3_1[0]+DCM321_3_2[0]*DCM321_3_2[0]+DCM321_3_3[0]*DCM321_3_3[0]!=1.0,Not(r3xr3Transpose)),Implies(DCM321_1_1[0]*DCM321_2_1[0]+DCM321_1_2[0]*DCM321_2_2[0]+DCM321_1_3[0]*DCM321_2_3[0]==0.0,r1xr2Transpose),Implies(DCM321_1_1[0]*DCM321_2_1[0]+DCM321_1_2[0]*DCM321_2_2[0]+DCM321_1_3[0]*DCM321_2_3[0]!=0.0,Not(r1xr2Transpose)),Implies(DCM321_1_1[0]*DCM321_3_1[0]+DCM321_1_2[0]*DCM321_3_2[0]+DCM321_1_3[0]*DCM321_3_3[0]==0.0,r1xr3Transpose),Implies(DCM321_1_1[0]*DCM321_3_1[0]+DCM321_1_2[0]*DCM321_3_2[0]+DCM321_1_3[0]*DCM321_3_3[0]!=0.0,Not(r1xr3Transpose)),Implies(DCM321_2_1[0]*DCM321_3_1[0]+DCM321_2_2[0]*DCM321_3_2[0]+DCM321_2_3[0]*DCM321_3_3[0]==0.0,r2xr3Transpose),Implies(DCM321_2_1[0]*DCM321_3_1[0]+DCM321_2_2[0]*DCM321_3_2[0]+DCM321_2_3[0]*DCM321_3_3[0]!=0.0,Not(r2xr3Transpose)),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_2_1[0]*DCM321_2_1[0]+DCM321_3_1[0]*DCM321_3_1[0]==1.0,c1xc1Transpose),Implies(DCM321_1_1[0]*DCM321_1_1[0]+DCM321_2_1[0]*DCM321_2_1[0]+DCM321_3_1[0]*DCM321_3_1[0]!=1.0,Not(c1xc1Transpose)),Implies(DCM321_1_2[0]*DCM321_1_2[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_3_2[0]*DCM321_3_2[0]==1.0,c2xc2Transpose),Implies(DCM321_1_2[0]*DCM321_1_2[0]+DCM321_2_2[0]*DCM321_2_2[0]+DCM321_3_2[0]*DCM321_3_2[0]!=1.0,Not(c2xc2Transpose)),Implies(DCM321_1_3[0]*DCM321_1_3[0]+DCM321_2_3[0]*DCM321_2_3[0]+DCM321_3_3[0]*DCM321_3_3[0]==1.0,c3xc3Transpose),Implies(DCM321_1_3[0]*DCM321_1_3[0]+DCM321_2_3[0]*DCM321_2_3[0]+DCM321_3_3[0]*DCM321_3_3[0]!=1.0,Not(c3xc3Transpose)),Implies(DCM321_1_1[0]*DCM321_1_2[0]+DCM321_2_1[0]*DCM321_2_2[0]+DCM321_3_1[0]*DCM321_3_2[0]==0.0,c1xc2Transpose),Implies(DCM321_1_1[0]*DCM321_1_2[0]+DCM321_2_1[0]*DCM321_2_2[0]+DCM321_3_1[0]*DCM321_3_2[0]!=0.0,Not(c1xc2Transpose)),Implies(DCM321_1_1[0]*DCM321_1_3[0]+DCM321_2_1[0]*DCM321_2_3[0]+DCM321_3_1[0]*DCM321_3_3[0]==0.0,c1xc3Transpose),Implies(DCM321_1_1[0]*DCM321_1_3[0]+DCM321_2_1[0]*DCM321_2_3[0]+DCM321_3_1[0]*DCM321_3_3[0]!=0.0,Not(c1xc3Transpose)),Implies(DCM321_1_2[0]*DCM321_1_3[0]+DCM321_2_2[0]*DCM321_2_3[0]+DCM321_3_2[0]*DCM321_3_3[0]==0.0,c2xc3Transpose),Implies(DCM321_1_2[0]*DCM321_1_3[0]+DCM321_2_2[0]*DCM321_2_3[0]+DCM321_3_2[0]*DCM321_3_3[0]!=0.0,Not(c2xc3Transpose)),Implies(DCM321_2_1[0]*DCM321_1_1[0]+DCM321_2_2[0]*DCM321_1_2[0]+DCM321_2_3[0]*DCM321_1_3[0]==0.0,r2xr1Transpose),Implies(DCM321_2_1[0]*DCM321_1_1[0]+DCM321_2_2[0]*DCM321_1_2[0]+DCM321_2_3[0]*DCM321_1_3[0]!=0.0,Not(r2xr1Transpose)),Implies(DCM321_3_1[0]*DCM321_1_1[0]+DCM321_3_2[0]*DCM321_1_2[0]+DCM321_3_3[0]*DCM321_1_3[0]==0.0,r3xr1Transpose),Implies(DCM321_3_1[0]*DCM321_1_1[0]+DCM321_3_2[0]*DCM321_1_2[0]+DCM321_3_3[0]*DCM321_1_3[0]!=0.0,Not(r3xr1Transpose)),Implies(DCM321_3_1[0]*DCM321_2_1[0]+DCM321_3_2[0]*DCM321_2_2[0]+DCM321_3_3[0]*DCM321_2_3[0]==0.0,r3xr2Transpose),Implies(DCM321_3_1[0]*DCM321_2_1[0]+DCM321_3_2[0]*DCM321_2_2[0]+DCM321_3_3[0]*DCM321_2_3[0]!=0.0,Not(r3xr2Transpose)))

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
