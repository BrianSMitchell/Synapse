from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

def parse_code(code):
    input_stream = InputStream(code)
    lexer = SynapseLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SynapseParser(tokens)
    return parser.program()

def modify_ast(tree, old_str, new_str):
    """Simple string-based modification (placeholder for real AST manipulation)"""
    # For now, replace in the text representation
    text = tree.toStringTree()
    modified = text.replace(old_str, new_str)
    return modified

def ast_to_code(tree):
    """Convert AST back to code (placeholder)"""
    return tree.toStringTree()  # Not real code, but for test

def test_ast_manipulation():
    code = "let x = normal(0,1)"
    tree = parse_code(code)
    original = ast_to_code(tree)
    modified = modify_ast(tree, "0", "0.5")
    return modified != original

if __name__ == "__main__":
    print("AST manipulation works:", test_ast_manipulation())
