grammar matlab;

@header {
package generated;

import requirements2Z3.rqt.*;

}

g returns [RQTable rqt]
:
	composedExpression {$rqt = $composedExpression.rqt;} |
	primaryExpression {$rqt = $primaryExpression.rqt;}
;

composedExpression returns [ComposedRQTable rqt]
:
	'table' fstName=IDENTIFIER CR fst=primaryExpression CR 'endtable' CR
	'table' sndName=IDENTIFIER CR snd=primaryExpression CR 'endtable' (CR)*
	{
		$rqt=new ComposedRQTable();
		$fst.rqt.setName($fstName.text); $snd.rqt.setName($sndName.text);
		$rqt.add($fst.rqt); $rqt.add($snd.rqt);
	}
	(CR 'table' name=IDENTIFIER CR primaryExpr=primaryExpression CR 'endtable' (CR|WS)*
	{
		$primaryExpr.rqt.setName($name.text);
		$rqt.add($primaryExpr.rqt);
	})*
;

primaryExpression returns [RQTable rqt]
:
	ts=timestampdefinition vsdefs=variablesdefinitions rqdefs=requirementsdefinitions
	{$rqt=new RQTable($ts.td,$vsdefs.vs,$rqdefs.rqs);}|
 vsdefs=variablesdefinitions rqdefs=requirementsdefinitions
	{$rqt=new RQTable(null,$vsdefs.vs,$rqdefs.rqs);}
;

timestampdefinition returns [TimestampDefinition td]
:
	'Ts=' c=CONSTANT SEMICOLUMN CR {$td=new TimestampDefinition(Double.parseDouble($c.text));}
;

variablesdefinitions returns [Variables vs]
:
	{$vs=new Variables();}
	'vardef' CR (variabledefinition {$vs.add($variabledefinition.v);})* 'endvardef' CR
;

variabledefinition returns [Variable v]
:
	i=IDENTIFIER COMMA spec=typeSpecifier COMMA type=io  SEMICOLUMN CR
	{$v=new Variable($i.text,$spec.tipo,$type.tipo);}
;

requirementsdefinitions returns [Requirements rqs]
:
	{$rqs=new Requirements();}
	'reqdef' CR (requirement {$rqs.add($requirement.rq);})* 'endreqdef'
;

requirement returns [Requirement rq]
:
	precondition=logical_expression ',' postcondition=logical_expression SEMICOLUMN CR
	{$rq=new Requirement($precondition.f,$postcondition.f);}	
;

logical_expression returns [PFormula f]
: LPAR nested=logical_expression RPAR {$f=$nested.f;}
| atomic_expression {$f=$atomic_expression.f;}
| NOT LPAR logical_expression RPAR {$f=new NegationFormula($logical_expression.f);}
| l=logical_expression AND r=logical_expression {$f=new AndFormula($l.f,$r.f);}
| l=logical_expression OR r=logical_expression {$f=new OrFormula($l.f,$r.f);}
| l=logical_expression IMPLIES r=logical_expression {$f=new ImpliesFormula($l.f,$r.f);}
;

atomic_expression returns [PFormula f]
:
	TRUE 						{$f=new True();}
	|	is_startup 				{$f=$is_startup.f;}
	|	is_not_startup  		{$f=$is_not_startup.f;}
	|	dur_expression			{$f=$dur_expression.f;}
	|	relational_expression 	{$f=$relational_expression.f;}
;

dur_expression returns [PFormula f]
:
	DUR LPAR or_exp=logical_expression RPAR durop=(GE_OP | LE_OP | EQ_OP | LEQ_OP | GEQ_OP | NE_OP) c=CONSTANT
	{$f=new DurFormula($or_exp.f,RelationalOperator.toRelationalOperator($durop.text),Double.parseDouble($c.text));}
;

