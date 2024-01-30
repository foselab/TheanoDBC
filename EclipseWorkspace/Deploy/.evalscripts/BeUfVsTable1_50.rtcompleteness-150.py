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
tau = Function('tau', IntSort(), RealSort())
# Timestamp structure monotonicity
s.add(And(tau(0)<tau(0 + 1),tau(1)<tau(1 + 1),tau(2)<tau(2 + 1),tau(3)<tau(3 + 1),tau(4)<tau(4 + 1),tau(5)<tau(5 + 1),tau(6)<tau(6 + 1),tau(7)<tau(7 + 1),tau(8)<tau(8 + 1),tau(9)<tau(9 + 1),tau(10)<tau(10 + 1),tau(11)<tau(11 + 1),tau(12)<tau(12 + 1),tau(13)<tau(13 + 1),tau(14)<tau(14 + 1),tau(15)<tau(15 + 1),tau(16)<tau(16 + 1),tau(17)<tau(17 + 1),tau(18)<tau(18 + 1),tau(19)<tau(19 + 1),tau(20)<tau(20 + 1),tau(21)<tau(21 + 1),tau(22)<tau(22 + 1),tau(23)<tau(23 + 1),tau(24)<tau(24 + 1),tau(25)<tau(25 + 1),tau(26)<tau(26 + 1),tau(27)<tau(27 + 1),tau(28)<tau(28 + 1),tau(29)<tau(29 + 1),tau(30)<tau(30 + 1),tau(31)<tau(31 + 1),tau(32)<tau(32 + 1),tau(33)<tau(33 + 1),tau(34)<tau(34 + 1),tau(35)<tau(35 + 1),tau(36)<tau(36 + 1),tau(37)<tau(37 + 1),tau(38)<tau(38 + 1),tau(39)<tau(39 + 1),tau(40)<tau(40 + 1),tau(41)<tau(41 + 1),tau(42)<tau(42 + 1),tau(43)<tau(43 + 1),tau(44)<tau(44 + 1),tau(45)<tau(45 + 1),tau(46)<tau(46 + 1),tau(47)<tau(47 + 1),tau(48)<tau(48 + 1),tau(49)<tau(49 + 1),tau(50)<tau(50 + 1),tau(51)<tau(51 + 1),tau(52)<tau(52 + 1),tau(53)<tau(53 + 1),tau(54)<tau(54 + 1),tau(55)<tau(55 + 1),tau(56)<tau(56 + 1),tau(57)<tau(57 + 1),tau(58)<tau(58 + 1),tau(59)<tau(59 + 1),tau(60)<tau(60 + 1),tau(61)<tau(61 + 1),tau(62)<tau(62 + 1),tau(63)<tau(63 + 1),tau(64)<tau(64 + 1),tau(65)<tau(65 + 1),tau(66)<tau(66 + 1),tau(67)<tau(67 + 1),tau(68)<tau(68 + 1),tau(69)<tau(69 + 1),tau(70)<tau(70 + 1),tau(71)<tau(71 + 1),tau(72)<tau(72 + 1),tau(73)<tau(73 + 1),tau(74)<tau(74 + 1),tau(75)<tau(75 + 1),tau(76)<tau(76 + 1),tau(77)<tau(77 + 1),tau(78)<tau(78 + 1),tau(79)<tau(79 + 1),tau(80)<tau(80 + 1),tau(81)<tau(81 + 1),tau(82)<tau(82 + 1),tau(83)<tau(83 + 1),tau(84)<tau(84 + 1),tau(85)<tau(85 + 1),tau(86)<tau(86 + 1),tau(87)<tau(87 + 1),tau(88)<tau(88 + 1),tau(89)<tau(89 + 1),tau(90)<tau(90 + 1),tau(91)<tau(91 + 1),tau(92)<tau(92 + 1),tau(93)<tau(93 + 1),tau(94)<tau(94 + 1),tau(95)<tau(95 + 1),tau(96)<tau(96 + 1),tau(97)<tau(97 + 1),tau(98)<tau(98 + 1),tau(99)<tau(99 + 1),tau(100)<tau(100 + 1),tau(101)<tau(101 + 1),tau(102)<tau(102 + 1),tau(103)<tau(103 + 1),tau(104)<tau(104 + 1),tau(105)<tau(105 + 1),tau(106)<tau(106 + 1),tau(107)<tau(107 + 1),tau(108)<tau(108 + 1),tau(109)<tau(109 + 1),tau(110)<tau(110 + 1),tau(111)<tau(111 + 1),tau(112)<tau(112 + 1),tau(113)<tau(113 + 1),tau(114)<tau(114 + 1),tau(115)<tau(115 + 1),tau(116)<tau(116 + 1),tau(117)<tau(117 + 1),tau(118)<tau(118 + 1),tau(119)<tau(119 + 1),tau(120)<tau(120 + 1),tau(121)<tau(121 + 1),tau(122)<tau(122 + 1),tau(123)<tau(123 + 1),tau(124)<tau(124 + 1),tau(125)<tau(125 + 1),tau(126)<tau(126 + 1),tau(127)<tau(127 + 1),tau(128)<tau(128 + 1),tau(129)<tau(129 + 1),tau(130)<tau(130 + 1),tau(131)<tau(131 + 1),tau(132)<tau(132 + 1),tau(133)<tau(133 + 1),tau(134)<tau(134 + 1),tau(135)<tau(135 + 1),tau(136)<tau(136 + 1),tau(137)<tau(137 + 1),tau(138)<tau(138 + 1),tau(139)<tau(139 + 1),tau(140)<tau(140 + 1),tau(141)<tau(141 + 1),tau(142)<tau(142 + 1),tau(143)<tau(143 + 1),tau(144)<tau(144 + 1),tau(145)<tau(145 + 1),tau(146)<tau(146 + 1),tau(147)<tau(147 + 1),tau(148)<tau(148 + 1)))
# Requirements Table
s.add(Or(And(Not(True),Not(And(Not(True),y[0]==50)),Not(And(Not(True),u[0]>0))),And(Not(False),Not(And(Not(False),y[0]==50)),Not(And(Not(False),u[1]>0))),And(Not(False),Not(And(Not(False),y[1]==50)),Not(And(Not(False),u[2]>0))),And(Not(False),Not(And(Not(False),y[2]==50)),Not(And(Not(False),u[3]>0))),And(Not(False),Not(And(Not(False),y[3]==50)),Not(And(Not(False),u[4]>0))),And(Not(False),Not(And(Not(False),y[4]==50)),Not(And(Not(False),u[5]>0))),And(Not(False),Not(And(Not(False),y[5]==50)),Not(And(Not(False),u[6]>0))),And(Not(False),Not(And(Not(False),y[6]==50)),Not(And(Not(False),u[7]>0))),And(Not(False),Not(And(Not(False),y[7]==50)),Not(And(Not(False),u[8]>0))),And(Not(False),Not(And(Not(False),y[8]==50)),Not(And(Not(False),u[9]>0))),And(Not(False),Not(And(Not(False),y[9]==50)),Not(And(Not(False),u[10]>0))),And(Not(False),Not(And(Not(False),y[10]==50)),Not(And(Not(False),u[11]>0))),And(Not(False),Not(And(Not(False),y[11]==50)),Not(And(Not(False),u[12]>0))),And(Not(False),Not(And(Not(False),y[12]==50)),Not(And(Not(False),u[13]>0))),And(Not(False),Not(And(Not(False),y[13]==50)),Not(And(Not(False),u[14]>0))),And(Not(False),Not(And(Not(False),y[14]==50)),Not(And(Not(False),u[15]>0))),And(Not(False),Not(And(Not(False),y[15]==50)),Not(And(Not(False),u[16]>0))),And(Not(False),Not(And(Not(False),y[16]==50)),Not(And(Not(False),u[17]>0))),And(Not(False),Not(And(Not(False),y[17]==50)),Not(And(Not(False),u[18]>0))),And(Not(False),Not(And(Not(False),y[18]==50)),Not(And(Not(False),u[19]>0))),And(Not(False),Not(And(Not(False),y[19]==50)),Not(And(Not(False),u[20]>0))),And(Not(False),Not(And(Not(False),y[20]==50)),Not(And(Not(False),u[21]>0))),And(Not(False),Not(And(Not(False),y[21]==50)),Not(And(Not(False),u[22]>0))),And(Not(False),Not(And(Not(False),y[22]==50)),Not(And(Not(False),u[23]>0))),And(Not(False),Not(And(Not(False),y[23]==50)),Not(And(Not(False),u[24]>0))),And(Not(False),Not(And(Not(False),y[24]==50)),Not(And(Not(False),u[25]>0))),And(Not(False),Not(And(Not(False),y[25]==50)),Not(And(Not(False),u[26]>0))),And(Not(False),Not(And(Not(False),y[26]==50)),Not(And(Not(False),u[27]>0))),And(Not(False),Not(And(Not(False),y[27]==50)),Not(And(Not(False),u[28]>0))),And(Not(False),Not(And(Not(False),y[28]==50)),Not(And(Not(False),u[29]>0))),And(Not(False),Not(And(Not(False),y[29]==50)),Not(And(Not(False),u[30]>0))),And(Not(False),Not(And(Not(False),y[30]==50)),Not(And(Not(False),u[31]>0))),And(Not(False),Not(And(Not(False),y[31]==50)),Not(And(Not(False),u[32]>0))),And(Not(False),Not(And(Not(False),y[32]==50)),Not(And(Not(False),u[33]>0))),And(Not(False),Not(And(Not(False),y[33]==50)),Not(And(Not(False),u[34]>0))),And(Not(False),Not(And(Not(False),y[34]==50)),Not(And(Not(False),u[35]>0))),And(Not(False),Not(And(Not(False),y[35]==50)),Not(And(Not(False),u[36]>0))),And(Not(False),Not(And(Not(False),y[36]==50)),Not(And(Not(False),u[37]>0))),And(Not(False),Not(And(Not(False),y[37]==50)),Not(And(Not(False),u[38]>0))),And(Not(False),Not(And(Not(False),y[38]==50)),Not(And(Not(False),u[39]>0))),And(Not(False),Not(And(Not(False),y[39]==50)),Not(And(Not(False),u[40]>0))),And(Not(False),Not(And(Not(False),y[40]==50)),Not(And(Not(False),u[41]>0))),And(Not(False),Not(And(Not(False),y[41]==50)),Not(And(Not(False),u[42]>0))),And(Not(False),Not(And(Not(False),y[42]==50)),Not(And(Not(False),u[43]>0))),And(Not(False),Not(And(Not(False),y[43]==50)),Not(And(Not(False),u[44]>0))),And(Not(False),Not(And(Not(False),y[44]==50)),Not(And(Not(False),u[45]>0))),And(Not(False),Not(And(Not(False),y[45]==50)),Not(And(Not(False),u[46]>0))),And(Not(False),Not(And(Not(False),y[46]==50)),Not(And(Not(False),u[47]>0))),And(Not(False),Not(And(Not(False),y[47]==50)),Not(And(Not(False),u[48]>0))),And(Not(False),Not(And(Not(False),y[48]==50)),Not(And(Not(False),u[49]>0))),And(Not(False),Not(And(Not(False),y[49]==50)),Not(And(Not(False),u[50]>0))),And(Not(False),Not(And(Not(False),y[50]==50)),Not(And(Not(False),u[51]>0))),And(Not(False),Not(And(Not(False),y[51]==50)),Not(And(Not(False),u[52]>0))),And(Not(False),Not(And(Not(False),y[52]==50)),Not(And(Not(False),u[53]>0))),And(Not(False),Not(And(Not(False),y[53]==50)),Not(And(Not(False),u[54]>0))),And(Not(False),Not(And(Not(False),y[54]==50)),Not(And(Not(False),u[55]>0))),And(Not(False),Not(And(Not(False),y[55]==50)),Not(And(Not(False),u[56]>0))),And(Not(False),Not(And(Not(False),y[56]==50)),Not(And(Not(False),u[57]>0))),And(Not(False),Not(And(Not(False),y[57]==50)),Not(And(Not(False),u[58]>0))),And(Not(False),Not(And(Not(False),y[58]==50)),Not(And(Not(False),u[59]>0))),And(Not(False),Not(And(Not(False),y[59]==50)),Not(And(Not(False),u[60]>0))),And(Not(False),Not(And(Not(False),y[60]==50)),Not(And(Not(False),u[61]>0))),And(Not(False),Not(And(Not(False),y[61]==50)),Not(And(Not(False),u[62]>0))),And(Not(False),Not(And(Not(False),y[62]==50)),Not(And(Not(False),u[63]>0))),And(Not(False),Not(And(Not(False),y[63]==50)),Not(And(Not(False),u[64]>0))),And(Not(False),Not(And(Not(False),y[64]==50)),Not(And(Not(False),u[65]>0))),And(Not(False),Not(And(Not(False),y[65]==50)),Not(And(Not(False),u[66]>0))),And(Not(False),Not(And(Not(False),y[66]==50)),Not(And(Not(False),u[67]>0))),And(Not(False),Not(And(Not(False),y[67]==50)),Not(And(Not(False),u[68]>0))),And(Not(False),Not(And(Not(False),y[68]==50)),Not(And(Not(False),u[69]>0))),And(Not(False),Not(And(Not(False),y[69]==50)),Not(And(Not(False),u[70]>0))),And(Not(False),Not(And(Not(False),y[70]==50)),Not(And(Not(False),u[71]>0))),And(Not(False),Not(And(Not(False),y[71]==50)),Not(And(Not(False),u[72]>0))),And(Not(False),Not(And(Not(False),y[72]==50)),Not(And(Not(False),u[73]>0))),And(Not(False),Not(And(Not(False),y[73]==50)),Not(And(Not(False),u[74]>0))),And(Not(False),Not(And(Not(False),y[74]==50)),Not(And(Not(False),u[75]>0))),And(Not(False),Not(And(Not(False),y[75]==50)),Not(And(Not(False),u[76]>0))),And(Not(False),Not(And(Not(False),y[76]==50)),Not(And(Not(False),u[77]>0))),And(Not(False),Not(And(Not(False),y[77]==50)),Not(And(Not(False),u[78]>0))),And(Not(False),Not(And(Not(False),y[78]==50)),Not(And(Not(False),u[79]>0))),And(Not(False),Not(And(Not(False),y[79]==50)),Not(And(Not(False),u[80]>0))),And(Not(False),Not(And(Not(False),y[80]==50)),Not(And(Not(False),u[81]>0))),And(Not(False),Not(And(Not(False),y[81]==50)),Not(And(Not(False),u[82]>0))),And(Not(False),Not(And(Not(False),y[82]==50)),Not(And(Not(False),u[83]>0))),And(Not(False),Not(And(Not(False),y[83]==50)),Not(And(Not(False),u[84]>0))),And(Not(False),Not(And(Not(False),y[84]==50)),Not(And(Not(False),u[85]>0))),And(Not(False),Not(And(Not(False),y[85]==50)),Not(And(Not(False),u[86]>0))),And(Not(False),Not(And(Not(False),y[86]==50)),Not(And(Not(False),u[87]>0))),And(Not(False),Not(And(Not(False),y[87]==50)),Not(And(Not(False),u[88]>0))),And(Not(False),Not(And(Not(False),y[88]==50)),Not(And(Not(False),u[89]>0))),And(Not(False),Not(And(Not(False),y[89]==50)),Not(And(Not(False),u[90]>0))),And(Not(False),Not(And(Not(False),y[90]==50)),Not(And(Not(False),u[91]>0))),And(Not(False),Not(And(Not(False),y[91]==50)),Not(And(Not(False),u[92]>0))),And(Not(False),Not(And(Not(False),y[92]==50)),Not(And(Not(False),u[93]>0))),And(Not(False),Not(And(Not(False),y[93]==50)),Not(And(Not(False),u[94]>0))),And(Not(False),Not(And(Not(False),y[94]==50)),Not(And(Not(False),u[95]>0))),And(Not(False),Not(And(Not(False),y[95]==50)),Not(And(Not(False),u[96]>0))),And(Not(False),Not(And(Not(False),y[96]==50)),Not(And(Not(False),u[97]>0))),And(Not(False),Not(And(Not(False),y[97]==50)),Not(And(Not(False),u[98]>0))),And(Not(False),Not(And(Not(False),y[98]==50)),Not(And(Not(False),u[99]>0))),And(Not(False),Not(And(Not(False),y[99]==50)),Not(And(Not(False),u[100]>0))),And(Not(False),Not(And(Not(False),y[100]==50)),Not(And(Not(False),u[101]>0))),And(Not(False),Not(And(Not(False),y[101]==50)),Not(And(Not(False),u[102]>0))),And(Not(False),Not(And(Not(False),y[102]==50)),Not(And(Not(False),u[103]>0))),And(Not(False),Not(And(Not(False),y[103]==50)),Not(And(Not(False),u[104]>0))),And(Not(False),Not(And(Not(False),y[104]==50)),Not(And(Not(False),u[105]>0))),And(Not(False),Not(And(Not(False),y[105]==50)),Not(And(Not(False),u[106]>0))),And(Not(False),Not(And(Not(False),y[106]==50)),Not(And(Not(False),u[107]>0))),And(Not(False),Not(And(Not(False),y[107]==50)),Not(And(Not(False),u[108]>0))),And(Not(False),Not(And(Not(False),y[108]==50)),Not(And(Not(False),u[109]>0))),And(Not(False),Not(And(Not(False),y[109]==50)),Not(And(Not(False),u[110]>0))),And(Not(False),Not(And(Not(False),y[110]==50)),Not(And(Not(False),u[111]>0))),And(Not(False),Not(And(Not(False),y[111]==50)),Not(And(Not(False),u[112]>0))),And(Not(False),Not(And(Not(False),y[112]==50)),Not(And(Not(False),u[113]>0))),And(Not(False),Not(And(Not(False),y[113]==50)),Not(And(Not(False),u[114]>0))),And(Not(False),Not(And(Not(False),y[114]==50)),Not(And(Not(False),u[115]>0))),And(Not(False),Not(And(Not(False),y[115]==50)),Not(And(Not(False),u[116]>0))),And(Not(False),Not(And(Not(False),y[116]==50)),Not(And(Not(False),u[117]>0))),And(Not(False),Not(And(Not(False),y[117]==50)),Not(And(Not(False),u[118]>0))),And(Not(False),Not(And(Not(False),y[118]==50)),Not(And(Not(False),u[119]>0))),And(Not(False),Not(And(Not(False),y[119]==50)),Not(And(Not(False),u[120]>0))),And(Not(False),Not(And(Not(False),y[120]==50)),Not(And(Not(False),u[121]>0))),And(Not(False),Not(And(Not(False),y[121]==50)),Not(And(Not(False),u[122]>0))),And(Not(False),Not(And(Not(False),y[122]==50)),Not(And(Not(False),u[123]>0))),And(Not(False),Not(And(Not(False),y[123]==50)),Not(And(Not(False),u[124]>0))),And(Not(False),Not(And(Not(False),y[124]==50)),Not(And(Not(False),u[125]>0))),And(Not(False),Not(And(Not(False),y[125]==50)),Not(And(Not(False),u[126]>0))),And(Not(False),Not(And(Not(False),y[126]==50)),Not(And(Not(False),u[127]>0))),And(Not(False),Not(And(Not(False),y[127]==50)),Not(And(Not(False),u[128]>0))),And(Not(False),Not(And(Not(False),y[128]==50)),Not(And(Not(False),u[129]>0))),And(Not(False),Not(And(Not(False),y[129]==50)),Not(And(Not(False),u[130]>0))),And(Not(False),Not(And(Not(False),y[130]==50)),Not(And(Not(False),u[131]>0))),And(Not(False),Not(And(Not(False),y[131]==50)),Not(And(Not(False),u[132]>0))),And(Not(False),Not(And(Not(False),y[132]==50)),Not(And(Not(False),u[133]>0))),And(Not(False),Not(And(Not(False),y[133]==50)),Not(And(Not(False),u[134]>0))),And(Not(False),Not(And(Not(False),y[134]==50)),Not(And(Not(False),u[135]>0))),And(Not(False),Not(And(Not(False),y[135]==50)),Not(And(Not(False),u[136]>0))),And(Not(False),Not(And(Not(False),y[136]==50)),Not(And(Not(False),u[137]>0))),And(Not(False),Not(And(Not(False),y[137]==50)),Not(And(Not(False),u[138]>0))),And(Not(False),Not(And(Not(False),y[138]==50)),Not(And(Not(False),u[139]>0))),And(Not(False),Not(And(Not(False),y[139]==50)),Not(And(Not(False),u[140]>0))),And(Not(False),Not(And(Not(False),y[140]==50)),Not(And(Not(False),u[141]>0))),And(Not(False),Not(And(Not(False),y[141]==50)),Not(And(Not(False),u[142]>0))),And(Not(False),Not(And(Not(False),y[142]==50)),Not(And(Not(False),u[143]>0))),And(Not(False),Not(And(Not(False),y[143]==50)),Not(And(Not(False),u[144]>0))),And(Not(False),Not(And(Not(False),y[144]==50)),Not(And(Not(False),u[145]>0))),And(Not(False),Not(And(Not(False),y[145]==50)),Not(And(Not(False),u[146]>0))),And(Not(False),Not(And(Not(False),y[146]==50)),Not(And(Not(False),u[147]>0))),And(Not(False),Not(And(Not(False),y[147]==50)),Not(And(Not(False),u[148]>0))),And(Not(False),Not(And(Not(False),y[148]==50)),Not(And(Not(False),u[149]>0))),And(Not(False),Not(And(Not(False),y[149]==50)),Not(And(Not(False),u[150]>0)))))
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
