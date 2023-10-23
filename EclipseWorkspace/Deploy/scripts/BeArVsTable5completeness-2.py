from z3 import *;
# Defines the Z3 solver
s = Solver()
# Define I and R
I = IntSort()
R = RealSort()
# Signal variables definition
u1=Array('u1',I,R)
y1=Array('y1',I,R)
u2=Array('u2',I,R)
y2=Array('y2',I,R)
u3=Array('u3',I,R)
y3=Array('y3',I,R)
u4=Array('u4',I,R)
y4=Array('y4',I,R)
u5=Array('u5',I,R)
y5=Array('y5',I,R)

# Quantification variables
j = Int('j')
i = Int('i')
k = Int('k')
# Timestamp structure
tau = Array('tau', I, R)
# Timestamp structure monotonicity
s.add(And(tau[0]<tau[0 + 1]))
# Requirements Table
s.add(Or(And(Not(u1[0]>10)),And(Not(u2[0]==5)),And(Not(u3[0]>0),Not(u5[0]==4),Not(u4[0]<3)),And(Not(u1[1]>10)),And(Not(u2[1]==5)),And(Not(u3[1]>0),Not(u5[1]==4),Not(u4[1]<3)),And(Not(u1[2]>10)),And(Not(u2[2]==5)),And(Not(u3[2]>0),Not(u5[2]==4),Not(u4[2]<3))))
# Processing the result
res=s.check()
if (res.r ==  Z3_L_FALSE):
	 print('Requirements Table Complete (unsat)')
	 sys.exit(1)
else:
	 if (res.r == Z3_L_TRUE):
		 print('Requirements Table Incomplete (sat)')
		 sys.exit(-1)
	 else:
		 print('unknown')
		 sys.exit(0)