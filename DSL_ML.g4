grammar DSL_ML;

// Regla principal
program
    : statement* EOF
    ;

// Declaraciones y operaciones generales
statement
    : variableDeclaration
    | assignment
    | arithmeticOperation
    | conditional
    | loop
    | matrixOperation
    | graphOperation
    | fileOperation
    | mlOperation
    | printStatement
    ;

// Declaraciones de variables
variableDeclaration
    : 'var' ID '=' expression ';'
    ;

// Asignaciones
assignment
    : ID '=' expression ';'
    ;

// Operaciones aritméticas
arithmeticOperation
    : expression ('+' | '-' | '*' | '/' | '%') expression ';'
    ;

// Expresiones
expression
    : NUMBER
    | STRING
    | BOOLEAN
    | ID
    | '(' expression ')'
    | functionCall
    ;

// Funciones
functionCall
    : 'plot' '(' argumentList ')'
    | 'readFile' '(' STRING ')'
    | 'writeFile' '(' STRING ',' expression ')'
    | 'regression' '(' STRING ',' STRING ',' STRING ')'
    | 'kmeans' '(' STRING ',' NUMBER ')'
    | 'transpose' '(' ID ')'
    | 'inverse' '(' ID ')'
    ;

// Condicionales
conditional
    : 'if' '(' condition ')' 'then' block ('else' block)?
    ;

// Ciclos
loop
    : 'while' '(' condition ')' block
    | 'for' '(' ID 'in' range ')' block
    ;

// Condiciones lógicas
condition
    : expression (comparisonOperator expression)?
    ;

comparisonOperator
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

// Bloques de código
block
    : '{' statement* '}'
    ;

// Rango (para bucles)
range
    : NUMBER '..' NUMBER
    ;

// Operaciones con matrices
matrixOperation
    : ID '=' '[' matrixRow (',' matrixRow)* ']'
    | ID '=' 'transpose' '(' ID ')'
    | ID '=' 'inverse' '(' ID ')'
    ;

matrixRow
    : '[' NUMBER (',' NUMBER)* ']'
    ;

// Operaciones de graficado
graphOperation
    : 'plot' '(' argumentList ')'
    ;

// Operaciones de archivos
fileOperation
    : 'readFile' '(' STRING ')'
    | 'writeFile' '(' STRING ',' expression ')'
    ;

// Operaciones de Machine Learning
mlOperation
    : 'regression' '(' STRING ',' STRING ',' STRING ')'
    | 'kmeans' '(' STRING ',' NUMBER ')'
    ;

// Impresión
printStatement
    : 'print' '(' expression ')' ';'
    ;

// Lista de argumentos
argumentList
    : expression (',' expression)*
    ;

// Tipos básicos
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';
BOOLEAN: 'true' | 'false';

// Espacios en blanco y comentarios
WHITESPACE: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;
