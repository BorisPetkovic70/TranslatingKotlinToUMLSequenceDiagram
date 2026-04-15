lexer grammar KotlinLexer;

// Ključne reči
CLASS: 'class';
INTERFACE: 'interface';
OBJECT: 'object';
DATA: 'data';
ENUM: 'enum';
FUN: 'fun';
VAL: 'val';
VAR: 'var';
INIT: 'init';
CONSTRUCTOR: 'constructor';
RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHEN: 'when';
FOR: 'for';
WHILE: 'while';
TRY: 'try';
CATCH: 'catch';
FINALLY: 'finally';
THROW: 'throw';
IMPORT: 'import';
PACKAGE: 'package';
IN: 'in';                    // <-- DODAJ OVO

// Modifikatori
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';
INTERNAL: 'internal';
OPEN: 'open';
ABSTRACT: 'abstract';
FINAL: 'final';
OVERRIDE: 'override';
STATIC: 'static';
COMPANION: 'companion';

// Osnovni tipovi
STRING_TYPE: 'String';
INT_TYPE: 'Int';
LONG_TYPE: 'Long';
DOUBLE_TYPE: 'Double';
FLOAT_TYPE: 'Float';
BOOLEAN_TYPE: 'Boolean';
CHAR_TYPE: 'Char';
UNIT_TYPE: 'Unit';
ANY_TYPE: 'Any';

// Operatori
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
EQUALS: '==';
NOT_EQUALS: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';

// Separatori
SEMICOLON: ';';
COMMA: ',';
DOT: '.';
COLON: ':';
QUESTION: '?';
ARROW: '->';

// Zagrade
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';

// Literali
STRING_LITERAL: '"' ( ~["\\\r\n] | EscapeSequence )* '"';
CHAR_LITERAL: '\'' ( ~['\\\r\n] | EscapeSequence ) '\'';
INTEGER_LITERAL: [0-9]+;
LONG_LITERAL: [0-9]+ 'L';
FLOAT_LITERAL: [0-9]+ '.' [0-9]+ 'f'?;
DOUBLE_LITERAL: [0-9]+ '.' [0-9]+;
BOOLEAN_LITERAL: 'true' | 'false';
NULL_LITERAL: 'null';

// Identifikatori - MORA BITI POSLJEDNJI!
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Escape sekvence
fragment EscapeSequence: '\\' [btnfr"'\\];

// Whitespace i komentari
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;