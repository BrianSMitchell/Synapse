import sys
sys.path.insert(0, 'src')
from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser
from generated.SynapseParser import SynapseParser
from synapse.core.distributions import normal

code = "let x = normal(0,1);"
input_stream = InputStream(code)
lexer = SynapseLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SynapseParser(tokens)
tree = parser.program()

# Get the let statement and its expression
stmt = tree.statement(0)
let_stmt = stmt.letStatement()
expr = let_stmt.expr()

print(f"Expression text: {expr.getText()}")
print(f"Expression type: {type(expr)}")
print(f"Has ID(): {hasattr(expr, 'ID')}")
if hasattr(expr, 'ID'):
    print(f"  ID(): {expr.ID()}")
    
# Navigate through the tree
orExpr = expr.orExpr()
print(f"orExpr: {type(orExpr)}")
if hasattr(orExpr, 'andExpr'):
    andExpr = orExpr.andExpr(0)
    print(f"andExpr: {type(andExpr)}")
    if hasattr(andExpr, 'eqExpr'):
        eqExpr = andExpr.eqExpr(0)
        print(f"eqExpr: {type(eqExpr)}")
        # Keep going down to primary
        relExpr = eqExpr.relExpr(0)
        addExpr = relExpr.addExpr(0)
        mulExpr = addExpr.mulExpr(0)
        unaryExpr = mulExpr.unaryExpr(0)
        primary = unaryExpr.primary()
        print(f"primary: {type(primary)}")
        print(f"primary text: {primary.getText()}")
        print(f"primary has ID: {primary.ID() is not None}")
        if primary.ID():
            print(f"  ID text: {primary.ID().getText()}")
        print(f"primary has exprList: {primary.exprList() is not None}")
