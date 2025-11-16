import sys
sys.path.insert(0, 'src')
from antlr4 import *
from generated.SynapseLexer import SynapseLexer

code = "let belief = bernoulli(0.7);"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
tokens.fill()

for token in tokens.tokens:
    print(f"{token.type:3d} {token.text:15s} ({lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else '?'})")
