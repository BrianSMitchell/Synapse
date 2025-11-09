grammar Synapse;

// Keywords
IMPORT: 'import';
DEF: 'def';
TRY: 'try';
CATCH: 'catch';
LET: 'let';
FOR: 'for';
IN: 'in';
IF: 'if';
ELSE: 'else';
MORPH: 'morph';
GOAL: 'goal';
SAMPLE: 'sample';

// Types
INT: 'int';
FLOAT: 'float';
LIST: 'list';
STRING_TYPE: 'string';

program: statement* EOF ;

statement: (importStatement | funcStatement | tryStatement | letStatement | assignStatement | forStatement | ifStatement | morphStatement | goalStatement | exprStatement) ';'? ;

importStatement: IMPORT ID ;

funcStatement: DEF ID '(' paramList? ')' '{' statement* '}' ;

tryStatement: TRY '{' statement* '}' CATCH '(' ID ')' '{' statement* '}' ;

paramList: ID (',' ID)* ;

TYPE: INT | FLOAT | LIST | STRING_TYPE ;

letStatement: LET ID (':' TYPE)? '=' expr ;

assignStatement: expr '=' expr ;

forStatement: FOR ID IN expr '{' statement* '}' ;

ifStatement: IF expr '{' statement* '}' (ELSE '{' statement* '}')? ;

morphStatement: MORPH ID '{' rule* '}' ;

goalStatement: GOAL ':' expr ;

exprStatement: expr ;

rule: IF expr '{' statement* '}' ;

// Expression with precedence
expr: orExpr ;

orExpr: andExpr (OR andExpr)* ;
andExpr: eqExpr (AND eqExpr)* ;
eqExpr: relExpr ((EQUAL | NOT_EQUAL) relExpr)* ;
relExpr: addExpr ((GREATER | LESS | GREATER_EQUAL | LESS_EQUAL) addExpr)* ;
addExpr: mulExpr ((PLUS | MINUS) mulExpr)* ;
mulExpr: unaryExpr ((MULT | DIV) unaryExpr)* ;

unaryExpr: (MINUS | NOT)? primary ;

primary: ID
       | NUMBER
       | STRING
       | '[' exprList ']'
       | ID '(' exprList ')'
       | primary '[' expr ']'
       | '(' expr ')'
       | SAMPLE '(' expr ')'
       ;

exprList: expr (',' expr)* ;

OR: 'or';
AND: 'and';
EQUAL: '==';
NOT_EQUAL: '!=';
GREATER: '>';
LESS: '<';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
NOT: '!';  // If needed

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' (~'"')* '"' ;

WS: [ \t\r\n]+ -> skip ;
