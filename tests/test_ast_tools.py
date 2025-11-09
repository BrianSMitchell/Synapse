import sys
sys.path.insert(0, 'src')

from synapse.core.ast_tools import parse_code, ast_to_code

def test_ast_parse():
    tree = parse_code("let x = normal(0,1)")
    code = ast_to_code(tree)
    assert "let" in code
