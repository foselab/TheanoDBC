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
s.add(And(tau[0]<tau[0 + 1],tau[1]<tau[1 + 1],tau[2]<tau[2 + 1],tau[3]<tau[3 + 1],tau[4]<tau[4 + 1],tau[5]<tau[5 + 1],tau[6]<tau[6 + 1],tau[7]<tau[7 + 1],tau[8]<tau[8 + 1],tau[9]<tau[9 + 1],tau[10]<tau[10 + 1],tau[11]<tau[11 + 1],tau[12]<tau[12 + 1],tau[13]<tau[13 + 1],tau[14]<tau[14 + 1],tau[15]<tau[15 + 1],tau[16]<tau[16 + 1],tau[17]<tau[17 + 1],tau[18]<tau[18 + 1],tau[19]<tau[19 + 1],tau[20]<tau[20 + 1],tau[21]<tau[21 + 1],tau[22]<tau[22 + 1],tau[23]<tau[23 + 1],tau[24]<tau[24 + 1],tau[25]<tau[25 + 1],tau[26]<tau[26 + 1],tau[27]<tau[27 + 1],tau[28]<tau[28 + 1],tau[29]<tau[29 + 1],tau[30]<tau[30 + 1],tau[31]<tau[31 + 1],tau[32]<tau[32 + 1],tau[33]<tau[33 + 1],tau[34]<tau[34 + 1],tau[35]<tau[35 + 1],tau[36]<tau[36 + 1],tau[37]<tau[37 + 1],tau[38]<tau[38 + 1],tau[39]<tau[39 + 1],tau[40]<tau[40 + 1],tau[41]<tau[41 + 1],tau[42]<tau[42 + 1],tau[43]<tau[43 + 1],tau[44]<tau[44 + 1],tau[45]<tau[45 + 1],tau[46]<tau[46 + 1],tau[47]<tau[47 + 1],tau[48]<tau[48 + 1],tau[49]<tau[49 + 1],tau[50]<tau[50 + 1],tau[51]<tau[51 + 1],tau[52]<tau[52 + 1],tau[53]<tau[53 + 1],tau[54]<tau[54 + 1],tau[55]<tau[55 + 1],tau[56]<tau[56 + 1],tau[57]<tau[57 + 1],tau[58]<tau[58 + 1],tau[59]<tau[59 + 1],tau[60]<tau[60 + 1],tau[61]<tau[61 + 1],tau[62]<tau[62 + 1],tau[63]<tau[63 + 1],tau[64]<tau[64 + 1],tau[65]<tau[65 + 1],tau[66]<tau[66 + 1],tau[67]<tau[67 + 1],tau[68]<tau[68 + 1],tau[69]<tau[69 + 1],tau[70]<tau[70 + 1],tau[71]<tau[71 + 1],tau[72]<tau[72 + 1],tau[73]<tau[73 + 1],tau[74]<tau[74 + 1],tau[75]<tau[75 + 1],tau[76]<tau[76 + 1],tau[77]<tau[77 + 1],tau[78]<tau[78 + 1],tau[79]<tau[79 + 1],tau[80]<tau[80 + 1],tau[81]<tau[81 + 1],tau[82]<tau[82 + 1],tau[83]<tau[83 + 1],tau[84]<tau[84 + 1],tau[85]<tau[85 + 1],tau[86]<tau[86 + 1],tau[87]<tau[87 + 1],tau[88]<tau[88 + 1],tau[89]<tau[89 + 1],tau[90]<tau[90 + 1],tau[91]<tau[91 + 1],tau[92]<tau[92 + 1],tau[93]<tau[93 + 1],tau[94]<tau[94 + 1],tau[95]<tau[95 + 1],tau[96]<tau[96 + 1],tau[97]<tau[97 + 1],tau[98]<tau[98 + 1],tau[99]<tau[99 + 1],tau[100]<tau[100 + 1],tau[101]<tau[101 + 1],tau[102]<tau[102 + 1],tau[103]<tau[103 + 1],tau[104]<tau[104 + 1],tau[105]<tau[105 + 1],tau[106]<tau[106 + 1],tau[107]<tau[107 + 1],tau[108]<tau[108 + 1],tau[109]<tau[109 + 1],tau[110]<tau[110 + 1],tau[111]<tau[111 + 1],tau[112]<tau[112 + 1],tau[113]<tau[113 + 1],tau[114]<tau[114 + 1],tau[115]<tau[115 + 1],tau[116]<tau[116 + 1],tau[117]<tau[117 + 1],tau[118]<tau[118 + 1],tau[119]<tau[119 + 1],tau[120]<tau[120 + 1],tau[121]<tau[121 + 1],tau[122]<tau[122 + 1],tau[123]<tau[123 + 1],tau[124]<tau[124 + 1],tau[125]<tau[125 + 1],tau[126]<tau[126 + 1],tau[127]<tau[127 + 1],tau[128]<tau[128 + 1],tau[129]<tau[129 + 1],tau[130]<tau[130 + 1],tau[131]<tau[131 + 1],tau[132]<tau[132 + 1],tau[133]<tau[133 + 1],tau[134]<tau[134 + 1],tau[135]<tau[135 + 1],tau[136]<tau[136 + 1],tau[137]<tau[137 + 1],tau[138]<tau[138 + 1],tau[139]<tau[139 + 1],tau[140]<tau[140 + 1],tau[141]<tau[141 + 1],tau[142]<tau[142 + 1],tau[143]<tau[143 + 1],tau[144]<tau[144 + 1],tau[145]<tau[145 + 1],tau[146]<tau[146 + 1],tau[147]<tau[147 + 1],tau[148]<tau[148 + 1],tau[149]<tau[149 + 1],tau[150]<tau[150 + 1],tau[151]<tau[151 + 1],tau[152]<tau[152 + 1],tau[153]<tau[153 + 1],tau[154]<tau[154 + 1],tau[155]<tau[155 + 1],tau[156]<tau[156 + 1],tau[157]<tau[157 + 1],tau[158]<tau[158 + 1],tau[159]<tau[159 + 1],tau[160]<tau[160 + 1],tau[161]<tau[161 + 1],tau[162]<tau[162 + 1],tau[163]<tau[163 + 1],tau[164]<tau[164 + 1],tau[165]<tau[165 + 1],tau[166]<tau[166 + 1],tau[167]<tau[167 + 1],tau[168]<tau[168 + 1],tau[169]<tau[169 + 1],tau[170]<tau[170 + 1],tau[171]<tau[171 + 1],tau[172]<tau[172 + 1],tau[173]<tau[173 + 1],tau[174]<tau[174 + 1],tau[175]<tau[175 + 1],tau[176]<tau[176 + 1],tau[177]<tau[177 + 1],tau[178]<tau[178 + 1],tau[179]<tau[179 + 1],tau[180]<tau[180 + 1],tau[181]<tau[181 + 1],tau[182]<tau[182 + 1],tau[183]<tau[183 + 1],tau[184]<tau[184 + 1],tau[185]<tau[185 + 1],tau[186]<tau[186 + 1],tau[187]<tau[187 + 1],tau[188]<tau[188 + 1],tau[189]<tau[189 + 1],tau[190]<tau[190 + 1],tau[191]<tau[191 + 1],tau[192]<tau[192 + 1],tau[193]<tau[193 + 1],tau[194]<tau[194 + 1],tau[195]<tau[195 + 1],tau[196]<tau[196 + 1],tau[197]<tau[197 + 1],tau[198]<tau[198 + 1],tau[199]<tau[199 + 1],tau[200]<tau[200 + 1],tau[201]<tau[201 + 1],tau[202]<tau[202 + 1],tau[203]<tau[203 + 1],tau[204]<tau[204 + 1],tau[205]<tau[205 + 1],tau[206]<tau[206 + 1],tau[207]<tau[207 + 1],tau[208]<tau[208 + 1],tau[209]<tau[209 + 1],tau[210]<tau[210 + 1],tau[211]<tau[211 + 1],tau[212]<tau[212 + 1],tau[213]<tau[213 + 1],tau[214]<tau[214 + 1],tau[215]<tau[215 + 1],tau[216]<tau[216 + 1],tau[217]<tau[217 + 1],tau[218]<tau[218 + 1],tau[219]<tau[219 + 1],tau[220]<tau[220 + 1],tau[221]<tau[221 + 1],tau[222]<tau[222 + 1],tau[223]<tau[223 + 1],tau[224]<tau[224 + 1],tau[225]<tau[225 + 1],tau[226]<tau[226 + 1],tau[227]<tau[227 + 1],tau[228]<tau[228 + 1],tau[229]<tau[229 + 1],tau[230]<tau[230 + 1],tau[231]<tau[231 + 1],tau[232]<tau[232 + 1],tau[233]<tau[233 + 1],tau[234]<tau[234 + 1],tau[235]<tau[235 + 1],tau[236]<tau[236 + 1],tau[237]<tau[237 + 1],tau[238]<tau[238 + 1],tau[239]<tau[239 + 1],tau[240]<tau[240 + 1],tau[241]<tau[241 + 1],tau[242]<tau[242 + 1],tau[243]<tau[243 + 1],tau[244]<tau[244 + 1],tau[245]<tau[245 + 1],tau[246]<tau[246 + 1],tau[247]<tau[247 + 1],tau[248]<tau[248 + 1],tau[249]<tau[249 + 1],tau[250]<tau[250 + 1],tau[251]<tau[251 + 1],tau[252]<tau[252 + 1],tau[253]<tau[253 + 1],tau[254]<tau[254 + 1],tau[255]<tau[255 + 1],tau[256]<tau[256 + 1],tau[257]<tau[257 + 1],tau[258]<tau[258 + 1],tau[259]<tau[259 + 1],tau[260]<tau[260 + 1],tau[261]<tau[261 + 1],tau[262]<tau[262 + 1],tau[263]<tau[263 + 1],tau[264]<tau[264 + 1],tau[265]<tau[265 + 1],tau[266]<tau[266 + 1],tau[267]<tau[267 + 1],tau[268]<tau[268 + 1],tau[269]<tau[269 + 1],tau[270]<tau[270 + 1],tau[271]<tau[271 + 1],tau[272]<tau[272 + 1],tau[273]<tau[273 + 1],tau[274]<tau[274 + 1],tau[275]<tau[275 + 1],tau[276]<tau[276 + 1],tau[277]<tau[277 + 1],tau[278]<tau[278 + 1],tau[279]<tau[279 + 1],tau[280]<tau[280 + 1],tau[281]<tau[281 + 1],tau[282]<tau[282 + 1],tau[283]<tau[283 + 1],tau[284]<tau[284 + 1],tau[285]<tau[285 + 1],tau[286]<tau[286 + 1],tau[287]<tau[287 + 1],tau[288]<tau[288 + 1],tau[289]<tau[289 + 1],tau[290]<tau[290 + 1],tau[291]<tau[291 + 1],tau[292]<tau[292 + 1],tau[293]<tau[293 + 1],tau[294]<tau[294 + 1],tau[295]<tau[295 + 1],tau[296]<tau[296 + 1],tau[297]<tau[297 + 1],tau[298]<tau[298 + 1],tau[299]<tau[299 + 1],tau[300]<tau[300 + 1],tau[301]<tau[301 + 1],tau[302]<tau[302 + 1],tau[303]<tau[303 + 1],tau[304]<tau[304 + 1],tau[305]<tau[305 + 1],tau[306]<tau[306 + 1],tau[307]<tau[307 + 1],tau[308]<tau[308 + 1],tau[309]<tau[309 + 1],tau[310]<tau[310 + 1],tau[311]<tau[311 + 1],tau[312]<tau[312 + 1],tau[313]<tau[313 + 1],tau[314]<tau[314 + 1],tau[315]<tau[315 + 1],tau[316]<tau[316 + 1],tau[317]<tau[317 + 1],tau[318]<tau[318 + 1],tau[319]<tau[319 + 1],tau[320]<tau[320 + 1],tau[321]<tau[321 + 1],tau[322]<tau[322 + 1],tau[323]<tau[323 + 1],tau[324]<tau[324 + 1],tau[325]<tau[325 + 1],tau[326]<tau[326 + 1],tau[327]<tau[327 + 1],tau[328]<tau[328 + 1],tau[329]<tau[329 + 1],tau[330]<tau[330 + 1],tau[331]<tau[331 + 1],tau[332]<tau[332 + 1],tau[333]<tau[333 + 1],tau[334]<tau[334 + 1],tau[335]<tau[335 + 1],tau[336]<tau[336 + 1],tau[337]<tau[337 + 1],tau[338]<tau[338 + 1],tau[339]<tau[339 + 1],tau[340]<tau[340 + 1],tau[341]<tau[341 + 1],tau[342]<tau[342 + 1],tau[343]<tau[343 + 1],tau[344]<tau[344 + 1],tau[345]<tau[345 + 1],tau[346]<tau[346 + 1],tau[347]<tau[347 + 1],tau[348]<tau[348 + 1],tau[349]<tau[349 + 1],tau[350]<tau[350 + 1],tau[351]<tau[351 + 1],tau[352]<tau[352 + 1],tau[353]<tau[353 + 1],tau[354]<tau[354 + 1],tau[355]<tau[355 + 1],tau[356]<tau[356 + 1],tau[357]<tau[357 + 1],tau[358]<tau[358 + 1],tau[359]<tau[359 + 1],tau[360]<tau[360 + 1],tau[361]<tau[361 + 1],tau[362]<tau[362 + 1],tau[363]<tau[363 + 1],tau[364]<tau[364 + 1],tau[365]<tau[365 + 1],tau[366]<tau[366 + 1],tau[367]<tau[367 + 1],tau[368]<tau[368 + 1],tau[369]<tau[369 + 1],tau[370]<tau[370 + 1],tau[371]<tau[371 + 1],tau[372]<tau[372 + 1],tau[373]<tau[373 + 1],tau[374]<tau[374 + 1],tau[375]<tau[375 + 1],tau[376]<tau[376 + 1],tau[377]<tau[377 + 1],tau[378]<tau[378 + 1],tau[379]<tau[379 + 1],tau[380]<tau[380 + 1],tau[381]<tau[381 + 1],tau[382]<tau[382 + 1],tau[383]<tau[383 + 1],tau[384]<tau[384 + 1],tau[385]<tau[385 + 1],tau[386]<tau[386 + 1],tau[387]<tau[387 + 1],tau[388]<tau[388 + 1],tau[389]<tau[389 + 1],tau[390]<tau[390 + 1],tau[391]<tau[391 + 1],tau[392]<tau[392 + 1],tau[393]<tau[393 + 1],tau[394]<tau[394 + 1],tau[395]<tau[395 + 1],tau[396]<tau[396 + 1],tau[397]<tau[397 + 1],tau[398]<tau[398 + 1],tau[399]<tau[399 + 1],tau[400]<tau[400 + 1],tau[401]<tau[401 + 1],tau[402]<tau[402 + 1],tau[403]<tau[403 + 1],tau[404]<tau[404 + 1],tau[405]<tau[405 + 1],tau[406]<tau[406 + 1],tau[407]<tau[407 + 1],tau[408]<tau[408 + 1],tau[409]<tau[409 + 1],tau[410]<tau[410 + 1],tau[411]<tau[411 + 1],tau[412]<tau[412 + 1],tau[413]<tau[413 + 1],tau[414]<tau[414 + 1],tau[415]<tau[415 + 1],tau[416]<tau[416 + 1],tau[417]<tau[417 + 1],tau[418]<tau[418 + 1],tau[419]<tau[419 + 1],tau[420]<tau[420 + 1],tau[421]<tau[421 + 1],tau[422]<tau[422 + 1],tau[423]<tau[423 + 1],tau[424]<tau[424 + 1],tau[425]<tau[425 + 1],tau[426]<tau[426 + 1],tau[427]<tau[427 + 1],tau[428]<tau[428 + 1],tau[429]<tau[429 + 1],tau[430]<tau[430 + 1],tau[431]<tau[431 + 1],tau[432]<tau[432 + 1],tau[433]<tau[433 + 1],tau[434]<tau[434 + 1],tau[435]<tau[435 + 1],tau[436]<tau[436 + 1],tau[437]<tau[437 + 1],tau[438]<tau[438 + 1],tau[439]<tau[439 + 1],tau[440]<tau[440 + 1],tau[441]<tau[441 + 1],tau[442]<tau[442 + 1],tau[443]<tau[443 + 1],tau[444]<tau[444 + 1],tau[445]<tau[445 + 1],tau[446]<tau[446 + 1],tau[447]<tau[447 + 1],tau[448]<tau[448 + 1]))
# Requirements Table
s.add(Or(And(Not(True),Not(And(Not(True),y[0]==350)),Not(Not(True))),And(Not(False),Not(And(Not(False),y[0]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[1]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[2]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[3]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[4]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[5]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[6]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[7]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[8]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[9]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[10]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[11]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[12]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[13]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[14]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[15]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[16]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[17]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[18]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[19]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[20]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[21]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[22]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[23]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[24]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[25]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[26]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[27]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[28]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[29]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[30]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[31]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[32]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[33]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[34]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[35]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[36]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[37]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[38]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[39]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[40]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[41]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[42]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[43]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[44]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[45]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[46]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[47]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[48]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[49]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[50]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[51]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[52]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[53]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[54]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[55]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[56]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[57]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[58]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[59]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[60]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[61]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[62]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[63]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[64]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[65]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[66]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[67]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[68]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[69]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[70]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[71]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[72]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[73]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[74]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[75]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[76]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[77]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[78]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[79]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[80]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[81]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[82]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[83]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[84]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[85]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[86]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[87]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[88]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[89]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[90]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[91]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[92]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[93]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[94]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[95]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[96]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[97]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[98]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[99]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[100]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[101]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[102]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[103]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[104]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[105]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[106]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[107]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[108]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[109]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[110]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[111]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[112]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[113]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[114]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[115]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[116]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[117]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[118]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[119]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[120]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[121]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[122]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[123]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[124]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[125]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[126]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[127]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[128]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[129]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[130]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[131]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[132]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[133]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[134]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[135]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[136]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[137]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[138]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[139]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[140]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[141]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[142]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[143]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[144]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[145]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[146]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[147]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[148]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[149]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[150]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[151]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[152]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[153]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[154]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[155]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[156]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[157]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[158]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[159]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[160]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[161]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[162]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[163]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[164]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[165]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[166]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[167]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[168]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[169]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[170]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[171]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[172]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[173]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[174]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[175]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[176]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[177]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[178]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[179]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[180]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[181]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[182]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[183]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[184]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[185]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[186]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[187]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[188]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[189]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[190]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[191]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[192]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[193]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[194]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[195]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[196]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[197]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[198]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[199]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[200]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[201]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[202]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[203]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[204]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[205]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[206]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[207]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[208]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[209]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[210]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[211]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[212]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[213]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[214]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[215]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[216]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[217]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[218]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[219]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[220]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[221]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[222]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[223]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[224]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[225]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[226]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[227]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[228]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[229]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[230]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[231]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[232]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[233]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[234]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[235]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[236]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[237]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[238]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[239]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[240]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[241]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[242]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[243]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[244]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[245]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[246]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[247]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[248]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[249]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[250]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[251]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[252]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[253]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[254]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[255]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[256]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[257]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[258]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[259]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[260]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[261]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[262]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[263]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[264]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[265]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[266]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[267]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[268]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[269]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[270]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[271]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[272]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[273]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[274]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[275]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[276]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[277]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[278]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[279]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[280]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[281]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[282]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[283]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[284]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[285]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[286]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[287]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[288]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[289]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[290]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[291]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[292]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[293]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[294]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[295]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[296]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[297]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[298]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[299]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[300]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[301]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[302]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[303]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[304]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[305]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[306]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[307]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[308]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[309]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[310]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[311]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[312]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[313]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[314]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[315]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[316]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[317]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[318]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[319]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[320]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[321]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[322]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[323]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[324]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[325]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[326]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[327]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[328]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[329]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[330]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[331]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[332]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[333]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[334]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[335]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[336]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[337]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[338]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[339]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[340]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[341]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[342]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[343]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[344]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[345]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[346]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[347]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[348]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[349]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[350]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[351]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[352]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[353]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[354]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[355]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[356]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[357]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[358]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[359]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[360]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[361]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[362]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[363]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[364]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[365]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[366]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[367]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[368]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[369]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[370]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[371]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[372]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[373]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[374]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[375]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[376]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[377]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[378]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[379]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[380]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[381]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[382]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[383]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[384]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[385]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[386]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[387]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[388]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[389]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[390]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[391]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[392]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[393]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[394]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[395]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[396]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[397]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[398]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[399]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[400]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[401]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[402]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[403]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[404]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[405]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[406]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[407]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[408]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[409]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[410]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[411]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[412]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[413]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[414]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[415]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[416]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[417]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[418]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[419]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[420]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[421]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[422]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[423]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[424]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[425]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[426]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[427]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[428]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[429]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[430]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[431]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[432]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[433]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[434]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[435]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[436]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[437]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[438]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[439]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[440]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[441]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[442]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[443]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[444]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[445]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[446]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[447]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[448]==350)),Not(Not(False))),And(Not(False),Not(And(Not(False),y[449]==350)),Not(Not(False)))))
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
