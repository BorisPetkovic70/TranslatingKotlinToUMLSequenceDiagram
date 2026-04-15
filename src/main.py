import sys, os, subprocess
from antlr4 import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from gen.KotlinLexer import KotlinLexer
from gen.KotlinParser import KotlinParser
from uml_visitor import KotlinSemanticAnalyzer
from plantuml_generator import PlantUMLSequenceGenerator

def main():
    if len(sys.argv) < 2: 
        print("Usage: python main.py <input.kt> [output_dir] [plantuml.jar]")
        return
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    jar_path = sys.argv[3] if len(sys.argv) > 3 else "plantuml.jar"

    print(f"Analysing code: {input_file}")

    # 1. Parsing Phase: Load the file and build the Abstract Syntax Tree (AST)
    stream = FileStream(input_file, encoding='utf-8')
    lexer = KotlinLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = KotlinParser(tokens)
    tree = parser.kotlinFile()

    # 2. Semantic Analysis: Traverse the AST to extract sequence flow
    analyzer = KotlinSemanticAnalyzer()
    analyzer.visit(tree)

    # 3. Data Preparation: Retrieve structured data for the generator
    data = analyzer.get_sequence_data()
    
    # Execution Trace Debug Info
    print("\n=== DEBUG INFO ===")
    print(f"Objects: {data['objects']}")
    print(f"Creation order: {data['creation_order']}")
    print(f"Var types: {data['var_types']}")
    print(f"Instance vars: {data['instance_vars']}")
    print(f"Sequence flow: {data['sequence_flow']}")
    print("==================\n")
    
    # 4. PlantUML Generation: Convert trace data into .puml syntax
    generator = PlantUMLSequenceGenerator()
    puml_code = generator.generate(data)
    
    # Output file management
    os.makedirs(output_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(input_file))[0]
    puml_path = os.path.join(output_dir, f"{base}.puml")
    
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write(puml_code)
    
    print(puml_code)

    # 5. Visual Rendering: Execute PlantUML JAR to produce PNG
    if os.path.exists(jar_path):
        subprocess.run(["java", "-jar", jar_path, puml_path], check=True)
        print(f"\nDiagram generated: {output_dir}/{base}.png")
    else:
        print(f"\nPlantUML JAR not found at: {jar_path}")

if __name__ == "__main__":
    main()