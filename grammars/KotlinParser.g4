parser grammar KotlinParser;

options {
    tokenVocab = KotlinLexer;
}

// Početno pravilo
kotlinFile: packageHeader? importList* topLevelObject* EOF;

// Package i import
packageHeader: PACKAGE IDENTIFIER (DOT IDENTIFIER)* ;
importList: IMPORT IDENTIFIER (DOT IDENTIFIER)* (DOT MULTIPLY)? ;

// Top-level objekti
topLevelObject: classDeclaration
              | interfaceDeclaration
              | objectDeclaration
              | enumDeclaration
              | functionDeclaration
              | propertyDeclaration
              ;

// Deklaracija klase
classDeclaration: modifiers? (DATA)? CLASS IDENTIFIER 
                  typeParameters? 
                  primaryConstructor?
                  (COLON superTypes)? 
                  classBody?;

// Primarni konstruktor
primaryConstructor: modifiers? CONSTRUCTOR? LPAREN primaryConstructorParameterList? RPAREN;

// Lista parametara za primarni konstruktor
primaryConstructorParameterList: primaryConstructorParameter (COMMA primaryConstructorParameter)*;

// Pojedinačni parametar primarnog konstruktora
primaryConstructorParameter: modifiers? (VAL | VAR)? IDENTIFIER COLON type_ (ASSIGN expression)?;

// Interfejs
interfaceDeclaration: modifiers? INTERFACE IDENTIFIER 
                      typeParameters? 
                      (COLON superTypes)? 
                      interfaceBody?;

// Object
objectDeclaration: modifiers? OBJECT IDENTIFIER 
                   (COLON superTypes)? 
                   classBody?;

// Enum
enumDeclaration: modifiers? ENUM CLASS IDENTIFIER 
                 (COLON superTypes)? 
                 enumBody?;

// Modifikatori
modifiers: modifier+;
modifier: PUBLIC | PRIVATE | PROTECTED | INTERNAL | OPEN | ABSTRACT | FINAL | OVERRIDE | COMPANION;

// Parametri
parameterList: parameter (COMMA parameter)*;
parameter: modifiers? (VAL | VAR)? IDENTIFIER COLON type_ (ASSIGN expression)?;

// Super tipovi
superTypes: superType (COMMA superType)*;
superType: IDENTIFIER typeArguments?;

// Type parametri
typeParameters: LESS_THAN typeParameter (COMMA typeParameter)* GREATER_THAN;
typeParameter: IDENTIFIER (COLON type_)?;

// Type argumenti
typeArguments: LESS_THAN type_ (COMMA type_)* GREATER_THAN;

// Tipovi
type_: IDENTIFIER typeArguments? QUESTION?
    | STRING_TYPE QUESTION?
    | INT_TYPE QUESTION?
    | LONG_TYPE QUESTION?
    | DOUBLE_TYPE QUESTION?
    | FLOAT_TYPE QUESTION?
    | BOOLEAN_TYPE QUESTION?
    | CHAR_TYPE QUESTION?
    | UNIT_TYPE QUESTION?
    | ANY_TYPE QUESTION?
    ;

// Tela
classBody: LBRACE classMemberDeclarations RBRACE;
interfaceBody: LBRACE interfaceMemberDeclarations RBRACE;
enumBody: LBRACE enumEntries? (SEMICOLON classMemberDeclarations)? RBRACE;

// Članovi klase
classMemberDeclarations: classMemberDeclaration*;
classMemberDeclaration: secondaryConstructor
                      | functionDeclaration
                      | propertyDeclaration
                      | classDeclaration
                      | interfaceDeclaration
                      | objectDeclaration
                      | initBlock
                      ;

// Članovi interfejsa
interfaceMemberDeclarations: interfaceMemberDeclaration*;
interfaceMemberDeclaration: functionDeclaration
                          | propertyDeclaration
                          | classDeclaration
                          | interfaceDeclaration
                          | objectDeclaration
                          ;

// Sekundarni konstruktor
secondaryConstructor: modifiers? CONSTRUCTOR LPAREN parameterList? RPAREN 
                      (COLON constructorDelegationCall)? 
                      block?;

// Init blok
initBlock: INIT block;

// Delegacija konstruktora
constructorDelegationCall: IDENTIFIER LPAREN argumentList? RPAREN;

// Enum entries
enumEntries: enumEntry (COMMA enumEntry)*;
enumEntry: IDENTIFIER (LPAREN argumentList? RPAREN)?;

// Deklaracija funkcije
functionDeclaration: modifiers? FUN typeParameters? IDENTIFIER 
                     LPAREN parameterList? RPAREN 
                     (COLON type_)? 
                     (block | ASSIGN expression)?;

// Deklaracija svojstva
propertyDeclaration: modifiers? (VAL | VAR) IDENTIFIER 
                     (COLON type_)? 
                     (ASSIGN expression)?
                     | propertyDelegate
                     | getter
                     | setter;

// Property delegate
propertyDelegate: IDENTIFIER IDENTIFIER;

// Getter i setter
getter: modifiers? IDENTIFIER (LPAREN RPAREN)? 
        (COLON type_)? 
        (ASSIGN expression | block)?;

setter: modifiers? IDENTIFIER LPAREN parameter RPAREN 
        (ASSIGN expression | block)?;

// Blok
block: LBRACE statements RBRACE;

// Statements
statements: statement*;

statement: 
    expression (ASSIGN expression)? SEMICOLON?
    | declaration SEMICOLON?
    | returnStatement SEMICOLON?
    | ifStatement
    | whileStatement
    | forStatement
    ;

// IF statement
ifStatement: IF LPAREN expression RPAREN block (ELSE block)?;

// WHILE statement
whileStatement: WHILE LPAREN expression RPAREN block;

// FOR statement
forStatement: FOR LPAREN IDENTIFIER IN expression RPAREN block;

// Return statement
returnStatement: RETURN expression?;

// Deklaracija
declaration: propertyDeclaration
           | functionDeclaration
           ;

// Argumenti
argumentList: expression (COMMA expression)*;

// ============= IZRAZI SA OPERATORIMA =============

expression: logicalOrExpression;

logicalOrExpression: 
    logicalAndExpression (LOGICAL_OR logicalAndExpression)*;

logicalAndExpression: 
    equalityExpression (LOGICAL_AND equalityExpression)*;

equalityExpression: 
    relationalExpression ((EQUALS | NOT_EQUALS) relationalExpression)*;

relationalExpression: 
    additiveExpression ((LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) additiveExpression)*;

additiveExpression: 
    multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: 
    unaryExpression ((MULTIPLY | DIVIDE | MODULO) unaryExpression)*;

unaryExpression: 
    (PLUS | MINUS | LOGICAL_NOT)? primaryExpression;

primaryExpression: 
    literal                                  
    | IDENTIFIER                             
    | functionCall                           
    | LPAREN expression RPAREN               
    | primaryExpression DOT functionCall     
    | primaryExpression DOT IDENTIFIER       
    | primaryExpression LBRACKET expression RBRACKET  
    ;

// Poziv funkcije
functionCall: IDENTIFIER LPAREN argumentList? RPAREN;

// Literali
literal: STRING_LITERAL
       | CHAR_LITERAL
       | INTEGER_LITERAL
       | LONG_LITERAL
       | FLOAT_LITERAL
       | DOUBLE_LITERAL
       | BOOLEAN_LITERAL
       | NULL_LITERAL
       ;