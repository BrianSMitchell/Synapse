grammar Synapse;

program: statement* EOF ;

statement: (importStatement | funcStatement | tryStatement | letStatement | assignStatement | forStatement | ifStatement | morphStatement | goalStatement | exprStatement) ';'? ;

importStatement: 'import' STRING ;

funcStatement: 'def' ID '(' paramList? ')' '{' statement* '}' ;

tryStatement: 'try' '{' statement* '}' 'catch' '(' ID ')' '{' statement* '}' ;

paramList: ID (',' ID)* ;

TYPE: 'int' | 'float' | 'list' | 'string' | ID ;

letStatement: 'let' ID (':' TYPE)? '=' expr ;

assignStatement: ID '=' expr ;

forStatement: 'for' ID 'in' expr '{' statement* '}' ;

ifStatement: 'if' expr '{' statement* '}' ('else' '{' statement* '}')? ;

morphStatement: 'morph' ID '{' rule* '}' ;

goalStatement: 'goal:' expr ;

exprStatement: expr ;

distribution: 'normal' | 'bernoulli' | 'uniform' ;  // Add more

exprList: expr (',' expr)* ;

rule: 'if' expr '{' statement* '}' ;

expr: ID
    | NUMBER
    | '-' NUMBER
    | STRING
    | '[' exprList ']'
    | ID '(' exprList ')'
    | expr '[' expr ']'
    | expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | expr '>' expr
    | expr '<' expr
    | expr '>=' expr
    | expr '<=' expr
    | expr '==' expr
    | expr '!=' expr
    | expr 'and' expr
    | expr 'or' expr
    | '(' expr ')'
    | 'sample' '(' expr ')'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' .*? '"' ;

COMMENT: '//' .*? '\n' -> skip ;
WS: [ \t\r\n]+ -> skip ;
