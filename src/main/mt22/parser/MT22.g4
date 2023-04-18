/*
 Họ và tên: Trần Huy Nam Hưng MSSV: 2052119
 */

grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls EOF;

/*DECLARATION LIST*/
decls: decl decls | decl;
decl: vardecl | funcdecl | arrayDecl;

/* ARRAY-ELEMENTs */
arr: LEFT_CURBRACK arrayList RIGHT_CURBRACK;
arrayList: non_null_arrayList |;
non_null_arrayList:
	arrayEle COMMA non_null_arrayList
	| arrayEle;
arrayEle: expr;

// stmtlist: stmt stmtlist|stmt;

/*VARIABLE DECLERATION*/
vardecl: initVardecl | noninitVardecl;
noninitVardecl: idlist COLON typ SEMICOLON;
initVardecl: IDENTIFIER initVardeclEle expr SEMICOLON;
initVardeclEle: (COMMA IDENTIFIER initVardeclEle expr COMMA)
	| COLON typ ASSIG_OP;
arrayDecl: initAardecl | noninitAardecl;
initAardecl: IDENTIFIER initAardeclEle expr SEMICOLON;
initAardeclEle: (COMMA IDENTIFIER initAardeclEle expr COMMA)
	| (
		COLON ARRAY_TYP LEFT_SQUAREBRACK (intList /*dimension*/) RIGHT_SQUAREBRACK OF typ ASSIG_OP
	);
noninitAardecl:
	idlist COLON ARRAY_TYP LEFT_SQUAREBRACK (
		intList /*dimension*/
	) RIGHT_SQUAREBRACK OF typ SEMICOLON;
intList: INT_LIT COMMA intList | INT_LIT;
// Đổi INT_LIT lại thành exprerssion
idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
typ: BOOLEAN | INT | FLOAT | ARRAY_TYP | STRING | AUTO;
exprlist: non_null_exprlist |;
non_null_exprlist: expr COMMA non_null_exprlist | expr;

/*Parameter declaration*/
paradecl:
	(INHERIT | OUT | INHERIT OUT |) (
		(
			(IDENTIFIER COLON typ)
			| (
				IDENTIFIER COLON ARRAY_TYP LEFT_SQUAREBRACK (
					intList /*dimension*/
				) RIGHT_SQUAREBRACK OF typ
			)
		)
	);

/*Function declaration*/
funcdecl: funcdecl_noInherit | funcdecl_Inherit;
funcdecl_noInherit:
	IDENTIFIER COLON FUNCTION functyp paramlist block_stmt;
funcdecl_Inherit:
	IDENTIFIER COLON FUNCTION functyp paramlist INHERIT IDENTIFIER block_stmt;
functyp:
	BOOLEAN
	| INT
	| FLOAT
	| ARRAY_TYP
	| STRING
	| VOID
	| AUTO
	| (
		ARRAY_TYP LEFT_SQUAREBRACK (intList /*dimension*/) RIGHT_SQUAREBRACK OF typ
	);
paramlist: LEFT_PAREN params RIGHT_PAREN;
params: non_null_params |;
non_null_params: paradecl COMMA non_null_params | paradecl;

//body: LEFT_CURBRACK bodyelements RIGHT_CURBRACK;

//EXPRESSIONS
expr:
	relational_expr CONCAT_OP relational_expr
	| relational_expr;
//concat_operand:STRING_LIT | IDENTIFIER;
relational_expr:
	logical_expr (relational_EQ_op | relational_noEQ_op) logical_expr
	| logical_expr;
relational_EQ_op: EQUAL_TO_OP | NOT_EQUAL_TO_OP;
relational_noEQ_op:
	LESS_OP
	| EQ_LESS_OP
	| GREATER_OP
	| EQ_GREATER_OP;
logical_expr: logical_expr logical_op add_expr | add_expr;
logical_op: CONJ_OP | DISJ_OP;
add_expr: add_expr (ADD_OP | SUB_OP) mul_expr | mul_expr;
mul_expr: mul_expr mul_op nega_expr | nega_expr;
mul_op: MUL_OP | DIV_OP | MOD_OP;
nega_expr: NEGA_OP nega_expr | sign_expr;
sign_expr: SUB_OP sign_expr | index_expr;
index_expr:
	IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK
	| funcall_expr;
index_list: expr COMMA index_list | expr;
funcall_expr:
	IDENTIFIER LEFT_PAREN exprlist RIGHT_PAREN
	| subexpr;
subexpr:
	IDENTIFIER
	| BOOL_LIT
	| INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| arr
	| LEFT_PAREN expr RIGHT_PAREN
	| special_function;

/* STATEMENTS */

stmt: matchStmt | unmatchStmt;
assign_stmt: lhs ASSIG_OP expr SEMICOLON;
lhs:
	IDENTIFIER
	| (IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK);
unmatchStmt:
	IF LEFT_PAREN expr RIGHT_PAREN stmt
	| IF LEFT_PAREN expr RIGHT_PAREN matchStmt ELSE unmatchStmt;
matchStmt:
	IF LEFT_PAREN expr RIGHT_PAREN matchStmt ELSE matchStmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| block_stmt
	| assign_stmt;
for_stmt:
	FOR LEFT_PAREN (
		IDENTIFIER
		| (
			IDENTIFIER LEFT_SQUAREBRACK index_list RIGHT_SQUAREBRACK
		)
	) ASSIG_OP expr COMMA expr COMMA expr RIGHT_PAREN stmt;
