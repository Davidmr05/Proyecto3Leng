import sys
from antlr4 import *
from DSL_MLLexer import DSL_MLLexer
from DSL_MLParser import DSL_MLParser
from MyDSLVisitor import MyDSLVisitor

def main(argv):
    with open(argv[1], 'r', encoding='utf-8') as f:
        input_text = f.read()
    
    input_stream = InputStream(input_text)
    lexer = DSL_MLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DSL_MLParser(stream)
    tree = parser.program()

    visitor = MyDSLVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python interpreter.py <archivo.dsl>")
        sys.exit(1)
    main(sys.argv)
