from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser
from generated.SynapseListener import SynapseListener
from synapse.core.distributions import normal, bernoulli, uniform

class SynapseInterpreter(SynapseListener):
    def __init__(self):
        self.variables = {}
        self.result = None

    def exitLetStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        self.variables[var_name] = value

    def exitAssignStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        self.variables[var_name] = value

    def exitExprStatement(self, ctx):
        expr = ctx.expr()
        self.result = self.eval_expr(expr)

    def eval_expr(self, expr_ctx):
        text = expr_ctx.getText()
        if expr_ctx.ID():
            return self.variables.get(expr_ctx.ID().getText(), 0)
        elif expr_ctx.NUMBER():
            return float(expr_ctx.NUMBER().getText())
        elif text.startswith('[') and text.endswith(']'):
            # List
            elements = [self.eval_expr(e) for e in expr_ctx.exprList().expr()]
            return elements
        elif 'sample(' in text:
            var_name = expr_ctx.expr(0).ID().getText()
            dist = self.variables[var_name]
            return dist.sample()
        elif '>' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left > right
        elif '<' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left < right
        elif '==' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left == right
        elif '+' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left + right
        # Add more ops
        return 0

def parse_and_execute(input_str):
    input_stream = InputStream(input_str)
    lexer = SynapseLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SynapseParser(tokens)
    tree = parser.program()
    interpreter = SynapseInterpreter()
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)
    return interpreter.result
