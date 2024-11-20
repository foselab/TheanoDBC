grammar matlab;

@header {
package generated;

import requirements2Z3.rqt.*;

}

g returns [RQTable rqt]
	: composedExpression {$rqt = $composedExpression.rqt;}
	| primaryExpression {$rqt = $primaryExpression.rqt;}
	;

composedExpression returns [ComposedRQTable rqt]
	: DEFTABLE fstName=IDENTIFIER CR fst=primaryExpression CR ENDTABLE CR
	  DEFTABLE sndName=IDENTIFIER CR snd=primaryExpression CR ENDTABLE CR*
	  {
	  	$rqt=new ComposedRQTable();
		$fst.rqt.setName($fstName.text); $snd.rqt.setName($sndName.text);
		$rqt.add($fst.rqt); $rqt.add($snd.rqt);
	  }
	  (CR DEFTABLE name=IDENTIFIER CR pe=primaryExpression CR ENDTABLE CR*
	  {
	  	$pe.rqt.setName($name.text);
	  	$rqt.add($pe.rqt);
  	  })*
	;

primaryExpression returns [RQTable rqt]
	: ts=timestampdefinition vsdefs=variablesdefinitions rqdefs=requirementsdefinitions
	  {$rqt=new RQTable($ts.td,$vsdefs.vs,$rqdefs.rqs);}
	| vsdefs=variablesdefinitions rqdefs=requirementsdefinitions
	  {$rqt=new RQTable(null,$vsdefs.vs,$rqdefs.rqs);}
	;

timestampdefinition returns [TimestampDefinition td]
	: 'Ts=' c=CONSTANT SEMICOLUMN CR {$td=new TimestampDefinition(Double.parseDouble($c.text));}
	;

variablesdefinitions returns [Variables vs]
	: {$vs=new Variables();}
	  DEFVARIABLES CR (variabledefinition {$vs.add($variabledefinition.v);})* ENDVARIABLES CR
	;

variabledefinition returns [Variable v]
	: i=IDENTIFIER COMMA spec=typeSpecifier COMMA type=io  SEMICOLUMN CR
	  {$v=new Variable($i.text,$spec.tipo,$type.tipo);}
	;

requirementsdefinitions returns [Requirements rqs]
	: {$rqs=new Requirements();}
	  DEFREQUIREMENTS CR (requirement {$rqs.add($requirement.rq);})* ENDREQUIREMENTS
	;

requirement returns [Requirement rq]
	: precondition=logical_expression ',' postcondition=logical_expression SEMICOLUMN CR
	  {$rq=new Requirement($precondition.f,$postcondition.f);}	
	;

primary_expression returns [Expression exp]
	: i=IDENTIFIER {$exp=new Identifier($i.text);}
	| c=CONSTANT {$exp=new Constant(Double.parseDouble($c.text));}
	| p=prev_expression {$exp=$p.exp;}
	;

unary_expression returns [Expression exp]
	: primary_expression {$exp=$primary_expression.exp;}
	| op=unary_operator p=primary_expression {$exp=new UnaryExpression(ArithmeticOperator.toArithmeticOperator($op.text),$p.exp);}
	;

unary_operator
	: PLUS
	| MINUS
	;

multiplicative_expression returns [Expression exp]
	: u=unary_expression {$exp=$u.exp;}
	| l=multiplicative_expression op=(MULT | DIV | EXP) r=unary_expression
	  {$exp=new ArithmeticExpression($l.exp,ArithmeticOperator.toArithmeticOperator($op.text),$r.exp); }
	;

arithmetic_expression returns [Expression exp]
	: multiplicative_expression {$exp=$multiplicative_expression.exp;}
	| l=arithmetic_expression aop=(PLUS | MINUS) r=multiplicative_expression
	  {$exp=new ArithmeticExpression($l.exp,ArithmeticOperator.toArithmeticOperator($aop.text),$r.exp);}
	;

relational_expression returns [PFormula f]
	: l=arithmetic_expression rop=(GE_OP | LE_OP | EQ_OP | LEQ_OP | GEQ_OP | NE_OP) r=arithmetic_expression
	  {$f=new RelationalExpression($l.exp,RelationalOperator.toRelationalOperator($rop.text),$r.exp);}
	;
	
and_expression returns [PFormula f]
    : atomic_expression {$f=$atomic_expression.f;}
    | l=and_expression AND r=atomic_expression {$f=new AndFormula($l.f,$r.f);}
    ;
    
