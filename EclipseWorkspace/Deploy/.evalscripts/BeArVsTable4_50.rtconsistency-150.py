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
s.add(And(tau[0]<tau[0 + 1],tau[1]<tau[1 + 1],tau[2]<tau[2 + 1],tau[3]<tau[3 + 1],tau[4]<tau[4 + 1],tau[5]<tau[5 + 1],tau[6]<tau[6 + 1],tau[7]<tau[7 + 1],tau[8]<tau[8 + 1],tau[9]<tau[9 + 1],tau[10]<tau[10 + 1],tau[11]<tau[11 + 1],tau[12]<tau[12 + 1],tau[13]<tau[13 + 1],tau[14]<tau[14 + 1],tau[15]<tau[15 + 1],tau[16]<tau[16 + 1],tau[17]<tau[17 + 1],tau[18]<tau[18 + 1],tau[19]<tau[19 + 1],tau[20]<tau[20 + 1],tau[21]<tau[21 + 1],tau[22]<tau[22 + 1],tau[23]<tau[23 + 1],tau[24]<tau[24 + 1],tau[25]<tau[25 + 1],tau[26]<tau[26 + 1],tau[27]<tau[27 + 1],tau[28]<tau[28 + 1],tau[29]<tau[29 + 1],tau[30]<tau[30 + 1],tau[31]<tau[31 + 1],tau[32]<tau[32 + 1],tau[33]<tau[33 + 1],tau[34]<tau[34 + 1],tau[35]<tau[35 + 1],tau[36]<tau[36 + 1],tau[37]<tau[37 + 1],tau[38]<tau[38 + 1],tau[39]<tau[39 + 1],tau[40]<tau[40 + 1],tau[41]<tau[41 + 1],tau[42]<tau[42 + 1],tau[43]<tau[43 + 1],tau[44]<tau[44 + 1],tau[45]<tau[45 + 1],tau[46]<tau[46 + 1],tau[47]<tau[47 + 1],tau[48]<tau[48 + 1],tau[49]<tau[49 + 1],tau[50]<tau[50 + 1],tau[51]<tau[51 + 1],tau[52]<tau[52 + 1],tau[53]<tau[53 + 1],tau[54]<tau[54 + 1],tau[55]<tau[55 + 1],tau[56]<tau[56 + 1],tau[57]<tau[57 + 1],tau[58]<tau[58 + 1],tau[59]<tau[59 + 1],tau[60]<tau[60 + 1],tau[61]<tau[61 + 1],tau[62]<tau[62 + 1],tau[63]<tau[63 + 1],tau[64]<tau[64 + 1],tau[65]<tau[65 + 1],tau[66]<tau[66 + 1],tau[67]<tau[67 + 1],tau[68]<tau[68 + 1],tau[69]<tau[69 + 1],tau[70]<tau[70 + 1],tau[71]<tau[71 + 1],tau[72]<tau[72 + 1],tau[73]<tau[73 + 1],tau[74]<tau[74 + 1],tau[75]<tau[75 + 1],tau[76]<tau[76 + 1],tau[77]<tau[77 + 1],tau[78]<tau[78 + 1],tau[79]<tau[79 + 1],tau[80]<tau[80 + 1],tau[81]<tau[81 + 1],tau[82]<tau[82 + 1],tau[83]<tau[83 + 1],tau[84]<tau[84 + 1],tau[85]<tau[85 + 1],tau[86]<tau[86 + 1],tau[87]<tau[87 + 1],tau[88]<tau[88 + 1],tau[89]<tau[89 + 1],tau[90]<tau[90 + 1],tau[91]<tau[91 + 1],tau[92]<tau[92 + 1],tau[93]<tau[93 + 1],tau[94]<tau[94 + 1],tau[95]<tau[95 + 1],tau[96]<tau[96 + 1],tau[97]<tau[97 + 1],tau[98]<tau[98 + 1],tau[99]<tau[99 + 1],tau[100]<tau[100 + 1],tau[101]<tau[101 + 1],tau[102]<tau[102 + 1],tau[103]<tau[103 + 1],tau[104]<tau[104 + 1],tau[105]<tau[105 + 1],tau[106]<tau[106 + 1],tau[107]<tau[107 + 1],tau[108]<tau[108 + 1],tau[109]<tau[109 + 1],tau[110]<tau[110 + 1],tau[111]<tau[111 + 1],tau[112]<tau[112 + 1],tau[113]<tau[113 + 1],tau[114]<tau[114 + 1],tau[115]<tau[115 + 1],tau[116]<tau[116 + 1],tau[117]<tau[117 + 1],tau[118]<tau[118 + 1],tau[119]<tau[119 + 1],tau[120]<tau[120 + 1],tau[121]<tau[121 + 1],tau[122]<tau[122 + 1],tau[123]<tau[123 + 1],tau[124]<tau[124 + 1],tau[125]<tau[125 + 1],tau[126]<tau[126 + 1],tau[127]<tau[127 + 1],tau[128]<tau[128 + 1],tau[129]<tau[129 + 1],tau[130]<tau[130 + 1],tau[131]<tau[131 + 1],tau[132]<tau[132 + 1],tau[133]<tau[133 + 1],tau[134]<tau[134 + 1],tau[135]<tau[135 + 1],tau[136]<tau[136 + 1],tau[137]<tau[137 + 1],tau[138]<tau[138 + 1],tau[139]<tau[139 + 1],tau[140]<tau[140 + 1],tau[141]<tau[141 + 1],tau[142]<tau[142 + 1],tau[143]<tau[143 + 1],tau[144]<tau[144 + 1],tau[145]<tau[145 + 1],tau[146]<tau[146 + 1],tau[147]<tau[147 + 1],tau[148]<tau[148 + 1]))
# Requirements Table
s.add(ForAll([y] , Or(Or(Not(Implies(True,y[0]==0)),Not(Implies(And(Not(True),u[0]==u[0]+1),y[0]==y[0]+1)),Not(Implies(And(Not(True),u[0]!=u[0]+1),y[0]<23)),Not(Implies(False,y[1]==0)),Not(Implies(And(Not(False),u[1]==u[0]+1),y[1]==y[0]+1)),Not(Implies(And(Not(False),u[1]!=u[0]+1),y[1]<23)),Not(Implies(False,y[2]==0)),Not(Implies(And(Not(False),u[2]==u[1]+1),y[2]==y[1]+1)),Not(Implies(And(Not(False),u[2]!=u[1]+1),y[2]<23)),Not(Implies(False,y[3]==0)),Not(Implies(And(Not(False),u[3]==u[2]+1),y[3]==y[2]+1)),Not(Implies(And(Not(False),u[3]!=u[2]+1),y[3]<23)),Not(Implies(False,y[4]==0)),Not(Implies(And(Not(False),u[4]==u[3]+1),y[4]==y[3]+1)),Not(Implies(And(Not(False),u[4]!=u[3]+1),y[4]<23)),Not(Implies(False,y[5]==0)),Not(Implies(And(Not(False),u[5]==u[4]+1),y[5]==y[4]+1)),Not(Implies(And(Not(False),u[5]!=u[4]+1),y[5]<23)),Not(Implies(False,y[6]==0)),Not(Implies(And(Not(False),u[6]==u[5]+1),y[6]==y[5]+1)),Not(Implies(And(Not(False),u[6]!=u[5]+1),y[6]<23)),Not(Implies(False,y[7]==0)),Not(Implies(And(Not(False),u[7]==u[6]+1),y[7]==y[6]+1)),Not(Implies(And(Not(False),u[7]!=u[6]+1),y[7]<23)),Not(Implies(False,y[8]==0)),Not(Implies(And(Not(False),u[8]==u[7]+1),y[8]==y[7]+1)),Not(Implies(And(Not(False),u[8]!=u[7]+1),y[8]<23)),Not(Implies(False,y[9]==0)),Not(Implies(And(Not(False),u[9]==u[8]+1),y[9]==y[8]+1)),Not(Implies(And(Not(False),u[9]!=u[8]+1),y[9]<23)),Not(Implies(False,y[10]==0)),Not(Implies(And(Not(False),u[10]==u[9]+1),y[10]==y[9]+1)),Not(Implies(And(Not(False),u[10]!=u[9]+1),y[10]<23)),Not(Implies(False,y[11]==0)),Not(Implies(And(Not(False),u[11]==u[10]+1),y[11]==y[10]+1)),Not(Implies(And(Not(False),u[11]!=u[10]+1),y[11]<23)),Not(Implies(False,y[12]==0)),Not(Implies(And(Not(False),u[12]==u[11]+1),y[12]==y[11]+1)),Not(Implies(And(Not(False),u[12]!=u[11]+1),y[12]<23)),Not(Implies(False,y[13]==0)),Not(Implies(And(Not(False),u[13]==u[12]+1),y[13]==y[12]+1)),Not(Implies(And(Not(False),u[13]!=u[12]+1),y[13]<23)),Not(Implies(False,y[14]==0)),Not(Implies(And(Not(False),u[14]==u[13]+1),y[14]==y[13]+1)),Not(Implies(And(Not(False),u[14]!=u[13]+1),y[14]<23)),Not(Implies(False,y[15]==0)),Not(Implies(And(Not(False),u[15]==u[14]+1),y[15]==y[14]+1)),Not(Implies(And(Not(False),u[15]!=u[14]+1),y[15]<23)),Not(Implies(False,y[16]==0)),Not(Implies(And(Not(False),u[16]==u[15]+1),y[16]==y[15]+1)),Not(Implies(And(Not(False),u[16]!=u[15]+1),y[16]<23)),Not(Implies(False,y[17]==0)),Not(Implies(And(Not(False),u[17]==u[16]+1),y[17]==y[16]+1)),Not(Implies(And(Not(False),u[17]!=u[16]+1),y[17]<23)),Not(Implies(False,y[18]==0)),Not(Implies(And(Not(False),u[18]==u[17]+1),y[18]==y[17]+1)),Not(Implies(And(Not(False),u[18]!=u[17]+1),y[18]<23)),Not(Implies(False,y[19]==0)),Not(Implies(And(Not(False),u[19]==u[18]+1),y[19]==y[18]+1)),Not(Implies(And(Not(False),u[19]!=u[18]+1),y[19]<23)),Not(Implies(False,y[20]==0)),Not(Implies(And(Not(False),u[20]==u[19]+1),y[20]==y[19]+1)),Not(Implies(And(Not(False),u[20]!=u[19]+1),y[20]<23)),Not(Implies(False,y[21]==0)),Not(Implies(And(Not(False),u[21]==u[20]+1),y[21]==y[20]+1)),Not(Implies(And(Not(False),u[21]!=u[20]+1),y[21]<23)),Not(Implies(False,y[22]==0)),Not(Implies(And(Not(False),u[22]==u[21]+1),y[22]==y[21]+1)),Not(Implies(And(Not(False),u[22]!=u[21]+1),y[22]<23)),Not(Implies(False,y[23]==0)),Not(Implies(And(Not(False),u[23]==u[22]+1),y[23]==y[22]+1)),Not(Implies(And(Not(False),u[23]!=u[22]+1),y[23]<23)),Not(Implies(False,y[24]==0)),Not(Implies(And(Not(False),u[24]==u[23]+1),y[24]==y[23]+1)),Not(Implies(And(Not(False),u[24]!=u[23]+1),y[24]<23)),Not(Implies(False,y[25]==0)),Not(Implies(And(Not(False),u[25]==u[24]+1),y[25]==y[24]+1)),Not(Implies(And(Not(False),u[25]!=u[24]+1),y[25]<23)),Not(Implies(False,y[26]==0)),Not(Implies(And(Not(False),u[26]==u[25]+1),y[26]==y[25]+1)),Not(Implies(And(Not(False),u[26]!=u[25]+1),y[26]<23)),Not(Implies(False,y[27]==0)),Not(Implies(And(Not(False),u[27]==u[26]+1),y[27]==y[26]+1)),Not(Implies(And(Not(False),u[27]!=u[26]+1),y[27]<23)),Not(Implies(False,y[28]==0)),Not(Implies(And(Not(False),u[28]==u[27]+1),y[28]==y[27]+1)),Not(Implies(And(Not(False),u[28]!=u[27]+1),y[28]<23)),Not(Implies(False,y[29]==0)),Not(Implies(And(Not(False),u[29]==u[28]+1),y[29]==y[28]+1)),Not(Implies(And(Not(False),u[29]!=u[28]+1),y[29]<23)),Not(Implies(False,y[30]==0)),Not(Implies(And(Not(False),u[30]==u[29]+1),y[30]==y[29]+1)),Not(Implies(And(Not(False),u[30]!=u[29]+1),y[30]<23)),Not(Implies(False,y[31]==0)),Not(Implies(And(Not(False),u[31]==u[30]+1),y[31]==y[30]+1)),Not(Implies(And(Not(False),u[31]!=u[30]+1),y[31]<23)),Not(Implies(False,y[32]==0)),Not(Implies(And(Not(False),u[32]==u[31]+1),y[32]==y[31]+1)),Not(Implies(And(Not(False),u[32]!=u[31]+1),y[32]<23)),Not(Implies(False,y[33]==0)),Not(Implies(And(Not(False),u[33]==u[32]+1),y[33]==y[32]+1)),Not(Implies(And(Not(False),u[33]!=u[32]+1),y[33]<23)),Not(Implies(False,y[34]==0)),Not(Implies(And(Not(False),u[34]==u[33]+1),y[34]==y[33]+1)),Not(Implies(And(Not(False),u[34]!=u[33]+1),y[34]<23)),Not(Implies(False,y[35]==0)),Not(Implies(And(Not(False),u[35]==u[34]+1),y[35]==y[34]+1)),Not(Implies(And(Not(False),u[35]!=u[34]+1),y[35]<23)),Not(Implies(False,y[36]==0)),Not(Implies(And(Not(False),u[36]==u[35]+1),y[36]==y[35]+1)),Not(Implies(And(Not(False),u[36]!=u[35]+1),y[36]<23)),Not(Implies(False,y[37]==0)),Not(Implies(And(Not(False),u[37]==u[36]+1),y[37]==y[36]+1)),Not(Implies(And(Not(False),u[37]!=u[36]+1),y[37]<23)),Not(Implies(False,y[38]==0)),Not(Implies(And(Not(False),u[38]==u[37]+1),y[38]==y[37]+1)),Not(Implies(And(Not(False),u[38]!=u[37]+1),y[38]<23)),Not(Implies(False,y[39]==0)),Not(Implies(And(Not(False),u[39]==u[38]+1),y[39]==y[38]+1)),Not(Implies(And(Not(False),u[39]!=u[38]+1),y[39]<23)),Not(Implies(False,y[40]==0)),Not(Implies(And(Not(False),u[40]==u[39]+1),y[40]==y[39]+1)),Not(Implies(And(Not(False),u[40]!=u[39]+1),y[40]<23)),Not(Implies(False,y[41]==0)),Not(Implies(And(Not(False),u[41]==u[40]+1),y[41]==y[40]+1)),Not(Implies(And(Not(False),u[41]!=u[40]+1),y[41]<23)),Not(Implies(False,y[42]==0)),Not(Implies(And(Not(False),u[42]==u[41]+1),y[42]==y[41]+1)),Not(Implies(And(Not(False),u[42]!=u[41]+1),y[42]<23)),Not(Implies(False,y[43]==0)),Not(Implies(And(Not(False),u[43]==u[42]+1),y[43]==y[42]+1)),Not(Implies(And(Not(False),u[43]!=u[42]+1),y[43]<23)),Not(Implies(False,y[44]==0)),Not(Implies(And(Not(False),u[44]==u[43]+1),y[44]==y[43]+1)),Not(Implies(And(Not(False),u[44]!=u[43]+1),y[44]<23)),Not(Implies(False,y[45]==0)),Not(Implies(And(Not(False),u[45]==u[44]+1),y[45]==y[44]+1)),Not(Implies(And(Not(False),u[45]!=u[44]+1),y[45]<23)),Not(Implies(False,y[46]==0)),Not(Implies(And(Not(False),u[46]==u[45]+1),y[46]==y[45]+1)),Not(Implies(And(Not(False),u[46]!=u[45]+1),y[46]<23)),Not(Implies(False,y[47]==0)),Not(Implies(And(Not(False),u[47]==u[46]+1),y[47]==y[46]+1)),Not(Implies(And(Not(False),u[47]!=u[46]+1),y[47]<23)),Not(Implies(False,y[48]==0)),Not(Implies(And(Not(False),u[48]==u[47]+1),y[48]==y[47]+1)),Not(Implies(And(Not(False),u[48]!=u[47]+1),y[48]<23)),Not(Implies(False,y[49]==0)),Not(Implies(And(Not(False),u[49]==u[48]+1),y[49]==y[48]+1)),Not(Implies(And(Not(False),u[49]!=u[48]+1),y[49]<23)),Not(Implies(False,y[50]==0)),Not(Implies(And(Not(False),u[50]==u[49]+1),y[50]==y[49]+1)),Not(Implies(And(Not(False),u[50]!=u[49]+1),y[50]<23)),Not(Implies(False,y[51]==0)),Not(Implies(And(Not(False),u[51]==u[50]+1),y[51]==y[50]+1)),Not(Implies(And(Not(False),u[51]!=u[50]+1),y[51]<23)),Not(Implies(False,y[52]==0)),Not(Implies(And(Not(False),u[52]==u[51]+1),y[52]==y[51]+1)),Not(Implies(And(Not(False),u[52]!=u[51]+1),y[52]<23)),Not(Implies(False,y[53]==0)),Not(Implies(And(Not(False),u[53]==u[52]+1),y[53]==y[52]+1)),Not(Implies(And(Not(False),u[53]!=u[52]+1),y[53]<23)),Not(Implies(False,y[54]==0)),Not(Implies(And(Not(False),u[54]==u[53]+1),y[54]==y[53]+1)),Not(Implies(And(Not(False),u[54]!=u[53]+1),y[54]<23)),Not(Implies(False,y[55]==0)),Not(Implies(And(Not(False),u[55]==u[54]+1),y[55]==y[54]+1)),Not(Implies(And(Not(False),u[55]!=u[54]+1),y[55]<23)),Not(Implies(False,y[56]==0)),Not(Implies(And(Not(False),u[56]==u[55]+1),y[56]==y[55]+1)),Not(Implies(And(Not(False),u[56]!=u[55]+1),y[56]<23)),Not(Implies(False,y[57]==0)),Not(Implies(And(Not(False),u[57]==u[56]+1),y[57]==y[56]+1)),Not(Implies(And(Not(False),u[57]!=u[56]+1),y[57]<23)),Not(Implies(False,y[58]==0)),Not(Implies(And(Not(False),u[58]==u[57]+1),y[58]==y[57]+1)),Not(Implies(And(Not(False),u[58]!=u[57]+1),y[58]<23)),Not(Implies(False,y[59]==0)),Not(Implies(And(Not(False),u[59]==u[58]+1),y[59]==y[58]+1)),Not(Implies(And(Not(False),u[59]!=u[58]+1),y[59]<23)),Not(Implies(False,y[60]==0)),Not(Implies(And(Not(False),u[60]==u[59]+1),y[60]==y[59]+1)),Not(Implies(And(Not(False),u[60]!=u[59]+1),y[60]<23)),Not(Implies(False,y[61]==0)),Not(Implies(And(Not(False),u[61]==u[60]+1),y[61]==y[60]+1)),Not(Implies(And(Not(False),u[61]!=u[60]+1),y[61]<23)),Not(Implies(False,y[62]==0)),Not(Implies(And(Not(False),u[62]==u[61]+1),y[62]==y[61]+1)),Not(Implies(And(Not(False),u[62]!=u[61]+1),y[62]<23)),Not(Implies(False,y[63]==0)),Not(Implies(And(Not(False),u[63]==u[62]+1),y[63]==y[62]+1)),Not(Implies(And(Not(False),u[63]!=u[62]+1),y[63]<23)),Not(Implies(False,y[64]==0)),Not(Implies(And(Not(False),u[64]==u[63]+1),y[64]==y[63]+1)),Not(Implies(And(Not(False),u[64]!=u[63]+1),y[64]<23)),Not(Implies(False,y[65]==0)),Not(Implies(And(Not(False),u[65]==u[64]+1),y[65]==y[64]+1)),Not(Implies(And(Not(False),u[65]!=u[64]+1),y[65]<23)),Not(Implies(False,y[66]==0)),Not(Implies(And(Not(False),u[66]==u[65]+1),y[66]==y[65]+1)),Not(Implies(And(Not(False),u[66]!=u[65]+1),y[66]<23)),Not(Implies(False,y[67]==0)),Not(Implies(And(Not(False),u[67]==u[66]+1),y[67]==y[66]+1)),Not(Implies(And(Not(False),u[67]!=u[66]+1),y[67]<23)),Not(Implies(False,y[68]==0)),Not(Implies(And(Not(False),u[68]==u[67]+1),y[68]==y[67]+1)),Not(Implies(And(Not(False),u[68]!=u[67]+1),y[68]<23)),Not(Implies(False,y[69]==0)),Not(Implies(And(Not(False),u[69]==u[68]+1),y[69]==y[68]+1)),Not(Implies(And(Not(False),u[69]!=u[68]+1),y[69]<23)),Not(Implies(False,y[70]==0)),Not(Implies(And(Not(False),u[70]==u[69]+1),y[70]==y[69]+1)),Not(Implies(And(Not(False),u[70]!=u[69]+1),y[70]<23)),Not(Implies(False,y[71]==0)),Not(Implies(And(Not(False),u[71]==u[70]+1),y[71]==y[70]+1)),Not(Implies(And(Not(False),u[71]!=u[70]+1),y[71]<23)),Not(Implies(False,y[72]==0)),Not(Implies(And(Not(False),u[72]==u[71]+1),y[72]==y[71]+1)),Not(Implies(And(Not(False),u[72]!=u[71]+1),y[72]<23)),Not(Implies(False,y[73]==0)),Not(Implies(And(Not(False),u[73]==u[72]+1),y[73]==y[72]+1)),Not(Implies(And(Not(False),u[73]!=u[72]+1),y[73]<23)),Not(Implies(False,y[74]==0)),Not(Implies(And(Not(False),u[74]==u[73]+1),y[74]==y[73]+1)),Not(Implies(And(Not(False),u[74]!=u[73]+1),y[74]<23)),Not(Implies(False,y[75]==0)),Not(Implies(And(Not(False),u[75]==u[74]+1),y[75]==y[74]+1)),Not(Implies(And(Not(False),u[75]!=u[74]+1),y[75]<23)),Not(Implies(False,y[76]==0)),Not(Implies(And(Not(False),u[76]==u[75]+1),y[76]==y[75]+1)),Not(Implies(And(Not(False),u[76]!=u[75]+1),y[76]<23)),Not(Implies(False,y[77]==0)),Not(Implies(And(Not(False),u[77]==u[76]+1),y[77]==y[76]+1)),Not(Implies(And(Not(False),u[77]!=u[76]+1),y[77]<23)),Not(Implies(False,y[78]==0)),Not(Implies(And(Not(False),u[78]==u[77]+1),y[78]==y[77]+1)),Not(Implies(And(Not(False),u[78]!=u[77]+1),y[78]<23)),Not(Implies(False,y[79]==0)),Not(Implies(And(Not(False),u[79]==u[78]+1),y[79]==y[78]+1)),Not(Implies(And(Not(False),u[79]!=u[78]+1),y[79]<23)),Not(Implies(False,y[80]==0)),Not(Implies(And(Not(False),u[80]==u[79]+1),y[80]==y[79]+1)),Not(Implies(And(Not(False),u[80]!=u[79]+1),y[80]<23)),Not(Implies(False,y[81]==0)),Not(Implies(And(Not(False),u[81]==u[80]+1),y[81]==y[80]+1)),Not(Implies(And(Not(False),u[81]!=u[80]+1),y[81]<23)),Not(Implies(False,y[82]==0)),Not(Implies(And(Not(False),u[82]==u[81]+1),y[82]==y[81]+1)),Not(Implies(And(Not(False),u[82]!=u[81]+1),y[82]<23)),Not(Implies(False,y[83]==0)),Not(Implies(And(Not(False),u[83]==u[82]+1),y[83]==y[82]+1)),Not(Implies(And(Not(False),u[83]!=u[82]+1),y[83]<23)),Not(Implies(False,y[84]==0)),Not(Implies(And(Not(False),u[84]==u[83]+1),y[84]==y[83]+1)),Not(Implies(And(Not(False),u[84]!=u[83]+1),y[84]<23)),Not(Implies(False,y[85]==0)),Not(Implies(And(Not(False),u[85]==u[84]+1),y[85]==y[84]+1)),Not(Implies(And(Not(False),u[85]!=u[84]+1),y[85]<23)),Not(Implies(False,y[86]==0)),Not(Implies(And(Not(False),u[86]==u[85]+1),y[86]==y[85]+1)),Not(Implies(And(Not(False),u[86]!=u[85]+1),y[86]<23)),Not(Implies(False,y[87]==0)),Not(Implies(And(Not(False),u[87]==u[86]+1),y[87]==y[86]+1)),Not(Implies(And(Not(False),u[87]!=u[86]+1),y[87]<23)),Not(Implies(False,y[88]==0)),Not(Implies(And(Not(False),u[88]==u[87]+1),y[88]==y[87]+1)),Not(Implies(And(Not(False),u[88]!=u[87]+1),y[88]<23)),Not(Implies(False,y[89]==0)),Not(Implies(And(Not(False),u[89]==u[88]+1),y[89]==y[88]+1)),Not(Implies(And(Not(False),u[89]!=u[88]+1),y[89]<23)),Not(Implies(False,y[90]==0)),Not(Implies(And(Not(False),u[90]==u[89]+1),y[90]==y[89]+1)),Not(Implies(And(Not(False),u[90]!=u[89]+1),y[90]<23)),Not(Implies(False,y[91]==0)),Not(Implies(And(Not(False),u[91]==u[90]+1),y[91]==y[90]+1)),Not(Implies(And(Not(False),u[91]!=u[90]+1),y[91]<23)),Not(Implies(False,y[92]==0)),Not(Implies(And(Not(False),u[92]==u[91]+1),y[92]==y[91]+1)),Not(Implies(And(Not(False),u[92]!=u[91]+1),y[92]<23)),Not(Implies(False,y[93]==0)),Not(Implies(And(Not(False),u[93]==u[92]+1),y[93]==y[92]+1)),Not(Implies(And(Not(False),u[93]!=u[92]+1),y[93]<23)),Not(Implies(False,y[94]==0)),Not(Implies(And(Not(False),u[94]==u[93]+1),y[94]==y[93]+1)),Not(Implies(And(Not(False),u[94]!=u[93]+1),y[94]<23)),Not(Implies(False,y[95]==0)),Not(Implies(And(Not(False),u[95]==u[94]+1),y[95]==y[94]+1)),Not(Implies(And(Not(False),u[95]!=u[94]+1),y[95]<23)),Not(Implies(False,y[96]==0)),Not(Implies(And(Not(False),u[96]==u[95]+1),y[96]==y[95]+1)),Not(Implies(And(Not(False),u[96]!=u[95]+1),y[96]<23)),Not(Implies(False,y[97]==0)),Not(Implies(And(Not(False),u[97]==u[96]+1),y[97]==y[96]+1)),Not(Implies(And(Not(False),u[97]!=u[96]+1),y[97]<23)),Not(Implies(False,y[98]==0)),Not(Implies(And(Not(False),u[98]==u[97]+1),y[98]==y[97]+1)),Not(Implies(And(Not(False),u[98]!=u[97]+1),y[98]<23)),Not(Implies(False,y[99]==0)),Not(Implies(And(Not(False),u[99]==u[98]+1),y[99]==y[98]+1)),Not(Implies(And(Not(False),u[99]!=u[98]+1),y[99]<23)),Not(Implies(False,y[100]==0)),Not(Implies(And(Not(False),u[100]==u[99]+1),y[100]==y[99]+1)),Not(Implies(And(Not(False),u[100]!=u[99]+1),y[100]<23)),Not(Implies(False,y[101]==0)),Not(Implies(And(Not(False),u[101]==u[100]+1),y[101]==y[100]+1)),Not(Implies(And(Not(False),u[101]!=u[100]+1),y[101]<23)),Not(Implies(False,y[102]==0)),Not(Implies(And(Not(False),u[102]==u[101]+1),y[102]==y[101]+1)),Not(Implies(And(Not(False),u[102]!=u[101]+1),y[102]<23)),Not(Implies(False,y[103]==0)),Not(Implies(And(Not(False),u[103]==u[102]+1),y[103]==y[102]+1)),Not(Implies(And(Not(False),u[103]!=u[102]+1),y[103]<23)),Not(Implies(False,y[104]==0)),Not(Implies(And(Not(False),u[104]==u[103]+1),y[104]==y[103]+1)),Not(Implies(And(Not(False),u[104]!=u[103]+1),y[104]<23)),Not(Implies(False,y[105]==0)),Not(Implies(And(Not(False),u[105]==u[104]+1),y[105]==y[104]+1)),Not(Implies(And(Not(False),u[105]!=u[104]+1),y[105]<23)),Not(Implies(False,y[106]==0)),Not(Implies(And(Not(False),u[106]==u[105]+1),y[106]==y[105]+1)),Not(Implies(And(Not(False),u[106]!=u[105]+1),y[106]<23)),Not(Implies(False,y[107]==0)),Not(Implies(And(Not(False),u[107]==u[106]+1),y[107]==y[106]+1)),Not(Implies(And(Not(False),u[107]!=u[106]+1),y[107]<23)),Not(Implies(False,y[108]==0)),Not(Implies(And(Not(False),u[108]==u[107]+1),y[108]==y[107]+1)),Not(Implies(And(Not(False),u[108]!=u[107]+1),y[108]<23)),Not(Implies(False,y[109]==0)),Not(Implies(And(Not(False),u[109]==u[108]+1),y[109]==y[108]+1)),Not(Implies(And(Not(False),u[109]!=u[108]+1),y[109]<23)),Not(Implies(False,y[110]==0)),Not(Implies(And(Not(False),u[110]==u[109]+1),y[110]==y[109]+1)),Not(Implies(And(Not(False),u[110]!=u[109]+1),y[110]<23)),Not(Implies(False,y[111]==0)),Not(Implies(And(Not(False),u[111]==u[110]+1),y[111]==y[110]+1)),Not(Implies(And(Not(False),u[111]!=u[110]+1),y[111]<23)),Not(Implies(False,y[112]==0)),Not(Implies(And(Not(False),u[112]==u[111]+1),y[112]==y[111]+1)),Not(Implies(And(Not(False),u[112]!=u[111]+1),y[112]<23)),Not(Implies(False,y[113]==0)),Not(Implies(And(Not(False),u[113]==u[112]+1),y[113]==y[112]+1)),Not(Implies(And(Not(False),u[113]!=u[112]+1),y[113]<23)),Not(Implies(False,y[114]==0)),Not(Implies(And(Not(False),u[114]==u[113]+1),y[114]==y[113]+1)),Not(Implies(And(Not(False),u[114]!=u[113]+1),y[114]<23)),Not(Implies(False,y[115]==0)),Not(Implies(And(Not(False),u[115]==u[114]+1),y[115]==y[114]+1)),Not(Implies(And(Not(False),u[115]!=u[114]+1),y[115]<23)),Not(Implies(False,y[116]==0)),Not(Implies(And(Not(False),u[116]==u[115]+1),y[116]==y[115]+1)),Not(Implies(And(Not(False),u[116]!=u[115]+1),y[116]<23)),Not(Implies(False,y[117]==0)),Not(Implies(And(Not(False),u[117]==u[116]+1),y[117]==y[116]+1)),Not(Implies(And(Not(False),u[117]!=u[116]+1),y[117]<23)),Not(Implies(False,y[118]==0)),Not(Implies(And(Not(False),u[118]==u[117]+1),y[118]==y[117]+1)),Not(Implies(And(Not(False),u[118]!=u[117]+1),y[118]<23)),Not(Implies(False,y[119]==0)),Not(Implies(And(Not(False),u[119]==u[118]+1),y[119]==y[118]+1)),Not(Implies(And(Not(False),u[119]!=u[118]+1),y[119]<23)),Not(Implies(False,y[120]==0)),Not(Implies(And(Not(False),u[120]==u[119]+1),y[120]==y[119]+1)),Not(Implies(And(Not(False),u[120]!=u[119]+1),y[120]<23)),Not(Implies(False,y[121]==0)),Not(Implies(And(Not(False),u[121]==u[120]+1),y[121]==y[120]+1)),Not(Implies(And(Not(False),u[121]!=u[120]+1),y[121]<23)),Not(Implies(False,y[122]==0)),Not(Implies(And(Not(False),u[122]==u[121]+1),y[122]==y[121]+1)),Not(Implies(And(Not(False),u[122]!=u[121]+1),y[122]<23)),Not(Implies(False,y[123]==0)),Not(Implies(And(Not(False),u[123]==u[122]+1),y[123]==y[122]+1)),Not(Implies(And(Not(False),u[123]!=u[122]+1),y[123]<23)),Not(Implies(False,y[124]==0)),Not(Implies(And(Not(False),u[124]==u[123]+1),y[124]==y[123]+1)),Not(Implies(And(Not(False),u[124]!=u[123]+1),y[124]<23)),Not(Implies(False,y[125]==0)),Not(Implies(And(Not(False),u[125]==u[124]+1),y[125]==y[124]+1)),Not(Implies(And(Not(False),u[125]!=u[124]+1),y[125]<23)),Not(Implies(False,y[126]==0)),Not(Implies(And(Not(False),u[126]==u[125]+1),y[126]==y[125]+1)),Not(Implies(And(Not(False),u[126]!=u[125]+1),y[126]<23)),Not(Implies(False,y[127]==0)),Not(Implies(And(Not(False),u[127]==u[126]+1),y[127]==y[126]+1)),Not(Implies(And(Not(False),u[127]!=u[126]+1),y[127]<23)),Not(Implies(False,y[128]==0)),Not(Implies(And(Not(False),u[128]==u[127]+1),y[128]==y[127]+1)),Not(Implies(And(Not(False),u[128]!=u[127]+1),y[128]<23)),Not(Implies(False,y[129]==0)),Not(Implies(And(Not(False),u[129]==u[128]+1),y[129]==y[128]+1)),Not(Implies(And(Not(False),u[129]!=u[128]+1),y[129]<23)),Not(Implies(False,y[130]==0)),Not(Implies(And(Not(False),u[130]==u[129]+1),y[130]==y[129]+1)),Not(Implies(And(Not(False),u[130]!=u[129]+1),y[130]<23)),Not(Implies(False,y[131]==0)),Not(Implies(And(Not(False),u[131]==u[130]+1),y[131]==y[130]+1)),Not(Implies(And(Not(False),u[131]!=u[130]+1),y[131]<23)),Not(Implies(False,y[132]==0)),Not(Implies(And(Not(False),u[132]==u[131]+1),y[132]==y[131]+1)),Not(Implies(And(Not(False),u[132]!=u[131]+1),y[132]<23)),Not(Implies(False,y[133]==0)),Not(Implies(And(Not(False),u[133]==u[132]+1),y[133]==y[132]+1)),Not(Implies(And(Not(False),u[133]!=u[132]+1),y[133]<23)),Not(Implies(False,y[134]==0)),Not(Implies(And(Not(False),u[134]==u[133]+1),y[134]==y[133]+1)),Not(Implies(And(Not(False),u[134]!=u[133]+1),y[134]<23)),Not(Implies(False,y[135]==0)),Not(Implies(And(Not(False),u[135]==u[134]+1),y[135]==y[134]+1)),Not(Implies(And(Not(False),u[135]!=u[134]+1),y[135]<23)),Not(Implies(False,y[136]==0)),Not(Implies(And(Not(False),u[136]==u[135]+1),y[136]==y[135]+1)),Not(Implies(And(Not(False),u[136]!=u[135]+1),y[136]<23)),Not(Implies(False,y[137]==0)),Not(Implies(And(Not(False),u[137]==u[136]+1),y[137]==y[136]+1)),Not(Implies(And(Not(False),u[137]!=u[136]+1),y[137]<23)),Not(Implies(False,y[138]==0)),Not(Implies(And(Not(False),u[138]==u[137]+1),y[138]==y[137]+1)),Not(Implies(And(Not(False),u[138]!=u[137]+1),y[138]<23)),Not(Implies(False,y[139]==0)),Not(Implies(And(Not(False),u[139]==u[138]+1),y[139]==y[138]+1)),Not(Implies(And(Not(False),u[139]!=u[138]+1),y[139]<23)),Not(Implies(False,y[140]==0)),Not(Implies(And(Not(False),u[140]==u[139]+1),y[140]==y[139]+1)),Not(Implies(And(Not(False),u[140]!=u[139]+1),y[140]<23)),Not(Implies(False,y[141]==0)),Not(Implies(And(Not(False),u[141]==u[140]+1),y[141]==y[140]+1)),Not(Implies(And(Not(False),u[141]!=u[140]+1),y[141]<23)),Not(Implies(False,y[142]==0)),Not(Implies(And(Not(False),u[142]==u[141]+1),y[142]==y[141]+1)),Not(Implies(And(Not(False),u[142]!=u[141]+1),y[142]<23)),Not(Implies(False,y[143]==0)),Not(Implies(And(Not(False),u[143]==u[142]+1),y[143]==y[142]+1)),Not(Implies(And(Not(False),u[143]!=u[142]+1),y[143]<23)),Not(Implies(False,y[144]==0)),Not(Implies(And(Not(False),u[144]==u[143]+1),y[144]==y[143]+1)),Not(Implies(And(Not(False),u[144]!=u[143]+1),y[144]<23)),Not(Implies(False,y[145]==0)),Not(Implies(And(Not(False),u[145]==u[144]+1),y[145]==y[144]+1)),Not(Implies(And(Not(False),u[145]!=u[144]+1),y[145]<23)),Not(Implies(False,y[146]==0)),Not(Implies(And(Not(False),u[146]==u[145]+1),y[146]==y[145]+1)),Not(Implies(And(Not(False),u[146]!=u[145]+1),y[146]<23)),Not(Implies(False,y[147]==0)),Not(Implies(And(Not(False),u[147]==u[146]+1),y[147]==y[146]+1)),Not(Implies(And(Not(False),u[147]!=u[146]+1),y[147]<23)),Not(Implies(False,y[148]==0)),Not(Implies(And(Not(False),u[148]==u[147]+1),y[148]==y[147]+1)),Not(Implies(And(Not(False),u[148]!=u[147]+1),y[148]<23)),Not(Implies(False,y[149]==0)),Not(Implies(And(Not(False),u[149]==u[148]+1),y[149]==y[148]+1)),Not(Implies(And(Not(False),u[149]!=u[148]+1),y[149]<23))))))
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
