from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

def test_lexer():
    input_stream = InputStream("let x = normal(0, 1)")
    lexer = SynapseLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    for token in tokens.tokens:
        print(f"{token.type}: '{token.text}'")

if __name__ == "__main__":
    test_lexer()
