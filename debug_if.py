import sys
sys.path.insert(0, 'src')
from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

code = "if sample(belief) > 0.5 { }"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SynapseParser(tokens)
tree = parser.program()

print("Parse tree:")
print(tree.toStringTree(recog=parser))
