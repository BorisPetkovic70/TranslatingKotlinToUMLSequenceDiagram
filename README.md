# Translating Kotlin To UML Sequence Diagram

This project is a specialized tool for the automatic generation of UML Sequence Diagrams directly from Kotlin source code. It utilizes ANTLR for lexical and syntactic analysis to build an interaction model, which is then translated into PlantUML code for final visualization.
##Structure
.
├── gen/                 # ANTLR generated files (Lexer, Parser, Visitor)
├── src/                 # Application source code
│   ├── main.py          # Entry point and process coordination
│   ├── uml_visitor.py   # Semantic analyzer (extracting calls and blocks)
│   └── plantuml_generator.py # PlantUML generator with activation logic
├── grammars/            # ANTLR g4 grammar definitions for Kotlin
├── input/               # Input Kotlin examples (.kt)
├── output/              # Generated diagrams (.puml and .png)
└── plantuml.jar         # Tool for rendering diagrams

##Requirements
-Python 3.10+
-ANTLR4 Python runtime: pip install antlr4-python3-runtime
-Java: Required to run plantuml.jar (verify with java -version)

##How to run
-python src/main.py input/complex2.kt output plantuml.jar
-The execution creates a output/complex2.puml file. If plantuml.jar is present, the tool automatically generates the output/complex2.png diagram.

##Key features
-Lifeline Tracking: Automatically detects object instantiations and maps them as sequence diagram participants.
-Method Inlining: The visitor can traverse into the body of called methods to represent deeper interaction levels (Call Stack simulation).
-Activation Bars: Precise generation of activate and deactivate commands based on call nesting depth.
-Return Values: Captures and displays specific variables and function results on dashed return arrows.
-Control Structure Mapping:
-Alt Fragments: Recognizes Kotlin if-else statements and groups them into conditional blocks.
-Loop Fragments: Recognizes and maps while and for loops.
-Object Creation: Automatically identifies and labels <<create>> messages upon constructor calls.