relational_expression returns [PFormula f]
:
	l=arithmetic_expression rop=(GE_OP | LE_OP | EQ_OP | LEQ_OP | GEQ_OP | NE_OP) r=arithmetic_expression
	{$f=new RelationalExpression($l.exp,RelationalOperator.toRelationalOperator($rop.text),$r.exp);}
	| LPAR nested=relational_expression RPAR { $f = $nested.f; }
;

arithmetic_expression returns [Expression exp]
:
	multiplicative_expression {$exp=$multiplicative_expression.exp;}
	| l=arithmetic_expression aop=(PLUS | MINUS) r=multiplicative_expression
	  {$exp=new ArithmeticExpression($l.exp,ArithmeticOperator.toArithmeticOperator($aop.text),$r.exp);}
	| LPAR nested=arithmetic_expression RPAR { $exp = $nested.exp;}
;

prev_expression returns [Expression exp]
:
	PREV LPAR i=IDENTIFIER {$exp=new PrevExpression(new Identifier($i.text));} RPAR
;

postfix_expression returns [Expression exp]
:
	i=IDENTIFIER {$exp=new Identifier($i.text);}
	| c=CONSTANT {$exp=new Constant(Double.parseDouble($c.text));}
	| p=prev_expression {$exp=$p.exp;}
;

unary_expression returns [Expression exp]
:
	p=postfix_expression {$exp=$p.exp;}
	| op=(PLUS | MINUS) p=postfix_expression {$exp=new UnaryExpression(ArithmeticOperator.toArithmeticOperator($op.text),$p.exp);}
;


multiplicative_expression returns [Expression exp]
:
	u=unary_expression {$exp=$u.exp;}
	| l=multiplicative_expression op=(MULT | DIV | EXP) r=unary_expression
	{$exp=new ArithmeticExpression($l.exp,ArithmeticOperator.toArithmeticOperator($op.text),$r.exp); }
;

is_startup returns [PFormula f]
:
	ISSTARTUP {$f=new IsStartup();}
;

is_not_startup returns [PFormula f]
:
	NOT ISSTARTUP {$f=new IsStartup();}
;


typeSpecifier returns [String tipo]
:
	INT  {$tipo="Int";} | 
	REAL {$tipo="Real";}
;

io returns [String tipo]
:
	INPUT {$tipo="input";}
	| OUTPUT {$tipo="output";}
;

INPUT: 'input';
OUTPUT: 'output';


INT:
'Int'
;

REAL:
 'Real'
;

NOT
:
	'!'
;

AND
:
	'&'
;

OR
:
	'|'
;

IMPLIES
:
	'->'
;

MULT
: 
	'*' 
;

DIV
:  
	'/'
; 
EXP
: 	
	'^'
;	
	
DEFVARIABLES
:
	'defVariables'
;

ENDVARIABLES
:
	'endVariables'
;

ISSTARTUP
:
	'isStartup'
;

PLUS
:
	'+'
;

MINUS
:
	'-'
;

ARRAYMUL
:
	'.*'
;

ARRAYDIV
:
	'.\\'
;

ARRAYRDIV
:
	'./'
;

ARRAYPOW
:
	'.^'
;

LPAR
:
	'('
;

RPAR
:
	')'
;

TRUE
:
	'true'
;

PREV
:
	'prev'
;

DUR
:
	'dur'
;



LE_OP
:
	'<'
;

GE_OP
:
	'>'
;

LEQ_OP
:
	'<='
;

GEQ_OP
:
	'>='
;

EQ_OP
:
	'=='
;

NE_OP
:
	'!='
;

CONSTANT
:
	NUMBER
	(
		E SIGN? NUMBER
	)?
;

fragment NUMBER
:
	('0' .. '9')+ ('.' ( '0' .. '9')+)?
;

fragment E
:
	'E' | 'e'
;

fragment SIGN
:
	('+' | '-')
;



CR
:
	[\r\n]+
;

IDENTIFIER
:
	[a-zA-Z] [a-zA-Z0-9_]*
;

COMMA
:
	','
;

SEMICOLUMN
:
	';'
;

WS
:
	[ \t]+ -> skip
;

