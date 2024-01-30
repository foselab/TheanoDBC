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
s.add(Or(And(Not(And(Not(True),u[0]>0)),Not(And(Not(True),y[0]==100)),Not(True)),And(Not(And(Not(False),u[1]>0)),Not(And(Not(False),y[0]==100)),Not(False)),And(Not(And(Not(False),u[2]>0)),Not(And(Not(False),y[1]==100)),Not(False)),And(Not(And(Not(False),u[3]>0)),Not(And(Not(False),y[2]==100)),Not(False)),And(Not(And(Not(False),u[4]>0)),Not(And(Not(False),y[3]==100)),Not(False)),And(Not(And(Not(False),u[5]>0)),Not(And(Not(False),y[4]==100)),Not(False)),And(Not(And(Not(False),u[6]>0)),Not(And(Not(False),y[5]==100)),Not(False)),And(Not(And(Not(False),u[7]>0)),Not(And(Not(False),y[6]==100)),Not(False)),And(Not(And(Not(False),u[8]>0)),Not(And(Not(False),y[7]==100)),Not(False)),And(Not(And(Not(False),u[9]>0)),Not(And(Not(False),y[8]==100)),Not(False)),And(Not(And(Not(False),u[10]>0)),Not(And(Not(False),y[9]==100)),Not(False)),And(Not(And(Not(False),u[11]>0)),Not(And(Not(False),y[10]==100)),Not(False)),And(Not(And(Not(False),u[12]>0)),Not(And(Not(False),y[11]==100)),Not(False)),And(Not(And(Not(False),u[13]>0)),Not(And(Not(False),y[12]==100)),Not(False)),And(Not(And(Not(False),u[14]>0)),Not(And(Not(False),y[13]==100)),Not(False)),And(Not(And(Not(False),u[15]>0)),Not(And(Not(False),y[14]==100)),Not(False)),And(Not(And(Not(False),u[16]>0)),Not(And(Not(False),y[15]==100)),Not(False)),And(Not(And(Not(False),u[17]>0)),Not(And(Not(False),y[16]==100)),Not(False)),And(Not(And(Not(False),u[18]>0)),Not(And(Not(False),y[17]==100)),Not(False)),And(Not(And(Not(False),u[19]>0)),Not(And(Not(False),y[18]==100)),Not(False)),And(Not(And(Not(False),u[20]>0)),Not(And(Not(False),y[19]==100)),Not(False)),And(Not(And(Not(False),u[21]>0)),Not(And(Not(False),y[20]==100)),Not(False)),And(Not(And(Not(False),u[22]>0)),Not(And(Not(False),y[21]==100)),Not(False)),And(Not(And(Not(False),u[23]>0)),Not(And(Not(False),y[22]==100)),Not(False)),And(Not(And(Not(False),u[24]>0)),Not(And(Not(False),y[23]==100)),Not(False)),And(Not(And(Not(False),u[25]>0)),Not(And(Not(False),y[24]==100)),Not(False)),And(Not(And(Not(False),u[26]>0)),Not(And(Not(False),y[25]==100)),Not(False)),And(Not(And(Not(False),u[27]>0)),Not(And(Not(False),y[26]==100)),Not(False)),And(Not(And(Not(False),u[28]>0)),Not(And(Not(False),y[27]==100)),Not(False)),And(Not(And(Not(False),u[29]>0)),Not(And(Not(False),y[28]==100)),Not(False)),And(Not(And(Not(False),u[30]>0)),Not(And(Not(False),y[29]==100)),Not(False)),And(Not(And(Not(False),u[31]>0)),Not(And(Not(False),y[30]==100)),Not(False)),And(Not(And(Not(False),u[32]>0)),Not(And(Not(False),y[31]==100)),Not(False)),And(Not(And(Not(False),u[33]>0)),Not(And(Not(False),y[32]==100)),Not(False)),And(Not(And(Not(False),u[34]>0)),Not(And(Not(False),y[33]==100)),Not(False)),And(Not(And(Not(False),u[35]>0)),Not(And(Not(False),y[34]==100)),Not(False)),And(Not(And(Not(False),u[36]>0)),Not(And(Not(False),y[35]==100)),Not(False)),And(Not(And(Not(False),u[37]>0)),Not(And(Not(False),y[36]==100)),Not(False)),And(Not(And(Not(False),u[38]>0)),Not(And(Not(False),y[37]==100)),Not(False)),And(Not(And(Not(False),u[39]>0)),Not(And(Not(False),y[38]==100)),Not(False)),And(Not(And(Not(False),u[40]>0)),Not(And(Not(False),y[39]==100)),Not(False)),And(Not(And(Not(False),u[41]>0)),Not(And(Not(False),y[40]==100)),Not(False)),And(Not(And(Not(False),u[42]>0)),Not(And(Not(False),y[41]==100)),Not(False)),And(Not(And(Not(False),u[43]>0)),Not(And(Not(False),y[42]==100)),Not(False)),And(Not(And(Not(False),u[44]>0)),Not(And(Not(False),y[43]==100)),Not(False)),And(Not(And(Not(False),u[45]>0)),Not(And(Not(False),y[44]==100)),Not(False)),And(Not(And(Not(False),u[46]>0)),Not(And(Not(False),y[45]==100)),Not(False)),And(Not(And(Not(False),u[47]>0)),Not(And(Not(False),y[46]==100)),Not(False)),And(Not(And(Not(False),u[48]>0)),Not(And(Not(False),y[47]==100)),Not(False)),And(Not(And(Not(False),u[49]>0)),Not(And(Not(False),y[48]==100)),Not(False)),And(Not(And(Not(False),u[50]>0)),Not(And(Not(False),y[49]==100)),Not(False)),And(Not(And(Not(False),u[51]>0)),Not(And(Not(False),y[50]==100)),Not(False)),And(Not(And(Not(False),u[52]>0)),Not(And(Not(False),y[51]==100)),Not(False)),And(Not(And(Not(False),u[53]>0)),Not(And(Not(False),y[52]==100)),Not(False)),And(Not(And(Not(False),u[54]>0)),Not(And(Not(False),y[53]==100)),Not(False)),And(Not(And(Not(False),u[55]>0)),Not(And(Not(False),y[54]==100)),Not(False)),And(Not(And(Not(False),u[56]>0)),Not(And(Not(False),y[55]==100)),Not(False)),And(Not(And(Not(False),u[57]>0)),Not(And(Not(False),y[56]==100)),Not(False)),And(Not(And(Not(False),u[58]>0)),Not(And(Not(False),y[57]==100)),Not(False)),And(Not(And(Not(False),u[59]>0)),Not(And(Not(False),y[58]==100)),Not(False)),And(Not(And(Not(False),u[60]>0)),Not(And(Not(False),y[59]==100)),Not(False)),And(Not(And(Not(False),u[61]>0)),Not(And(Not(False),y[60]==100)),Not(False)),And(Not(And(Not(False),u[62]>0)),Not(And(Not(False),y[61]==100)),Not(False)),And(Not(And(Not(False),u[63]>0)),Not(And(Not(False),y[62]==100)),Not(False)),And(Not(And(Not(False),u[64]>0)),Not(And(Not(False),y[63]==100)),Not(False)),And(Not(And(Not(False),u[65]>0)),Not(And(Not(False),y[64]==100)),Not(False)),And(Not(And(Not(False),u[66]>0)),Not(And(Not(False),y[65]==100)),Not(False)),And(Not(And(Not(False),u[67]>0)),Not(And(Not(False),y[66]==100)),Not(False)),And(Not(And(Not(False),u[68]>0)),Not(And(Not(False),y[67]==100)),Not(False)),And(Not(And(Not(False),u[69]>0)),Not(And(Not(False),y[68]==100)),Not(False)),And(Not(And(Not(False),u[70]>0)),Not(And(Not(False),y[69]==100)),Not(False)),And(Not(And(Not(False),u[71]>0)),Not(And(Not(False),y[70]==100)),Not(False)),And(Not(And(Not(False),u[72]>0)),Not(And(Not(False),y[71]==100)),Not(False)),And(Not(And(Not(False),u[73]>0)),Not(And(Not(False),y[72]==100)),Not(False)),And(Not(And(Not(False),u[74]>0)),Not(And(Not(False),y[73]==100)),Not(False)),And(Not(And(Not(False),u[75]>0)),Not(And(Not(False),y[74]==100)),Not(False)),And(Not(And(Not(False),u[76]>0)),Not(And(Not(False),y[75]==100)),Not(False)),And(Not(And(Not(False),u[77]>0)),Not(And(Not(False),y[76]==100)),Not(False)),And(Not(And(Not(False),u[78]>0)),Not(And(Not(False),y[77]==100)),Not(False)),And(Not(And(Not(False),u[79]>0)),Not(And(Not(False),y[78]==100)),Not(False)),And(Not(And(Not(False),u[80]>0)),Not(And(Not(False),y[79]==100)),Not(False)),And(Not(And(Not(False),u[81]>0)),Not(And(Not(False),y[80]==100)),Not(False)),And(Not(And(Not(False),u[82]>0)),Not(And(Not(False),y[81]==100)),Not(False)),And(Not(And(Not(False),u[83]>0)),Not(And(Not(False),y[82]==100)),Not(False)),And(Not(And(Not(False),u[84]>0)),Not(And(Not(False),y[83]==100)),Not(False)),And(Not(And(Not(False),u[85]>0)),Not(And(Not(False),y[84]==100)),Not(False)),And(Not(And(Not(False),u[86]>0)),Not(And(Not(False),y[85]==100)),Not(False)),And(Not(And(Not(False),u[87]>0)),Not(And(Not(False),y[86]==100)),Not(False)),And(Not(And(Not(False),u[88]>0)),Not(And(Not(False),y[87]==100)),Not(False)),And(Not(And(Not(False),u[89]>0)),Not(And(Not(False),y[88]==100)),Not(False)),And(Not(And(Not(False),u[90]>0)),Not(And(Not(False),y[89]==100)),Not(False)),And(Not(And(Not(False),u[91]>0)),Not(And(Not(False),y[90]==100)),Not(False)),And(Not(And(Not(False),u[92]>0)),Not(And(Not(False),y[91]==100)),Not(False)),And(Not(And(Not(False),u[93]>0)),Not(And(Not(False),y[92]==100)),Not(False)),And(Not(And(Not(False),u[94]>0)),Not(And(Not(False),y[93]==100)),Not(False)),And(Not(And(Not(False),u[95]>0)),Not(And(Not(False),y[94]==100)),Not(False)),And(Not(And(Not(False),u[96]>0)),Not(And(Not(False),y[95]==100)),Not(False)),And(Not(And(Not(False),u[97]>0)),Not(And(Not(False),y[96]==100)),Not(False)),And(Not(And(Not(False),u[98]>0)),Not(And(Not(False),y[97]==100)),Not(False)),And(Not(And(Not(False),u[99]>0)),Not(And(Not(False),y[98]==100)),Not(False)),And(Not(And(Not(False),u[100]>0)),Not(And(Not(False),y[99]==100)),Not(False)),And(Not(And(Not(False),u[101]>0)),Not(And(Not(False),y[100]==100)),Not(False)),And(Not(And(Not(False),u[102]>0)),Not(And(Not(False),y[101]==100)),Not(False)),And(Not(And(Not(False),u[103]>0)),Not(And(Not(False),y[102]==100)),Not(False)),And(Not(And(Not(False),u[104]>0)),Not(And(Not(False),y[103]==100)),Not(False)),And(Not(And(Not(False),u[105]>0)),Not(And(Not(False),y[104]==100)),Not(False)),And(Not(And(Not(False),u[106]>0)),Not(And(Not(False),y[105]==100)),Not(False)),And(Not(And(Not(False),u[107]>0)),Not(And(Not(False),y[106]==100)),Not(False)),And(Not(And(Not(False),u[108]>0)),Not(And(Not(False),y[107]==100)),Not(False)),And(Not(And(Not(False),u[109]>0)),Not(And(Not(False),y[108]==100)),Not(False)),And(Not(And(Not(False),u[110]>0)),Not(And(Not(False),y[109]==100)),Not(False)),And(Not(And(Not(False),u[111]>0)),Not(And(Not(False),y[110]==100)),Not(False)),And(Not(And(Not(False),u[112]>0)),Not(And(Not(False),y[111]==100)),Not(False)),And(Not(And(Not(False),u[113]>0)),Not(And(Not(False),y[112]==100)),Not(False)),And(Not(And(Not(False),u[114]>0)),Not(And(Not(False),y[113]==100)),Not(False)),And(Not(And(Not(False),u[115]>0)),Not(And(Not(False),y[114]==100)),Not(False)),And(Not(And(Not(False),u[116]>0)),Not(And(Not(False),y[115]==100)),Not(False)),And(Not(And(Not(False),u[117]>0)),Not(And(Not(False),y[116]==100)),Not(False)),And(Not(And(Not(False),u[118]>0)),Not(And(Not(False),y[117]==100)),Not(False)),And(Not(And(Not(False),u[119]>0)),Not(And(Not(False),y[118]==100)),Not(False)),And(Not(And(Not(False),u[120]>0)),Not(And(Not(False),y[119]==100)),Not(False)),And(Not(And(Not(False),u[121]>0)),Not(And(Not(False),y[120]==100)),Not(False)),And(Not(And(Not(False),u[122]>0)),Not(And(Not(False),y[121]==100)),Not(False)),And(Not(And(Not(False),u[123]>0)),Not(And(Not(False),y[122]==100)),Not(False)),And(Not(And(Not(False),u[124]>0)),Not(And(Not(False),y[123]==100)),Not(False)),And(Not(And(Not(False),u[125]>0)),Not(And(Not(False),y[124]==100)),Not(False)),And(Not(And(Not(False),u[126]>0)),Not(And(Not(False),y[125]==100)),Not(False)),And(Not(And(Not(False),u[127]>0)),Not(And(Not(False),y[126]==100)),Not(False)),And(Not(And(Not(False),u[128]>0)),Not(And(Not(False),y[127]==100)),Not(False)),And(Not(And(Not(False),u[129]>0)),Not(And(Not(False),y[128]==100)),Not(False)),And(Not(And(Not(False),u[130]>0)),Not(And(Not(False),y[129]==100)),Not(False)),And(Not(And(Not(False),u[131]>0)),Not(And(Not(False),y[130]==100)),Not(False)),And(Not(And(Not(False),u[132]>0)),Not(And(Not(False),y[131]==100)),Not(False)),And(Not(And(Not(False),u[133]>0)),Not(And(Not(False),y[132]==100)),Not(False)),And(Not(And(Not(False),u[134]>0)),Not(And(Not(False),y[133]==100)),Not(False)),And(Not(And(Not(False),u[135]>0)),Not(And(Not(False),y[134]==100)),Not(False)),And(Not(And(Not(False),u[136]>0)),Not(And(Not(False),y[135]==100)),Not(False)),And(Not(And(Not(False),u[137]>0)),Not(And(Not(False),y[136]==100)),Not(False)),And(Not(And(Not(False),u[138]>0)),Not(And(Not(False),y[137]==100)),Not(False)),And(Not(And(Not(False),u[139]>0)),Not(And(Not(False),y[138]==100)),Not(False)),And(Not(And(Not(False),u[140]>0)),Not(And(Not(False),y[139]==100)),Not(False)),And(Not(And(Not(False),u[141]>0)),Not(And(Not(False),y[140]==100)),Not(False)),And(Not(And(Not(False),u[142]>0)),Not(And(Not(False),y[141]==100)),Not(False)),And(Not(And(Not(False),u[143]>0)),Not(And(Not(False),y[142]==100)),Not(False)),And(Not(And(Not(False),u[144]>0)),Not(And(Not(False),y[143]==100)),Not(False)),And(Not(And(Not(False),u[145]>0)),Not(And(Not(False),y[144]==100)),Not(False)),And(Not(And(Not(False),u[146]>0)),Not(And(Not(False),y[145]==100)),Not(False)),And(Not(And(Not(False),u[147]>0)),Not(And(Not(False),y[146]==100)),Not(False)),And(Not(And(Not(False),u[148]>0)),Not(And(Not(False),y[147]==100)),Not(False)),And(Not(And(Not(False),u[149]>0)),Not(And(Not(False),y[148]==100)),Not(False)),And(Not(And(Not(False),u[150]>0)),Not(And(Not(False),y[149]==100)),Not(False)),And(Not(And(Not(False),u[151]>0)),Not(And(Not(False),y[150]==100)),Not(False)),And(Not(And(Not(False),u[152]>0)),Not(And(Not(False),y[151]==100)),Not(False)),And(Not(And(Not(False),u[153]>0)),Not(And(Not(False),y[152]==100)),Not(False)),And(Not(And(Not(False),u[154]>0)),Not(And(Not(False),y[153]==100)),Not(False)),And(Not(And(Not(False),u[155]>0)),Not(And(Not(False),y[154]==100)),Not(False)),And(Not(And(Not(False),u[156]>0)),Not(And(Not(False),y[155]==100)),Not(False)),And(Not(And(Not(False),u[157]>0)),Not(And(Not(False),y[156]==100)),Not(False)),And(Not(And(Not(False),u[158]>0)),Not(And(Not(False),y[157]==100)),Not(False)),And(Not(And(Not(False),u[159]>0)),Not(And(Not(False),y[158]==100)),Not(False)),And(Not(And(Not(False),u[160]>0)),Not(And(Not(False),y[159]==100)),Not(False)),And(Not(And(Not(False),u[161]>0)),Not(And(Not(False),y[160]==100)),Not(False)),And(Not(And(Not(False),u[162]>0)),Not(And(Not(False),y[161]==100)),Not(False)),And(Not(And(Not(False),u[163]>0)),Not(And(Not(False),y[162]==100)),Not(False)),And(Not(And(Not(False),u[164]>0)),Not(And(Not(False),y[163]==100)),Not(False)),And(Not(And(Not(False),u[165]>0)),Not(And(Not(False),y[164]==100)),Not(False)),And(Not(And(Not(False),u[166]>0)),Not(And(Not(False),y[165]==100)),Not(False)),And(Not(And(Not(False),u[167]>0)),Not(And(Not(False),y[166]==100)),Not(False)),And(Not(And(Not(False),u[168]>0)),Not(And(Not(False),y[167]==100)),Not(False)),And(Not(And(Not(False),u[169]>0)),Not(And(Not(False),y[168]==100)),Not(False)),And(Not(And(Not(False),u[170]>0)),Not(And(Not(False),y[169]==100)),Not(False)),And(Not(And(Not(False),u[171]>0)),Not(And(Not(False),y[170]==100)),Not(False)),And(Not(And(Not(False),u[172]>0)),Not(And(Not(False),y[171]==100)),Not(False)),And(Not(And(Not(False),u[173]>0)),Not(And(Not(False),y[172]==100)),Not(False)),And(Not(And(Not(False),u[174]>0)),Not(And(Not(False),y[173]==100)),Not(False)),And(Not(And(Not(False),u[175]>0)),Not(And(Not(False),y[174]==100)),Not(False)),And(Not(And(Not(False),u[176]>0)),Not(And(Not(False),y[175]==100)),Not(False)),And(Not(And(Not(False),u[177]>0)),Not(And(Not(False),y[176]==100)),Not(False)),And(Not(And(Not(False),u[178]>0)),Not(And(Not(False),y[177]==100)),Not(False)),And(Not(And(Not(False),u[179]>0)),Not(And(Not(False),y[178]==100)),Not(False)),And(Not(And(Not(False),u[180]>0)),Not(And(Not(False),y[179]==100)),Not(False)),And(Not(And(Not(False),u[181]>0)),Not(And(Not(False),y[180]==100)),Not(False)),And(Not(And(Not(False),u[182]>0)),Not(And(Not(False),y[181]==100)),Not(False)),And(Not(And(Not(False),u[183]>0)),Not(And(Not(False),y[182]==100)),Not(False)),And(Not(And(Not(False),u[184]>0)),Not(And(Not(False),y[183]==100)),Not(False)),And(Not(And(Not(False),u[185]>0)),Not(And(Not(False),y[184]==100)),Not(False)),And(Not(And(Not(False),u[186]>0)),Not(And(Not(False),y[185]==100)),Not(False)),And(Not(And(Not(False),u[187]>0)),Not(And(Not(False),y[186]==100)),Not(False)),And(Not(And(Not(False),u[188]>0)),Not(And(Not(False),y[187]==100)),Not(False)),And(Not(And(Not(False),u[189]>0)),Not(And(Not(False),y[188]==100)),Not(False)),And(Not(And(Not(False),u[190]>0)),Not(And(Not(False),y[189]==100)),Not(False)),And(Not(And(Not(False),u[191]>0)),Not(And(Not(False),y[190]==100)),Not(False)),And(Not(And(Not(False),u[192]>0)),Not(And(Not(False),y[191]==100)),Not(False)),And(Not(And(Not(False),u[193]>0)),Not(And(Not(False),y[192]==100)),Not(False)),And(Not(And(Not(False),u[194]>0)),Not(And(Not(False),y[193]==100)),Not(False)),And(Not(And(Not(False),u[195]>0)),Not(And(Not(False),y[194]==100)),Not(False)),And(Not(And(Not(False),u[196]>0)),Not(And(Not(False),y[195]==100)),Not(False)),And(Not(And(Not(False),u[197]>0)),Not(And(Not(False),y[196]==100)),Not(False)),And(Not(And(Not(False),u[198]>0)),Not(And(Not(False),y[197]==100)),Not(False)),And(Not(And(Not(False),u[199]>0)),Not(And(Not(False),y[198]==100)),Not(False)),And(Not(And(Not(False),u[200]>0)),Not(And(Not(False),y[199]==100)),Not(False))))
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
