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
s.add(And(tau(1)-tau(0)==2.0,tau(2)-tau(1)==2.0,tau(3)-tau(2)==2.0,tau(4)-tau(3)==2.0,tau(5)-tau(4)==2.0,tau(6)-tau(5)==2.0,tau(7)-tau(6)==2.0,tau(8)-tau(7)==2.0,tau(9)-tau(8)==2.0,tau(10)-tau(9)==2.0,tau(11)-tau(10)==2.0,tau(12)-tau(11)==2.0,tau(13)-tau(12)==2.0,tau(14)-tau(13)==2.0,tau(15)-tau(14)==2.0,tau(16)-tau(15)==2.0,tau(17)-tau(16)==2.0,tau(18)-tau(17)==2.0,tau(19)-tau(18)==2.0,tau(20)-tau(19)==2.0,tau(21)-tau(20)==2.0,tau(22)-tau(21)==2.0,tau(23)-tau(22)==2.0,tau(24)-tau(23)==2.0,tau(25)-tau(24)==2.0,tau(26)-tau(25)==2.0,tau(27)-tau(26)==2.0,tau(28)-tau(27)==2.0,tau(29)-tau(28)==2.0,tau(30)-tau(29)==2.0,tau(31)-tau(30)==2.0,tau(32)-tau(31)==2.0,tau(33)-tau(32)==2.0,tau(34)-tau(33)==2.0,tau(35)-tau(34)==2.0,tau(36)-tau(35)==2.0,tau(37)-tau(36)==2.0,tau(38)-tau(37)==2.0,tau(39)-tau(38)==2.0,tau(40)-tau(39)==2.0,tau(41)-tau(40)==2.0,tau(42)-tau(41)==2.0,tau(43)-tau(42)==2.0,tau(44)-tau(43)==2.0,tau(45)-tau(44)==2.0,tau(46)-tau(45)==2.0,tau(47)-tau(46)==2.0,tau(48)-tau(47)==2.0,tau(49)-tau(48)==2.0,tau(50)-tau(49)==2.0,tau(51)-tau(50)==2.0,tau(52)-tau(51)==2.0,tau(53)-tau(52)==2.0,tau(54)-tau(53)==2.0,tau(55)-tau(54)==2.0,tau(56)-tau(55)==2.0,tau(57)-tau(56)==2.0,tau(58)-tau(57)==2.0,tau(59)-tau(58)==2.0,tau(60)-tau(59)==2.0,tau(61)-tau(60)==2.0,tau(62)-tau(61)==2.0,tau(63)-tau(62)==2.0,tau(64)-tau(63)==2.0,tau(65)-tau(64)==2.0,tau(66)-tau(65)==2.0,tau(67)-tau(66)==2.0,tau(68)-tau(67)==2.0,tau(69)-tau(68)==2.0,tau(70)-tau(69)==2.0,tau(71)-tau(70)==2.0,tau(72)-tau(71)==2.0,tau(73)-tau(72)==2.0,tau(74)-tau(73)==2.0,tau(75)-tau(74)==2.0,tau(76)-tau(75)==2.0,tau(77)-tau(76)==2.0,tau(78)-tau(77)==2.0,tau(79)-tau(78)==2.0,tau(80)-tau(79)==2.0,tau(81)-tau(80)==2.0,tau(82)-tau(81)==2.0,tau(83)-tau(82)==2.0,tau(84)-tau(83)==2.0,tau(85)-tau(84)==2.0,tau(86)-tau(85)==2.0,tau(87)-tau(86)==2.0,tau(88)-tau(87)==2.0,tau(89)-tau(88)==2.0,tau(90)-tau(89)==2.0,tau(91)-tau(90)==2.0,tau(92)-tau(91)==2.0,tau(93)-tau(92)==2.0,tau(94)-tau(93)==2.0,tau(95)-tau(94)==2.0,tau(96)-tau(95)==2.0,tau(97)-tau(96)==2.0,tau(98)-tau(97)==2.0,tau(99)-tau(98)==2.0,tau(100)-tau(99)==2.0,tau(101)-tau(100)==2.0,tau(102)-tau(101)==2.0,tau(103)-tau(102)==2.0,tau(104)-tau(103)==2.0,tau(105)-tau(104)==2.0,tau(106)-tau(105)==2.0,tau(107)-tau(106)==2.0,tau(108)-tau(107)==2.0,tau(109)-tau(108)==2.0,tau(110)-tau(109)==2.0,tau(111)-tau(110)==2.0,tau(112)-tau(111)==2.0,tau(113)-tau(112)==2.0,tau(114)-tau(113)==2.0,tau(115)-tau(114)==2.0,tau(116)-tau(115)==2.0,tau(117)-tau(116)==2.0,tau(118)-tau(117)==2.0,tau(119)-tau(118)==2.0,tau(120)-tau(119)==2.0,tau(121)-tau(120)==2.0,tau(122)-tau(121)==2.0,tau(123)-tau(122)==2.0,tau(124)-tau(123)==2.0,tau(125)-tau(124)==2.0,tau(126)-tau(125)==2.0,tau(127)-tau(126)==2.0,tau(128)-tau(127)==2.0,tau(129)-tau(128)==2.0,tau(130)-tau(129)==2.0,tau(131)-tau(130)==2.0,tau(132)-tau(131)==2.0,tau(133)-tau(132)==2.0,tau(134)-tau(133)==2.0,tau(135)-tau(134)==2.0,tau(136)-tau(135)==2.0,tau(137)-tau(136)==2.0,tau(138)-tau(137)==2.0,tau(139)-tau(138)==2.0,tau(140)-tau(139)==2.0,tau(141)-tau(140)==2.0,tau(142)-tau(141)==2.0,tau(143)-tau(142)==2.0,tau(144)-tau(143)==2.0,tau(145)-tau(144)==2.0,tau(146)-tau(145)==2.0,tau(147)-tau(146)==2.0,tau(148)-tau(147)==2.0,tau(149)-tau(148)==2.0,tau(150)-tau(149)==2.0,tau(151)-tau(150)==2.0,tau(152)-tau(151)==2.0,tau(153)-tau(152)==2.0,tau(154)-tau(153)==2.0,tau(155)-tau(154)==2.0,tau(156)-tau(155)==2.0,tau(157)-tau(156)==2.0,tau(158)-tau(157)==2.0,tau(159)-tau(158)==2.0,tau(160)-tau(159)==2.0,tau(161)-tau(160)==2.0,tau(162)-tau(161)==2.0,tau(163)-tau(162)==2.0,tau(164)-tau(163)==2.0,tau(165)-tau(164)==2.0,tau(166)-tau(165)==2.0,tau(167)-tau(166)==2.0,tau(168)-tau(167)==2.0,tau(169)-tau(168)==2.0,tau(170)-tau(169)==2.0,tau(171)-tau(170)==2.0,tau(172)-tau(171)==2.0,tau(173)-tau(172)==2.0,tau(174)-tau(173)==2.0,tau(175)-tau(174)==2.0,tau(176)-tau(175)==2.0,tau(177)-tau(176)==2.0,tau(178)-tau(177)==2.0,tau(179)-tau(178)==2.0,tau(180)-tau(179)==2.0,tau(181)-tau(180)==2.0,tau(182)-tau(181)==2.0,tau(183)-tau(182)==2.0,tau(184)-tau(183)==2.0,tau(185)-tau(184)==2.0,tau(186)-tau(185)==2.0,tau(187)-tau(186)==2.0,tau(188)-tau(187)==2.0,tau(189)-tau(188)==2.0,tau(190)-tau(189)==2.0,tau(191)-tau(190)==2.0,tau(192)-tau(191)==2.0,tau(193)-tau(192)==2.0,tau(194)-tau(193)==2.0,tau(195)-tau(194)==2.0,tau(196)-tau(195)==2.0,tau(197)-tau(196)==2.0,tau(198)-tau(197)==2.0,tau(199)-tau(198)==2.0,tau(200)-tau(199)==2.0,tau(201)-tau(200)==2.0,tau(202)-tau(201)==2.0,tau(203)-tau(202)==2.0,tau(204)-tau(203)==2.0,tau(205)-tau(204)==2.0,tau(206)-tau(205)==2.0,tau(207)-tau(206)==2.0,tau(208)-tau(207)==2.0,tau(209)-tau(208)==2.0,tau(210)-tau(209)==2.0,tau(211)-tau(210)==2.0,tau(212)-tau(211)==2.0,tau(213)-tau(212)==2.0,tau(214)-tau(213)==2.0,tau(215)-tau(214)==2.0,tau(216)-tau(215)==2.0,tau(217)-tau(216)==2.0,tau(218)-tau(217)==2.0,tau(219)-tau(218)==2.0,tau(220)-tau(219)==2.0,tau(221)-tau(220)==2.0,tau(222)-tau(221)==2.0,tau(223)-tau(222)==2.0,tau(224)-tau(223)==2.0,tau(225)-tau(224)==2.0,tau(226)-tau(225)==2.0,tau(227)-tau(226)==2.0,tau(228)-tau(227)==2.0,tau(229)-tau(228)==2.0,tau(230)-tau(229)==2.0,tau(231)-tau(230)==2.0,tau(232)-tau(231)==2.0,tau(233)-tau(232)==2.0,tau(234)-tau(233)==2.0,tau(235)-tau(234)==2.0,tau(236)-tau(235)==2.0,tau(237)-tau(236)==2.0,tau(238)-tau(237)==2.0,tau(239)-tau(238)==2.0,tau(240)-tau(239)==2.0,tau(241)-tau(240)==2.0,tau(242)-tau(241)==2.0,tau(243)-tau(242)==2.0,tau(244)-tau(243)==2.0,tau(245)-tau(244)==2.0,tau(246)-tau(245)==2.0,tau(247)-tau(246)==2.0,tau(248)-tau(247)==2.0,tau(249)-tau(248)==2.0))
# Requirements Table
s.add(Or(And(Not(And(Not(True),u[0]==u[0]+1)),Not(And(Not(True),u[0]!=u[0]+1)),Not(True)),And(Not(And(Not(False),u[1]==u[0]+1)),Not(And(Not(False),u[1]!=u[0]+1)),Not(False)),And(Not(And(Not(False),u[2]==u[1]+1)),Not(And(Not(False),u[2]!=u[1]+1)),Not(False)),And(Not(And(Not(False),u[3]==u[2]+1)),Not(And(Not(False),u[3]!=u[2]+1)),Not(False)),And(Not(And(Not(False),u[4]==u[3]+1)),Not(And(Not(False),u[4]!=u[3]+1)),Not(False)),And(Not(And(Not(False),u[5]==u[4]+1)),Not(And(Not(False),u[5]!=u[4]+1)),Not(False)),And(Not(And(Not(False),u[6]==u[5]+1)),Not(And(Not(False),u[6]!=u[5]+1)),Not(False)),And(Not(And(Not(False),u[7]==u[6]+1)),Not(And(Not(False),u[7]!=u[6]+1)),Not(False)),And(Not(And(Not(False),u[8]==u[7]+1)),Not(And(Not(False),u[8]!=u[7]+1)),Not(False)),And(Not(And(Not(False),u[9]==u[8]+1)),Not(And(Not(False),u[9]!=u[8]+1)),Not(False)),And(Not(And(Not(False),u[10]==u[9]+1)),Not(And(Not(False),u[10]!=u[9]+1)),Not(False)),And(Not(And(Not(False),u[11]==u[10]+1)),Not(And(Not(False),u[11]!=u[10]+1)),Not(False)),And(Not(And(Not(False),u[12]==u[11]+1)),Not(And(Not(False),u[12]!=u[11]+1)),Not(False)),And(Not(And(Not(False),u[13]==u[12]+1)),Not(And(Not(False),u[13]!=u[12]+1)),Not(False)),And(Not(And(Not(False),u[14]==u[13]+1)),Not(And(Not(False),u[14]!=u[13]+1)),Not(False)),And(Not(And(Not(False),u[15]==u[14]+1)),Not(And(Not(False),u[15]!=u[14]+1)),Not(False)),And(Not(And(Not(False),u[16]==u[15]+1)),Not(And(Not(False),u[16]!=u[15]+1)),Not(False)),And(Not(And(Not(False),u[17]==u[16]+1)),Not(And(Not(False),u[17]!=u[16]+1)),Not(False)),And(Not(And(Not(False),u[18]==u[17]+1)),Not(And(Not(False),u[18]!=u[17]+1)),Not(False)),And(Not(And(Not(False),u[19]==u[18]+1)),Not(And(Not(False),u[19]!=u[18]+1)),Not(False)),And(Not(And(Not(False),u[20]==u[19]+1)),Not(And(Not(False),u[20]!=u[19]+1)),Not(False)),And(Not(And(Not(False),u[21]==u[20]+1)),Not(And(Not(False),u[21]!=u[20]+1)),Not(False)),And(Not(And(Not(False),u[22]==u[21]+1)),Not(And(Not(False),u[22]!=u[21]+1)),Not(False)),And(Not(And(Not(False),u[23]==u[22]+1)),Not(And(Not(False),u[23]!=u[22]+1)),Not(False)),And(Not(And(Not(False),u[24]==u[23]+1)),Not(And(Not(False),u[24]!=u[23]+1)),Not(False)),And(Not(And(Not(False),u[25]==u[24]+1)),Not(And(Not(False),u[25]!=u[24]+1)),Not(False)),And(Not(And(Not(False),u[26]==u[25]+1)),Not(And(Not(False),u[26]!=u[25]+1)),Not(False)),And(Not(And(Not(False),u[27]==u[26]+1)),Not(And(Not(False),u[27]!=u[26]+1)),Not(False)),And(Not(And(Not(False),u[28]==u[27]+1)),Not(And(Not(False),u[28]!=u[27]+1)),Not(False)),And(Not(And(Not(False),u[29]==u[28]+1)),Not(And(Not(False),u[29]!=u[28]+1)),Not(False)),And(Not(And(Not(False),u[30]==u[29]+1)),Not(And(Not(False),u[30]!=u[29]+1)),Not(False)),And(Not(And(Not(False),u[31]==u[30]+1)),Not(And(Not(False),u[31]!=u[30]+1)),Not(False)),And(Not(And(Not(False),u[32]==u[31]+1)),Not(And(Not(False),u[32]!=u[31]+1)),Not(False)),And(Not(And(Not(False),u[33]==u[32]+1)),Not(And(Not(False),u[33]!=u[32]+1)),Not(False)),And(Not(And(Not(False),u[34]==u[33]+1)),Not(And(Not(False),u[34]!=u[33]+1)),Not(False)),And(Not(And(Not(False),u[35]==u[34]+1)),Not(And(Not(False),u[35]!=u[34]+1)),Not(False)),And(Not(And(Not(False),u[36]==u[35]+1)),Not(And(Not(False),u[36]!=u[35]+1)),Not(False)),And(Not(And(Not(False),u[37]==u[36]+1)),Not(And(Not(False),u[37]!=u[36]+1)),Not(False)),And(Not(And(Not(False),u[38]==u[37]+1)),Not(And(Not(False),u[38]!=u[37]+1)),Not(False)),And(Not(And(Not(False),u[39]==u[38]+1)),Not(And(Not(False),u[39]!=u[38]+1)),Not(False)),And(Not(And(Not(False),u[40]==u[39]+1)),Not(And(Not(False),u[40]!=u[39]+1)),Not(False)),And(Not(And(Not(False),u[41]==u[40]+1)),Not(And(Not(False),u[41]!=u[40]+1)),Not(False)),And(Not(And(Not(False),u[42]==u[41]+1)),Not(And(Not(False),u[42]!=u[41]+1)),Not(False)),And(Not(And(Not(False),u[43]==u[42]+1)),Not(And(Not(False),u[43]!=u[42]+1)),Not(False)),And(Not(And(Not(False),u[44]==u[43]+1)),Not(And(Not(False),u[44]!=u[43]+1)),Not(False)),And(Not(And(Not(False),u[45]==u[44]+1)),Not(And(Not(False),u[45]!=u[44]+1)),Not(False)),And(Not(And(Not(False),u[46]==u[45]+1)),Not(And(Not(False),u[46]!=u[45]+1)),Not(False)),And(Not(And(Not(False),u[47]==u[46]+1)),Not(And(Not(False),u[47]!=u[46]+1)),Not(False)),And(Not(And(Not(False),u[48]==u[47]+1)),Not(And(Not(False),u[48]!=u[47]+1)),Not(False)),And(Not(And(Not(False),u[49]==u[48]+1)),Not(And(Not(False),u[49]!=u[48]+1)),Not(False)),And(Not(And(Not(False),u[50]==u[49]+1)),Not(And(Not(False),u[50]!=u[49]+1)),Not(False)),And(Not(And(Not(False),u[51]==u[50]+1)),Not(And(Not(False),u[51]!=u[50]+1)),Not(False)),And(Not(And(Not(False),u[52]==u[51]+1)),Not(And(Not(False),u[52]!=u[51]+1)),Not(False)),And(Not(And(Not(False),u[53]==u[52]+1)),Not(And(Not(False),u[53]!=u[52]+1)),Not(False)),And(Not(And(Not(False),u[54]==u[53]+1)),Not(And(Not(False),u[54]!=u[53]+1)),Not(False)),And(Not(And(Not(False),u[55]==u[54]+1)),Not(And(Not(False),u[55]!=u[54]+1)),Not(False)),And(Not(And(Not(False),u[56]==u[55]+1)),Not(And(Not(False),u[56]!=u[55]+1)),Not(False)),And(Not(And(Not(False),u[57]==u[56]+1)),Not(And(Not(False),u[57]!=u[56]+1)),Not(False)),And(Not(And(Not(False),u[58]==u[57]+1)),Not(And(Not(False),u[58]!=u[57]+1)),Not(False)),And(Not(And(Not(False),u[59]==u[58]+1)),Not(And(Not(False),u[59]!=u[58]+1)),Not(False)),And(Not(And(Not(False),u[60]==u[59]+1)),Not(And(Not(False),u[60]!=u[59]+1)),Not(False)),And(Not(And(Not(False),u[61]==u[60]+1)),Not(And(Not(False),u[61]!=u[60]+1)),Not(False)),And(Not(And(Not(False),u[62]==u[61]+1)),Not(And(Not(False),u[62]!=u[61]+1)),Not(False)),And(Not(And(Not(False),u[63]==u[62]+1)),Not(And(Not(False),u[63]!=u[62]+1)),Not(False)),And(Not(And(Not(False),u[64]==u[63]+1)),Not(And(Not(False),u[64]!=u[63]+1)),Not(False)),And(Not(And(Not(False),u[65]==u[64]+1)),Not(And(Not(False),u[65]!=u[64]+1)),Not(False)),And(Not(And(Not(False),u[66]==u[65]+1)),Not(And(Not(False),u[66]!=u[65]+1)),Not(False)),And(Not(And(Not(False),u[67]==u[66]+1)),Not(And(Not(False),u[67]!=u[66]+1)),Not(False)),And(Not(And(Not(False),u[68]==u[67]+1)),Not(And(Not(False),u[68]!=u[67]+1)),Not(False)),And(Not(And(Not(False),u[69]==u[68]+1)),Not(And(Not(False),u[69]!=u[68]+1)),Not(False)),And(Not(And(Not(False),u[70]==u[69]+1)),Not(And(Not(False),u[70]!=u[69]+1)),Not(False)),And(Not(And(Not(False),u[71]==u[70]+1)),Not(And(Not(False),u[71]!=u[70]+1)),Not(False)),And(Not(And(Not(False),u[72]==u[71]+1)),Not(And(Not(False),u[72]!=u[71]+1)),Not(False)),And(Not(And(Not(False),u[73]==u[72]+1)),Not(And(Not(False),u[73]!=u[72]+1)),Not(False)),And(Not(And(Not(False),u[74]==u[73]+1)),Not(And(Not(False),u[74]!=u[73]+1)),Not(False)),And(Not(And(Not(False),u[75]==u[74]+1)),Not(And(Not(False),u[75]!=u[74]+1)),Not(False)),And(Not(And(Not(False),u[76]==u[75]+1)),Not(And(Not(False),u[76]!=u[75]+1)),Not(False)),And(Not(And(Not(False),u[77]==u[76]+1)),Not(And(Not(False),u[77]!=u[76]+1)),Not(False)),And(Not(And(Not(False),u[78]==u[77]+1)),Not(And(Not(False),u[78]!=u[77]+1)),Not(False)),And(Not(And(Not(False),u[79]==u[78]+1)),Not(And(Not(False),u[79]!=u[78]+1)),Not(False)),And(Not(And(Not(False),u[80]==u[79]+1)),Not(And(Not(False),u[80]!=u[79]+1)),Not(False)),And(Not(And(Not(False),u[81]==u[80]+1)),Not(And(Not(False),u[81]!=u[80]+1)),Not(False)),And(Not(And(Not(False),u[82]==u[81]+1)),Not(And(Not(False),u[82]!=u[81]+1)),Not(False)),And(Not(And(Not(False),u[83]==u[82]+1)),Not(And(Not(False),u[83]!=u[82]+1)),Not(False)),And(Not(And(Not(False),u[84]==u[83]+1)),Not(And(Not(False),u[84]!=u[83]+1)),Not(False)),And(Not(And(Not(False),u[85]==u[84]+1)),Not(And(Not(False),u[85]!=u[84]+1)),Not(False)),And(Not(And(Not(False),u[86]==u[85]+1)),Not(And(Not(False),u[86]!=u[85]+1)),Not(False)),And(Not(And(Not(False),u[87]==u[86]+1)),Not(And(Not(False),u[87]!=u[86]+1)),Not(False)),And(Not(And(Not(False),u[88]==u[87]+1)),Not(And(Not(False),u[88]!=u[87]+1)),Not(False)),And(Not(And(Not(False),u[89]==u[88]+1)),Not(And(Not(False),u[89]!=u[88]+1)),Not(False)),And(Not(And(Not(False),u[90]==u[89]+1)),Not(And(Not(False),u[90]!=u[89]+1)),Not(False)),And(Not(And(Not(False),u[91]==u[90]+1)),Not(And(Not(False),u[91]!=u[90]+1)),Not(False)),And(Not(And(Not(False),u[92]==u[91]+1)),Not(And(Not(False),u[92]!=u[91]+1)),Not(False)),And(Not(And(Not(False),u[93]==u[92]+1)),Not(And(Not(False),u[93]!=u[92]+1)),Not(False)),And(Not(And(Not(False),u[94]==u[93]+1)),Not(And(Not(False),u[94]!=u[93]+1)),Not(False)),And(Not(And(Not(False),u[95]==u[94]+1)),Not(And(Not(False),u[95]!=u[94]+1)),Not(False)),And(Not(And(Not(False),u[96]==u[95]+1)),Not(And(Not(False),u[96]!=u[95]+1)),Not(False)),And(Not(And(Not(False),u[97]==u[96]+1)),Not(And(Not(False),u[97]!=u[96]+1)),Not(False)),And(Not(And(Not(False),u[98]==u[97]+1)),Not(And(Not(False),u[98]!=u[97]+1)),Not(False)),And(Not(And(Not(False),u[99]==u[98]+1)),Not(And(Not(False),u[99]!=u[98]+1)),Not(False)),And(Not(And(Not(False),u[100]==u[99]+1)),Not(And(Not(False),u[100]!=u[99]+1)),Not(False)),And(Not(And(Not(False),u[101]==u[100]+1)),Not(And(Not(False),u[101]!=u[100]+1)),Not(False)),And(Not(And(Not(False),u[102]==u[101]+1)),Not(And(Not(False),u[102]!=u[101]+1)),Not(False)),And(Not(And(Not(False),u[103]==u[102]+1)),Not(And(Not(False),u[103]!=u[102]+1)),Not(False)),And(Not(And(Not(False),u[104]==u[103]+1)),Not(And(Not(False),u[104]!=u[103]+1)),Not(False)),And(Not(And(Not(False),u[105]==u[104]+1)),Not(And(Not(False),u[105]!=u[104]+1)),Not(False)),And(Not(And(Not(False),u[106]==u[105]+1)),Not(And(Not(False),u[106]!=u[105]+1)),Not(False)),And(Not(And(Not(False),u[107]==u[106]+1)),Not(And(Not(False),u[107]!=u[106]+1)),Not(False)),And(Not(And(Not(False),u[108]==u[107]+1)),Not(And(Not(False),u[108]!=u[107]+1)),Not(False)),And(Not(And(Not(False),u[109]==u[108]+1)),Not(And(Not(False),u[109]!=u[108]+1)),Not(False)),And(Not(And(Not(False),u[110]==u[109]+1)),Not(And(Not(False),u[110]!=u[109]+1)),Not(False)),And(Not(And(Not(False),u[111]==u[110]+1)),Not(And(Not(False),u[111]!=u[110]+1)),Not(False)),And(Not(And(Not(False),u[112]==u[111]+1)),Not(And(Not(False),u[112]!=u[111]+1)),Not(False)),And(Not(And(Not(False),u[113]==u[112]+1)),Not(And(Not(False),u[113]!=u[112]+1)),Not(False)),And(Not(And(Not(False),u[114]==u[113]+1)),Not(And(Not(False),u[114]!=u[113]+1)),Not(False)),And(Not(And(Not(False),u[115]==u[114]+1)),Not(And(Not(False),u[115]!=u[114]+1)),Not(False)),And(Not(And(Not(False),u[116]==u[115]+1)),Not(And(Not(False),u[116]!=u[115]+1)),Not(False)),And(Not(And(Not(False),u[117]==u[116]+1)),Not(And(Not(False),u[117]!=u[116]+1)),Not(False)),And(Not(And(Not(False),u[118]==u[117]+1)),Not(And(Not(False),u[118]!=u[117]+1)),Not(False)),And(Not(And(Not(False),u[119]==u[118]+1)),Not(And(Not(False),u[119]!=u[118]+1)),Not(False)),And(Not(And(Not(False),u[120]==u[119]+1)),Not(And(Not(False),u[120]!=u[119]+1)),Not(False)),And(Not(And(Not(False),u[121]==u[120]+1)),Not(And(Not(False),u[121]!=u[120]+1)),Not(False)),And(Not(And(Not(False),u[122]==u[121]+1)),Not(And(Not(False),u[122]!=u[121]+1)),Not(False)),And(Not(And(Not(False),u[123]==u[122]+1)),Not(And(Not(False),u[123]!=u[122]+1)),Not(False)),And(Not(And(Not(False),u[124]==u[123]+1)),Not(And(Not(False),u[124]!=u[123]+1)),Not(False)),And(Not(And(Not(False),u[125]==u[124]+1)),Not(And(Not(False),u[125]!=u[124]+1)),Not(False)),And(Not(And(Not(False),u[126]==u[125]+1)),Not(And(Not(False),u[126]!=u[125]+1)),Not(False)),And(Not(And(Not(False),u[127]==u[126]+1)),Not(And(Not(False),u[127]!=u[126]+1)),Not(False)),And(Not(And(Not(False),u[128]==u[127]+1)),Not(And(Not(False),u[128]!=u[127]+1)),Not(False)),And(Not(And(Not(False),u[129]==u[128]+1)),Not(And(Not(False),u[129]!=u[128]+1)),Not(False)),And(Not(And(Not(False),u[130]==u[129]+1)),Not(And(Not(False),u[130]!=u[129]+1)),Not(False)),And(Not(And(Not(False),u[131]==u[130]+1)),Not(And(Not(False),u[131]!=u[130]+1)),Not(False)),And(Not(And(Not(False),u[132]==u[131]+1)),Not(And(Not(False),u[132]!=u[131]+1)),Not(False)),And(Not(And(Not(False),u[133]==u[132]+1)),Not(And(Not(False),u[133]!=u[132]+1)),Not(False)),And(Not(And(Not(False),u[134]==u[133]+1)),Not(And(Not(False),u[134]!=u[133]+1)),Not(False)),And(Not(And(Not(False),u[135]==u[134]+1)),Not(And(Not(False),u[135]!=u[134]+1)),Not(False)),And(Not(And(Not(False),u[136]==u[135]+1)),Not(And(Not(False),u[136]!=u[135]+1)),Not(False)),And(Not(And(Not(False),u[137]==u[136]+1)),Not(And(Not(False),u[137]!=u[136]+1)),Not(False)),And(Not(And(Not(False),u[138]==u[137]+1)),Not(And(Not(False),u[138]!=u[137]+1)),Not(False)),And(Not(And(Not(False),u[139]==u[138]+1)),Not(And(Not(False),u[139]!=u[138]+1)),Not(False)),And(Not(And(Not(False),u[140]==u[139]+1)),Not(And(Not(False),u[140]!=u[139]+1)),Not(False)),And(Not(And(Not(False),u[141]==u[140]+1)),Not(And(Not(False),u[141]!=u[140]+1)),Not(False)),And(Not(And(Not(False),u[142]==u[141]+1)),Not(And(Not(False),u[142]!=u[141]+1)),Not(False)),And(Not(And(Not(False),u[143]==u[142]+1)),Not(And(Not(False),u[143]!=u[142]+1)),Not(False)),And(Not(And(Not(False),u[144]==u[143]+1)),Not(And(Not(False),u[144]!=u[143]+1)),Not(False)),And(Not(And(Not(False),u[145]==u[144]+1)),Not(And(Not(False),u[145]!=u[144]+1)),Not(False)),And(Not(And(Not(False),u[146]==u[145]+1)),Not(And(Not(False),u[146]!=u[145]+1)),Not(False)),And(Not(And(Not(False),u[147]==u[146]+1)),Not(And(Not(False),u[147]!=u[146]+1)),Not(False)),And(Not(And(Not(False),u[148]==u[147]+1)),Not(And(Not(False),u[148]!=u[147]+1)),Not(False)),And(Not(And(Not(False),u[149]==u[148]+1)),Not(And(Not(False),u[149]!=u[148]+1)),Not(False)),And(Not(And(Not(False),u[150]==u[149]+1)),Not(And(Not(False),u[150]!=u[149]+1)),Not(False)),And(Not(And(Not(False),u[151]==u[150]+1)),Not(And(Not(False),u[151]!=u[150]+1)),Not(False)),And(Not(And(Not(False),u[152]==u[151]+1)),Not(And(Not(False),u[152]!=u[151]+1)),Not(False)),And(Not(And(Not(False),u[153]==u[152]+1)),Not(And(Not(False),u[153]!=u[152]+1)),Not(False)),And(Not(And(Not(False),u[154]==u[153]+1)),Not(And(Not(False),u[154]!=u[153]+1)),Not(False)),And(Not(And(Not(False),u[155]==u[154]+1)),Not(And(Not(False),u[155]!=u[154]+1)),Not(False)),And(Not(And(Not(False),u[156]==u[155]+1)),Not(And(Not(False),u[156]!=u[155]+1)),Not(False)),And(Not(And(Not(False),u[157]==u[156]+1)),Not(And(Not(False),u[157]!=u[156]+1)),Not(False)),And(Not(And(Not(False),u[158]==u[157]+1)),Not(And(Not(False),u[158]!=u[157]+1)),Not(False)),And(Not(And(Not(False),u[159]==u[158]+1)),Not(And(Not(False),u[159]!=u[158]+1)),Not(False)),And(Not(And(Not(False),u[160]==u[159]+1)),Not(And(Not(False),u[160]!=u[159]+1)),Not(False)),And(Not(And(Not(False),u[161]==u[160]+1)),Not(And(Not(False),u[161]!=u[160]+1)),Not(False)),And(Not(And(Not(False),u[162]==u[161]+1)),Not(And(Not(False),u[162]!=u[161]+1)),Not(False)),And(Not(And(Not(False),u[163]==u[162]+1)),Not(And(Not(False),u[163]!=u[162]+1)),Not(False)),And(Not(And(Not(False),u[164]==u[163]+1)),Not(And(Not(False),u[164]!=u[163]+1)),Not(False)),And(Not(And(Not(False),u[165]==u[164]+1)),Not(And(Not(False),u[165]!=u[164]+1)),Not(False)),And(Not(And(Not(False),u[166]==u[165]+1)),Not(And(Not(False),u[166]!=u[165]+1)),Not(False)),And(Not(And(Not(False),u[167]==u[166]+1)),Not(And(Not(False),u[167]!=u[166]+1)),Not(False)),And(Not(And(Not(False),u[168]==u[167]+1)),Not(And(Not(False),u[168]!=u[167]+1)),Not(False)),And(Not(And(Not(False),u[169]==u[168]+1)),Not(And(Not(False),u[169]!=u[168]+1)),Not(False)),And(Not(And(Not(False),u[170]==u[169]+1)),Not(And(Not(False),u[170]!=u[169]+1)),Not(False)),And(Not(And(Not(False),u[171]==u[170]+1)),Not(And(Not(False),u[171]!=u[170]+1)),Not(False)),And(Not(And(Not(False),u[172]==u[171]+1)),Not(And(Not(False),u[172]!=u[171]+1)),Not(False)),And(Not(And(Not(False),u[173]==u[172]+1)),Not(And(Not(False),u[173]!=u[172]+1)),Not(False)),And(Not(And(Not(False),u[174]==u[173]+1)),Not(And(Not(False),u[174]!=u[173]+1)),Not(False)),And(Not(And(Not(False),u[175]==u[174]+1)),Not(And(Not(False),u[175]!=u[174]+1)),Not(False)),And(Not(And(Not(False),u[176]==u[175]+1)),Not(And(Not(False),u[176]!=u[175]+1)),Not(False)),And(Not(And(Not(False),u[177]==u[176]+1)),Not(And(Not(False),u[177]!=u[176]+1)),Not(False)),And(Not(And(Not(False),u[178]==u[177]+1)),Not(And(Not(False),u[178]!=u[177]+1)),Not(False)),And(Not(And(Not(False),u[179]==u[178]+1)),Not(And(Not(False),u[179]!=u[178]+1)),Not(False)),And(Not(And(Not(False),u[180]==u[179]+1)),Not(And(Not(False),u[180]!=u[179]+1)),Not(False)),And(Not(And(Not(False),u[181]==u[180]+1)),Not(And(Not(False),u[181]!=u[180]+1)),Not(False)),And(Not(And(Not(False),u[182]==u[181]+1)),Not(And(Not(False),u[182]!=u[181]+1)),Not(False)),And(Not(And(Not(False),u[183]==u[182]+1)),Not(And(Not(False),u[183]!=u[182]+1)),Not(False)),And(Not(And(Not(False),u[184]==u[183]+1)),Not(And(Not(False),u[184]!=u[183]+1)),Not(False)),And(Not(And(Not(False),u[185]==u[184]+1)),Not(And(Not(False),u[185]!=u[184]+1)),Not(False)),And(Not(And(Not(False),u[186]==u[185]+1)),Not(And(Not(False),u[186]!=u[185]+1)),Not(False)),And(Not(And(Not(False),u[187]==u[186]+1)),Not(And(Not(False),u[187]!=u[186]+1)),Not(False)),And(Not(And(Not(False),u[188]==u[187]+1)),Not(And(Not(False),u[188]!=u[187]+1)),Not(False)),And(Not(And(Not(False),u[189]==u[188]+1)),Not(And(Not(False),u[189]!=u[188]+1)),Not(False)),And(Not(And(Not(False),u[190]==u[189]+1)),Not(And(Not(False),u[190]!=u[189]+1)),Not(False)),And(Not(And(Not(False),u[191]==u[190]+1)),Not(And(Not(False),u[191]!=u[190]+1)),Not(False)),And(Not(And(Not(False),u[192]==u[191]+1)),Not(And(Not(False),u[192]!=u[191]+1)),Not(False)),And(Not(And(Not(False),u[193]==u[192]+1)),Not(And(Not(False),u[193]!=u[192]+1)),Not(False)),And(Not(And(Not(False),u[194]==u[193]+1)),Not(And(Not(False),u[194]!=u[193]+1)),Not(False)),And(Not(And(Not(False),u[195]==u[194]+1)),Not(And(Not(False),u[195]!=u[194]+1)),Not(False)),And(Not(And(Not(False),u[196]==u[195]+1)),Not(And(Not(False),u[196]!=u[195]+1)),Not(False)),And(Not(And(Not(False),u[197]==u[196]+1)),Not(And(Not(False),u[197]!=u[196]+1)),Not(False)),And(Not(And(Not(False),u[198]==u[197]+1)),Not(And(Not(False),u[198]!=u[197]+1)),Not(False)),And(Not(And(Not(False),u[199]==u[198]+1)),Not(And(Not(False),u[199]!=u[198]+1)),Not(False)),And(Not(And(Not(False),u[200]==u[199]+1)),Not(And(Not(False),u[200]!=u[199]+1)),Not(False)),And(Not(And(Not(False),u[201]==u[200]+1)),Not(And(Not(False),u[201]!=u[200]+1)),Not(False)),And(Not(And(Not(False),u[202]==u[201]+1)),Not(And(Not(False),u[202]!=u[201]+1)),Not(False)),And(Not(And(Not(False),u[203]==u[202]+1)),Not(And(Not(False),u[203]!=u[202]+1)),Not(False)),And(Not(And(Not(False),u[204]==u[203]+1)),Not(And(Not(False),u[204]!=u[203]+1)),Not(False)),And(Not(And(Not(False),u[205]==u[204]+1)),Not(And(Not(False),u[205]!=u[204]+1)),Not(False)),And(Not(And(Not(False),u[206]==u[205]+1)),Not(And(Not(False),u[206]!=u[205]+1)),Not(False)),And(Not(And(Not(False),u[207]==u[206]+1)),Not(And(Not(False),u[207]!=u[206]+1)),Not(False)),And(Not(And(Not(False),u[208]==u[207]+1)),Not(And(Not(False),u[208]!=u[207]+1)),Not(False)),And(Not(And(Not(False),u[209]==u[208]+1)),Not(And(Not(False),u[209]!=u[208]+1)),Not(False)),And(Not(And(Not(False),u[210]==u[209]+1)),Not(And(Not(False),u[210]!=u[209]+1)),Not(False)),And(Not(And(Not(False),u[211]==u[210]+1)),Not(And(Not(False),u[211]!=u[210]+1)),Not(False)),And(Not(And(Not(False),u[212]==u[211]+1)),Not(And(Not(False),u[212]!=u[211]+1)),Not(False)),And(Not(And(Not(False),u[213]==u[212]+1)),Not(And(Not(False),u[213]!=u[212]+1)),Not(False)),And(Not(And(Not(False),u[214]==u[213]+1)),Not(And(Not(False),u[214]!=u[213]+1)),Not(False)),And(Not(And(Not(False),u[215]==u[214]+1)),Not(And(Not(False),u[215]!=u[214]+1)),Not(False)),And(Not(And(Not(False),u[216]==u[215]+1)),Not(And(Not(False),u[216]!=u[215]+1)),Not(False)),And(Not(And(Not(False),u[217]==u[216]+1)),Not(And(Not(False),u[217]!=u[216]+1)),Not(False)),And(Not(And(Not(False),u[218]==u[217]+1)),Not(And(Not(False),u[218]!=u[217]+1)),Not(False)),And(Not(And(Not(False),u[219]==u[218]+1)),Not(And(Not(False),u[219]!=u[218]+1)),Not(False)),And(Not(And(Not(False),u[220]==u[219]+1)),Not(And(Not(False),u[220]!=u[219]+1)),Not(False)),And(Not(And(Not(False),u[221]==u[220]+1)),Not(And(Not(False),u[221]!=u[220]+1)),Not(False)),And(Not(And(Not(False),u[222]==u[221]+1)),Not(And(Not(False),u[222]!=u[221]+1)),Not(False)),And(Not(And(Not(False),u[223]==u[222]+1)),Not(And(Not(False),u[223]!=u[222]+1)),Not(False)),And(Not(And(Not(False),u[224]==u[223]+1)),Not(And(Not(False),u[224]!=u[223]+1)),Not(False)),And(Not(And(Not(False),u[225]==u[224]+1)),Not(And(Not(False),u[225]!=u[224]+1)),Not(False)),And(Not(And(Not(False),u[226]==u[225]+1)),Not(And(Not(False),u[226]!=u[225]+1)),Not(False)),And(Not(And(Not(False),u[227]==u[226]+1)),Not(And(Not(False),u[227]!=u[226]+1)),Not(False)),And(Not(And(Not(False),u[228]==u[227]+1)),Not(And(Not(False),u[228]!=u[227]+1)),Not(False)),And(Not(And(Not(False),u[229]==u[228]+1)),Not(And(Not(False),u[229]!=u[228]+1)),Not(False)),And(Not(And(Not(False),u[230]==u[229]+1)),Not(And(Not(False),u[230]!=u[229]+1)),Not(False)),And(Not(And(Not(False),u[231]==u[230]+1)),Not(And(Not(False),u[231]!=u[230]+1)),Not(False)),And(Not(And(Not(False),u[232]==u[231]+1)),Not(And(Not(False),u[232]!=u[231]+1)),Not(False)),And(Not(And(Not(False),u[233]==u[232]+1)),Not(And(Not(False),u[233]!=u[232]+1)),Not(False)),And(Not(And(Not(False),u[234]==u[233]+1)),Not(And(Not(False),u[234]!=u[233]+1)),Not(False)),And(Not(And(Not(False),u[235]==u[234]+1)),Not(And(Not(False),u[235]!=u[234]+1)),Not(False)),And(Not(And(Not(False),u[236]==u[235]+1)),Not(And(Not(False),u[236]!=u[235]+1)),Not(False)),And(Not(And(Not(False),u[237]==u[236]+1)),Not(And(Not(False),u[237]!=u[236]+1)),Not(False)),And(Not(And(Not(False),u[238]==u[237]+1)),Not(And(Not(False),u[238]!=u[237]+1)),Not(False)),And(Not(And(Not(False),u[239]==u[238]+1)),Not(And(Not(False),u[239]!=u[238]+1)),Not(False)),And(Not(And(Not(False),u[240]==u[239]+1)),Not(And(Not(False),u[240]!=u[239]+1)),Not(False)),And(Not(And(Not(False),u[241]==u[240]+1)),Not(And(Not(False),u[241]!=u[240]+1)),Not(False)),And(Not(And(Not(False),u[242]==u[241]+1)),Not(And(Not(False),u[242]!=u[241]+1)),Not(False)),And(Not(And(Not(False),u[243]==u[242]+1)),Not(And(Not(False),u[243]!=u[242]+1)),Not(False)),And(Not(And(Not(False),u[244]==u[243]+1)),Not(And(Not(False),u[244]!=u[243]+1)),Not(False)),And(Not(And(Not(False),u[245]==u[244]+1)),Not(And(Not(False),u[245]!=u[244]+1)),Not(False)),And(Not(And(Not(False),u[246]==u[245]+1)),Not(And(Not(False),u[246]!=u[245]+1)),Not(False)),And(Not(And(Not(False),u[247]==u[246]+1)),Not(And(Not(False),u[247]!=u[246]+1)),Not(False)),And(Not(And(Not(False),u[248]==u[247]+1)),Not(And(Not(False),u[248]!=u[247]+1)),Not(False)),And(Not(And(Not(False),u[249]==u[248]+1)),Not(And(Not(False),u[249]!=u[248]+1)),Not(False)),And(Not(And(Not(False),u[250]==u[249]+1)),Not(And(Not(False),u[250]!=u[249]+1)),Not(False))))
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
