from z3 import *;
# Defines the Z3 solver
s = Solver()
# Define I and R
I = IntSort()
R = RealSort()
# Signal variables definition
u=Array('u',I,I)
y=Array('y',I,I)

# Quantification variables
j = Int('j')
i = Int('i')
k = Int('k')
# Timestamp structure
tau = Array('tau', I, R)
# Timestamp structure monotonicity
s.add(And(tau[0]<tau[0 + 1],tau[1]<tau[1 + 1],tau[2]<tau[2 + 1],tau[3]<tau[3 + 1],tau[4]<tau[4 + 1],tau[5]<tau[5 + 1],tau[6]<tau[6 + 1],tau[7]<tau[7 + 1],tau[8]<tau[8 + 1]))
# Requirements Table
s.add(ForAll([y] , And(Or(Not(Implies(True,y[0]==0)),Not(Implies(And(Not(True),u[0]>0),y[0]==y[0]+1)),Not(Implies(And(Not(True),y[0]==1023),y[0]==23)),Not(Implies(False,y[1]==0)),Not(Implies(And(Not(False),u[1]>0),y[1]==y[0]+1)),Not(Implies(And(Not(False),y[0]==1023),y[1]==23)),Not(Implies(False,y[2]==0)),Not(Implies(And(Not(False),u[2]>0),y[2]==y[1]+1)),Not(Implies(And(Not(False),y[1]==1023),y[2]==23)),Not(Implies(False,y[3]==0)),Not(Implies(And(Not(False),u[3]>0),y[3]==y[2]+1)),Not(Implies(And(Not(False),y[2]==1023),y[3]==23)),Not(Implies(False,y[4]==0)),Not(Implies(And(Not(False),u[4]>0),y[4]==y[3]+1)),Not(Implies(And(Not(False),y[3]==1023),y[4]==23)),Not(Implies(False,y[5]==0)),Not(Implies(And(Not(False),u[5]>0),y[5]==y[4]+1)),Not(Implies(And(Not(False),y[4]==1023),y[5]==23)),Not(Implies(False,y[6]==0)),Not(Implies(And(Not(False),u[6]>0),y[6]==y[5]+1)),Not(Implies(And(Not(False),y[5]==1023),y[6]==23)),Not(Implies(False,y[7]==0)),Not(Implies(And(Not(False),u[7]>0),y[7]==y[6]+1)),Not(Implies(And(Not(False),y[6]==1023),y[7]==23)),Not(Implies(False,y[8]==0)),Not(Implies(And(Not(False),u[8]>0),y[8]==y[7]+1)),Not(Implies(And(Not(False),y[7]==1023),y[8]==23)),Not(Implies(False,y[9]==0)),Not(Implies(And(Not(False),u[9]>0),y[9]==y[8]+1)),Not(Implies(And(Not(False),y[8]==1023),y[9]==23))))))
# Processing the result
res=s.check()
if (res.r ==  Z3_L_FALSE):
	 print('Requirements Table Consistent (unsat)')
	 sys.exit(1)
else:
	 if (res.r == Z3_L_TRUE):
		 print('Requirements Table Not Consistent (sat)')
		 sys.exit(-1)
	 else:
		 print('unknown')
		 sys.exit(0)