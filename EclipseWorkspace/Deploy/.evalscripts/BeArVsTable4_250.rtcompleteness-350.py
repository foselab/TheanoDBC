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
s.add(Or(And(Not(True),Not(And(Not(True),u[0]!=u[0]+1)),Not(And(Not(True),u[0]==u[0]+1))),And(Not(False),Not(And(Not(False),u[1]!=u[0]+1)),Not(And(Not(False),u[1]==u[0]+1))),And(Not(False),Not(And(Not(False),u[2]!=u[1]+1)),Not(And(Not(False),u[2]==u[1]+1))),And(Not(False),Not(And(Not(False),u[3]!=u[2]+1)),Not(And(Not(False),u[3]==u[2]+1))),And(Not(False),Not(And(Not(False),u[4]!=u[3]+1)),Not(And(Not(False),u[4]==u[3]+1))),And(Not(False),Not(And(Not(False),u[5]!=u[4]+1)),Not(And(Not(False),u[5]==u[4]+1))),And(Not(False),Not(And(Not(False),u[6]!=u[5]+1)),Not(And(Not(False),u[6]==u[5]+1))),And(Not(False),Not(And(Not(False),u[7]!=u[6]+1)),Not(And(Not(False),u[7]==u[6]+1))),And(Not(False),Not(And(Not(False),u[8]!=u[7]+1)),Not(And(Not(False),u[8]==u[7]+1))),And(Not(False),Not(And(Not(False),u[9]!=u[8]+1)),Not(And(Not(False),u[9]==u[8]+1))),And(Not(False),Not(And(Not(False),u[10]!=u[9]+1)),Not(And(Not(False),u[10]==u[9]+1))),And(Not(False),Not(And(Not(False),u[11]!=u[10]+1)),Not(And(Not(False),u[11]==u[10]+1))),And(Not(False),Not(And(Not(False),u[12]!=u[11]+1)),Not(And(Not(False),u[12]==u[11]+1))),And(Not(False),Not(And(Not(False),u[13]!=u[12]+1)),Not(And(Not(False),u[13]==u[12]+1))),And(Not(False),Not(And(Not(False),u[14]!=u[13]+1)),Not(And(Not(False),u[14]==u[13]+1))),And(Not(False),Not(And(Not(False),u[15]!=u[14]+1)),Not(And(Not(False),u[15]==u[14]+1))),And(Not(False),Not(And(Not(False),u[16]!=u[15]+1)),Not(And(Not(False),u[16]==u[15]+1))),And(Not(False),Not(And(Not(False),u[17]!=u[16]+1)),Not(And(Not(False),u[17]==u[16]+1))),And(Not(False),Not(And(Not(False),u[18]!=u[17]+1)),Not(And(Not(False),u[18]==u[17]+1))),And(Not(False),Not(And(Not(False),u[19]!=u[18]+1)),Not(And(Not(False),u[19]==u[18]+1))),And(Not(False),Not(And(Not(False),u[20]!=u[19]+1)),Not(And(Not(False),u[20]==u[19]+1))),And(Not(False),Not(And(Not(False),u[21]!=u[20]+1)),Not(And(Not(False),u[21]==u[20]+1))),And(Not(False),Not(And(Not(False),u[22]!=u[21]+1)),Not(And(Not(False),u[22]==u[21]+1))),And(Not(False),Not(And(Not(False),u[23]!=u[22]+1)),Not(And(Not(False),u[23]==u[22]+1))),And(Not(False),Not(And(Not(False),u[24]!=u[23]+1)),Not(And(Not(False),u[24]==u[23]+1))),And(Not(False),Not(And(Not(False),u[25]!=u[24]+1)),Not(And(Not(False),u[25]==u[24]+1))),And(Not(False),Not(And(Not(False),u[26]!=u[25]+1)),Not(And(Not(False),u[26]==u[25]+1))),And(Not(False),Not(And(Not(False),u[27]!=u[26]+1)),Not(And(Not(False),u[27]==u[26]+1))),And(Not(False),Not(And(Not(False),u[28]!=u[27]+1)),Not(And(Not(False),u[28]==u[27]+1))),And(Not(False),Not(And(Not(False),u[29]!=u[28]+1)),Not(And(Not(False),u[29]==u[28]+1))),And(Not(False),Not(And(Not(False),u[30]!=u[29]+1)),Not(And(Not(False),u[30]==u[29]+1))),And(Not(False),Not(And(Not(False),u[31]!=u[30]+1)),Not(And(Not(False),u[31]==u[30]+1))),And(Not(False),Not(And(Not(False),u[32]!=u[31]+1)),Not(And(Not(False),u[32]==u[31]+1))),And(Not(False),Not(And(Not(False),u[33]!=u[32]+1)),Not(And(Not(False),u[33]==u[32]+1))),And(Not(False),Not(And(Not(False),u[34]!=u[33]+1)),Not(And(Not(False),u[34]==u[33]+1))),And(Not(False),Not(And(Not(False),u[35]!=u[34]+1)),Not(And(Not(False),u[35]==u[34]+1))),And(Not(False),Not(And(Not(False),u[36]!=u[35]+1)),Not(And(Not(False),u[36]==u[35]+1))),And(Not(False),Not(And(Not(False),u[37]!=u[36]+1)),Not(And(Not(False),u[37]==u[36]+1))),And(Not(False),Not(And(Not(False),u[38]!=u[37]+1)),Not(And(Not(False),u[38]==u[37]+1))),And(Not(False),Not(And(Not(False),u[39]!=u[38]+1)),Not(And(Not(False),u[39]==u[38]+1))),And(Not(False),Not(And(Not(False),u[40]!=u[39]+1)),Not(And(Not(False),u[40]==u[39]+1))),And(Not(False),Not(And(Not(False),u[41]!=u[40]+1)),Not(And(Not(False),u[41]==u[40]+1))),And(Not(False),Not(And(Not(False),u[42]!=u[41]+1)),Not(And(Not(False),u[42]==u[41]+1))),And(Not(False),Not(And(Not(False),u[43]!=u[42]+1)),Not(And(Not(False),u[43]==u[42]+1))),And(Not(False),Not(And(Not(False),u[44]!=u[43]+1)),Not(And(Not(False),u[44]==u[43]+1))),And(Not(False),Not(And(Not(False),u[45]!=u[44]+1)),Not(And(Not(False),u[45]==u[44]+1))),And(Not(False),Not(And(Not(False),u[46]!=u[45]+1)),Not(And(Not(False),u[46]==u[45]+1))),And(Not(False),Not(And(Not(False),u[47]!=u[46]+1)),Not(And(Not(False),u[47]==u[46]+1))),And(Not(False),Not(And(Not(False),u[48]!=u[47]+1)),Not(And(Not(False),u[48]==u[47]+1))),And(Not(False),Not(And(Not(False),u[49]!=u[48]+1)),Not(And(Not(False),u[49]==u[48]+1))),And(Not(False),Not(And(Not(False),u[50]!=u[49]+1)),Not(And(Not(False),u[50]==u[49]+1))),And(Not(False),Not(And(Not(False),u[51]!=u[50]+1)),Not(And(Not(False),u[51]==u[50]+1))),And(Not(False),Not(And(Not(False),u[52]!=u[51]+1)),Not(And(Not(False),u[52]==u[51]+1))),And(Not(False),Not(And(Not(False),u[53]!=u[52]+1)),Not(And(Not(False),u[53]==u[52]+1))),And(Not(False),Not(And(Not(False),u[54]!=u[53]+1)),Not(And(Not(False),u[54]==u[53]+1))),And(Not(False),Not(And(Not(False),u[55]!=u[54]+1)),Not(And(Not(False),u[55]==u[54]+1))),And(Not(False),Not(And(Not(False),u[56]!=u[55]+1)),Not(And(Not(False),u[56]==u[55]+1))),And(Not(False),Not(And(Not(False),u[57]!=u[56]+1)),Not(And(Not(False),u[57]==u[56]+1))),And(Not(False),Not(And(Not(False),u[58]!=u[57]+1)),Not(And(Not(False),u[58]==u[57]+1))),And(Not(False),Not(And(Not(False),u[59]!=u[58]+1)),Not(And(Not(False),u[59]==u[58]+1))),And(Not(False),Not(And(Not(False),u[60]!=u[59]+1)),Not(And(Not(False),u[60]==u[59]+1))),And(Not(False),Not(And(Not(False),u[61]!=u[60]+1)),Not(And(Not(False),u[61]==u[60]+1))),And(Not(False),Not(And(Not(False),u[62]!=u[61]+1)),Not(And(Not(False),u[62]==u[61]+1))),And(Not(False),Not(And(Not(False),u[63]!=u[62]+1)),Not(And(Not(False),u[63]==u[62]+1))),And(Not(False),Not(And(Not(False),u[64]!=u[63]+1)),Not(And(Not(False),u[64]==u[63]+1))),And(Not(False),Not(And(Not(False),u[65]!=u[64]+1)),Not(And(Not(False),u[65]==u[64]+1))),And(Not(False),Not(And(Not(False),u[66]!=u[65]+1)),Not(And(Not(False),u[66]==u[65]+1))),And(Not(False),Not(And(Not(False),u[67]!=u[66]+1)),Not(And(Not(False),u[67]==u[66]+1))),And(Not(False),Not(And(Not(False),u[68]!=u[67]+1)),Not(And(Not(False),u[68]==u[67]+1))),And(Not(False),Not(And(Not(False),u[69]!=u[68]+1)),Not(And(Not(False),u[69]==u[68]+1))),And(Not(False),Not(And(Not(False),u[70]!=u[69]+1)),Not(And(Not(False),u[70]==u[69]+1))),And(Not(False),Not(And(Not(False),u[71]!=u[70]+1)),Not(And(Not(False),u[71]==u[70]+1))),And(Not(False),Not(And(Not(False),u[72]!=u[71]+1)),Not(And(Not(False),u[72]==u[71]+1))),And(Not(False),Not(And(Not(False),u[73]!=u[72]+1)),Not(And(Not(False),u[73]==u[72]+1))),And(Not(False),Not(And(Not(False),u[74]!=u[73]+1)),Not(And(Not(False),u[74]==u[73]+1))),And(Not(False),Not(And(Not(False),u[75]!=u[74]+1)),Not(And(Not(False),u[75]==u[74]+1))),And(Not(False),Not(And(Not(False),u[76]!=u[75]+1)),Not(And(Not(False),u[76]==u[75]+1))),And(Not(False),Not(And(Not(False),u[77]!=u[76]+1)),Not(And(Not(False),u[77]==u[76]+1))),And(Not(False),Not(And(Not(False),u[78]!=u[77]+1)),Not(And(Not(False),u[78]==u[77]+1))),And(Not(False),Not(And(Not(False),u[79]!=u[78]+1)),Not(And(Not(False),u[79]==u[78]+1))),And(Not(False),Not(And(Not(False),u[80]!=u[79]+1)),Not(And(Not(False),u[80]==u[79]+1))),And(Not(False),Not(And(Not(False),u[81]!=u[80]+1)),Not(And(Not(False),u[81]==u[80]+1))),And(Not(False),Not(And(Not(False),u[82]!=u[81]+1)),Not(And(Not(False),u[82]==u[81]+1))),And(Not(False),Not(And(Not(False),u[83]!=u[82]+1)),Not(And(Not(False),u[83]==u[82]+1))),And(Not(False),Not(And(Not(False),u[84]!=u[83]+1)),Not(And(Not(False),u[84]==u[83]+1))),And(Not(False),Not(And(Not(False),u[85]!=u[84]+1)),Not(And(Not(False),u[85]==u[84]+1))),And(Not(False),Not(And(Not(False),u[86]!=u[85]+1)),Not(And(Not(False),u[86]==u[85]+1))),And(Not(False),Not(And(Not(False),u[87]!=u[86]+1)),Not(And(Not(False),u[87]==u[86]+1))),And(Not(False),Not(And(Not(False),u[88]!=u[87]+1)),Not(And(Not(False),u[88]==u[87]+1))),And(Not(False),Not(And(Not(False),u[89]!=u[88]+1)),Not(And(Not(False),u[89]==u[88]+1))),And(Not(False),Not(And(Not(False),u[90]!=u[89]+1)),Not(And(Not(False),u[90]==u[89]+1))),And(Not(False),Not(And(Not(False),u[91]!=u[90]+1)),Not(And(Not(False),u[91]==u[90]+1))),And(Not(False),Not(And(Not(False),u[92]!=u[91]+1)),Not(And(Not(False),u[92]==u[91]+1))),And(Not(False),Not(And(Not(False),u[93]!=u[92]+1)),Not(And(Not(False),u[93]==u[92]+1))),And(Not(False),Not(And(Not(False),u[94]!=u[93]+1)),Not(And(Not(False),u[94]==u[93]+1))),And(Not(False),Not(And(Not(False),u[95]!=u[94]+1)),Not(And(Not(False),u[95]==u[94]+1))),And(Not(False),Not(And(Not(False),u[96]!=u[95]+1)),Not(And(Not(False),u[96]==u[95]+1))),And(Not(False),Not(And(Not(False),u[97]!=u[96]+1)),Not(And(Not(False),u[97]==u[96]+1))),And(Not(False),Not(And(Not(False),u[98]!=u[97]+1)),Not(And(Not(False),u[98]==u[97]+1))),And(Not(False),Not(And(Not(False),u[99]!=u[98]+1)),Not(And(Not(False),u[99]==u[98]+1))),And(Not(False),Not(And(Not(False),u[100]!=u[99]+1)),Not(And(Not(False),u[100]==u[99]+1))),And(Not(False),Not(And(Not(False),u[101]!=u[100]+1)),Not(And(Not(False),u[101]==u[100]+1))),And(Not(False),Not(And(Not(False),u[102]!=u[101]+1)),Not(And(Not(False),u[102]==u[101]+1))),And(Not(False),Not(And(Not(False),u[103]!=u[102]+1)),Not(And(Not(False),u[103]==u[102]+1))),And(Not(False),Not(And(Not(False),u[104]!=u[103]+1)),Not(And(Not(False),u[104]==u[103]+1))),And(Not(False),Not(And(Not(False),u[105]!=u[104]+1)),Not(And(Not(False),u[105]==u[104]+1))),And(Not(False),Not(And(Not(False),u[106]!=u[105]+1)),Not(And(Not(False),u[106]==u[105]+1))),And(Not(False),Not(And(Not(False),u[107]!=u[106]+1)),Not(And(Not(False),u[107]==u[106]+1))),And(Not(False),Not(And(Not(False),u[108]!=u[107]+1)),Not(And(Not(False),u[108]==u[107]+1))),And(Not(False),Not(And(Not(False),u[109]!=u[108]+1)),Not(And(Not(False),u[109]==u[108]+1))),And(Not(False),Not(And(Not(False),u[110]!=u[109]+1)),Not(And(Not(False),u[110]==u[109]+1))),And(Not(False),Not(And(Not(False),u[111]!=u[110]+1)),Not(And(Not(False),u[111]==u[110]+1))),And(Not(False),Not(And(Not(False),u[112]!=u[111]+1)),Not(And(Not(False),u[112]==u[111]+1))),And(Not(False),Not(And(Not(False),u[113]!=u[112]+1)),Not(And(Not(False),u[113]==u[112]+1))),And(Not(False),Not(And(Not(False),u[114]!=u[113]+1)),Not(And(Not(False),u[114]==u[113]+1))),And(Not(False),Not(And(Not(False),u[115]!=u[114]+1)),Not(And(Not(False),u[115]==u[114]+1))),And(Not(False),Not(And(Not(False),u[116]!=u[115]+1)),Not(And(Not(False),u[116]==u[115]+1))),And(Not(False),Not(And(Not(False),u[117]!=u[116]+1)),Not(And(Not(False),u[117]==u[116]+1))),And(Not(False),Not(And(Not(False),u[118]!=u[117]+1)),Not(And(Not(False),u[118]==u[117]+1))),And(Not(False),Not(And(Not(False),u[119]!=u[118]+1)),Not(And(Not(False),u[119]==u[118]+1))),And(Not(False),Not(And(Not(False),u[120]!=u[119]+1)),Not(And(Not(False),u[120]==u[119]+1))),And(Not(False),Not(And(Not(False),u[121]!=u[120]+1)),Not(And(Not(False),u[121]==u[120]+1))),And(Not(False),Not(And(Not(False),u[122]!=u[121]+1)),Not(And(Not(False),u[122]==u[121]+1))),And(Not(False),Not(And(Not(False),u[123]!=u[122]+1)),Not(And(Not(False),u[123]==u[122]+1))),And(Not(False),Not(And(Not(False),u[124]!=u[123]+1)),Not(And(Not(False),u[124]==u[123]+1))),And(Not(False),Not(And(Not(False),u[125]!=u[124]+1)),Not(And(Not(False),u[125]==u[124]+1))),And(Not(False),Not(And(Not(False),u[126]!=u[125]+1)),Not(And(Not(False),u[126]==u[125]+1))),And(Not(False),Not(And(Not(False),u[127]!=u[126]+1)),Not(And(Not(False),u[127]==u[126]+1))),And(Not(False),Not(And(Not(False),u[128]!=u[127]+1)),Not(And(Not(False),u[128]==u[127]+1))),And(Not(False),Not(And(Not(False),u[129]!=u[128]+1)),Not(And(Not(False),u[129]==u[128]+1))),And(Not(False),Not(And(Not(False),u[130]!=u[129]+1)),Not(And(Not(False),u[130]==u[129]+1))),And(Not(False),Not(And(Not(False),u[131]!=u[130]+1)),Not(And(Not(False),u[131]==u[130]+1))),And(Not(False),Not(And(Not(False),u[132]!=u[131]+1)),Not(And(Not(False),u[132]==u[131]+1))),And(Not(False),Not(And(Not(False),u[133]!=u[132]+1)),Not(And(Not(False),u[133]==u[132]+1))),And(Not(False),Not(And(Not(False),u[134]!=u[133]+1)),Not(And(Not(False),u[134]==u[133]+1))),And(Not(False),Not(And(Not(False),u[135]!=u[134]+1)),Not(And(Not(False),u[135]==u[134]+1))),And(Not(False),Not(And(Not(False),u[136]!=u[135]+1)),Not(And(Not(False),u[136]==u[135]+1))),And(Not(False),Not(And(Not(False),u[137]!=u[136]+1)),Not(And(Not(False),u[137]==u[136]+1))),And(Not(False),Not(And(Not(False),u[138]!=u[137]+1)),Not(And(Not(False),u[138]==u[137]+1))),And(Not(False),Not(And(Not(False),u[139]!=u[138]+1)),Not(And(Not(False),u[139]==u[138]+1))),And(Not(False),Not(And(Not(False),u[140]!=u[139]+1)),Not(And(Not(False),u[140]==u[139]+1))),And(Not(False),Not(And(Not(False),u[141]!=u[140]+1)),Not(And(Not(False),u[141]==u[140]+1))),And(Not(False),Not(And(Not(False),u[142]!=u[141]+1)),Not(And(Not(False),u[142]==u[141]+1))),And(Not(False),Not(And(Not(False),u[143]!=u[142]+1)),Not(And(Not(False),u[143]==u[142]+1))),And(Not(False),Not(And(Not(False),u[144]!=u[143]+1)),Not(And(Not(False),u[144]==u[143]+1))),And(Not(False),Not(And(Not(False),u[145]!=u[144]+1)),Not(And(Not(False),u[145]==u[144]+1))),And(Not(False),Not(And(Not(False),u[146]!=u[145]+1)),Not(And(Not(False),u[146]==u[145]+1))),And(Not(False),Not(And(Not(False),u[147]!=u[146]+1)),Not(And(Not(False),u[147]==u[146]+1))),And(Not(False),Not(And(Not(False),u[148]!=u[147]+1)),Not(And(Not(False),u[148]==u[147]+1))),And(Not(False),Not(And(Not(False),u[149]!=u[148]+1)),Not(And(Not(False),u[149]==u[148]+1))),And(Not(False),Not(And(Not(False),u[150]!=u[149]+1)),Not(And(Not(False),u[150]==u[149]+1))),And(Not(False),Not(And(Not(False),u[151]!=u[150]+1)),Not(And(Not(False),u[151]==u[150]+1))),And(Not(False),Not(And(Not(False),u[152]!=u[151]+1)),Not(And(Not(False),u[152]==u[151]+1))),And(Not(False),Not(And(Not(False),u[153]!=u[152]+1)),Not(And(Not(False),u[153]==u[152]+1))),And(Not(False),Not(And(Not(False),u[154]!=u[153]+1)),Not(And(Not(False),u[154]==u[153]+1))),And(Not(False),Not(And(Not(False),u[155]!=u[154]+1)),Not(And(Not(False),u[155]==u[154]+1))),And(Not(False),Not(And(Not(False),u[156]!=u[155]+1)),Not(And(Not(False),u[156]==u[155]+1))),And(Not(False),Not(And(Not(False),u[157]!=u[156]+1)),Not(And(Not(False),u[157]==u[156]+1))),And(Not(False),Not(And(Not(False),u[158]!=u[157]+1)),Not(And(Not(False),u[158]==u[157]+1))),And(Not(False),Not(And(Not(False),u[159]!=u[158]+1)),Not(And(Not(False),u[159]==u[158]+1))),And(Not(False),Not(And(Not(False),u[160]!=u[159]+1)),Not(And(Not(False),u[160]==u[159]+1))),And(Not(False),Not(And(Not(False),u[161]!=u[160]+1)),Not(And(Not(False),u[161]==u[160]+1))),And(Not(False),Not(And(Not(False),u[162]!=u[161]+1)),Not(And(Not(False),u[162]==u[161]+1))),And(Not(False),Not(And(Not(False),u[163]!=u[162]+1)),Not(And(Not(False),u[163]==u[162]+1))),And(Not(False),Not(And(Not(False),u[164]!=u[163]+1)),Not(And(Not(False),u[164]==u[163]+1))),And(Not(False),Not(And(Not(False),u[165]!=u[164]+1)),Not(And(Not(False),u[165]==u[164]+1))),And(Not(False),Not(And(Not(False),u[166]!=u[165]+1)),Not(And(Not(False),u[166]==u[165]+1))),And(Not(False),Not(And(Not(False),u[167]!=u[166]+1)),Not(And(Not(False),u[167]==u[166]+1))),And(Not(False),Not(And(Not(False),u[168]!=u[167]+1)),Not(And(Not(False),u[168]==u[167]+1))),And(Not(False),Not(And(Not(False),u[169]!=u[168]+1)),Not(And(Not(False),u[169]==u[168]+1))),And(Not(False),Not(And(Not(False),u[170]!=u[169]+1)),Not(And(Not(False),u[170]==u[169]+1))),And(Not(False),Not(And(Not(False),u[171]!=u[170]+1)),Not(And(Not(False),u[171]==u[170]+1))),And(Not(False),Not(And(Not(False),u[172]!=u[171]+1)),Not(And(Not(False),u[172]==u[171]+1))),And(Not(False),Not(And(Not(False),u[173]!=u[172]+1)),Not(And(Not(False),u[173]==u[172]+1))),And(Not(False),Not(And(Not(False),u[174]!=u[173]+1)),Not(And(Not(False),u[174]==u[173]+1))),And(Not(False),Not(And(Not(False),u[175]!=u[174]+1)),Not(And(Not(False),u[175]==u[174]+1))),And(Not(False),Not(And(Not(False),u[176]!=u[175]+1)),Not(And(Not(False),u[176]==u[175]+1))),And(Not(False),Not(And(Not(False),u[177]!=u[176]+1)),Not(And(Not(False),u[177]==u[176]+1))),And(Not(False),Not(And(Not(False),u[178]!=u[177]+1)),Not(And(Not(False),u[178]==u[177]+1))),And(Not(False),Not(And(Not(False),u[179]!=u[178]+1)),Not(And(Not(False),u[179]==u[178]+1))),And(Not(False),Not(And(Not(False),u[180]!=u[179]+1)),Not(And(Not(False),u[180]==u[179]+1))),And(Not(False),Not(And(Not(False),u[181]!=u[180]+1)),Not(And(Not(False),u[181]==u[180]+1))),And(Not(False),Not(And(Not(False),u[182]!=u[181]+1)),Not(And(Not(False),u[182]==u[181]+1))),And(Not(False),Not(And(Not(False),u[183]!=u[182]+1)),Not(And(Not(False),u[183]==u[182]+1))),And(Not(False),Not(And(Not(False),u[184]!=u[183]+1)),Not(And(Not(False),u[184]==u[183]+1))),And(Not(False),Not(And(Not(False),u[185]!=u[184]+1)),Not(And(Not(False),u[185]==u[184]+1))),And(Not(False),Not(And(Not(False),u[186]!=u[185]+1)),Not(And(Not(False),u[186]==u[185]+1))),And(Not(False),Not(And(Not(False),u[187]!=u[186]+1)),Not(And(Not(False),u[187]==u[186]+1))),And(Not(False),Not(And(Not(False),u[188]!=u[187]+1)),Not(And(Not(False),u[188]==u[187]+1))),And(Not(False),Not(And(Not(False),u[189]!=u[188]+1)),Not(And(Not(False),u[189]==u[188]+1))),And(Not(False),Not(And(Not(False),u[190]!=u[189]+1)),Not(And(Not(False),u[190]==u[189]+1))),And(Not(False),Not(And(Not(False),u[191]!=u[190]+1)),Not(And(Not(False),u[191]==u[190]+1))),And(Not(False),Not(And(Not(False),u[192]!=u[191]+1)),Not(And(Not(False),u[192]==u[191]+1))),And(Not(False),Not(And(Not(False),u[193]!=u[192]+1)),Not(And(Not(False),u[193]==u[192]+1))),And(Not(False),Not(And(Not(False),u[194]!=u[193]+1)),Not(And(Not(False),u[194]==u[193]+1))),And(Not(False),Not(And(Not(False),u[195]!=u[194]+1)),Not(And(Not(False),u[195]==u[194]+1))),And(Not(False),Not(And(Not(False),u[196]!=u[195]+1)),Not(And(Not(False),u[196]==u[195]+1))),And(Not(False),Not(And(Not(False),u[197]!=u[196]+1)),Not(And(Not(False),u[197]==u[196]+1))),And(Not(False),Not(And(Not(False),u[198]!=u[197]+1)),Not(And(Not(False),u[198]==u[197]+1))),And(Not(False),Not(And(Not(False),u[199]!=u[198]+1)),Not(And(Not(False),u[199]==u[198]+1))),And(Not(False),Not(And(Not(False),u[200]!=u[199]+1)),Not(And(Not(False),u[200]==u[199]+1))),And(Not(False),Not(And(Not(False),u[201]!=u[200]+1)),Not(And(Not(False),u[201]==u[200]+1))),And(Not(False),Not(And(Not(False),u[202]!=u[201]+1)),Not(And(Not(False),u[202]==u[201]+1))),And(Not(False),Not(And(Not(False),u[203]!=u[202]+1)),Not(And(Not(False),u[203]==u[202]+1))),And(Not(False),Not(And(Not(False),u[204]!=u[203]+1)),Not(And(Not(False),u[204]==u[203]+1))),And(Not(False),Not(And(Not(False),u[205]!=u[204]+1)),Not(And(Not(False),u[205]==u[204]+1))),And(Not(False),Not(And(Not(False),u[206]!=u[205]+1)),Not(And(Not(False),u[206]==u[205]+1))),And(Not(False),Not(And(Not(False),u[207]!=u[206]+1)),Not(And(Not(False),u[207]==u[206]+1))),And(Not(False),Not(And(Not(False),u[208]!=u[207]+1)),Not(And(Not(False),u[208]==u[207]+1))),And(Not(False),Not(And(Not(False),u[209]!=u[208]+1)),Not(And(Not(False),u[209]==u[208]+1))),And(Not(False),Not(And(Not(False),u[210]!=u[209]+1)),Not(And(Not(False),u[210]==u[209]+1))),And(Not(False),Not(And(Not(False),u[211]!=u[210]+1)),Not(And(Not(False),u[211]==u[210]+1))),And(Not(False),Not(And(Not(False),u[212]!=u[211]+1)),Not(And(Not(False),u[212]==u[211]+1))),And(Not(False),Not(And(Not(False),u[213]!=u[212]+1)),Not(And(Not(False),u[213]==u[212]+1))),And(Not(False),Not(And(Not(False),u[214]!=u[213]+1)),Not(And(Not(False),u[214]==u[213]+1))),And(Not(False),Not(And(Not(False),u[215]!=u[214]+1)),Not(And(Not(False),u[215]==u[214]+1))),And(Not(False),Not(And(Not(False),u[216]!=u[215]+1)),Not(And(Not(False),u[216]==u[215]+1))),And(Not(False),Not(And(Not(False),u[217]!=u[216]+1)),Not(And(Not(False),u[217]==u[216]+1))),And(Not(False),Not(And(Not(False),u[218]!=u[217]+1)),Not(And(Not(False),u[218]==u[217]+1))),And(Not(False),Not(And(Not(False),u[219]!=u[218]+1)),Not(And(Not(False),u[219]==u[218]+1))),And(Not(False),Not(And(Not(False),u[220]!=u[219]+1)),Not(And(Not(False),u[220]==u[219]+1))),And(Not(False),Not(And(Not(False),u[221]!=u[220]+1)),Not(And(Not(False),u[221]==u[220]+1))),And(Not(False),Not(And(Not(False),u[222]!=u[221]+1)),Not(And(Not(False),u[222]==u[221]+1))),And(Not(False),Not(And(Not(False),u[223]!=u[222]+1)),Not(And(Not(False),u[223]==u[222]+1))),And(Not(False),Not(And(Not(False),u[224]!=u[223]+1)),Not(And(Not(False),u[224]==u[223]+1))),And(Not(False),Not(And(Not(False),u[225]!=u[224]+1)),Not(And(Not(False),u[225]==u[224]+1))),And(Not(False),Not(And(Not(False),u[226]!=u[225]+1)),Not(And(Not(False),u[226]==u[225]+1))),And(Not(False),Not(And(Not(False),u[227]!=u[226]+1)),Not(And(Not(False),u[227]==u[226]+1))),And(Not(False),Not(And(Not(False),u[228]!=u[227]+1)),Not(And(Not(False),u[228]==u[227]+1))),And(Not(False),Not(And(Not(False),u[229]!=u[228]+1)),Not(And(Not(False),u[229]==u[228]+1))),And(Not(False),Not(And(Not(False),u[230]!=u[229]+1)),Not(And(Not(False),u[230]==u[229]+1))),And(Not(False),Not(And(Not(False),u[231]!=u[230]+1)),Not(And(Not(False),u[231]==u[230]+1))),And(Not(False),Not(And(Not(False),u[232]!=u[231]+1)),Not(And(Not(False),u[232]==u[231]+1))),And(Not(False),Not(And(Not(False),u[233]!=u[232]+1)),Not(And(Not(False),u[233]==u[232]+1))),And(Not(False),Not(And(Not(False),u[234]!=u[233]+1)),Not(And(Not(False),u[234]==u[233]+1))),And(Not(False),Not(And(Not(False),u[235]!=u[234]+1)),Not(And(Not(False),u[235]==u[234]+1))),And(Not(False),Not(And(Not(False),u[236]!=u[235]+1)),Not(And(Not(False),u[236]==u[235]+1))),And(Not(False),Not(And(Not(False),u[237]!=u[236]+1)),Not(And(Not(False),u[237]==u[236]+1))),And(Not(False),Not(And(Not(False),u[238]!=u[237]+1)),Not(And(Not(False),u[238]==u[237]+1))),And(Not(False),Not(And(Not(False),u[239]!=u[238]+1)),Not(And(Not(False),u[239]==u[238]+1))),And(Not(False),Not(And(Not(False),u[240]!=u[239]+1)),Not(And(Not(False),u[240]==u[239]+1))),And(Not(False),Not(And(Not(False),u[241]!=u[240]+1)),Not(And(Not(False),u[241]==u[240]+1))),And(Not(False),Not(And(Not(False),u[242]!=u[241]+1)),Not(And(Not(False),u[242]==u[241]+1))),And(Not(False),Not(And(Not(False),u[243]!=u[242]+1)),Not(And(Not(False),u[243]==u[242]+1))),And(Not(False),Not(And(Not(False),u[244]!=u[243]+1)),Not(And(Not(False),u[244]==u[243]+1))),And(Not(False),Not(And(Not(False),u[245]!=u[244]+1)),Not(And(Not(False),u[245]==u[244]+1))),And(Not(False),Not(And(Not(False),u[246]!=u[245]+1)),Not(And(Not(False),u[246]==u[245]+1))),And(Not(False),Not(And(Not(False),u[247]!=u[246]+1)),Not(And(Not(False),u[247]==u[246]+1))),And(Not(False),Not(And(Not(False),u[248]!=u[247]+1)),Not(And(Not(False),u[248]==u[247]+1))),And(Not(False),Not(And(Not(False),u[249]!=u[248]+1)),Not(And(Not(False),u[249]==u[248]+1))),And(Not(False),Not(And(Not(False),u[250]!=u[249]+1)),Not(And(Not(False),u[250]==u[249]+1))),And(Not(False),Not(And(Not(False),u[251]!=u[250]+1)),Not(And(Not(False),u[251]==u[250]+1))),And(Not(False),Not(And(Not(False),u[252]!=u[251]+1)),Not(And(Not(False),u[252]==u[251]+1))),And(Not(False),Not(And(Not(False),u[253]!=u[252]+1)),Not(And(Not(False),u[253]==u[252]+1))),And(Not(False),Not(And(Not(False),u[254]!=u[253]+1)),Not(And(Not(False),u[254]==u[253]+1))),And(Not(False),Not(And(Not(False),u[255]!=u[254]+1)),Not(And(Not(False),u[255]==u[254]+1))),And(Not(False),Not(And(Not(False),u[256]!=u[255]+1)),Not(And(Not(False),u[256]==u[255]+1))),And(Not(False),Not(And(Not(False),u[257]!=u[256]+1)),Not(And(Not(False),u[257]==u[256]+1))),And(Not(False),Not(And(Not(False),u[258]!=u[257]+1)),Not(And(Not(False),u[258]==u[257]+1))),And(Not(False),Not(And(Not(False),u[259]!=u[258]+1)),Not(And(Not(False),u[259]==u[258]+1))),And(Not(False),Not(And(Not(False),u[260]!=u[259]+1)),Not(And(Not(False),u[260]==u[259]+1))),And(Not(False),Not(And(Not(False),u[261]!=u[260]+1)),Not(And(Not(False),u[261]==u[260]+1))),And(Not(False),Not(And(Not(False),u[262]!=u[261]+1)),Not(And(Not(False),u[262]==u[261]+1))),And(Not(False),Not(And(Not(False),u[263]!=u[262]+1)),Not(And(Not(False),u[263]==u[262]+1))),And(Not(False),Not(And(Not(False),u[264]!=u[263]+1)),Not(And(Not(False),u[264]==u[263]+1))),And(Not(False),Not(And(Not(False),u[265]!=u[264]+1)),Not(And(Not(False),u[265]==u[264]+1))),And(Not(False),Not(And(Not(False),u[266]!=u[265]+1)),Not(And(Not(False),u[266]==u[265]+1))),And(Not(False),Not(And(Not(False),u[267]!=u[266]+1)),Not(And(Not(False),u[267]==u[266]+1))),And(Not(False),Not(And(Not(False),u[268]!=u[267]+1)),Not(And(Not(False),u[268]==u[267]+1))),And(Not(False),Not(And(Not(False),u[269]!=u[268]+1)),Not(And(Not(False),u[269]==u[268]+1))),And(Not(False),Not(And(Not(False),u[270]!=u[269]+1)),Not(And(Not(False),u[270]==u[269]+1))),And(Not(False),Not(And(Not(False),u[271]!=u[270]+1)),Not(And(Not(False),u[271]==u[270]+1))),And(Not(False),Not(And(Not(False),u[272]!=u[271]+1)),Not(And(Not(False),u[272]==u[271]+1))),And(Not(False),Not(And(Not(False),u[273]!=u[272]+1)),Not(And(Not(False),u[273]==u[272]+1))),And(Not(False),Not(And(Not(False),u[274]!=u[273]+1)),Not(And(Not(False),u[274]==u[273]+1))),And(Not(False),Not(And(Not(False),u[275]!=u[274]+1)),Not(And(Not(False),u[275]==u[274]+1))),And(Not(False),Not(And(Not(False),u[276]!=u[275]+1)),Not(And(Not(False),u[276]==u[275]+1))),And(Not(False),Not(And(Not(False),u[277]!=u[276]+1)),Not(And(Not(False),u[277]==u[276]+1))),And(Not(False),Not(And(Not(False),u[278]!=u[277]+1)),Not(And(Not(False),u[278]==u[277]+1))),And(Not(False),Not(And(Not(False),u[279]!=u[278]+1)),Not(And(Not(False),u[279]==u[278]+1))),And(Not(False),Not(And(Not(False),u[280]!=u[279]+1)),Not(And(Not(False),u[280]==u[279]+1))),And(Not(False),Not(And(Not(False),u[281]!=u[280]+1)),Not(And(Not(False),u[281]==u[280]+1))),And(Not(False),Not(And(Not(False),u[282]!=u[281]+1)),Not(And(Not(False),u[282]==u[281]+1))),And(Not(False),Not(And(Not(False),u[283]!=u[282]+1)),Not(And(Not(False),u[283]==u[282]+1))),And(Not(False),Not(And(Not(False),u[284]!=u[283]+1)),Not(And(Not(False),u[284]==u[283]+1))),And(Not(False),Not(And(Not(False),u[285]!=u[284]+1)),Not(And(Not(False),u[285]==u[284]+1))),And(Not(False),Not(And(Not(False),u[286]!=u[285]+1)),Not(And(Not(False),u[286]==u[285]+1))),And(Not(False),Not(And(Not(False),u[287]!=u[286]+1)),Not(And(Not(False),u[287]==u[286]+1))),And(Not(False),Not(And(Not(False),u[288]!=u[287]+1)),Not(And(Not(False),u[288]==u[287]+1))),And(Not(False),Not(And(Not(False),u[289]!=u[288]+1)),Not(And(Not(False),u[289]==u[288]+1))),And(Not(False),Not(And(Not(False),u[290]!=u[289]+1)),Not(And(Not(False),u[290]==u[289]+1))),And(Not(False),Not(And(Not(False),u[291]!=u[290]+1)),Not(And(Not(False),u[291]==u[290]+1))),And(Not(False),Not(And(Not(False),u[292]!=u[291]+1)),Not(And(Not(False),u[292]==u[291]+1))),And(Not(False),Not(And(Not(False),u[293]!=u[292]+1)),Not(And(Not(False),u[293]==u[292]+1))),And(Not(False),Not(And(Not(False),u[294]!=u[293]+1)),Not(And(Not(False),u[294]==u[293]+1))),And(Not(False),Not(And(Not(False),u[295]!=u[294]+1)),Not(And(Not(False),u[295]==u[294]+1))),And(Not(False),Not(And(Not(False),u[296]!=u[295]+1)),Not(And(Not(False),u[296]==u[295]+1))),And(Not(False),Not(And(Not(False),u[297]!=u[296]+1)),Not(And(Not(False),u[297]==u[296]+1))),And(Not(False),Not(And(Not(False),u[298]!=u[297]+1)),Not(And(Not(False),u[298]==u[297]+1))),And(Not(False),Not(And(Not(False),u[299]!=u[298]+1)),Not(And(Not(False),u[299]==u[298]+1))),And(Not(False),Not(And(Not(False),u[300]!=u[299]+1)),Not(And(Not(False),u[300]==u[299]+1))),And(Not(False),Not(And(Not(False),u[301]!=u[300]+1)),Not(And(Not(False),u[301]==u[300]+1))),And(Not(False),Not(And(Not(False),u[302]!=u[301]+1)),Not(And(Not(False),u[302]==u[301]+1))),And(Not(False),Not(And(Not(False),u[303]!=u[302]+1)),Not(And(Not(False),u[303]==u[302]+1))),And(Not(False),Not(And(Not(False),u[304]!=u[303]+1)),Not(And(Not(False),u[304]==u[303]+1))),And(Not(False),Not(And(Not(False),u[305]!=u[304]+1)),Not(And(Not(False),u[305]==u[304]+1))),And(Not(False),Not(And(Not(False),u[306]!=u[305]+1)),Not(And(Not(False),u[306]==u[305]+1))),And(Not(False),Not(And(Not(False),u[307]!=u[306]+1)),Not(And(Not(False),u[307]==u[306]+1))),And(Not(False),Not(And(Not(False),u[308]!=u[307]+1)),Not(And(Not(False),u[308]==u[307]+1))),And(Not(False),Not(And(Not(False),u[309]!=u[308]+1)),Not(And(Not(False),u[309]==u[308]+1))),And(Not(False),Not(And(Not(False),u[310]!=u[309]+1)),Not(And(Not(False),u[310]==u[309]+1))),And(Not(False),Not(And(Not(False),u[311]!=u[310]+1)),Not(And(Not(False),u[311]==u[310]+1))),And(Not(False),Not(And(Not(False),u[312]!=u[311]+1)),Not(And(Not(False),u[312]==u[311]+1))),And(Not(False),Not(And(Not(False),u[313]!=u[312]+1)),Not(And(Not(False),u[313]==u[312]+1))),And(Not(False),Not(And(Not(False),u[314]!=u[313]+1)),Not(And(Not(False),u[314]==u[313]+1))),And(Not(False),Not(And(Not(False),u[315]!=u[314]+1)),Not(And(Not(False),u[315]==u[314]+1))),And(Not(False),Not(And(Not(False),u[316]!=u[315]+1)),Not(And(Not(False),u[316]==u[315]+1))),And(Not(False),Not(And(Not(False),u[317]!=u[316]+1)),Not(And(Not(False),u[317]==u[316]+1))),And(Not(False),Not(And(Not(False),u[318]!=u[317]+1)),Not(And(Not(False),u[318]==u[317]+1))),And(Not(False),Not(And(Not(False),u[319]!=u[318]+1)),Not(And(Not(False),u[319]==u[318]+1))),And(Not(False),Not(And(Not(False),u[320]!=u[319]+1)),Not(And(Not(False),u[320]==u[319]+1))),And(Not(False),Not(And(Not(False),u[321]!=u[320]+1)),Not(And(Not(False),u[321]==u[320]+1))),And(Not(False),Not(And(Not(False),u[322]!=u[321]+1)),Not(And(Not(False),u[322]==u[321]+1))),And(Not(False),Not(And(Not(False),u[323]!=u[322]+1)),Not(And(Not(False),u[323]==u[322]+1))),And(Not(False),Not(And(Not(False),u[324]!=u[323]+1)),Not(And(Not(False),u[324]==u[323]+1))),And(Not(False),Not(And(Not(False),u[325]!=u[324]+1)),Not(And(Not(False),u[325]==u[324]+1))),And(Not(False),Not(And(Not(False),u[326]!=u[325]+1)),Not(And(Not(False),u[326]==u[325]+1))),And(Not(False),Not(And(Not(False),u[327]!=u[326]+1)),Not(And(Not(False),u[327]==u[326]+1))),And(Not(False),Not(And(Not(False),u[328]!=u[327]+1)),Not(And(Not(False),u[328]==u[327]+1))),And(Not(False),Not(And(Not(False),u[329]!=u[328]+1)),Not(And(Not(False),u[329]==u[328]+1))),And(Not(False),Not(And(Not(False),u[330]!=u[329]+1)),Not(And(Not(False),u[330]==u[329]+1))),And(Not(False),Not(And(Not(False),u[331]!=u[330]+1)),Not(And(Not(False),u[331]==u[330]+1))),And(Not(False),Not(And(Not(False),u[332]!=u[331]+1)),Not(And(Not(False),u[332]==u[331]+1))),And(Not(False),Not(And(Not(False),u[333]!=u[332]+1)),Not(And(Not(False),u[333]==u[332]+1))),And(Not(False),Not(And(Not(False),u[334]!=u[333]+1)),Not(And(Not(False),u[334]==u[333]+1))),And(Not(False),Not(And(Not(False),u[335]!=u[334]+1)),Not(And(Not(False),u[335]==u[334]+1))),And(Not(False),Not(And(Not(False),u[336]!=u[335]+1)),Not(And(Not(False),u[336]==u[335]+1))),And(Not(False),Not(And(Not(False),u[337]!=u[336]+1)),Not(And(Not(False),u[337]==u[336]+1))),And(Not(False),Not(And(Not(False),u[338]!=u[337]+1)),Not(And(Not(False),u[338]==u[337]+1))),And(Not(False),Not(And(Not(False),u[339]!=u[338]+1)),Not(And(Not(False),u[339]==u[338]+1))),And(Not(False),Not(And(Not(False),u[340]!=u[339]+1)),Not(And(Not(False),u[340]==u[339]+1))),And(Not(False),Not(And(Not(False),u[341]!=u[340]+1)),Not(And(Not(False),u[341]==u[340]+1))),And(Not(False),Not(And(Not(False),u[342]!=u[341]+1)),Not(And(Not(False),u[342]==u[341]+1))),And(Not(False),Not(And(Not(False),u[343]!=u[342]+1)),Not(And(Not(False),u[343]==u[342]+1))),And(Not(False),Not(And(Not(False),u[344]!=u[343]+1)),Not(And(Not(False),u[344]==u[343]+1))),And(Not(False),Not(And(Not(False),u[345]!=u[344]+1)),Not(And(Not(False),u[345]==u[344]+1))),And(Not(False),Not(And(Not(False),u[346]!=u[345]+1)),Not(And(Not(False),u[346]==u[345]+1))),And(Not(False),Not(And(Not(False),u[347]!=u[346]+1)),Not(And(Not(False),u[347]==u[346]+1))),And(Not(False),Not(And(Not(False),u[348]!=u[347]+1)),Not(And(Not(False),u[348]==u[347]+1))),And(Not(False),Not(And(Not(False),u[349]!=u[348]+1)),Not(And(Not(False),u[349]==u[348]+1))),And(Not(False),Not(And(Not(False),u[350]!=u[349]+1)),Not(And(Not(False),u[350]==u[349]+1)))))
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
