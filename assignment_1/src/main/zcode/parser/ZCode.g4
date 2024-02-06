// 2110264

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: NEW_LINE* decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

// Variable ----------------
vardecl: (vardecl_not_full | vardecl_full | vardecl_array) NEW_LINE+;
vardecl_full: VAR ID ASSIGN exp;
vardecl_not_full: (atomic_types | DYNAMIC) ID (ASSIGN exp)?;
vardecl_array: array_type (ASSIGN array_lit)?;
// exp_list: exp COMMA exp_list | exp; id_list: ID COMMA id_list | ID;

// Function -----------------
funcdecl: FUNC ID LP param_list RP NEW_LINE* (NEW_LINE
	| block_stmt | return_stmt);
// func_prototype: FUNC ID LP param_list RP NEW_LINE*;
// func_body: block_stmt | return_stmt;

paramdecl: atomic_types ID dimensions?;
param_list: param_prime |;
param_prime: paramdecl COMMA param_prime | paramdecl;

// Special function
spec_func:
	read_number
	| write_number
	| read_bool
	| write
	| read_string
	| write_string;

write_string: WRITESTRING LP exp RP;
read_string: READSTRING LP RP;
write: WRITEBOOL LP exp RP;
read_bool: READBOOL LP RP;
write_number: WRITENUM LP exp RP;
read_number: READNUM LP RP;

READNUM: 'readNumber';
WRITENUM: 'writeNumber';
READBOOL: 'readBool';
WRITEBOOL: 'writeBool';
READSTRING: 'readString';
WRITESTRING: 'writeString';

// Statements -----------------
stmt:
	(
		assign_stmt
		| if_stmt
		| for_stmt
		| block_stmt
		| break_stmt
		| continue_stmt
		| return_stmt
		| call_stmt
	);
assign_stmt: lhs ASSIGN exp NEW_LINE+;
if_stmt: IF sub_exp newline_list stmt (elif_stmt)* ( ELSE NEW_LINE* stmt)?;
elif_stmt: ELIF sub_exp newline_list stmt;
for_stmt: FOR ID UNTIL exp BY exp newline_list stmt;

break_stmt: BREAK NEW_LINE+;
continue_stmt: CONTINUE NEW_LINE+;
return_stmt: RETURN (exp)? NEW_LINE+;
call_stmt: ID LP expr_list RP NEW_LINE+ | spec_func NEW_LINE+;
block_stmt: BEGIN NEW_LINE+ blocked_list END NEW_LINE+;
blocked_list: stmt_plus_vardecl blocked_list |;
// blocked_list_prime: stmt_plus_vardecl blocked_list_prime | stmt_plus_vardecl;
stmt_plus_vardecl: (stmt | vardecl);

lhs: ID index_operator?;

// Expression -----------------
exp: exp0;
expr_list: exprprime |;
exprprime: exp COMMA exprprime | exp;

exp0: exp1 CONCAT exp1 | exp1;
exp1:
	exp2 (
		EQUAL
		| NOT_SAME
		| SAME
		| LESS_THAN
		| LESS_THAN_EQUAL
		| GREATER_THAN
		| GREATER_THAN_EQUAL
	) exp2
	| exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7:
	ID
	| constant
	| func_call
	| sub_exp
	| index_expr
	| spec_func;

func_call: ID LP expr_list RP;
constant: number_lit | BOOL_LIT | STRING_LIT | array_lit;
sub_exp: LP exp RP;

index_expr: (ID | func_call) index_operator;
index_operator: LS exprprime RS;

// Array -------------------
array_lit: LS non_empty_expr_list RS;
non_empty_expr_list: exp COMMA non_empty_expr_list | exp;
array_type: atomic_types ID dimensions;
dimensions: LS number_lits RS;
number_lits: number_lit COMMA number_lits | number_lit;
atomic_types: BOOL | NUMBER | STRING;

// Comment list --------------------
newline_list: NEW_LINE newline_list |;


// Literal -----------------

BOOL_LIT: TRUE | FALSE;

number_lit: FLOAT_LIT | INT_LIT;
FLOAT_LIT: ( INT_LIT DEC_PART? EXP_PART? | INT_LIT EXP_PART);
INT_LIT: '0' | [0-9]([0-9])*;

fragment DEC_PART: '.' ([0-9])*;
fragment EXP_PART: [eE] [+-]? ([0-9])+;

STRING_LIT:
	'"' (ESC | ~[\\\n"] | '\'"')* '"' {self.text = self.text[1:-1]};

fragment ESC: '\\' [bfrnt'\\];
fragment ILLEGAL_ESC: '\\' ~[bfrnt'\\];

// fragment NL: [\r\n] ;

LP: '(';
RP: ')';
LS: '[';
RS: ']';
COMMA: ',';

// DOT: '.'; SEMI: ';'; COLON: ':'; LC: '{'; RC: '}';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
ASSIGN: '<-';
NOT_SAME: '!=';
LESS_THAN: '<';
LESS_THAN_EQUAL: '<=';
GREATER_THAN_EQUAL: '>=';
GREATER_THAN: '>';
CONCAT: '...';
SAME: '==';

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// ARRAY: 'array'; AUTO: 'auto'; DO: 'do'; FLOAT: 'float'; INTEGER: 'integer'; VOID: 'void'; WHILE:
// 'while'; OUT: 'out'; OF: 'of'; INHERIT: 'inherit';

// COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '##' ~[\r\n]*  -> skip; //

ID: [_a-zA-Z] ([a-zA-Z0-9_])*;

NEW_LINE: '\r'? '\n' {self.text = '\n'};

WS: [ \t\f\b]+ -> skip;

UNCLOSE_STRING:
	'"' (~[\\\n"] | ESC | '\'"')* (EOF | [\r\n]) {
	raise UncloseString(self.text[1:].replace('\n', '').replace('\r', ''))
};
ILLEGAL_ESCAPE:
	'"' (~[\\\n"] | ESC | '\'"')* ILLEGAL_ESC {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};