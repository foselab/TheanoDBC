from z3 import *;
I = IntSort()
R = RealSort()
tau = Function('tau', IntSort(), RealSort())
j = Int('j')
i = Int('i')
k = Int('k')
u=Array('u', I, I)
y=Array('y', I, I)
Ts = Real('Ts')
s = Solver()
s.add(And(And(tau(0)==0.0,tau(1)==2.0,tau(2)==4.0,tau(3)==6.0,tau(4)==8.0,tau(5)==10.0,tau(6)==12.0,tau(7)==14.0,tau(8)==16.0,tau(9)==18.0,tau(10)==20.0,tau(11)==22.0,tau(12)==24.0,tau(13)==26.0,tau(14)==28.0,tau(15)==30.0,tau(16)==32.0,tau(17)==34.0,tau(18)==36.0,tau(19)==38.0,tau(20)==40.0,tau(21)==42.0,tau(22)==44.0,tau(23)==46.0,tau(24)==48.0,tau(25)==50.0,tau(26)==52.0,tau(27)==54.0,tau(28)==56.0,tau(29)==58.0,tau(30)==60.0,tau(31)==62.0,tau(32)==64.0,tau(33)==66.0,tau(34)==68.0,tau(35)==70.0,tau(36)==72.0,tau(37)==74.0,tau(38)==76.0,tau(39)==78.0,tau(40)==80.0,tau(41)==82.0,tau(42)==84.0,tau(43)==86.0,tau(44)==88.0,tau(45)==90.0,tau(46)==92.0,tau(47)==94.0,tau(48)==96.0,tau(49)==98.0,tau(50)==100.0,tau(51)==102.0,tau(52)==104.0,tau(53)==106.0,tau(54)==108.0,tau(55)==110.0,tau(56)==112.0,tau(57)==114.0,tau(58)==116.0,tau(59)==118.0,tau(60)==120.0,tau(61)==122.0,tau(62)==124.0,tau(63)==126.0,tau(64)==128.0,tau(65)==130.0,tau(66)==132.0,tau(67)==134.0,tau(68)==136.0,tau(69)==138.0,tau(70)==140.0,tau(71)==142.0,tau(72)==144.0,tau(73)==146.0,tau(74)==148.0,tau(75)==150.0,tau(76)==152.0,tau(77)==154.0,tau(78)==156.0,tau(79)==158.0,tau(80)==160.0,tau(81)==162.0,tau(82)==164.0,tau(83)==166.0,tau(84)==168.0,tau(85)==170.0,tau(86)==172.0,tau(87)==174.0,tau(88)==176.0,tau(89)==178.0,tau(90)==180.0,tau(91)==182.0,tau(92)==184.0,tau(93)==186.0,tau(94)==188.0,tau(95)==190.0,tau(96)==192.0,tau(97)==194.0,tau(98)==196.0,tau(99)==198.0,tau(100)==200.0,tau(101)==202.0,tau(102)==204.0,tau(103)==206.0,tau(104)==208.0,tau(105)==210.0,tau(106)==212.0,tau(107)==214.0,tau(108)==216.0,tau(109)==218.0,tau(110)==220.0,tau(111)==222.0,tau(112)==224.0,tau(113)==226.0,tau(114)==228.0,tau(115)==230.0,tau(116)==232.0,tau(117)==234.0,tau(118)==236.0,tau(119)==238.0,tau(120)==240.0,tau(121)==242.0,tau(122)==244.0,tau(123)==246.0,tau(124)==248.0,tau(125)==250.0,tau(126)==252.0,tau(127)==254.0,tau(128)==256.0,tau(129)==258.0,tau(130)==260.0,tau(131)==262.0,tau(132)==264.0,tau(133)==266.0,tau(134)==268.0,tau(135)==270.0,tau(136)==272.0,tau(137)==274.0,tau(138)==276.0,tau(139)==278.0,tau(140)==280.0,tau(141)==282.0,tau(142)==284.0,tau(143)==286.0,tau(144)==288.0,tau(145)==290.0,tau(146)==292.0,tau(147)==294.0,tau(148)==296.0,tau(149)==298.0,tau(150)==300.0,tau(151)==302.0,tau(152)==304.0,tau(153)==306.0,tau(154)==308.0,tau(155)==310.0,tau(156)==312.0,tau(157)==314.0,tau(158)==316.0,tau(159)==318.0,tau(160)==320.0,tau(161)==322.0,tau(162)==324.0,tau(163)==326.0,tau(164)==328.0,tau(165)==330.0,tau(166)==332.0,tau(167)==334.0,tau(168)==336.0,tau(169)==338.0,tau(170)==340.0,tau(171)==342.0,tau(172)==344.0,tau(173)==346.0,tau(174)==348.0,tau(175)==350.0,tau(176)==352.0,tau(177)==354.0,tau(178)==356.0,tau(179)==358.0,tau(180)==360.0,tau(181)==362.0,tau(182)==364.0,tau(183)==366.0,tau(184)==368.0,tau(185)==370.0,tau(186)==372.0,tau(187)==374.0,tau(188)==376.0,tau(189)==378.0,tau(190)==380.0,tau(191)==382.0,tau(192)==384.0,tau(193)==386.0,tau(194)==388.0,tau(195)==390.0,tau(196)==392.0,tau(197)==394.0,tau(198)==396.0,tau(199)==398.0,tau(200)==400.0,tau(201)==402.0,tau(202)==404.0,tau(203)==406.0,tau(204)==408.0,tau(205)==410.0,tau(206)==412.0,tau(207)==414.0,tau(208)==416.0,tau(209)==418.0,tau(210)==420.0,tau(211)==422.0,tau(212)==424.0,tau(213)==426.0,tau(214)==428.0,tau(215)==430.0,tau(216)==432.0,tau(217)==434.0,tau(218)==436.0,tau(219)==438.0,tau(220)==440.0,tau(221)==442.0,tau(222)==444.0,tau(223)==446.0,tau(224)==448.0,tau(225)==450.0,tau(226)==452.0,tau(227)==454.0,tau(228)==456.0,tau(229)==458.0,tau(230)==460.0,tau(231)==462.0,tau(232)==464.0,tau(233)==466.0,tau(234)==468.0,tau(235)==470.0,tau(236)==472.0,tau(237)==474.0,tau(238)==476.0,tau(239)==478.0,tau(240)==480.0,tau(241)==482.0,tau(242)==484.0,tau(243)==486.0,tau(244)==488.0,tau(245)==490.0,tau(246)==492.0,tau(247)==494.0,tau(248)==496.0,tau(249)==498.0,tau(250)==500.0,tau(251)==502.0,tau(252)==504.0,tau(253)==506.0,tau(254)==508.0,tau(255)==510.0,tau(256)==512.0,tau(257)==514.0,tau(258)==516.0,tau(259)==518.0,tau(260)==520.0,tau(261)==522.0,tau(262)==524.0,tau(263)==526.0,tau(264)==528.0,tau(265)==530.0,tau(266)==532.0,tau(267)==534.0,tau(268)==536.0,tau(269)==538.0,tau(270)==540.0,tau(271)==542.0,tau(272)==544.0,tau(273)==546.0,tau(274)==548.0,tau(275)==550.0,tau(276)==552.0,tau(277)==554.0,tau(278)==556.0,tau(279)==558.0,tau(280)==560.0,tau(281)==562.0,tau(282)==564.0,tau(283)==566.0,tau(284)==568.0,tau(285)==570.0,tau(286)==572.0,tau(287)==574.0,tau(288)==576.0,tau(289)==578.0,tau(290)==580.0,tau(291)==582.0,tau(292)==584.0,tau(293)==586.0,tau(294)==588.0,tau(295)==590.0,tau(296)==592.0,tau(297)==594.0,tau(298)==596.0,tau(299)==598.0),ForAll([y] , And(Or(Not(y[0]==0),Not(Implies(u[1]>0,y[1]==y[0]+1)),Not(Implies(y[0]==1023,y[1]==23)),Not(Implies(u[2]>0,y[2]==y[1]+1)),Not(Implies(y[1]==1023,y[2]==23)),Not(Implies(u[3]>0,y[3]==y[2]+1)),Not(Implies(y[2]==1023,y[3]==23)),Not(Implies(u[4]>0,y[4]==y[3]+1)),Not(Implies(y[3]==1023,y[4]==23)),Not(Implies(u[5]>0,y[5]==y[4]+1)),Not(Implies(y[4]==1023,y[5]==23)),Not(Implies(u[6]>0,y[6]==y[5]+1)),Not(Implies(y[5]==1023,y[6]==23)),Not(Implies(u[7]>0,y[7]==y[6]+1)),Not(Implies(y[6]==1023,y[7]==23)),Not(Implies(u[8]>0,y[8]==y[7]+1)),Not(Implies(y[7]==1023,y[8]==23)),Not(Implies(u[9]>0,y[9]==y[8]+1)),Not(Implies(y[8]==1023,y[9]==23)),Not(Implies(u[10]>0,y[10]==y[9]+1)),Not(Implies(y[9]==1023,y[10]==23)),Not(Implies(u[11]>0,y[11]==y[10]+1)),Not(Implies(y[10]==1023,y[11]==23)),Not(Implies(u[12]>0,y[12]==y[11]+1)),Not(Implies(y[11]==1023,y[12]==23)),Not(Implies(u[13]>0,y[13]==y[12]+1)),Not(Implies(y[12]==1023,y[13]==23)),Not(Implies(u[14]>0,y[14]==y[13]+1)),Not(Implies(y[13]==1023,y[14]==23)),Not(Implies(u[15]>0,y[15]==y[14]+1)),Not(Implies(y[14]==1023,y[15]==23)),Not(Implies(u[16]>0,y[16]==y[15]+1)),Not(Implies(y[15]==1023,y[16]==23)),Not(Implies(u[17]>0,y[17]==y[16]+1)),Not(Implies(y[16]==1023,y[17]==23)),Not(Implies(u[18]>0,y[18]==y[17]+1)),Not(Implies(y[17]==1023,y[18]==23)),Not(Implies(u[19]>0,y[19]==y[18]+1)),Not(Implies(y[18]==1023,y[19]==23)),Not(Implies(u[20]>0,y[20]==y[19]+1)),Not(Implies(y[19]==1023,y[20]==23)),Not(Implies(u[21]>0,y[21]==y[20]+1)),Not(Implies(y[20]==1023,y[21]==23)),Not(Implies(u[22]>0,y[22]==y[21]+1)),Not(Implies(y[21]==1023,y[22]==23)),Not(Implies(u[23]>0,y[23]==y[22]+1)),Not(Implies(y[22]==1023,y[23]==23)),Not(Implies(u[24]>0,y[24]==y[23]+1)),Not(Implies(y[23]==1023,y[24]==23)),Not(Implies(u[25]>0,y[25]==y[24]+1)),Not(Implies(y[24]==1023,y[25]==23)),Not(Implies(u[26]>0,y[26]==y[25]+1)),Not(Implies(y[25]==1023,y[26]==23)),Not(Implies(u[27]>0,y[27]==y[26]+1)),Not(Implies(y[26]==1023,y[27]==23)),Not(Implies(u[28]>0,y[28]==y[27]+1)),Not(Implies(y[27]==1023,y[28]==23)),Not(Implies(u[29]>0,y[29]==y[28]+1)),Not(Implies(y[28]==1023,y[29]==23)),Not(Implies(u[30]>0,y[30]==y[29]+1)),Not(Implies(y[29]==1023,y[30]==23)),Not(Implies(u[31]>0,y[31]==y[30]+1)),Not(Implies(y[30]==1023,y[31]==23)),Not(Implies(u[32]>0,y[32]==y[31]+1)),Not(Implies(y[31]==1023,y[32]==23)),Not(Implies(u[33]>0,y[33]==y[32]+1)),Not(Implies(y[32]==1023,y[33]==23)),Not(Implies(u[34]>0,y[34]==y[33]+1)),Not(Implies(y[33]==1023,y[34]==23)),Not(Implies(u[35]>0,y[35]==y[34]+1)),Not(Implies(y[34]==1023,y[35]==23)),Not(Implies(u[36]>0,y[36]==y[35]+1)),Not(Implies(y[35]==1023,y[36]==23)),Not(Implies(u[37]>0,y[37]==y[36]+1)),Not(Implies(y[36]==1023,y[37]==23)),Not(Implies(u[38]>0,y[38]==y[37]+1)),Not(Implies(y[37]==1023,y[38]==23)),Not(Implies(u[39]>0,y[39]==y[38]+1)),Not(Implies(y[38]==1023,y[39]==23)),Not(Implies(u[40]>0,y[40]==y[39]+1)),Not(Implies(y[39]==1023,y[40]==23)),Not(Implies(u[41]>0,y[41]==y[40]+1)),Not(Implies(y[40]==1023,y[41]==23)),Not(Implies(u[42]>0,y[42]==y[41]+1)),Not(Implies(y[41]==1023,y[42]==23)),Not(Implies(u[43]>0,y[43]==y[42]+1)),Not(Implies(y[42]==1023,y[43]==23)),Not(Implies(u[44]>0,y[44]==y[43]+1)),Not(Implies(y[43]==1023,y[44]==23)),Not(Implies(u[45]>0,y[45]==y[44]+1)),Not(Implies(y[44]==1023,y[45]==23)),Not(Implies(u[46]>0,y[46]==y[45]+1)),Not(Implies(y[45]==1023,y[46]==23)),Not(Implies(u[47]>0,y[47]==y[46]+1)),Not(Implies(y[46]==1023,y[47]==23)),Not(Implies(u[48]>0,y[48]==y[47]+1)),Not(Implies(y[47]==1023,y[48]==23)),Not(Implies(u[49]>0,y[49]==y[48]+1)),Not(Implies(y[48]==1023,y[49]==23)),Not(Implies(u[50]>0,y[50]==y[49]+1)),Not(Implies(y[49]==1023,y[50]==23)),Not(Implies(u[51]>0,y[51]==y[50]+1)),Not(Implies(y[50]==1023,y[51]==23)),Not(Implies(u[52]>0,y[52]==y[51]+1)),Not(Implies(y[51]==1023,y[52]==23)),Not(Implies(u[53]>0,y[53]==y[52]+1)),Not(Implies(y[52]==1023,y[53]==23)),Not(Implies(u[54]>0,y[54]==y[53]+1)),Not(Implies(y[53]==1023,y[54]==23)),Not(Implies(u[55]>0,y[55]==y[54]+1)),Not(Implies(y[54]==1023,y[55]==23)),Not(Implies(u[56]>0,y[56]==y[55]+1)),Not(Implies(y[55]==1023,y[56]==23)),Not(Implies(u[57]>0,y[57]==y[56]+1)),Not(Implies(y[56]==1023,y[57]==23)),Not(Implies(u[58]>0,y[58]==y[57]+1)),Not(Implies(y[57]==1023,y[58]==23)),Not(Implies(u[59]>0,y[59]==y[58]+1)),Not(Implies(y[58]==1023,y[59]==23)),Not(Implies(u[60]>0,y[60]==y[59]+1)),Not(Implies(y[59]==1023,y[60]==23)),Not(Implies(u[61]>0,y[61]==y[60]+1)),Not(Implies(y[60]==1023,y[61]==23)),Not(Implies(u[62]>0,y[62]==y[61]+1)),Not(Implies(y[61]==1023,y[62]==23)),Not(Implies(u[63]>0,y[63]==y[62]+1)),Not(Implies(y[62]==1023,y[63]==23)),Not(Implies(u[64]>0,y[64]==y[63]+1)),Not(Implies(y[63]==1023,y[64]==23)),Not(Implies(u[65]>0,y[65]==y[64]+1)),Not(Implies(y[64]==1023,y[65]==23)),Not(Implies(u[66]>0,y[66]==y[65]+1)),Not(Implies(y[65]==1023,y[66]==23)),Not(Implies(u[67]>0,y[67]==y[66]+1)),Not(Implies(y[66]==1023,y[67]==23)),Not(Implies(u[68]>0,y[68]==y[67]+1)),Not(Implies(y[67]==1023,y[68]==23)),Not(Implies(u[69]>0,y[69]==y[68]+1)),Not(Implies(y[68]==1023,y[69]==23)),Not(Implies(u[70]>0,y[70]==y[69]+1)),Not(Implies(y[69]==1023,y[70]==23)),Not(Implies(u[71]>0,y[71]==y[70]+1)),Not(Implies(y[70]==1023,y[71]==23)),Not(Implies(u[72]>0,y[72]==y[71]+1)),Not(Implies(y[71]==1023,y[72]==23)),Not(Implies(u[73]>0,y[73]==y[72]+1)),Not(Implies(y[72]==1023,y[73]==23)),Not(Implies(u[74]>0,y[74]==y[73]+1)),Not(Implies(y[73]==1023,y[74]==23)),Not(Implies(u[75]>0,y[75]==y[74]+1)),Not(Implies(y[74]==1023,y[75]==23)),Not(Implies(u[76]>0,y[76]==y[75]+1)),Not(Implies(y[75]==1023,y[76]==23)),Not(Implies(u[77]>0,y[77]==y[76]+1)),Not(Implies(y[76]==1023,y[77]==23)),Not(Implies(u[78]>0,y[78]==y[77]+1)),Not(Implies(y[77]==1023,y[78]==23)),Not(Implies(u[79]>0,y[79]==y[78]+1)),Not(Implies(y[78]==1023,y[79]==23)),Not(Implies(u[80]>0,y[80]==y[79]+1)),Not(Implies(y[79]==1023,y[80]==23)),Not(Implies(u[81]>0,y[81]==y[80]+1)),Not(Implies(y[80]==1023,y[81]==23)),Not(Implies(u[82]>0,y[82]==y[81]+1)),Not(Implies(y[81]==1023,y[82]==23)),Not(Implies(u[83]>0,y[83]==y[82]+1)),Not(Implies(y[82]==1023,y[83]==23)),Not(Implies(u[84]>0,y[84]==y[83]+1)),Not(Implies(y[83]==1023,y[84]==23)),Not(Implies(u[85]>0,y[85]==y[84]+1)),Not(Implies(y[84]==1023,y[85]==23)),Not(Implies(u[86]>0,y[86]==y[85]+1)),Not(Implies(y[85]==1023,y[86]==23)),Not(Implies(u[87]>0,y[87]==y[86]+1)),Not(Implies(y[86]==1023,y[87]==23)),Not(Implies(u[88]>0,y[88]==y[87]+1)),Not(Implies(y[87]==1023,y[88]==23)),Not(Implies(u[89]>0,y[89]==y[88]+1)),Not(Implies(y[88]==1023,y[89]==23)),Not(Implies(u[90]>0,y[90]==y[89]+1)),Not(Implies(y[89]==1023,y[90]==23)),Not(Implies(u[91]>0,y[91]==y[90]+1)),Not(Implies(y[90]==1023,y[91]==23)),Not(Implies(u[92]>0,y[92]==y[91]+1)),Not(Implies(y[91]==1023,y[92]==23)),Not(Implies(u[93]>0,y[93]==y[92]+1)),Not(Implies(y[92]==1023,y[93]==23)),Not(Implies(u[94]>0,y[94]==y[93]+1)),Not(Implies(y[93]==1023,y[94]==23)),Not(Implies(u[95]>0,y[95]==y[94]+1)),Not(Implies(y[94]==1023,y[95]==23)),Not(Implies(u[96]>0,y[96]==y[95]+1)),Not(Implies(y[95]==1023,y[96]==23)),Not(Implies(u[97]>0,y[97]==y[96]+1)),Not(Implies(y[96]==1023,y[97]==23)),Not(Implies(u[98]>0,y[98]==y[97]+1)),Not(Implies(y[97]==1023,y[98]==23)),Not(Implies(u[99]>0,y[99]==y[98]+1)),Not(Implies(y[98]==1023,y[99]==23)),Not(Implies(u[100]>0,y[100]==y[99]+1)),Not(Implies(y[99]==1023,y[100]==23)),Not(Implies(u[101]>0,y[101]==y[100]+1)),Not(Implies(y[100]==1023,y[101]==23)),Not(Implies(u[102]>0,y[102]==y[101]+1)),Not(Implies(y[101]==1023,y[102]==23)),Not(Implies(u[103]>0,y[103]==y[102]+1)),Not(Implies(y[102]==1023,y[103]==23)),Not(Implies(u[104]>0,y[104]==y[103]+1)),Not(Implies(y[103]==1023,y[104]==23)),Not(Implies(u[105]>0,y[105]==y[104]+1)),Not(Implies(y[104]==1023,y[105]==23)),Not(Implies(u[106]>0,y[106]==y[105]+1)),Not(Implies(y[105]==1023,y[106]==23)),Not(Implies(u[107]>0,y[107]==y[106]+1)),Not(Implies(y[106]==1023,y[107]==23)),Not(Implies(u[108]>0,y[108]==y[107]+1)),Not(Implies(y[107]==1023,y[108]==23)),Not(Implies(u[109]>0,y[109]==y[108]+1)),Not(Implies(y[108]==1023,y[109]==23)),Not(Implies(u[110]>0,y[110]==y[109]+1)),Not(Implies(y[109]==1023,y[110]==23)),Not(Implies(u[111]>0,y[111]==y[110]+1)),Not(Implies(y[110]==1023,y[111]==23)),Not(Implies(u[112]>0,y[112]==y[111]+1)),Not(Implies(y[111]==1023,y[112]==23)),Not(Implies(u[113]>0,y[113]==y[112]+1)),Not(Implies(y[112]==1023,y[113]==23)),Not(Implies(u[114]>0,y[114]==y[113]+1)),Not(Implies(y[113]==1023,y[114]==23)),Not(Implies(u[115]>0,y[115]==y[114]+1)),Not(Implies(y[114]==1023,y[115]==23)),Not(Implies(u[116]>0,y[116]==y[115]+1)),Not(Implies(y[115]==1023,y[116]==23)),Not(Implies(u[117]>0,y[117]==y[116]+1)),Not(Implies(y[116]==1023,y[117]==23)),Not(Implies(u[118]>0,y[118]==y[117]+1)),Not(Implies(y[117]==1023,y[118]==23)),Not(Implies(u[119]>0,y[119]==y[118]+1)),Not(Implies(y[118]==1023,y[119]==23)),Not(Implies(u[120]>0,y[120]==y[119]+1)),Not(Implies(y[119]==1023,y[120]==23)),Not(Implies(u[121]>0,y[121]==y[120]+1)),Not(Implies(y[120]==1023,y[121]==23)),Not(Implies(u[122]>0,y[122]==y[121]+1)),Not(Implies(y[121]==1023,y[122]==23)),Not(Implies(u[123]>0,y[123]==y[122]+1)),Not(Implies(y[122]==1023,y[123]==23)),Not(Implies(u[124]>0,y[124]==y[123]+1)),Not(Implies(y[123]==1023,y[124]==23)),Not(Implies(u[125]>0,y[125]==y[124]+1)),Not(Implies(y[124]==1023,y[125]==23)),Not(Implies(u[126]>0,y[126]==y[125]+1)),Not(Implies(y[125]==1023,y[126]==23)),Not(Implies(u[127]>0,y[127]==y[126]+1)),Not(Implies(y[126]==1023,y[127]==23)),Not(Implies(u[128]>0,y[128]==y[127]+1)),Not(Implies(y[127]==1023,y[128]==23)),Not(Implies(u[129]>0,y[129]==y[128]+1)),Not(Implies(y[128]==1023,y[129]==23)),Not(Implies(u[130]>0,y[130]==y[129]+1)),Not(Implies(y[129]==1023,y[130]==23)),Not(Implies(u[131]>0,y[131]==y[130]+1)),Not(Implies(y[130]==1023,y[131]==23)),Not(Implies(u[132]>0,y[132]==y[131]+1)),Not(Implies(y[131]==1023,y[132]==23)),Not(Implies(u[133]>0,y[133]==y[132]+1)),Not(Implies(y[132]==1023,y[133]==23)),Not(Implies(u[134]>0,y[134]==y[133]+1)),Not(Implies(y[133]==1023,y[134]==23)),Not(Implies(u[135]>0,y[135]==y[134]+1)),Not(Implies(y[134]==1023,y[135]==23)),Not(Implies(u[136]>0,y[136]==y[135]+1)),Not(Implies(y[135]==1023,y[136]==23)),Not(Implies(u[137]>0,y[137]==y[136]+1)),Not(Implies(y[136]==1023,y[137]==23)),Not(Implies(u[138]>0,y[138]==y[137]+1)),Not(Implies(y[137]==1023,y[138]==23)),Not(Implies(u[139]>0,y[139]==y[138]+1)),Not(Implies(y[138]==1023,y[139]==23)),Not(Implies(u[140]>0,y[140]==y[139]+1)),Not(Implies(y[139]==1023,y[140]==23)),Not(Implies(u[141]>0,y[141]==y[140]+1)),Not(Implies(y[140]==1023,y[141]==23)),Not(Implies(u[142]>0,y[142]==y[141]+1)),Not(Implies(y[141]==1023,y[142]==23)),Not(Implies(u[143]>0,y[143]==y[142]+1)),Not(Implies(y[142]==1023,y[143]==23)),Not(Implies(u[144]>0,y[144]==y[143]+1)),Not(Implies(y[143]==1023,y[144]==23)),Not(Implies(u[145]>0,y[145]==y[144]+1)),Not(Implies(y[144]==1023,y[145]==23)),Not(Implies(u[146]>0,y[146]==y[145]+1)),Not(Implies(y[145]==1023,y[146]==23)),Not(Implies(u[147]>0,y[147]==y[146]+1)),Not(Implies(y[146]==1023,y[147]==23)),Not(Implies(u[148]>0,y[148]==y[147]+1)),Not(Implies(y[147]==1023,y[148]==23)),Not(Implies(u[149]>0,y[149]==y[148]+1)),Not(Implies(y[148]==1023,y[149]==23)),Not(Implies(u[150]>0,y[150]==y[149]+1)),Not(Implies(y[149]==1023,y[150]==23)),Not(Implies(u[151]>0,y[151]==y[150]+1)),Not(Implies(y[150]==1023,y[151]==23)),Not(Implies(u[152]>0,y[152]==y[151]+1)),Not(Implies(y[151]==1023,y[152]==23)),Not(Implies(u[153]>0,y[153]==y[152]+1)),Not(Implies(y[152]==1023,y[153]==23)),Not(Implies(u[154]>0,y[154]==y[153]+1)),Not(Implies(y[153]==1023,y[154]==23)),Not(Implies(u[155]>0,y[155]==y[154]+1)),Not(Implies(y[154]==1023,y[155]==23)),Not(Implies(u[156]>0,y[156]==y[155]+1)),Not(Implies(y[155]==1023,y[156]==23)),Not(Implies(u[157]>0,y[157]==y[156]+1)),Not(Implies(y[156]==1023,y[157]==23)),Not(Implies(u[158]>0,y[158]==y[157]+1)),Not(Implies(y[157]==1023,y[158]==23)),Not(Implies(u[159]>0,y[159]==y[158]+1)),Not(Implies(y[158]==1023,y[159]==23)),Not(Implies(u[160]>0,y[160]==y[159]+1)),Not(Implies(y[159]==1023,y[160]==23)),Not(Implies(u[161]>0,y[161]==y[160]+1)),Not(Implies(y[160]==1023,y[161]==23)),Not(Implies(u[162]>0,y[162]==y[161]+1)),Not(Implies(y[161]==1023,y[162]==23)),Not(Implies(u[163]>0,y[163]==y[162]+1)),Not(Implies(y[162]==1023,y[163]==23)),Not(Implies(u[164]>0,y[164]==y[163]+1)),Not(Implies(y[163]==1023,y[164]==23)),Not(Implies(u[165]>0,y[165]==y[164]+1)),Not(Implies(y[164]==1023,y[165]==23)),Not(Implies(u[166]>0,y[166]==y[165]+1)),Not(Implies(y[165]==1023,y[166]==23)),Not(Implies(u[167]>0,y[167]==y[166]+1)),Not(Implies(y[166]==1023,y[167]==23)),Not(Implies(u[168]>0,y[168]==y[167]+1)),Not(Implies(y[167]==1023,y[168]==23)),Not(Implies(u[169]>0,y[169]==y[168]+1)),Not(Implies(y[168]==1023,y[169]==23)),Not(Implies(u[170]>0,y[170]==y[169]+1)),Not(Implies(y[169]==1023,y[170]==23)),Not(Implies(u[171]>0,y[171]==y[170]+1)),Not(Implies(y[170]==1023,y[171]==23)),Not(Implies(u[172]>0,y[172]==y[171]+1)),Not(Implies(y[171]==1023,y[172]==23)),Not(Implies(u[173]>0,y[173]==y[172]+1)),Not(Implies(y[172]==1023,y[173]==23)),Not(Implies(u[174]>0,y[174]==y[173]+1)),Not(Implies(y[173]==1023,y[174]==23)),Not(Implies(u[175]>0,y[175]==y[174]+1)),Not(Implies(y[174]==1023,y[175]==23)),Not(Implies(u[176]>0,y[176]==y[175]+1)),Not(Implies(y[175]==1023,y[176]==23)),Not(Implies(u[177]>0,y[177]==y[176]+1)),Not(Implies(y[176]==1023,y[177]==23)),Not(Implies(u[178]>0,y[178]==y[177]+1)),Not(Implies(y[177]==1023,y[178]==23)),Not(Implies(u[179]>0,y[179]==y[178]+1)),Not(Implies(y[178]==1023,y[179]==23)),Not(Implies(u[180]>0,y[180]==y[179]+1)),Not(Implies(y[179]==1023,y[180]==23)),Not(Implies(u[181]>0,y[181]==y[180]+1)),Not(Implies(y[180]==1023,y[181]==23)),Not(Implies(u[182]>0,y[182]==y[181]+1)),Not(Implies(y[181]==1023,y[182]==23)),Not(Implies(u[183]>0,y[183]==y[182]+1)),Not(Implies(y[182]==1023,y[183]==23)),Not(Implies(u[184]>0,y[184]==y[183]+1)),Not(Implies(y[183]==1023,y[184]==23)),Not(Implies(u[185]>0,y[185]==y[184]+1)),Not(Implies(y[184]==1023,y[185]==23)),Not(Implies(u[186]>0,y[186]==y[185]+1)),Not(Implies(y[185]==1023,y[186]==23)),Not(Implies(u[187]>0,y[187]==y[186]+1)),Not(Implies(y[186]==1023,y[187]==23)),Not(Implies(u[188]>0,y[188]==y[187]+1)),Not(Implies(y[187]==1023,y[188]==23)),Not(Implies(u[189]>0,y[189]==y[188]+1)),Not(Implies(y[188]==1023,y[189]==23)),Not(Implies(u[190]>0,y[190]==y[189]+1)),Not(Implies(y[189]==1023,y[190]==23)),Not(Implies(u[191]>0,y[191]==y[190]+1)),Not(Implies(y[190]==1023,y[191]==23)),Not(Implies(u[192]>0,y[192]==y[191]+1)),Not(Implies(y[191]==1023,y[192]==23)),Not(Implies(u[193]>0,y[193]==y[192]+1)),Not(Implies(y[192]==1023,y[193]==23)),Not(Implies(u[194]>0,y[194]==y[193]+1)),Not(Implies(y[193]==1023,y[194]==23)),Not(Implies(u[195]>0,y[195]==y[194]+1)),Not(Implies(y[194]==1023,y[195]==23)),Not(Implies(u[196]>0,y[196]==y[195]+1)),Not(Implies(y[195]==1023,y[196]==23)),Not(Implies(u[197]>0,y[197]==y[196]+1)),Not(Implies(y[196]==1023,y[197]==23)),Not(Implies(u[198]>0,y[198]==y[197]+1)),Not(Implies(y[197]==1023,y[198]==23)),Not(Implies(u[199]>0,y[199]==y[198]+1)),Not(Implies(y[198]==1023,y[199]==23)),Not(Implies(u[200]>0,y[200]==y[199]+1)),Not(Implies(y[199]==1023,y[200]==23)),Not(Implies(u[201]>0,y[201]==y[200]+1)),Not(Implies(y[200]==1023,y[201]==23)),Not(Implies(u[202]>0,y[202]==y[201]+1)),Not(Implies(y[201]==1023,y[202]==23)),Not(Implies(u[203]>0,y[203]==y[202]+1)),Not(Implies(y[202]==1023,y[203]==23)),Not(Implies(u[204]>0,y[204]==y[203]+1)),Not(Implies(y[203]==1023,y[204]==23)),Not(Implies(u[205]>0,y[205]==y[204]+1)),Not(Implies(y[204]==1023,y[205]==23)),Not(Implies(u[206]>0,y[206]==y[205]+1)),Not(Implies(y[205]==1023,y[206]==23)),Not(Implies(u[207]>0,y[207]==y[206]+1)),Not(Implies(y[206]==1023,y[207]==23)),Not(Implies(u[208]>0,y[208]==y[207]+1)),Not(Implies(y[207]==1023,y[208]==23)),Not(Implies(u[209]>0,y[209]==y[208]+1)),Not(Implies(y[208]==1023,y[209]==23)),Not(Implies(u[210]>0,y[210]==y[209]+1)),Not(Implies(y[209]==1023,y[210]==23)),Not(Implies(u[211]>0,y[211]==y[210]+1)),Not(Implies(y[210]==1023,y[211]==23)),Not(Implies(u[212]>0,y[212]==y[211]+1)),Not(Implies(y[211]==1023,y[212]==23)),Not(Implies(u[213]>0,y[213]==y[212]+1)),Not(Implies(y[212]==1023,y[213]==23)),Not(Implies(u[214]>0,y[214]==y[213]+1)),Not(Implies(y[213]==1023,y[214]==23)),Not(Implies(u[215]>0,y[215]==y[214]+1)),Not(Implies(y[214]==1023,y[215]==23)),Not(Implies(u[216]>0,y[216]==y[215]+1)),Not(Implies(y[215]==1023,y[216]==23)),Not(Implies(u[217]>0,y[217]==y[216]+1)),Not(Implies(y[216]==1023,y[217]==23)),Not(Implies(u[218]>0,y[218]==y[217]+1)),Not(Implies(y[217]==1023,y[218]==23)),Not(Implies(u[219]>0,y[219]==y[218]+1)),Not(Implies(y[218]==1023,y[219]==23)),Not(Implies(u[220]>0,y[220]==y[219]+1)),Not(Implies(y[219]==1023,y[220]==23)),Not(Implies(u[221]>0,y[221]==y[220]+1)),Not(Implies(y[220]==1023,y[221]==23)),Not(Implies(u[222]>0,y[222]==y[221]+1)),Not(Implies(y[221]==1023,y[222]==23)),Not(Implies(u[223]>0,y[223]==y[222]+1)),Not(Implies(y[222]==1023,y[223]==23)),Not(Implies(u[224]>0,y[224]==y[223]+1)),Not(Implies(y[223]==1023,y[224]==23)),Not(Implies(u[225]>0,y[225]==y[224]+1)),Not(Implies(y[224]==1023,y[225]==23)),Not(Implies(u[226]>0,y[226]==y[225]+1)),Not(Implies(y[225]==1023,y[226]==23)),Not(Implies(u[227]>0,y[227]==y[226]+1)),Not(Implies(y[226]==1023,y[227]==23)),Not(Implies(u[228]>0,y[228]==y[227]+1)),Not(Implies(y[227]==1023,y[228]==23)),Not(Implies(u[229]>0,y[229]==y[228]+1)),Not(Implies(y[228]==1023,y[229]==23)),Not(Implies(u[230]>0,y[230]==y[229]+1)),Not(Implies(y[229]==1023,y[230]==23)),Not(Implies(u[231]>0,y[231]==y[230]+1)),Not(Implies(y[230]==1023,y[231]==23)),Not(Implies(u[232]>0,y[232]==y[231]+1)),Not(Implies(y[231]==1023,y[232]==23)),Not(Implies(u[233]>0,y[233]==y[232]+1)),Not(Implies(y[232]==1023,y[233]==23)),Not(Implies(u[234]>0,y[234]==y[233]+1)),Not(Implies(y[233]==1023,y[234]==23)),Not(Implies(u[235]>0,y[235]==y[234]+1)),Not(Implies(y[234]==1023,y[235]==23)),Not(Implies(u[236]>0,y[236]==y[235]+1)),Not(Implies(y[235]==1023,y[236]==23)),Not(Implies(u[237]>0,y[237]==y[236]+1)),Not(Implies(y[236]==1023,y[237]==23)),Not(Implies(u[238]>0,y[238]==y[237]+1)),Not(Implies(y[237]==1023,y[238]==23)),Not(Implies(u[239]>0,y[239]==y[238]+1)),Not(Implies(y[238]==1023,y[239]==23)),Not(Implies(u[240]>0,y[240]==y[239]+1)),Not(Implies(y[239]==1023,y[240]==23)),Not(Implies(u[241]>0,y[241]==y[240]+1)),Not(Implies(y[240]==1023,y[241]==23)),Not(Implies(u[242]>0,y[242]==y[241]+1)),Not(Implies(y[241]==1023,y[242]==23)),Not(Implies(u[243]>0,y[243]==y[242]+1)),Not(Implies(y[242]==1023,y[243]==23)),Not(Implies(u[244]>0,y[244]==y[243]+1)),Not(Implies(y[243]==1023,y[244]==23)),Not(Implies(u[245]>0,y[245]==y[244]+1)),Not(Implies(y[244]==1023,y[245]==23)),Not(Implies(u[246]>0,y[246]==y[245]+1)),Not(Implies(y[245]==1023,y[246]==23)),Not(Implies(u[247]>0,y[247]==y[246]+1)),Not(Implies(y[246]==1023,y[247]==23)),Not(Implies(u[248]>0,y[248]==y[247]+1)),Not(Implies(y[247]==1023,y[248]==23)),Not(Implies(u[249]>0,y[249]==y[248]+1)),Not(Implies(y[248]==1023,y[249]==23)),Not(Implies(u[250]>0,y[250]==y[249]+1)),Not(Implies(y[249]==1023,y[250]==23)),Not(Implies(u[251]>0,y[251]==y[250]+1)),Not(Implies(y[250]==1023,y[251]==23)),Not(Implies(u[252]>0,y[252]==y[251]+1)),Not(Implies(y[251]==1023,y[252]==23)),Not(Implies(u[253]>0,y[253]==y[252]+1)),Not(Implies(y[252]==1023,y[253]==23)),Not(Implies(u[254]>0,y[254]==y[253]+1)),Not(Implies(y[253]==1023,y[254]==23)),Not(Implies(u[255]>0,y[255]==y[254]+1)),Not(Implies(y[254]==1023,y[255]==23)),Not(Implies(u[256]>0,y[256]==y[255]+1)),Not(Implies(y[255]==1023,y[256]==23)),Not(Implies(u[257]>0,y[257]==y[256]+1)),Not(Implies(y[256]==1023,y[257]==23)),Not(Implies(u[258]>0,y[258]==y[257]+1)),Not(Implies(y[257]==1023,y[258]==23)),Not(Implies(u[259]>0,y[259]==y[258]+1)),Not(Implies(y[258]==1023,y[259]==23)),Not(Implies(u[260]>0,y[260]==y[259]+1)),Not(Implies(y[259]==1023,y[260]==23)),Not(Implies(u[261]>0,y[261]==y[260]+1)),Not(Implies(y[260]==1023,y[261]==23)),Not(Implies(u[262]>0,y[262]==y[261]+1)),Not(Implies(y[261]==1023,y[262]==23)),Not(Implies(u[263]>0,y[263]==y[262]+1)),Not(Implies(y[262]==1023,y[263]==23)),Not(Implies(u[264]>0,y[264]==y[263]+1)),Not(Implies(y[263]==1023,y[264]==23)),Not(Implies(u[265]>0,y[265]==y[264]+1)),Not(Implies(y[264]==1023,y[265]==23)),Not(Implies(u[266]>0,y[266]==y[265]+1)),Not(Implies(y[265]==1023,y[266]==23)),Not(Implies(u[267]>0,y[267]==y[266]+1)),Not(Implies(y[266]==1023,y[267]==23)),Not(Implies(u[268]>0,y[268]==y[267]+1)),Not(Implies(y[267]==1023,y[268]==23)),Not(Implies(u[269]>0,y[269]==y[268]+1)),Not(Implies(y[268]==1023,y[269]==23)),Not(Implies(u[270]>0,y[270]==y[269]+1)),Not(Implies(y[269]==1023,y[270]==23)),Not(Implies(u[271]>0,y[271]==y[270]+1)),Not(Implies(y[270]==1023,y[271]==23)),Not(Implies(u[272]>0,y[272]==y[271]+1)),Not(Implies(y[271]==1023,y[272]==23)),Not(Implies(u[273]>0,y[273]==y[272]+1)),Not(Implies(y[272]==1023,y[273]==23)),Not(Implies(u[274]>0,y[274]==y[273]+1)),Not(Implies(y[273]==1023,y[274]==23)),Not(Implies(u[275]>0,y[275]==y[274]+1)),Not(Implies(y[274]==1023,y[275]==23)),Not(Implies(u[276]>0,y[276]==y[275]+1)),Not(Implies(y[275]==1023,y[276]==23)),Not(Implies(u[277]>0,y[277]==y[276]+1)),Not(Implies(y[276]==1023,y[277]==23)),Not(Implies(u[278]>0,y[278]==y[277]+1)),Not(Implies(y[277]==1023,y[278]==23)),Not(Implies(u[279]>0,y[279]==y[278]+1)),Not(Implies(y[278]==1023,y[279]==23)),Not(Implies(u[280]>0,y[280]==y[279]+1)),Not(Implies(y[279]==1023,y[280]==23)),Not(Implies(u[281]>0,y[281]==y[280]+1)),Not(Implies(y[280]==1023,y[281]==23)),Not(Implies(u[282]>0,y[282]==y[281]+1)),Not(Implies(y[281]==1023,y[282]==23)),Not(Implies(u[283]>0,y[283]==y[282]+1)),Not(Implies(y[282]==1023,y[283]==23)),Not(Implies(u[284]>0,y[284]==y[283]+1)),Not(Implies(y[283]==1023,y[284]==23)),Not(Implies(u[285]>0,y[285]==y[284]+1)),Not(Implies(y[284]==1023,y[285]==23)),Not(Implies(u[286]>0,y[286]==y[285]+1)),Not(Implies(y[285]==1023,y[286]==23)),Not(Implies(u[287]>0,y[287]==y[286]+1)),Not(Implies(y[286]==1023,y[287]==23)),Not(Implies(u[288]>0,y[288]==y[287]+1)),Not(Implies(y[287]==1023,y[288]==23)),Not(Implies(u[289]>0,y[289]==y[288]+1)),Not(Implies(y[288]==1023,y[289]==23)),Not(Implies(u[290]>0,y[290]==y[289]+1)),Not(Implies(y[289]==1023,y[290]==23)),Not(Implies(u[291]>0,y[291]==y[290]+1)),Not(Implies(y[290]==1023,y[291]==23)),Not(Implies(u[292]>0,y[292]==y[291]+1)),Not(Implies(y[291]==1023,y[292]==23)),Not(Implies(u[293]>0,y[293]==y[292]+1)),Not(Implies(y[292]==1023,y[293]==23)),Not(Implies(u[294]>0,y[294]==y[293]+1)),Not(Implies(y[293]==1023,y[294]==23)),Not(Implies(u[295]>0,y[295]==y[294]+1)),Not(Implies(y[294]==1023,y[295]==23)),Not(Implies(u[296]>0,y[296]==y[295]+1)),Not(Implies(y[295]==1023,y[296]==23)),Not(Implies(u[297]>0,y[297]==y[296]+1)),Not(Implies(y[296]==1023,y[297]==23)),Not(Implies(u[298]>0,y[298]==y[297]+1)),Not(Implies(y[297]==1023,y[298]==23)),Not(Implies(u[299]>0,y[299]==y[298]+1)),Not(Implies(y[298]==1023,y[299]==23)))))))
res=s.check()
if (res.r ==  Z3_L_FALSE):
	 print('Requirements Table Consistent (unsat)')
	 sys.exit(1)
else:
	 if (res.r == Z3_L_TRUE):
		 print('Requirements Table Inconsistent (sat)')
		 sys.exit(-1)
	 else:
		 print('unknown')
		 sys.exit(0)
