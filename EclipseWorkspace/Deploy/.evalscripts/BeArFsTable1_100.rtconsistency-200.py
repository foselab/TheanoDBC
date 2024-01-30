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
s.add(And(tau[1]-tau[0]==2.0,tau[2]-tau[1]==2.0,tau[3]-tau[2]==2.0,tau[4]-tau[3]==2.0,tau[5]-tau[4]==2.0,tau[6]-tau[5]==2.0,tau[7]-tau[6]==2.0,tau[8]-tau[7]==2.0,tau[9]-tau[8]==2.0,tau[10]-tau[9]==2.0,tau[11]-tau[10]==2.0,tau[12]-tau[11]==2.0,tau[13]-tau[12]==2.0,tau[14]-tau[13]==2.0,tau[15]-tau[14]==2.0,tau[16]-tau[15]==2.0,tau[17]-tau[16]==2.0,tau[18]-tau[17]==2.0,tau[19]-tau[18]==2.0,tau[20]-tau[19]==2.0,tau[21]-tau[20]==2.0,tau[22]-tau[21]==2.0,tau[23]-tau[22]==2.0,tau[24]-tau[23]==2.0,tau[25]-tau[24]==2.0,tau[26]-tau[25]==2.0,tau[27]-tau[26]==2.0,tau[28]-tau[27]==2.0,tau[29]-tau[28]==2.0,tau[30]-tau[29]==2.0,tau[31]-tau[30]==2.0,tau[32]-tau[31]==2.0,tau[33]-tau[32]==2.0,tau[34]-tau[33]==2.0,tau[35]-tau[34]==2.0,tau[36]-tau[35]==2.0,tau[37]-tau[36]==2.0,tau[38]-tau[37]==2.0,tau[39]-tau[38]==2.0,tau[40]-tau[39]==2.0,tau[41]-tau[40]==2.0,tau[42]-tau[41]==2.0,tau[43]-tau[42]==2.0,tau[44]-tau[43]==2.0,tau[45]-tau[44]==2.0,tau[46]-tau[45]==2.0,tau[47]-tau[46]==2.0,tau[48]-tau[47]==2.0,tau[49]-tau[48]==2.0,tau[50]-tau[49]==2.0,tau[51]-tau[50]==2.0,tau[52]-tau[51]==2.0,tau[53]-tau[52]==2.0,tau[54]-tau[53]==2.0,tau[55]-tau[54]==2.0,tau[56]-tau[55]==2.0,tau[57]-tau[56]==2.0,tau[58]-tau[57]==2.0,tau[59]-tau[58]==2.0,tau[60]-tau[59]==2.0,tau[61]-tau[60]==2.0,tau[62]-tau[61]==2.0,tau[63]-tau[62]==2.0,tau[64]-tau[63]==2.0,tau[65]-tau[64]==2.0,tau[66]-tau[65]==2.0,tau[67]-tau[66]==2.0,tau[68]-tau[67]==2.0,tau[69]-tau[68]==2.0,tau[70]-tau[69]==2.0,tau[71]-tau[70]==2.0,tau[72]-tau[71]==2.0,tau[73]-tau[72]==2.0,tau[74]-tau[73]==2.0,tau[75]-tau[74]==2.0,tau[76]-tau[75]==2.0,tau[77]-tau[76]==2.0,tau[78]-tau[77]==2.0,tau[79]-tau[78]==2.0,tau[80]-tau[79]==2.0,tau[81]-tau[80]==2.0,tau[82]-tau[81]==2.0,tau[83]-tau[82]==2.0,tau[84]-tau[83]==2.0,tau[85]-tau[84]==2.0,tau[86]-tau[85]==2.0,tau[87]-tau[86]==2.0,tau[88]-tau[87]==2.0,tau[89]-tau[88]==2.0,tau[90]-tau[89]==2.0,tau[91]-tau[90]==2.0,tau[92]-tau[91]==2.0,tau[93]-tau[92]==2.0,tau[94]-tau[93]==2.0,tau[95]-tau[94]==2.0,tau[96]-tau[95]==2.0,tau[97]-tau[96]==2.0,tau[98]-tau[97]==2.0,tau[99]-tau[98]==2.0,tau[100]-tau[99]==2.0,tau[101]-tau[100]==2.0,tau[102]-tau[101]==2.0,tau[103]-tau[102]==2.0,tau[104]-tau[103]==2.0,tau[105]-tau[104]==2.0,tau[106]-tau[105]==2.0,tau[107]-tau[106]==2.0,tau[108]-tau[107]==2.0,tau[109]-tau[108]==2.0,tau[110]-tau[109]==2.0,tau[111]-tau[110]==2.0,tau[112]-tau[111]==2.0,tau[113]-tau[112]==2.0,tau[114]-tau[113]==2.0,tau[115]-tau[114]==2.0,tau[116]-tau[115]==2.0,tau[117]-tau[116]==2.0,tau[118]-tau[117]==2.0,tau[119]-tau[118]==2.0,tau[120]-tau[119]==2.0,tau[121]-tau[120]==2.0,tau[122]-tau[121]==2.0,tau[123]-tau[122]==2.0,tau[124]-tau[123]==2.0,tau[125]-tau[124]==2.0,tau[126]-tau[125]==2.0,tau[127]-tau[126]==2.0,tau[128]-tau[127]==2.0,tau[129]-tau[128]==2.0,tau[130]-tau[129]==2.0,tau[131]-tau[130]==2.0,tau[132]-tau[131]==2.0,tau[133]-tau[132]==2.0,tau[134]-tau[133]==2.0,tau[135]-tau[134]==2.0,tau[136]-tau[135]==2.0,tau[137]-tau[136]==2.0,tau[138]-tau[137]==2.0,tau[139]-tau[138]==2.0,tau[140]-tau[139]==2.0,tau[141]-tau[140]==2.0,tau[142]-tau[141]==2.0,tau[143]-tau[142]==2.0,tau[144]-tau[143]==2.0,tau[145]-tau[144]==2.0,tau[146]-tau[145]==2.0,tau[147]-tau[146]==2.0,tau[148]-tau[147]==2.0,tau[149]-tau[148]==2.0,tau[150]-tau[149]==2.0,tau[151]-tau[150]==2.0,tau[152]-tau[151]==2.0,tau[153]-tau[152]==2.0,tau[154]-tau[153]==2.0,tau[155]-tau[154]==2.0,tau[156]-tau[155]==2.0,tau[157]-tau[156]==2.0,tau[158]-tau[157]==2.0,tau[159]-tau[158]==2.0,tau[160]-tau[159]==2.0,tau[161]-tau[160]==2.0,tau[162]-tau[161]==2.0,tau[163]-tau[162]==2.0,tau[164]-tau[163]==2.0,tau[165]-tau[164]==2.0,tau[166]-tau[165]==2.0,tau[167]-tau[166]==2.0,tau[168]-tau[167]==2.0,tau[169]-tau[168]==2.0,tau[170]-tau[169]==2.0,tau[171]-tau[170]==2.0,tau[172]-tau[171]==2.0,tau[173]-tau[172]==2.0,tau[174]-tau[173]==2.0,tau[175]-tau[174]==2.0,tau[176]-tau[175]==2.0,tau[177]-tau[176]==2.0,tau[178]-tau[177]==2.0,tau[179]-tau[178]==2.0,tau[180]-tau[179]==2.0,tau[181]-tau[180]==2.0,tau[182]-tau[181]==2.0,tau[183]-tau[182]==2.0,tau[184]-tau[183]==2.0,tau[185]-tau[184]==2.0,tau[186]-tau[185]==2.0,tau[187]-tau[186]==2.0,tau[188]-tau[187]==2.0,tau[189]-tau[188]==2.0,tau[190]-tau[189]==2.0,tau[191]-tau[190]==2.0,tau[192]-tau[191]==2.0,tau[193]-tau[192]==2.0,tau[194]-tau[193]==2.0,tau[195]-tau[194]==2.0,tau[196]-tau[195]==2.0,tau[197]-tau[196]==2.0,tau[198]-tau[197]==2.0,tau[199]-tau[198]==2.0))
# Requirements Table
s.add(ForAll([y] , Or(Or(Not(Implies(True,y[0]==0)),Not(Implies(And(Not(True),u[0]>0),y[0]==y[0]+1)),Not(Implies(And(Not(True),y[0]==100),y[0]<23)),Not(Implies(False,y[1]==0)),Not(Implies(And(Not(False),u[1]>0),y[1]==y[0]+1)),Not(Implies(And(Not(False),y[0]==100),y[1]<23)),Not(Implies(False,y[2]==0)),Not(Implies(And(Not(False),u[2]>0),y[2]==y[1]+1)),Not(Implies(And(Not(False),y[1]==100),y[2]<23)),Not(Implies(False,y[3]==0)),Not(Implies(And(Not(False),u[3]>0),y[3]==y[2]+1)),Not(Implies(And(Not(False),y[2]==100),y[3]<23)),Not(Implies(False,y[4]==0)),Not(Implies(And(Not(False),u[4]>0),y[4]==y[3]+1)),Not(Implies(And(Not(False),y[3]==100),y[4]<23)),Not(Implies(False,y[5]==0)),Not(Implies(And(Not(False),u[5]>0),y[5]==y[4]+1)),Not(Implies(And(Not(False),y[4]==100),y[5]<23)),Not(Implies(False,y[6]==0)),Not(Implies(And(Not(False),u[6]>0),y[6]==y[5]+1)),Not(Implies(And(Not(False),y[5]==100),y[6]<23)),Not(Implies(False,y[7]==0)),Not(Implies(And(Not(False),u[7]>0),y[7]==y[6]+1)),Not(Implies(And(Not(False),y[6]==100),y[7]<23)),Not(Implies(False,y[8]==0)),Not(Implies(And(Not(False),u[8]>0),y[8]==y[7]+1)),Not(Implies(And(Not(False),y[7]==100),y[8]<23)),Not(Implies(False,y[9]==0)),Not(Implies(And(Not(False),u[9]>0),y[9]==y[8]+1)),Not(Implies(And(Not(False),y[8]==100),y[9]<23)),Not(Implies(False,y[10]==0)),Not(Implies(And(Not(False),u[10]>0),y[10]==y[9]+1)),Not(Implies(And(Not(False),y[9]==100),y[10]<23)),Not(Implies(False,y[11]==0)),Not(Implies(And(Not(False),u[11]>0),y[11]==y[10]+1)),Not(Implies(And(Not(False),y[10]==100),y[11]<23)),Not(Implies(False,y[12]==0)),Not(Implies(And(Not(False),u[12]>0),y[12]==y[11]+1)),Not(Implies(And(Not(False),y[11]==100),y[12]<23)),Not(Implies(False,y[13]==0)),Not(Implies(And(Not(False),u[13]>0),y[13]==y[12]+1)),Not(Implies(And(Not(False),y[12]==100),y[13]<23)),Not(Implies(False,y[14]==0)),Not(Implies(And(Not(False),u[14]>0),y[14]==y[13]+1)),Not(Implies(And(Not(False),y[13]==100),y[14]<23)),Not(Implies(False,y[15]==0)),Not(Implies(And(Not(False),u[15]>0),y[15]==y[14]+1)),Not(Implies(And(Not(False),y[14]==100),y[15]<23)),Not(Implies(False,y[16]==0)),Not(Implies(And(Not(False),u[16]>0),y[16]==y[15]+1)),Not(Implies(And(Not(False),y[15]==100),y[16]<23)),Not(Implies(False,y[17]==0)),Not(Implies(And(Not(False),u[17]>0),y[17]==y[16]+1)),Not(Implies(And(Not(False),y[16]==100),y[17]<23)),Not(Implies(False,y[18]==0)),Not(Implies(And(Not(False),u[18]>0),y[18]==y[17]+1)),Not(Implies(And(Not(False),y[17]==100),y[18]<23)),Not(Implies(False,y[19]==0)),Not(Implies(And(Not(False),u[19]>0),y[19]==y[18]+1)),Not(Implies(And(Not(False),y[18]==100),y[19]<23)),Not(Implies(False,y[20]==0)),Not(Implies(And(Not(False),u[20]>0),y[20]==y[19]+1)),Not(Implies(And(Not(False),y[19]==100),y[20]<23)),Not(Implies(False,y[21]==0)),Not(Implies(And(Not(False),u[21]>0),y[21]==y[20]+1)),Not(Implies(And(Not(False),y[20]==100),y[21]<23)),Not(Implies(False,y[22]==0)),Not(Implies(And(Not(False),u[22]>0),y[22]==y[21]+1)),Not(Implies(And(Not(False),y[21]==100),y[22]<23)),Not(Implies(False,y[23]==0)),Not(Implies(And(Not(False),u[23]>0),y[23]==y[22]+1)),Not(Implies(And(Not(False),y[22]==100),y[23]<23)),Not(Implies(False,y[24]==0)),Not(Implies(And(Not(False),u[24]>0),y[24]==y[23]+1)),Not(Implies(And(Not(False),y[23]==100),y[24]<23)),Not(Implies(False,y[25]==0)),Not(Implies(And(Not(False),u[25]>0),y[25]==y[24]+1)),Not(Implies(And(Not(False),y[24]==100),y[25]<23)),Not(Implies(False,y[26]==0)),Not(Implies(And(Not(False),u[26]>0),y[26]==y[25]+1)),Not(Implies(And(Not(False),y[25]==100),y[26]<23)),Not(Implies(False,y[27]==0)),Not(Implies(And(Not(False),u[27]>0),y[27]==y[26]+1)),Not(Implies(And(Not(False),y[26]==100),y[27]<23)),Not(Implies(False,y[28]==0)),Not(Implies(And(Not(False),u[28]>0),y[28]==y[27]+1)),Not(Implies(And(Not(False),y[27]==100),y[28]<23)),Not(Implies(False,y[29]==0)),Not(Implies(And(Not(False),u[29]>0),y[29]==y[28]+1)),Not(Implies(And(Not(False),y[28]==100),y[29]<23)),Not(Implies(False,y[30]==0)),Not(Implies(And(Not(False),u[30]>0),y[30]==y[29]+1)),Not(Implies(And(Not(False),y[29]==100),y[30]<23)),Not(Implies(False,y[31]==0)),Not(Implies(And(Not(False),u[31]>0),y[31]==y[30]+1)),Not(Implies(And(Not(False),y[30]==100),y[31]<23)),Not(Implies(False,y[32]==0)),Not(Implies(And(Not(False),u[32]>0),y[32]==y[31]+1)),Not(Implies(And(Not(False),y[31]==100),y[32]<23)),Not(Implies(False,y[33]==0)),Not(Implies(And(Not(False),u[33]>0),y[33]==y[32]+1)),Not(Implies(And(Not(False),y[32]==100),y[33]<23)),Not(Implies(False,y[34]==0)),Not(Implies(And(Not(False),u[34]>0),y[34]==y[33]+1)),Not(Implies(And(Not(False),y[33]==100),y[34]<23)),Not(Implies(False,y[35]==0)),Not(Implies(And(Not(False),u[35]>0),y[35]==y[34]+1)),Not(Implies(And(Not(False),y[34]==100),y[35]<23)),Not(Implies(False,y[36]==0)),Not(Implies(And(Not(False),u[36]>0),y[36]==y[35]+1)),Not(Implies(And(Not(False),y[35]==100),y[36]<23)),Not(Implies(False,y[37]==0)),Not(Implies(And(Not(False),u[37]>0),y[37]==y[36]+1)),Not(Implies(And(Not(False),y[36]==100),y[37]<23)),Not(Implies(False,y[38]==0)),Not(Implies(And(Not(False),u[38]>0),y[38]==y[37]+1)),Not(Implies(And(Not(False),y[37]==100),y[38]<23)),Not(Implies(False,y[39]==0)),Not(Implies(And(Not(False),u[39]>0),y[39]==y[38]+1)),Not(Implies(And(Not(False),y[38]==100),y[39]<23)),Not(Implies(False,y[40]==0)),Not(Implies(And(Not(False),u[40]>0),y[40]==y[39]+1)),Not(Implies(And(Not(False),y[39]==100),y[40]<23)),Not(Implies(False,y[41]==0)),Not(Implies(And(Not(False),u[41]>0),y[41]==y[40]+1)),Not(Implies(And(Not(False),y[40]==100),y[41]<23)),Not(Implies(False,y[42]==0)),Not(Implies(And(Not(False),u[42]>0),y[42]==y[41]+1)),Not(Implies(And(Not(False),y[41]==100),y[42]<23)),Not(Implies(False,y[43]==0)),Not(Implies(And(Not(False),u[43]>0),y[43]==y[42]+1)),Not(Implies(And(Not(False),y[42]==100),y[43]<23)),Not(Implies(False,y[44]==0)),Not(Implies(And(Not(False),u[44]>0),y[44]==y[43]+1)),Not(Implies(And(Not(False),y[43]==100),y[44]<23)),Not(Implies(False,y[45]==0)),Not(Implies(And(Not(False),u[45]>0),y[45]==y[44]+1)),Not(Implies(And(Not(False),y[44]==100),y[45]<23)),Not(Implies(False,y[46]==0)),Not(Implies(And(Not(False),u[46]>0),y[46]==y[45]+1)),Not(Implies(And(Not(False),y[45]==100),y[46]<23)),Not(Implies(False,y[47]==0)),Not(Implies(And(Not(False),u[47]>0),y[47]==y[46]+1)),Not(Implies(And(Not(False),y[46]==100),y[47]<23)),Not(Implies(False,y[48]==0)),Not(Implies(And(Not(False),u[48]>0),y[48]==y[47]+1)),Not(Implies(And(Not(False),y[47]==100),y[48]<23)),Not(Implies(False,y[49]==0)),Not(Implies(And(Not(False),u[49]>0),y[49]==y[48]+1)),Not(Implies(And(Not(False),y[48]==100),y[49]<23)),Not(Implies(False,y[50]==0)),Not(Implies(And(Not(False),u[50]>0),y[50]==y[49]+1)),Not(Implies(And(Not(False),y[49]==100),y[50]<23)),Not(Implies(False,y[51]==0)),Not(Implies(And(Not(False),u[51]>0),y[51]==y[50]+1)),Not(Implies(And(Not(False),y[50]==100),y[51]<23)),Not(Implies(False,y[52]==0)),Not(Implies(And(Not(False),u[52]>0),y[52]==y[51]+1)),Not(Implies(And(Not(False),y[51]==100),y[52]<23)),Not(Implies(False,y[53]==0)),Not(Implies(And(Not(False),u[53]>0),y[53]==y[52]+1)),Not(Implies(And(Not(False),y[52]==100),y[53]<23)),Not(Implies(False,y[54]==0)),Not(Implies(And(Not(False),u[54]>0),y[54]==y[53]+1)),Not(Implies(And(Not(False),y[53]==100),y[54]<23)),Not(Implies(False,y[55]==0)),Not(Implies(And(Not(False),u[55]>0),y[55]==y[54]+1)),Not(Implies(And(Not(False),y[54]==100),y[55]<23)),Not(Implies(False,y[56]==0)),Not(Implies(And(Not(False),u[56]>0),y[56]==y[55]+1)),Not(Implies(And(Not(False),y[55]==100),y[56]<23)),Not(Implies(False,y[57]==0)),Not(Implies(And(Not(False),u[57]>0),y[57]==y[56]+1)),Not(Implies(And(Not(False),y[56]==100),y[57]<23)),Not(Implies(False,y[58]==0)),Not(Implies(And(Not(False),u[58]>0),y[58]==y[57]+1)),Not(Implies(And(Not(False),y[57]==100),y[58]<23)),Not(Implies(False,y[59]==0)),Not(Implies(And(Not(False),u[59]>0),y[59]==y[58]+1)),Not(Implies(And(Not(False),y[58]==100),y[59]<23)),Not(Implies(False,y[60]==0)),Not(Implies(And(Not(False),u[60]>0),y[60]==y[59]+1)),Not(Implies(And(Not(False),y[59]==100),y[60]<23)),Not(Implies(False,y[61]==0)),Not(Implies(And(Not(False),u[61]>0),y[61]==y[60]+1)),Not(Implies(And(Not(False),y[60]==100),y[61]<23)),Not(Implies(False,y[62]==0)),Not(Implies(And(Not(False),u[62]>0),y[62]==y[61]+1)),Not(Implies(And(Not(False),y[61]==100),y[62]<23)),Not(Implies(False,y[63]==0)),Not(Implies(And(Not(False),u[63]>0),y[63]==y[62]+1)),Not(Implies(And(Not(False),y[62]==100),y[63]<23)),Not(Implies(False,y[64]==0)),Not(Implies(And(Not(False),u[64]>0),y[64]==y[63]+1)),Not(Implies(And(Not(False),y[63]==100),y[64]<23)),Not(Implies(False,y[65]==0)),Not(Implies(And(Not(False),u[65]>0),y[65]==y[64]+1)),Not(Implies(And(Not(False),y[64]==100),y[65]<23)),Not(Implies(False,y[66]==0)),Not(Implies(And(Not(False),u[66]>0),y[66]==y[65]+1)),Not(Implies(And(Not(False),y[65]==100),y[66]<23)),Not(Implies(False,y[67]==0)),Not(Implies(And(Not(False),u[67]>0),y[67]==y[66]+1)),Not(Implies(And(Not(False),y[66]==100),y[67]<23)),Not(Implies(False,y[68]==0)),Not(Implies(And(Not(False),u[68]>0),y[68]==y[67]+1)),Not(Implies(And(Not(False),y[67]==100),y[68]<23)),Not(Implies(False,y[69]==0)),Not(Implies(And(Not(False),u[69]>0),y[69]==y[68]+1)),Not(Implies(And(Not(False),y[68]==100),y[69]<23)),Not(Implies(False,y[70]==0)),Not(Implies(And(Not(False),u[70]>0),y[70]==y[69]+1)),Not(Implies(And(Not(False),y[69]==100),y[70]<23)),Not(Implies(False,y[71]==0)),Not(Implies(And(Not(False),u[71]>0),y[71]==y[70]+1)),Not(Implies(And(Not(False),y[70]==100),y[71]<23)),Not(Implies(False,y[72]==0)),Not(Implies(And(Not(False),u[72]>0),y[72]==y[71]+1)),Not(Implies(And(Not(False),y[71]==100),y[72]<23)),Not(Implies(False,y[73]==0)),Not(Implies(And(Not(False),u[73]>0),y[73]==y[72]+1)),Not(Implies(And(Not(False),y[72]==100),y[73]<23)),Not(Implies(False,y[74]==0)),Not(Implies(And(Not(False),u[74]>0),y[74]==y[73]+1)),Not(Implies(And(Not(False),y[73]==100),y[74]<23)),Not(Implies(False,y[75]==0)),Not(Implies(And(Not(False),u[75]>0),y[75]==y[74]+1)),Not(Implies(And(Not(False),y[74]==100),y[75]<23)),Not(Implies(False,y[76]==0)),Not(Implies(And(Not(False),u[76]>0),y[76]==y[75]+1)),Not(Implies(And(Not(False),y[75]==100),y[76]<23)),Not(Implies(False,y[77]==0)),Not(Implies(And(Not(False),u[77]>0),y[77]==y[76]+1)),Not(Implies(And(Not(False),y[76]==100),y[77]<23)),Not(Implies(False,y[78]==0)),Not(Implies(And(Not(False),u[78]>0),y[78]==y[77]+1)),Not(Implies(And(Not(False),y[77]==100),y[78]<23)),Not(Implies(False,y[79]==0)),Not(Implies(And(Not(False),u[79]>0),y[79]==y[78]+1)),Not(Implies(And(Not(False),y[78]==100),y[79]<23)),Not(Implies(False,y[80]==0)),Not(Implies(And(Not(False),u[80]>0),y[80]==y[79]+1)),Not(Implies(And(Not(False),y[79]==100),y[80]<23)),Not(Implies(False,y[81]==0)),Not(Implies(And(Not(False),u[81]>0),y[81]==y[80]+1)),Not(Implies(And(Not(False),y[80]==100),y[81]<23)),Not(Implies(False,y[82]==0)),Not(Implies(And(Not(False),u[82]>0),y[82]==y[81]+1)),Not(Implies(And(Not(False),y[81]==100),y[82]<23)),Not(Implies(False,y[83]==0)),Not(Implies(And(Not(False),u[83]>0),y[83]==y[82]+1)),Not(Implies(And(Not(False),y[82]==100),y[83]<23)),Not(Implies(False,y[84]==0)),Not(Implies(And(Not(False),u[84]>0),y[84]==y[83]+1)),Not(Implies(And(Not(False),y[83]==100),y[84]<23)),Not(Implies(False,y[85]==0)),Not(Implies(And(Not(False),u[85]>0),y[85]==y[84]+1)),Not(Implies(And(Not(False),y[84]==100),y[85]<23)),Not(Implies(False,y[86]==0)),Not(Implies(And(Not(False),u[86]>0),y[86]==y[85]+1)),Not(Implies(And(Not(False),y[85]==100),y[86]<23)),Not(Implies(False,y[87]==0)),Not(Implies(And(Not(False),u[87]>0),y[87]==y[86]+1)),Not(Implies(And(Not(False),y[86]==100),y[87]<23)),Not(Implies(False,y[88]==0)),Not(Implies(And(Not(False),u[88]>0),y[88]==y[87]+1)),Not(Implies(And(Not(False),y[87]==100),y[88]<23)),Not(Implies(False,y[89]==0)),Not(Implies(And(Not(False),u[89]>0),y[89]==y[88]+1)),Not(Implies(And(Not(False),y[88]==100),y[89]<23)),Not(Implies(False,y[90]==0)),Not(Implies(And(Not(False),u[90]>0),y[90]==y[89]+1)),Not(Implies(And(Not(False),y[89]==100),y[90]<23)),Not(Implies(False,y[91]==0)),Not(Implies(And(Not(False),u[91]>0),y[91]==y[90]+1)),Not(Implies(And(Not(False),y[90]==100),y[91]<23)),Not(Implies(False,y[92]==0)),Not(Implies(And(Not(False),u[92]>0),y[92]==y[91]+1)),Not(Implies(And(Not(False),y[91]==100),y[92]<23)),Not(Implies(False,y[93]==0)),Not(Implies(And(Not(False),u[93]>0),y[93]==y[92]+1)),Not(Implies(And(Not(False),y[92]==100),y[93]<23)),Not(Implies(False,y[94]==0)),Not(Implies(And(Not(False),u[94]>0),y[94]==y[93]+1)),Not(Implies(And(Not(False),y[93]==100),y[94]<23)),Not(Implies(False,y[95]==0)),Not(Implies(And(Not(False),u[95]>0),y[95]==y[94]+1)),Not(Implies(And(Not(False),y[94]==100),y[95]<23)),Not(Implies(False,y[96]==0)),Not(Implies(And(Not(False),u[96]>0),y[96]==y[95]+1)),Not(Implies(And(Not(False),y[95]==100),y[96]<23)),Not(Implies(False,y[97]==0)),Not(Implies(And(Not(False),u[97]>0),y[97]==y[96]+1)),Not(Implies(And(Not(False),y[96]==100),y[97]<23)),Not(Implies(False,y[98]==0)),Not(Implies(And(Not(False),u[98]>0),y[98]==y[97]+1)),Not(Implies(And(Not(False),y[97]==100),y[98]<23)),Not(Implies(False,y[99]==0)),Not(Implies(And(Not(False),u[99]>0),y[99]==y[98]+1)),Not(Implies(And(Not(False),y[98]==100),y[99]<23)),Not(Implies(False,y[100]==0)),Not(Implies(And(Not(False),u[100]>0),y[100]==y[99]+1)),Not(Implies(And(Not(False),y[99]==100),y[100]<23)),Not(Implies(False,y[101]==0)),Not(Implies(And(Not(False),u[101]>0),y[101]==y[100]+1)),Not(Implies(And(Not(False),y[100]==100),y[101]<23)),Not(Implies(False,y[102]==0)),Not(Implies(And(Not(False),u[102]>0),y[102]==y[101]+1)),Not(Implies(And(Not(False),y[101]==100),y[102]<23)),Not(Implies(False,y[103]==0)),Not(Implies(And(Not(False),u[103]>0),y[103]==y[102]+1)),Not(Implies(And(Not(False),y[102]==100),y[103]<23)),Not(Implies(False,y[104]==0)),Not(Implies(And(Not(False),u[104]>0),y[104]==y[103]+1)),Not(Implies(And(Not(False),y[103]==100),y[104]<23)),Not(Implies(False,y[105]==0)),Not(Implies(And(Not(False),u[105]>0),y[105]==y[104]+1)),Not(Implies(And(Not(False),y[104]==100),y[105]<23)),Not(Implies(False,y[106]==0)),Not(Implies(And(Not(False),u[106]>0),y[106]==y[105]+1)),Not(Implies(And(Not(False),y[105]==100),y[106]<23)),Not(Implies(False,y[107]==0)),Not(Implies(And(Not(False),u[107]>0),y[107]==y[106]+1)),Not(Implies(And(Not(False),y[106]==100),y[107]<23)),Not(Implies(False,y[108]==0)),Not(Implies(And(Not(False),u[108]>0),y[108]==y[107]+1)),Not(Implies(And(Not(False),y[107]==100),y[108]<23)),Not(Implies(False,y[109]==0)),Not(Implies(And(Not(False),u[109]>0),y[109]==y[108]+1)),Not(Implies(And(Not(False),y[108]==100),y[109]<23)),Not(Implies(False,y[110]==0)),Not(Implies(And(Not(False),u[110]>0),y[110]==y[109]+1)),Not(Implies(And(Not(False),y[109]==100),y[110]<23)),Not(Implies(False,y[111]==0)),Not(Implies(And(Not(False),u[111]>0),y[111]==y[110]+1)),Not(Implies(And(Not(False),y[110]==100),y[111]<23)),Not(Implies(False,y[112]==0)),Not(Implies(And(Not(False),u[112]>0),y[112]==y[111]+1)),Not(Implies(And(Not(False),y[111]==100),y[112]<23)),Not(Implies(False,y[113]==0)),Not(Implies(And(Not(False),u[113]>0),y[113]==y[112]+1)),Not(Implies(And(Not(False),y[112]==100),y[113]<23)),Not(Implies(False,y[114]==0)),Not(Implies(And(Not(False),u[114]>0),y[114]==y[113]+1)),Not(Implies(And(Not(False),y[113]==100),y[114]<23)),Not(Implies(False,y[115]==0)),Not(Implies(And(Not(False),u[115]>0),y[115]==y[114]+1)),Not(Implies(And(Not(False),y[114]==100),y[115]<23)),Not(Implies(False,y[116]==0)),Not(Implies(And(Not(False),u[116]>0),y[116]==y[115]+1)),Not(Implies(And(Not(False),y[115]==100),y[116]<23)),Not(Implies(False,y[117]==0)),Not(Implies(And(Not(False),u[117]>0),y[117]==y[116]+1)),Not(Implies(And(Not(False),y[116]==100),y[117]<23)),Not(Implies(False,y[118]==0)),Not(Implies(And(Not(False),u[118]>0),y[118]==y[117]+1)),Not(Implies(And(Not(False),y[117]==100),y[118]<23)),Not(Implies(False,y[119]==0)),Not(Implies(And(Not(False),u[119]>0),y[119]==y[118]+1)),Not(Implies(And(Not(False),y[118]==100),y[119]<23)),Not(Implies(False,y[120]==0)),Not(Implies(And(Not(False),u[120]>0),y[120]==y[119]+1)),Not(Implies(And(Not(False),y[119]==100),y[120]<23)),Not(Implies(False,y[121]==0)),Not(Implies(And(Not(False),u[121]>0),y[121]==y[120]+1)),Not(Implies(And(Not(False),y[120]==100),y[121]<23)),Not(Implies(False,y[122]==0)),Not(Implies(And(Not(False),u[122]>0),y[122]==y[121]+1)),Not(Implies(And(Not(False),y[121]==100),y[122]<23)),Not(Implies(False,y[123]==0)),Not(Implies(And(Not(False),u[123]>0),y[123]==y[122]+1)),Not(Implies(And(Not(False),y[122]==100),y[123]<23)),Not(Implies(False,y[124]==0)),Not(Implies(And(Not(False),u[124]>0),y[124]==y[123]+1)),Not(Implies(And(Not(False),y[123]==100),y[124]<23)),Not(Implies(False,y[125]==0)),Not(Implies(And(Not(False),u[125]>0),y[125]==y[124]+1)),Not(Implies(And(Not(False),y[124]==100),y[125]<23)),Not(Implies(False,y[126]==0)),Not(Implies(And(Not(False),u[126]>0),y[126]==y[125]+1)),Not(Implies(And(Not(False),y[125]==100),y[126]<23)),Not(Implies(False,y[127]==0)),Not(Implies(And(Not(False),u[127]>0),y[127]==y[126]+1)),Not(Implies(And(Not(False),y[126]==100),y[127]<23)),Not(Implies(False,y[128]==0)),Not(Implies(And(Not(False),u[128]>0),y[128]==y[127]+1)),Not(Implies(And(Not(False),y[127]==100),y[128]<23)),Not(Implies(False,y[129]==0)),Not(Implies(And(Not(False),u[129]>0),y[129]==y[128]+1)),Not(Implies(And(Not(False),y[128]==100),y[129]<23)),Not(Implies(False,y[130]==0)),Not(Implies(And(Not(False),u[130]>0),y[130]==y[129]+1)),Not(Implies(And(Not(False),y[129]==100),y[130]<23)),Not(Implies(False,y[131]==0)),Not(Implies(And(Not(False),u[131]>0),y[131]==y[130]+1)),Not(Implies(And(Not(False),y[130]==100),y[131]<23)),Not(Implies(False,y[132]==0)),Not(Implies(And(Not(False),u[132]>0),y[132]==y[131]+1)),Not(Implies(And(Not(False),y[131]==100),y[132]<23)),Not(Implies(False,y[133]==0)),Not(Implies(And(Not(False),u[133]>0),y[133]==y[132]+1)),Not(Implies(And(Not(False),y[132]==100),y[133]<23)),Not(Implies(False,y[134]==0)),Not(Implies(And(Not(False),u[134]>0),y[134]==y[133]+1)),Not(Implies(And(Not(False),y[133]==100),y[134]<23)),Not(Implies(False,y[135]==0)),Not(Implies(And(Not(False),u[135]>0),y[135]==y[134]+1)),Not(Implies(And(Not(False),y[134]==100),y[135]<23)),Not(Implies(False,y[136]==0)),Not(Implies(And(Not(False),u[136]>0),y[136]==y[135]+1)),Not(Implies(And(Not(False),y[135]==100),y[136]<23)),Not(Implies(False,y[137]==0)),Not(Implies(And(Not(False),u[137]>0),y[137]==y[136]+1)),Not(Implies(And(Not(False),y[136]==100),y[137]<23)),Not(Implies(False,y[138]==0)),Not(Implies(And(Not(False),u[138]>0),y[138]==y[137]+1)),Not(Implies(And(Not(False),y[137]==100),y[138]<23)),Not(Implies(False,y[139]==0)),Not(Implies(And(Not(False),u[139]>0),y[139]==y[138]+1)),Not(Implies(And(Not(False),y[138]==100),y[139]<23)),Not(Implies(False,y[140]==0)),Not(Implies(And(Not(False),u[140]>0),y[140]==y[139]+1)),Not(Implies(And(Not(False),y[139]==100),y[140]<23)),Not(Implies(False,y[141]==0)),Not(Implies(And(Not(False),u[141]>0),y[141]==y[140]+1)),Not(Implies(And(Not(False),y[140]==100),y[141]<23)),Not(Implies(False,y[142]==0)),Not(Implies(And(Not(False),u[142]>0),y[142]==y[141]+1)),Not(Implies(And(Not(False),y[141]==100),y[142]<23)),Not(Implies(False,y[143]==0)),Not(Implies(And(Not(False),u[143]>0),y[143]==y[142]+1)),Not(Implies(And(Not(False),y[142]==100),y[143]<23)),Not(Implies(False,y[144]==0)),Not(Implies(And(Not(False),u[144]>0),y[144]==y[143]+1)),Not(Implies(And(Not(False),y[143]==100),y[144]<23)),Not(Implies(False,y[145]==0)),Not(Implies(And(Not(False),u[145]>0),y[145]==y[144]+1)),Not(Implies(And(Not(False),y[144]==100),y[145]<23)),Not(Implies(False,y[146]==0)),Not(Implies(And(Not(False),u[146]>0),y[146]==y[145]+1)),Not(Implies(And(Not(False),y[145]==100),y[146]<23)),Not(Implies(False,y[147]==0)),Not(Implies(And(Not(False),u[147]>0),y[147]==y[146]+1)),Not(Implies(And(Not(False),y[146]==100),y[147]<23)),Not(Implies(False,y[148]==0)),Not(Implies(And(Not(False),u[148]>0),y[148]==y[147]+1)),Not(Implies(And(Not(False),y[147]==100),y[148]<23)),Not(Implies(False,y[149]==0)),Not(Implies(And(Not(False),u[149]>0),y[149]==y[148]+1)),Not(Implies(And(Not(False),y[148]==100),y[149]<23)),Not(Implies(False,y[150]==0)),Not(Implies(And(Not(False),u[150]>0),y[150]==y[149]+1)),Not(Implies(And(Not(False),y[149]==100),y[150]<23)),Not(Implies(False,y[151]==0)),Not(Implies(And(Not(False),u[151]>0),y[151]==y[150]+1)),Not(Implies(And(Not(False),y[150]==100),y[151]<23)),Not(Implies(False,y[152]==0)),Not(Implies(And(Not(False),u[152]>0),y[152]==y[151]+1)),Not(Implies(And(Not(False),y[151]==100),y[152]<23)),Not(Implies(False,y[153]==0)),Not(Implies(And(Not(False),u[153]>0),y[153]==y[152]+1)),Not(Implies(And(Not(False),y[152]==100),y[153]<23)),Not(Implies(False,y[154]==0)),Not(Implies(And(Not(False),u[154]>0),y[154]==y[153]+1)),Not(Implies(And(Not(False),y[153]==100),y[154]<23)),Not(Implies(False,y[155]==0)),Not(Implies(And(Not(False),u[155]>0),y[155]==y[154]+1)),Not(Implies(And(Not(False),y[154]==100),y[155]<23)),Not(Implies(False,y[156]==0)),Not(Implies(And(Not(False),u[156]>0),y[156]==y[155]+1)),Not(Implies(And(Not(False),y[155]==100),y[156]<23)),Not(Implies(False,y[157]==0)),Not(Implies(And(Not(False),u[157]>0),y[157]==y[156]+1)),Not(Implies(And(Not(False),y[156]==100),y[157]<23)),Not(Implies(False,y[158]==0)),Not(Implies(And(Not(False),u[158]>0),y[158]==y[157]+1)),Not(Implies(And(Not(False),y[157]==100),y[158]<23)),Not(Implies(False,y[159]==0)),Not(Implies(And(Not(False),u[159]>0),y[159]==y[158]+1)),Not(Implies(And(Not(False),y[158]==100),y[159]<23)),Not(Implies(False,y[160]==0)),Not(Implies(And(Not(False),u[160]>0),y[160]==y[159]+1)),Not(Implies(And(Not(False),y[159]==100),y[160]<23)),Not(Implies(False,y[161]==0)),Not(Implies(And(Not(False),u[161]>0),y[161]==y[160]+1)),Not(Implies(And(Not(False),y[160]==100),y[161]<23)),Not(Implies(False,y[162]==0)),Not(Implies(And(Not(False),u[162]>0),y[162]==y[161]+1)),Not(Implies(And(Not(False),y[161]==100),y[162]<23)),Not(Implies(False,y[163]==0)),Not(Implies(And(Not(False),u[163]>0),y[163]==y[162]+1)),Not(Implies(And(Not(False),y[162]==100),y[163]<23)),Not(Implies(False,y[164]==0)),Not(Implies(And(Not(False),u[164]>0),y[164]==y[163]+1)),Not(Implies(And(Not(False),y[163]==100),y[164]<23)),Not(Implies(False,y[165]==0)),Not(Implies(And(Not(False),u[165]>0),y[165]==y[164]+1)),Not(Implies(And(Not(False),y[164]==100),y[165]<23)),Not(Implies(False,y[166]==0)),Not(Implies(And(Not(False),u[166]>0),y[166]==y[165]+1)),Not(Implies(And(Not(False),y[165]==100),y[166]<23)),Not(Implies(False,y[167]==0)),Not(Implies(And(Not(False),u[167]>0),y[167]==y[166]+1)),Not(Implies(And(Not(False),y[166]==100),y[167]<23)),Not(Implies(False,y[168]==0)),Not(Implies(And(Not(False),u[168]>0),y[168]==y[167]+1)),Not(Implies(And(Not(False),y[167]==100),y[168]<23)),Not(Implies(False,y[169]==0)),Not(Implies(And(Not(False),u[169]>0),y[169]==y[168]+1)),Not(Implies(And(Not(False),y[168]==100),y[169]<23)),Not(Implies(False,y[170]==0)),Not(Implies(And(Not(False),u[170]>0),y[170]==y[169]+1)),Not(Implies(And(Not(False),y[169]==100),y[170]<23)),Not(Implies(False,y[171]==0)),Not(Implies(And(Not(False),u[171]>0),y[171]==y[170]+1)),Not(Implies(And(Not(False),y[170]==100),y[171]<23)),Not(Implies(False,y[172]==0)),Not(Implies(And(Not(False),u[172]>0),y[172]==y[171]+1)),Not(Implies(And(Not(False),y[171]==100),y[172]<23)),Not(Implies(False,y[173]==0)),Not(Implies(And(Not(False),u[173]>0),y[173]==y[172]+1)),Not(Implies(And(Not(False),y[172]==100),y[173]<23)),Not(Implies(False,y[174]==0)),Not(Implies(And(Not(False),u[174]>0),y[174]==y[173]+1)),Not(Implies(And(Not(False),y[173]==100),y[174]<23)),Not(Implies(False,y[175]==0)),Not(Implies(And(Not(False),u[175]>0),y[175]==y[174]+1)),Not(Implies(And(Not(False),y[174]==100),y[175]<23)),Not(Implies(False,y[176]==0)),Not(Implies(And(Not(False),u[176]>0),y[176]==y[175]+1)),Not(Implies(And(Not(False),y[175]==100),y[176]<23)),Not(Implies(False,y[177]==0)),Not(Implies(And(Not(False),u[177]>0),y[177]==y[176]+1)),Not(Implies(And(Not(False),y[176]==100),y[177]<23)),Not(Implies(False,y[178]==0)),Not(Implies(And(Not(False),u[178]>0),y[178]==y[177]+1)),Not(Implies(And(Not(False),y[177]==100),y[178]<23)),Not(Implies(False,y[179]==0)),Not(Implies(And(Not(False),u[179]>0),y[179]==y[178]+1)),Not(Implies(And(Not(False),y[178]==100),y[179]<23)),Not(Implies(False,y[180]==0)),Not(Implies(And(Not(False),u[180]>0),y[180]==y[179]+1)),Not(Implies(And(Not(False),y[179]==100),y[180]<23)),Not(Implies(False,y[181]==0)),Not(Implies(And(Not(False),u[181]>0),y[181]==y[180]+1)),Not(Implies(And(Not(False),y[180]==100),y[181]<23)),Not(Implies(False,y[182]==0)),Not(Implies(And(Not(False),u[182]>0),y[182]==y[181]+1)),Not(Implies(And(Not(False),y[181]==100),y[182]<23)),Not(Implies(False,y[183]==0)),Not(Implies(And(Not(False),u[183]>0),y[183]==y[182]+1)),Not(Implies(And(Not(False),y[182]==100),y[183]<23)),Not(Implies(False,y[184]==0)),Not(Implies(And(Not(False),u[184]>0),y[184]==y[183]+1)),Not(Implies(And(Not(False),y[183]==100),y[184]<23)),Not(Implies(False,y[185]==0)),Not(Implies(And(Not(False),u[185]>0),y[185]==y[184]+1)),Not(Implies(And(Not(False),y[184]==100),y[185]<23)),Not(Implies(False,y[186]==0)),Not(Implies(And(Not(False),u[186]>0),y[186]==y[185]+1)),Not(Implies(And(Not(False),y[185]==100),y[186]<23)),Not(Implies(False,y[187]==0)),Not(Implies(And(Not(False),u[187]>0),y[187]==y[186]+1)),Not(Implies(And(Not(False),y[186]==100),y[187]<23)),Not(Implies(False,y[188]==0)),Not(Implies(And(Not(False),u[188]>0),y[188]==y[187]+1)),Not(Implies(And(Not(False),y[187]==100),y[188]<23)),Not(Implies(False,y[189]==0)),Not(Implies(And(Not(False),u[189]>0),y[189]==y[188]+1)),Not(Implies(And(Not(False),y[188]==100),y[189]<23)),Not(Implies(False,y[190]==0)),Not(Implies(And(Not(False),u[190]>0),y[190]==y[189]+1)),Not(Implies(And(Not(False),y[189]==100),y[190]<23)),Not(Implies(False,y[191]==0)),Not(Implies(And(Not(False),u[191]>0),y[191]==y[190]+1)),Not(Implies(And(Not(False),y[190]==100),y[191]<23)),Not(Implies(False,y[192]==0)),Not(Implies(And(Not(False),u[192]>0),y[192]==y[191]+1)),Not(Implies(And(Not(False),y[191]==100),y[192]<23)),Not(Implies(False,y[193]==0)),Not(Implies(And(Not(False),u[193]>0),y[193]==y[192]+1)),Not(Implies(And(Not(False),y[192]==100),y[193]<23)),Not(Implies(False,y[194]==0)),Not(Implies(And(Not(False),u[194]>0),y[194]==y[193]+1)),Not(Implies(And(Not(False),y[193]==100),y[194]<23)),Not(Implies(False,y[195]==0)),Not(Implies(And(Not(False),u[195]>0),y[195]==y[194]+1)),Not(Implies(And(Not(False),y[194]==100),y[195]<23)),Not(Implies(False,y[196]==0)),Not(Implies(And(Not(False),u[196]>0),y[196]==y[195]+1)),Not(Implies(And(Not(False),y[195]==100),y[196]<23)),Not(Implies(False,y[197]==0)),Not(Implies(And(Not(False),u[197]>0),y[197]==y[196]+1)),Not(Implies(And(Not(False),y[196]==100),y[197]<23)),Not(Implies(False,y[198]==0)),Not(Implies(And(Not(False),u[198]>0),y[198]==y[197]+1)),Not(Implies(And(Not(False),y[197]==100),y[198]<23)),Not(Implies(False,y[199]==0)),Not(Implies(And(Not(False),u[199]>0),y[199]==y[198]+1)),Not(Implies(And(Not(False),y[198]==100),y[199]<23))))))
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
