import sys
sys.path.insert(0, 'src')
from synapse.parser.parser import parse_and_execute

# Test just bernoulli
result = parse_and_execute("let belief = bernoulli(0.7);")
print(f"Result: {result}")
print(f"Variables: {parse_and_execute('let belief = bernoulli(0.7);') and 'N/A'}")

# Need to check variables directly
from synapse.parser.parser import SynapseInterpreter
from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

code = "let belief = bernoulli(0.7);"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SynapseParser(tokens)
tree = parser.program()

interpreter = SynapseInterpreter()
walker = ParseTreeWalker()
walker.walk(interpreter, tree)

print(f"Variables after: {interpreter.variables}")
print(f"belief = {interpreter.variables.get('belief')}")
print(f"Type: {type(interpreter.variables.get('belief'))}")
