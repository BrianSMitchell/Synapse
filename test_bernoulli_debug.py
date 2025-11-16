import sys
sys.path.insert(0, 'src')
from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

code = "let belief = bernoulli(0.7);"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SynapseParser(tokens)
tree = parser.program()

print("Full tree:")
print(tree.toStringTree(recog=parser))

# Get the let statement
stmt = tree.statement(0)
let_stmt = stmt.letStatement()
expr = let_stmt.expr()

print(f"\nLet expression text: {expr.getText()}")
