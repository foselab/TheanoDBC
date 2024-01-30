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
s.add(And(tau[0]<tau[0 + 1],tau[1]<tau[1 + 1],tau[2]<tau[2 + 1],tau[3]<tau[3 + 1],tau[4]<tau[4 + 1],tau[5]<tau[5 + 1],tau[6]<tau[6 + 1],tau[7]<tau[7 + 1],tau[8]<tau[8 + 1],tau[9]<tau[9 + 1],tau[10]<tau[10 + 1],tau[11]<tau[11 + 1],tau[12]<tau[12 + 1],tau[13]<tau[13 + 1],tau[14]<tau[14 + 1],tau[15]<tau[15 + 1],tau[16]<tau[16 + 1],tau[17]<tau[17 + 1],tau[18]<tau[18 + 1],tau[19]<tau[19 + 1],tau[20]<tau[20 + 1],tau[21]<tau[21 + 1],tau[22]<tau[22 + 1],tau[23]<tau[23 + 1],tau[24]<tau[24 + 1],tau[25]<tau[25 + 1],tau[26]<tau[26 + 1],tau[27]<tau[27 + 1],tau[28]<tau[28 + 1],tau[29]<tau[29 + 1],tau[30]<tau[30 + 1],tau[31]<tau[31 + 1],tau[32]<tau[32 + 1],tau[33]<tau[33 + 1],tau[34]<tau[34 + 1],tau[35]<tau[35 + 1],tau[36]<tau[36 + 1],tau[37]<tau[37 + 1],tau[38]<tau[38 + 1],tau[39]<tau[39 + 1],tau[40]<tau[40 + 1],tau[41]<tau[41 + 1],tau[42]<tau[42 + 1],tau[43]<tau[43 + 1],tau[44]<tau[44 + 1],tau[45]<tau[45 + 1],tau[46]<tau[46 + 1],tau[47]<tau[47 + 1],tau[48]<tau[48 + 1],tau[49]<tau[49 + 1],tau[50]<tau[50 + 1],tau[51]<tau[51 + 1],tau[52]<tau[52 + 1],tau[53]<tau[53 + 1],tau[54]<tau[54 + 1],tau[55]<tau[55 + 1],tau[56]<tau[56 + 1],tau[57]<tau[57 + 1],tau[58]<tau[58 + 1],tau[59]<tau[59 + 1],tau[60]<tau[60 + 1],tau[61]<tau[61 + 1],tau[62]<tau[62 + 1],tau[63]<tau[63 + 1],tau[64]<tau[64 + 1],tau[65]<tau[65 + 1],tau[66]<tau[66 + 1],tau[67]<tau[67 + 1],tau[68]<tau[68 + 1],tau[69]<tau[69 + 1],tau[70]<tau[70 + 1],tau[71]<tau[71 + 1],tau[72]<tau[72 + 1],tau[73]<tau[73 + 1],tau[74]<tau[74 + 1],tau[75]<tau[75 + 1],tau[76]<tau[76 + 1],tau[77]<tau[77 + 1],tau[78]<tau[78 + 1],tau[79]<tau[79 + 1],tau[80]<tau[80 + 1],tau[81]<tau[81 + 1],tau[82]<tau[82 + 1],tau[83]<tau[83 + 1],tau[84]<tau[84 + 1],tau[85]<tau[85 + 1],tau[86]<tau[86 + 1],tau[87]<tau[87 + 1],tau[88]<tau[88 + 1],tau[89]<tau[89 + 1],tau[90]<tau[90 + 1],tau[91]<tau[91 + 1],tau[92]<tau[92 + 1],tau[93]<tau[93 + 1],tau[94]<tau[94 + 1],tau[95]<tau[95 + 1],tau[96]<tau[96 + 1],tau[97]<tau[97 + 1],tau[98]<tau[98 + 1],tau[99]<tau[99 + 1],tau[100]<tau[100 + 1],tau[101]<tau[101 + 1],tau[102]<tau[102 + 1],tau[103]<tau[103 + 1],tau[104]<tau[104 + 1],tau[105]<tau[105 + 1],tau[106]<tau[106 + 1],tau[107]<tau[107 + 1],tau[108]<tau[108 + 1],tau[109]<tau[109 + 1],tau[110]<tau[110 + 1],tau[111]<tau[111 + 1],tau[112]<tau[112 + 1],tau[113]<tau[113 + 1],tau[114]<tau[114 + 1],tau[115]<tau[115 + 1],tau[116]<tau[116 + 1],tau[117]<tau[117 + 1],tau[118]<tau[118 + 1],tau[119]<tau[119 + 1],tau[120]<tau[120 + 1],tau[121]<tau[121 + 1],tau[122]<tau[122 + 1],tau[123]<tau[123 + 1],tau[124]<tau[124 + 1],tau[125]<tau[125 + 1],tau[126]<tau[126 + 1],tau[127]<tau[127 + 1],tau[128]<tau[128 + 1],tau[129]<tau[129 + 1],tau[130]<tau[130 + 1],tau[131]<tau[131 + 1],tau[132]<tau[132 + 1],tau[133]<tau[133 + 1],tau[134]<tau[134 + 1],tau[135]<tau[135 + 1],tau[136]<tau[136 + 1],tau[137]<tau[137 + 1],tau[138]<tau[138 + 1],tau[139]<tau[139 + 1],tau[140]<tau[140 + 1],tau[141]<tau[141 + 1],tau[142]<tau[142 + 1],tau[143]<tau[143 + 1],tau[144]<tau[144 + 1],tau[145]<tau[145 + 1],tau[146]<tau[146 + 1],tau[147]<tau[147 + 1],tau[148]<tau[148 + 1],tau[149]<tau[149 + 1],tau[150]<tau[150 + 1],tau[151]<tau[151 + 1],tau[152]<tau[152 + 1],tau[153]<tau[153 + 1],tau[154]<tau[154 + 1],tau[155]<tau[155 + 1],tau[156]<tau[156 + 1],tau[157]<tau[157 + 1],tau[158]<tau[158 + 1],tau[159]<tau[159 + 1],tau[160]<tau[160 + 1],tau[161]<tau[161 + 1],tau[162]<tau[162 + 1],tau[163]<tau[163 + 1],tau[164]<tau[164 + 1],tau[165]<tau[165 + 1],tau[166]<tau[166 + 1],tau[167]<tau[167 + 1],tau[168]<tau[168 + 1],tau[169]<tau[169 + 1],tau[170]<tau[170 + 1],tau[171]<tau[171 + 1],tau[172]<tau[172 + 1],tau[173]<tau[173 + 1],tau[174]<tau[174 + 1],tau[175]<tau[175 + 1],tau[176]<tau[176 + 1],tau[177]<tau[177 + 1],tau[178]<tau[178 + 1],tau[179]<tau[179 + 1],tau[180]<tau[180 + 1],tau[181]<tau[181 + 1],tau[182]<tau[182 + 1],tau[183]<tau[183 + 1],tau[184]<tau[184 + 1],tau[185]<tau[185 + 1],tau[186]<tau[186 + 1],tau[187]<tau[187 + 1],tau[188]<tau[188 + 1],tau[189]<tau[189 + 1],tau[190]<tau[190 + 1],tau[191]<tau[191 + 1],tau[192]<tau[192 + 1],tau[193]<tau[193 + 1],tau[194]<tau[194 + 1],tau[195]<tau[195 + 1],tau[196]<tau[196 + 1],tau[197]<tau[197 + 1],tau[198]<tau[198 + 1],tau[199]<tau[199 + 1],tau[200]<tau[200 + 1],tau[201]<tau[201 + 1],tau[202]<tau[202 + 1],tau[203]<tau[203 + 1],tau[204]<tau[204 + 1],tau[205]<tau[205 + 1],tau[206]<tau[206 + 1],tau[207]<tau[207 + 1],tau[208]<tau[208 + 1],tau[209]<tau[209 + 1],tau[210]<tau[210 + 1],tau[211]<tau[211 + 1],tau[212]<tau[212 + 1],tau[213]<tau[213 + 1],tau[214]<tau[214 + 1],tau[215]<tau[215 + 1],tau[216]<tau[216 + 1],tau[217]<tau[217 + 1],tau[218]<tau[218 + 1],tau[219]<tau[219 + 1],tau[220]<tau[220 + 1],tau[221]<tau[221 + 1],tau[222]<tau[222 + 1],tau[223]<tau[223 + 1],tau[224]<tau[224 + 1],tau[225]<tau[225 + 1],tau[226]<tau[226 + 1],tau[227]<tau[227 + 1],tau[228]<tau[228 + 1],tau[229]<tau[229 + 1],tau[230]<tau[230 + 1],tau[231]<tau[231 + 1],tau[232]<tau[232 + 1],tau[233]<tau[233 + 1],tau[234]<tau[234 + 1],tau[235]<tau[235 + 1],tau[236]<tau[236 + 1],tau[237]<tau[237 + 1],tau[238]<tau[238 + 1],tau[239]<tau[239 + 1],tau[240]<tau[240 + 1],tau[241]<tau[241 + 1],tau[242]<tau[242 + 1],tau[243]<tau[243 + 1],tau[244]<tau[244 + 1],tau[245]<tau[245 + 1],tau[246]<tau[246 + 1],tau[247]<tau[247 + 1],tau[248]<tau[248 + 1],tau[249]<tau[249 + 1],tau[250]<tau[250 + 1],tau[251]<tau[251 + 1],tau[252]<tau[252 + 1],tau[253]<tau[253 + 1],tau[254]<tau[254 + 1],tau[255]<tau[255 + 1],tau[256]<tau[256 + 1],tau[257]<tau[257 + 1],tau[258]<tau[258 + 1],tau[259]<tau[259 + 1],tau[260]<tau[260 + 1],tau[261]<tau[261 + 1],tau[262]<tau[262 + 1],tau[263]<tau[263 + 1],tau[264]<tau[264 + 1],tau[265]<tau[265 + 1],tau[266]<tau[266 + 1],tau[267]<tau[267 + 1],tau[268]<tau[268 + 1],tau[269]<tau[269 + 1],tau[270]<tau[270 + 1],tau[271]<tau[271 + 1],tau[272]<tau[272 + 1],tau[273]<tau[273 + 1],tau[274]<tau[274 + 1],tau[275]<tau[275 + 1],tau[276]<tau[276 + 1],tau[277]<tau[277 + 1],tau[278]<tau[278 + 1],tau[279]<tau[279 + 1],tau[280]<tau[280 + 1],tau[281]<tau[281 + 1],tau[282]<tau[282 + 1],tau[283]<tau[283 + 1],tau[284]<tau[284 + 1],tau[285]<tau[285 + 1],tau[286]<tau[286 + 1],tau[287]<tau[287 + 1],tau[288]<tau[288 + 1],tau[289]<tau[289 + 1],tau[290]<tau[290 + 1],tau[291]<tau[291 + 1],tau[292]<tau[292 + 1],tau[293]<tau[293 + 1],tau[294]<tau[294 + 1],tau[295]<tau[295 + 1],tau[296]<tau[296 + 1],tau[297]<tau[297 + 1],tau[298]<tau[298 + 1],tau[299]<tau[299 + 1],tau[300]<tau[300 + 1],tau[301]<tau[301 + 1],tau[302]<tau[302 + 1],tau[303]<tau[303 + 1],tau[304]<tau[304 + 1],tau[305]<tau[305 + 1],tau[306]<tau[306 + 1],tau[307]<tau[307 + 1],tau[308]<tau[308 + 1],tau[309]<tau[309 + 1],tau[310]<tau[310 + 1],tau[311]<tau[311 + 1],tau[312]<tau[312 + 1],tau[313]<tau[313 + 1],tau[314]<tau[314 + 1],tau[315]<tau[315 + 1],tau[316]<tau[316 + 1],tau[317]<tau[317 + 1],tau[318]<tau[318 + 1],tau[319]<tau[319 + 1],tau[320]<tau[320 + 1],tau[321]<tau[321 + 1],tau[322]<tau[322 + 1],tau[323]<tau[323 + 1],tau[324]<tau[324 + 1],tau[325]<tau[325 + 1],tau[326]<tau[326 + 1],tau[327]<tau[327 + 1],tau[328]<tau[328 + 1],tau[329]<tau[329 + 1],tau[330]<tau[330 + 1],tau[331]<tau[331 + 1],tau[332]<tau[332 + 1],tau[333]<tau[333 + 1],tau[334]<tau[334 + 1],tau[335]<tau[335 + 1],tau[336]<tau[336 + 1],tau[337]<tau[337 + 1],tau[338]<tau[338 + 1],tau[339]<tau[339 + 1],tau[340]<tau[340 + 1],tau[341]<tau[341 + 1],tau[342]<tau[342 + 1],tau[343]<tau[343 + 1],tau[344]<tau[344 + 1],tau[345]<tau[345 + 1],tau[346]<tau[346 + 1],tau[347]<tau[347 + 1],tau[348]<tau[348 + 1]))
# Requirements Table
s.add(Or(And(Not(True),Not(And(Not(True),y[0]==250)),Not(Not(True))),And(Not(False),Not(And(Not(False),y[0]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[1]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[2]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[3]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[4]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[5]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[6]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[7]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[8]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[9]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[10]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[11]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[12]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[13]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[14]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[15]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[16]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[17]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[18]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[19]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[20]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[21]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[22]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[23]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[24]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[25]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[26]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[27]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[28]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[29]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[30]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[31]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[32]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[33]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[34]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[35]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[36]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[37]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[38]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[39]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[40]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[41]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[42]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[43]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[44]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[45]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[46]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[47]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[48]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[49]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[50]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[51]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[52]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[53]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[54]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[55]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[56]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[57]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[58]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[59]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[60]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[61]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[62]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[63]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[64]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[65]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[66]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[67]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[68]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[69]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[70]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[71]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[72]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[73]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[74]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[75]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[76]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[77]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[78]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[79]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[80]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[81]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[82]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[83]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[84]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[85]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[86]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[87]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[88]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[89]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[90]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[91]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[92]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[93]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[94]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[95]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[96]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[97]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[98]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[99]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[100]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[101]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[102]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[103]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[104]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[105]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[106]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[107]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[108]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[109]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[110]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[111]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[112]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[113]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[114]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[115]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[116]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[117]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[118]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[119]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[120]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[121]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[122]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[123]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[124]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[125]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[126]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[127]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[128]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[129]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[130]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[131]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[132]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[133]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[134]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[135]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[136]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[137]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[138]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[139]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[140]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[141]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[142]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[143]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[144]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[145]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[146]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[147]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[148]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[149]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[150]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[151]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[152]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[153]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[154]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[155]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[156]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[157]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[158]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[159]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[160]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[161]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[162]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[163]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[164]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[165]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[166]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[167]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[168]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[169]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[170]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[171]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[172]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[173]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[174]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[175]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[176]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[177]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[178]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[179]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[180]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[181]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[182]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[183]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[184]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[185]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[186]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[187]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[188]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[189]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[190]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[191]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[192]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[193]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[194]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[195]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[196]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[197]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[198]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[199]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[200]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[201]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[202]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[203]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[204]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[205]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[206]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[207]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[208]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[209]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[210]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[211]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[212]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[213]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[214]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[215]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[216]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[217]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[218]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[219]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[220]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[221]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[222]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[223]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[224]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[225]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[226]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[227]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[228]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[229]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[230]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[231]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[232]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[233]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[234]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[235]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[236]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[237]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[238]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[239]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[240]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[241]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[242]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[243]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[244]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[245]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[246]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[247]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[248]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[249]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[250]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[251]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[252]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[253]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[254]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[255]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[256]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[257]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[258]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[259]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[260]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[261]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[262]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[263]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[264]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[265]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[266]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[267]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[268]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[269]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[270]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[271]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[272]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[273]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[274]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[275]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[276]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[277]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[278]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[279]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[280]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[281]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[282]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[283]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[284]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[285]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[286]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[287]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[288]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[289]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[290]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[291]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[292]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[293]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[294]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[295]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[296]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[297]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[298]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[299]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[300]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[301]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[302]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[303]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[304]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[305]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[306]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[307]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[308]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[309]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[310]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[311]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[312]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[313]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[314]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[315]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[316]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[317]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[318]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[319]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[320]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[321]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[322]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[323]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[324]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[325]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[326]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[327]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[328]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[329]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[330]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[331]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[332]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[333]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[334]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[335]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[336]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[337]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[338]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[339]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[340]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[341]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[342]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[343]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[344]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[345]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[346]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[347]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[348]==250)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[349]==250)),Not(Not(False)))))
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