or_expression returns [PFormula f]
    : and_expression {$f=$and_expression.f;}
    | l=or_expression OR r=and_expression {$f=new OrFormula($l.f,$r.f);}
    ;
    
implies_expression returns [PFormula f]
    : or_expression {$f=$or_expression.f;}
    | l=implies_expression IMPLIES r=or_expression  {$f=new ImpliesFormula($l.f,$r.f);}
    ;

logical_expression returns [PFormula f]
	: implies_expression {$f=$implies_expression.f;} 
	;

atomic_expression returns [PFormula f]
	: TRUE								{$f=new True();}
	| i=IDENTIFIER						{$f=new BooleanVariable($i.text, true);} 
	| NOT LPAR logical_expression RPAR	{$f=new NegationFormula($logical_expression.f);}
	| is_startup 						{$f=$is_startup.f;}
	| is_not_startup  					{$f=$is_not_startup.f;}
	| dur_expression					{$f=$dur_expression.f;}
	| LPAR logical_expression RPAR		{$f=$logical_expression.f;}
	| relational_expression 			{$f=$relational_expression.f;}
	;

dur_expression returns [PFormula f]
	: DUR LPAR or_exp=logical_expression RPAR durop=(GE_OP | LE_OP | EQ_OP | LEQ_OP | GEQ_OP | NE_OP) c=CONSTANT
	  {$f=new DurFormula($or_exp.f,RelationalOperator.toRelationalOperator($durop.text),Double.parseDouble($c.text));}
	;

prev_expression returns [Expression exp]
	: PREV LPAR i=IDENTIFIER {$exp=new PrevExpression(new Identifier($i.text));} RPAR
	;

is_startup returns [PFormula f]
	: ISSTARTUP {$f=new IsStartup();}
	;

is_not_startup returns [PFormula f]
	: NOT ISSTARTUP {$f=new IsStartup();}
	;

typeSpecifier returns [String tipo]
	: INT  {$tipo="Int";}
	| REAL {$tipo="Real";}
	| BOOL {$tipo="Bool";}
	;

io returns [String tipo]
	: INPUT		{$tipo="input";}
	| OUTPUT	{$tipo="output";}
	;

INPUT
	: 'input'
	;

OUTPUT
	: 'output'
	;

INT
	: 'Int'
	;

REAL
	: 'Real'
	;

BOOL
	: 'Bool'
	;

NOT
	: '!'
	;

AND
	: '&'
	;

OR
	: '|'
	;

IMPLIES
	: '->'
	;

MULT
	: '*' 
	;

DIV
	: '/'
	;
	 
EXP
	: '^'
	;	

DEFTABLE
	: 'table'
	;
	
ENDTABLE
	: 'endtable'
	;
	
DEFVARIABLES
	: 'vardef'
	;

ENDVARIABLES
	: 'endvardef'
	;
	
DEFREQUIREMENTS
	: 'reqdef'
	;

ENDREQUIREMENTS
	: 'endreqdef'
	;

ISSTARTUP
	: 'isStartup'
	;

PLUS
	: '+'
	;

MINUS
	: '-'
	;

ARRAYMUL
	: '.*'
	;

ARRAYDIV
	: '.\\'
	;

ARRAYRDIV
	: './'
	;

ARRAYPOW
	: '.^'
	;

LPAR
	: '('
	;

RPAR
	: ')'
	;

TRUE
	: 'true'
	;

PREV
	: 'prev'
	;

DUR
	: 'dur'
	;

LE_OP
	: '<'
	;

GE_OP
	: '>'
	;

LEQ_OP
	: '<='
	;

GEQ_OP
	: '>='
	;

EQ_OP
	: '=='
	;

NE_OP
	: '!='
	;

IDENTIFIER
	: [a-zA-Z] [a-zA-Z0-9_]*
	;

CONSTANT
    : NUMBER (E SIGN? NUMBER)?
    ;

fragment NUMBER
    : ('0' .. '9')+ ('.' ('0' .. '9')+)?
    ;

fragment E
    : 'E'
    | 'e'
    ;

fragment SIGN
    : ('+' | '-')
    ;

COMMA
	: ','
	;

SEMICOLUMN
	: ';'
	;

CR
    : [\r\n]+
    ;

WS
    : [ \t]+ -> skip
    ;
