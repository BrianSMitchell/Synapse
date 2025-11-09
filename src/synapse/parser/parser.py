from antlr4 import *
from generated.SynapseLexer import SynapseLexer
from generated.SynapseParser import SynapseParser
from generated.SynapseListener import SynapseListener
from synapse.core.distributions import normal, bernoulli, uniform
from synapse.core.ast_tools import parse_code

class SynapseInterpreter(SynapseListener):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.result = None

    def exitImportStatement(self, ctx):
        file_path = ctx.STRING().getText().strip('"')
        try:
            with open(file_path, 'r') as f:
                imported_code = f.read()
            # Parse and execute in the same context
            imported_tree = parse_code(imported_code)
            walker = ParseTreeWalker()
            walker.walk(self, imported_tree)
        except Exception as e:
            print(f"Import error: {e}")

    def exitFuncStatement(self, ctx):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()] if ctx.paramList() else []
        body = ctx.statement()  # List of statements
        self.functions[func_name] = {'params': params, 'body': body}

    def exitLetStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        self.variables[var_name] = value

    def exitAssignStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        self.variables[var_name] = value

    def exitForStatement(self, ctx):
        var_name = ctx.ID().getText()
        iterable = self.eval_expr(ctx.expr())
        for item in iterable:
            self.variables[var_name] = item
            # Execute body
            for stmt in ctx.statement():
                self.walk(stmt)  # Walk each statement in body

    def exitExprStatement(self, ctx):
        expr = ctx.expr()
        self.result = self.eval_expr(expr)

    def eval_expr(self, expr_ctx):
        text = expr_ctx.getText()
        if expr_ctx.ID():
            return self.variables.get(expr_ctx.ID().getText(), 0)
        elif expr_ctx.NUMBER():
            return float(expr_ctx.NUMBER().getText())
        elif text.startswith('-') and text[1:].isdigit():
            return -float(text[1:])
        elif text.startswith('[') and text.endswith(']'):
            # List
            elements = [self.eval_expr(e) for e in expr_ctx.exprList().expr()]
            return elements
        elif text.count('(') == 1 and text.count(')') == 1 and not text.startswith('sample'):
            # Function call: ID(exprList)
            func_name = expr_ctx.ID().getText()
            args = [self.eval_expr(e) for e in expr_ctx.exprList().expr()]
            if func_name == 'print':
                print(*args)
                return None
            elif func_name in self.functions:
                func = self.functions[func_name]
                # Create new scope? For simplicity, assign params to variables
                old_vars = self.variables.copy()
                for param, arg in zip(func['params'], args):
                    self.variables[param] = arg
                # Execute body
                for stmt in func['body']:
                    self.walk(stmt)
                # Result is the last expr, but since functions return last, assume last statement sets result
                result = self.result
                self.variables = old_vars  # Restore
                return result
            else:
                raise ValueError(f"Function {func_name} not defined")
        elif '[' in text and ']' in text:
            # Indexing: expr[expr]
            array = self.eval_expr(expr_ctx.expr(0))
            index = int(self.eval_expr(expr_ctx.expr(1)))
            return array[index]
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
        elif '>=' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left >= right
        elif '<=' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left <= right
        elif '==' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left == right
        elif '!=' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left != right
        elif 'and' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left and right
        elif 'or' in text:
            left = self.eval_expr(expr_ctx.expr(0))
            right = self.eval_expr(expr_ctx.expr(1))
            return left or right
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
