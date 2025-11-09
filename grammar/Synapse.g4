grammar Synapse;

program: statement* EOF ;

statement: (letStatement | ifStatement | morphStatement | goalStatement | exprStatement) ';'? ;

letStatement: 'let' ID '=' distribution '(' exprList ')' ;

ifStatement: 'if' expr '{' statement* '}' ('else' '{' statement* '}')? ;

morphStatement: 'morph' ID '{' rule* '}' ;

goalStatement: 'goal:' expr ;

exprStatement: expr ;

distribution: 'normal' | 'bernoulli' | 'uniform' ;  // Add more

exprList: expr (',' expr)* ;

rule: 'if' expr '{' statement* '}' ;

expr: ID
    | NUMBER
    | STRING
    | expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | expr '>' expr
    | '(' expr ')'
    | 'sample' '(' expr ')'
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' .*? '"' ;

WS: [ \t\r\n]+ -> skip ;
