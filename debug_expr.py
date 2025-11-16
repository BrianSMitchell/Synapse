import sys
sys.path.insert(0, 'src')
from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser

code = "sample(belief)"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SynapseParser(tokens)
tree = parser.program()

# Get first statement
stmt = tree.statement(0)
expr_stmt = stmt.exprStatement()
expr = expr_stmt.expr()

print(f"expr: {expr.getText()}")
print("Full tree:")
print(tree.toStringTree(recog=parser))

# Navigate to the primary
or_expr = expr.orExpr()
and_expr = or_expr.andExpr(0)
eq_expr = and_expr.eqExpr(0)
rel_expr = eq_expr.relExpr(0)
add_expr = rel_expr.addExpr(0)
mul_expr = add_expr.mulExpr(0)
unary_expr = mul_expr.unaryExpr(0)
primary = unary_expr.primary()

print(f"primary text: {primary.getText()}")
print(f"primary has expr: {hasattr(primary, 'expr')}")
if hasattr(primary, 'expr'):
    expr_in_primary = primary.expr()
    if isinstance(expr_in_primary, list):
        print(f"  expr list length: {len(expr_in_primary)}")
        for i, e in enumerate(expr_in_primary):
            print(f"    expr[{i}]: {e.getText()}")
    else:
        print(f"  expr: {expr_in_primary.getText() if expr_in_primary else 'None'}")
