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
        self.types = {}
        self.result = None

    # def exitImportStatement(self, ctx):
    #     pass  # Placeholder

    def exitFuncStatement(self, ctx):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()] if ctx.paramList() else []
        body = ctx.statement()  # List of statements
        self.functions[func_name] = {'params': params, 'body': body}

    def exitLetStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.eval_expr(ctx.expr())
        if ctx.TYPE():
            expected_type = ctx.TYPE().getText()
            actual_type = self.get_type(value)
            if expected_type != actual_type:
                print(f"Type mismatch: expected {expected_type}, got {actual_type}")
            self.types[var_name] = expected_type
        self.variables[var_name] = value

    def exitAssignStatement(self, ctx):
        left = ctx.expr(0)
        value = self.eval_expr(ctx.expr(1))
        self.assign_to_expr(left, value)

    def assign_to_expr(self, expr_ctx, value):
        if hasattr(expr_ctx, 'ID') and expr_ctx.ID():
            # Simple variable
            var_name = expr_ctx.ID().getText()
            self.variables[var_name] = value
        elif '[' in str(expr_ctx) and ']' in str(expr_ctx):
            # Array indexing
            if hasattr(expr_ctx, 'expr'):
                array_expr = expr_ctx.expr(0)
                index_expr = expr_ctx.expr(1)
                array = self.eval_expr(array_expr)
                index = int(self.eval_expr(index_expr))
                array[index] = value
        else:
            print("Assignment not supported for this expression")

    def exitForStatement(self, ctx):
        if hasattr(ctx, 'ID') and hasattr(ctx, 'expr') and hasattr(ctx, 'statement') and ctx.statement() and ctx.expr():
            var_name = ctx.ID().getText()
            iterable = self.eval_expr(ctx.expr())
            if iterable is not None:
                for item in iterable:
                    self.variables[var_name] = item
                    # Execute body
                    for stmt in ctx.statement():
                        self.walk(stmt)  # Walk each statement in body

    def exitTryStatement(self, ctx):
        if hasattr(ctx, 'statement') and hasattr(ctx, 'ID') and ctx.statement():
            try:
                # Execute try block
                try_stmts = ctx.statement(0)
                if try_stmts:
                    for stmt in try_stmts:
                        self.walk(stmt)
            except Exception as e:
                # Catch: assign error to var
                error_var = ctx.ID().getText()
                self.variables[error_var] = str(e)
                # Execute catch block
                catch_stmts = ctx.statement(1)
                if catch_stmts:
                    for stmt in catch_stmts:
                        self.walk(stmt)

    def exitExprStatement(self, ctx):
        expr = ctx.expr()
        self.result = self.eval_expr(expr)

    def eval_expr(self, expr_ctx):
        text = expr_ctx.getText()
        if hasattr(expr_ctx, 'ID') and expr_ctx.ID():
            return self.variables.get(expr_ctx.ID().getText(), 0)
        elif hasattr(expr_ctx, 'NUMBER') and expr_ctx.NUMBER():
            return float(expr_ctx.NUMBER().getText())
        elif text.startswith('-') and text[1:].isdigit():
            return -float(text[1:])
        elif text.startswith('[') and text.endswith(']'):
            # List
            if hasattr(expr_ctx, 'exprList'):
                elements = [self.eval_expr(e) for e in expr_ctx.exprList().expr()]
                return elements
        elif text.count('(') == 1 and text.count(')') == 1 and not text.startswith('sample'):
            # Function call: ID(exprList)
            if hasattr(expr_ctx, 'ID') and hasattr(expr_ctx, 'exprList'):
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

    def get_type(self, value):
        if isinstance(value, int) or (isinstance(value, float) and value.is_integer()):
            return 'int'
        elif isinstance(value, float):
            return 'float'
        elif isinstance(value, list):
            return 'list'
        elif isinstance(value, str):
            return 'string'
        else:
            return 'unknown'



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