while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
do_while_stmt:
	DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMICOLON;
break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
return_stmt: (RETURN expr SEMICOLON) | (RETURN SEMICOLON);
call_stmt:
	special_function SEMICOLON
	| IDENTIFIER LEFT_PAREN exprlist RIGHT_PAREN SEMICOLON;
block_stmt: LEFT_CURBRACK blockelements RIGHT_CURBRACK;
blockelements: non_null_blockelements |;
non_null_blockelements:
	blockelement non_null_blockelements
	| blockelement;
blockelement: stmt | vardecl | arrayDecl;

/* SPECIAL FUNCTION */
special_function:
	read_integer
	| print_integer
	| read_float
	| write_float
	| read_boolean
	| print_boolean
	| read_string
	| print_string
	| super_func
	| prevent_default;
read_integer: READINT LEFT_PAREN exprlist RIGHT_PAREN;
READINT: 'readInteger';
print_integer: PRINTINT LEFT_PAREN exprlist RIGHT_PAREN;
PRINTINT: 'printInteger';
read_float: READFLOAT LEFT_PAREN exprlist RIGHT_PAREN;
READFLOAT: 'readFloat';
write_float: WRITEFLOAT LEFT_PAREN exprlist RIGHT_PAREN;
WRITEFLOAT: 'writeFloat';
read_boolean: READBOOLEAN LEFT_PAREN exprlist RIGHT_PAREN;
READBOOLEAN: 'readBoolean';
print_boolean: PRINTBOOL LEFT_PAREN exprlist RIGHT_PAREN;
PRINTBOOL: 'printBoolean';
read_string: READSTRING LEFT_PAREN exprlist RIGHT_PAREN;
READSTRING: 'readString';
print_string: PRINTSTRING LEFT_PAREN exprlist RIGHT_PAREN;
PRINTSTRING: 'printString';
super_func: SUPERFUNC LEFT_PAREN exprlist RIGHT_PAREN;
SUPERFUNC: 'super';
prevent_default: PREVENTDEFAULT LEFT_PAREN exprlist RIGHT_PAREN;
PREVENTDEFAULT: 'preventDefault';

/*LEXER*/

COMMENT: ('/*' .*? '*/' | ('//' (~[\r\n\f])*)) -> skip;

BOOL_LIT: 'false' | 'true';

//KEYWORD
AUTO: 'auto';
INT: 'integer';
VOID: 'void';
ARRAY_TYP: 'array';
BREAK: 'break';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
STRING: 'string';
FOR: 'for';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

//OPERATORS
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
NEGA_OP: '!';
CONJ_OP: '&&';
DISJ_OP: '||';
EQUAL_TO_OP: '==';
NOT_EQUAL_TO_OP: '!=';
LESS_OP: '<';
EQ_LESS_OP: '<=';
GREATER_OP: '>';
EQ_GREATER_OP: '>=';
CONCAT_OP: '::';

//SEP
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LEFT_CURBRACK: '{';
RIGHT_CURBRACK: '}';
ASSIG_OP: '=';
LEFT_SQUAREBRACK: '[';
RIGHT_SQUAREBRACK: ']';
DOT: '.';

IDENTIFIER: ([a-zA-Z_] [a-zA-Z0-9_]*);

//LITERALS
INT_LIT:
	[1-9] DIGIT*? ('_'? DIGIT DIGIT*?)* {self.text = "".join(self.text.split("_"))
		}
	| [1-9] DIGIT*
	| [0];
fragment DIGIT: [0-9];
//INDEX:([0-9]|[1-9][0-9]+);

//STRING
// STRING_LIT:(~'"'|'\\"')* '"';
STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
ILLEGAL_ESCAPE:
	'"' STRING_CHAR* ILLEGALFRAG {raise IllegalEscape(self.text[1:])};
UNCLOSE_STRING:
	'"' STRING_CHAR* ([\n\r] | EOF) {
	if (self.text.find('\n') != -1) :
		raise UncloseString(self.text[1:(self.text.find('\n')-1)])
	elif (self.text.find('\r') != -1):
		raise UncloseString(self.text[1:self.text.find('\r')])	
	elif(self.text[-1]=='\"'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])	
};

fragment STRING_CHAR: ~["\\\b\f\n\r'] | ESCAPEFRAG;
fragment ESCAPEFRAG: '\\' ["\\brfnt'];
fragment ILLEGALFRAG: '\\' ~["\\brfnt'];

FLOAT_LIT:
	INT_LIT DECPART EXPPART {self.text = "".join(self.text.split("_"))}
	| DECPART EXPPART
	| INT_LIT EXPPART {self.text = "".join(self.text.split("_"))}
	| INT_LIT DECPART {self.text = "".join(self.text.split("_"))};
fragment DECPART: '.' [0-9]*;
//1.
fragment EXPPART: [eE] ('-' | '+')? [0-9]+;

//ARRAY: [{] ([ ]? ELEMENT ',')* ([ ]? ELEMENT)? [}]; fragment ELEMENT: ( INT_LIT | STRING_LIT|
// FLOAT_LIT);

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};

//ILLEGAL_ESCAPE:'"'STRING_CHAR* ('\\'~[bfrnt']) STRING_CHAR*'"' {raise IllegalEscape(self.text[1:])};