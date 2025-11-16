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
        self.walker = ParseTreeWalker()  # For walking subtrees
        self.in_function_def = False  # Flag to skip walking function bodies during definition

    def walk(self, ctx):
        """Walk a subtree"""
        self.walker.walk(self, ctx)

    # def exitImportStatement(self, ctx):
    #     pass  # Placeholder

    def exitFuncStatement(self, ctx):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()] if ctx.paramList() else []
        body = ctx.statement()  # List of statements
        self.functions[func_name] = {'params': params, 'body': body}
        # Note: Don't walk the function body - it will be walked when the function is called

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
            print(f"DEBUG: exitForStatement: var_name={var_name}, iterable={iterable}")
            if iterable is not None:
                for item in iterable:
                    self.variables[var_name] = item
                    # Execute body
                    body_stmts = ctx.statement()
                    # Handle both list and single statement
                    if isinstance(body_stmts, list):
                        for stmt in body_stmts:
                            self.walk(stmt)
                    else:
                        self.walk(body_stmts)

    def exitIfStatement(self, ctx):
        if hasattr(ctx, 'expr') and ctx.expr():
            condition = self.eval_expr(ctx.expr())
            if condition:
                # Execute then block
                if hasattr(ctx, 'statement') and ctx.statement():
                    for stmt in ctx.statement():
                        self.walk(stmt)
            else:
                # Execute else block if present (second statement block)
                if hasattr(ctx, 'statement') and len(ctx.statement()) > 1:
                    for stmt in ctx.statement()[1:]:
                        self.walk(stmt)

    def exitTryStatement(self, ctx):
        if hasattr(ctx, 'statement') and hasattr(ctx, 'ID') and ctx.statement():
            try:
                # Execute try block
                try_stmts = ctx.statement(0) if len(ctx.statement()) > 0 else None
                if try_stmts:
                    # Handle both list and single statement
                    if isinstance(try_stmts, list):
                        for stmt in try_stmts:
                            self.walk(stmt)
                    else:
                        self.walk(try_stmts)
            except Exception as e:
                # Catch: assign error to var
                error_var = ctx.ID().getText()
                self.variables[error_var] = str(e)
                # Execute catch block
                catch_stmts = ctx.statement(1) if len(ctx.statement()) > 1 else None
                if catch_stmts:
                    # Handle both list and single statement
                    if isinstance(catch_stmts, list):
                        for stmt in catch_stmts:
                            self.walk(stmt)
                    else:
                        self.walk(catch_stmts)

    def exitExprStatement(self, ctx):
        expr = ctx.expr()
        self.result = self.eval_expr(expr)

    def eval_expr(self, expr_ctx):
        # Handle relExpr with binary operators
        if hasattr(expr_ctx, 'relExpr'):
            rel_exprs = expr_ctx.relExpr()
            if rel_exprs:
                if isinstance(rel_exprs, list) and len(rel_exprs) >= 2:
                    # Binary operator: evaluate left and right
                    left = self.eval_expr(rel_exprs[0])
                    # Get the operator
                    if hasattr(expr_ctx, 'GREATER') and expr_ctx.GREATER():
                        right = self.eval_expr(rel_exprs[1])
                        return left > right
                    elif hasattr(expr_ctx, 'LESS') and expr_ctx.LESS():
                        right = self.eval_expr(rel_exprs[1])
                        return left < right
                    elif hasattr(expr_ctx, 'GREATER_EQUAL') and expr_ctx.GREATER_EQUAL():
                        right = self.eval_expr(rel_exprs[1])
                        return left >= right
                    elif hasattr(expr_ctx, 'LESS_EQUAL') and expr_ctx.LESS_EQUAL():
                        right = self.eval_expr(rel_exprs[1])
                        return left <= right
                    else:
                        return left
                else:
                    rel_expr = rel_exprs[0] if isinstance(rel_exprs, list) else rel_exprs
                    return self.eval_expr(rel_expr)
        
        # Navigate through operator precedence hierarchy
        if hasattr(expr_ctx, 'orExpr'):
            or_exprs = expr_ctx.orExpr()
            if or_exprs:
                if isinstance(or_exprs, list) and len(or_exprs) > 0:
                    or_expr = or_exprs[0]
                else:
                    or_expr = or_exprs
                return self.eval_expr(or_expr)
        
        if hasattr(expr_ctx, 'andExpr'):
            and_exprs = expr_ctx.andExpr()
            if and_exprs:
                if isinstance(and_exprs, list) and len(and_exprs) > 0:
                    and_expr = and_exprs[0]
                else:
                    and_expr = and_exprs
                return self.eval_expr(and_expr)
        
        if hasattr(expr_ctx, 'eqExpr'):
            eq_exprs = expr_ctx.eqExpr()
            if eq_exprs:
                if isinstance(eq_exprs, list) and len(eq_exprs) > 0:
                    eq_expr = eq_exprs[0]
                else:
                    eq_expr = eq_exprs
                return self.eval_expr(eq_expr)
        
        if hasattr(expr_ctx, 'addExpr'):
            add_exprs = expr_ctx.addExpr()
            if add_exprs:
                if isinstance(add_exprs, list) and len(add_exprs) > 0:
                    add_expr = add_exprs[0]
                else:
                    add_expr = add_exprs
                return self.eval_expr(add_expr)
        
        if hasattr(expr_ctx, 'mulExpr'):
            mul_exprs = expr_ctx.mulExpr()
            if mul_exprs:
                if isinstance(mul_exprs, list) and len(mul_exprs) > 0:
                    mul_expr = mul_exprs[0]
                else:
                    mul_expr = mul_exprs
                return self.eval_expr(mul_expr)
        
        if hasattr(expr_ctx, 'unaryExpr'):
            unary_exprs = expr_ctx.unaryExpr()
            if unary_exprs:
                if isinstance(unary_exprs, list) and len(unary_exprs) > 0:
                    unary_expr = unary_exprs[0]
                else:
                    unary_expr = unary_exprs
                return self.eval_expr(unary_expr)
        
        if hasattr(expr_ctx, 'primary'):
            primary = expr_ctx.primary()
            if primary:
                return self.eval_primary(primary)
        
        # Fallback
        text = expr_ctx.getText()
        if text.isdigit():
            return float(text)
        return self.variables.get(text, 0)

    def eval_primary(self, primary_ctx):
        """Evaluate a primary expression"""
        text = primary_ctx.getText()
        # print(f"DEBUG eval_primary called with text='{text[:50]}'...")
        
        # ID (variable reference)
        if primary_ctx.ID():
            var_name = primary_ctx.ID().getText()
            # Could be a function call: ID(exprList)
            if primary_ctx.exprList():
                # Function call
                args = [self.eval_expr(e) for e in primary_ctx.exprList().expr()]
                return self.call_function(var_name, args)
            else:
                # Variable reference
                val = self.variables.get(var_name, 0)
                return val
        
        # NUMBER
        elif primary_ctx.NUMBER():
            return float(primary_ctx.NUMBER().getText())
        
        # STRING
        elif primary_ctx.STRING():
            return primary_ctx.STRING().getText().strip('"')
        
        # List: [exprList]
        elif text.startswith('[') and text.endswith(']'):
            if primary_ctx.exprList():
                elements = [self.eval_expr(e) for e in primary_ctx.exprList().expr()]
                return elements
            return []
        
        # SAMPLE '(' expr ')'
        elif text.startswith('sample(') and hasattr(primary_ctx, 'expr'):
            expr = primary_ctx.expr()
            if expr:
                dist = self.eval_expr(expr)
                if hasattr(dist, 'sample'):
                    return dist.sample()
                else:
                    raise ValueError("sample() requires a distribution argument")
        
        # Parenthesized expression: (expr)
        elif text.startswith('(') and text.endswith(')'):
            if primary_ctx.expr():
                return self.eval_expr(primary_ctx.expr())
        
        # Array access: primary[expr]
        # Handle nested subscripts like grid[x][y] by collecting all indices
        elif '[' in text and ']' in text and hasattr(primary_ctx, 'primary') and primary_ctx.primary():
            # Collect all subscripts from nested structure
            subscripts = []  # List of (context, index) pairs
            current = primary_ctx
            
            # Walk the subscript chain to collect all indices
            # Continue while current has a .primary() method and it returns non-None
            while hasattr(current, 'primary') and current.primary() is not None:
                expr = current.expr()
                if expr:
                    index = int(self.eval_expr(expr))
                    subscripts.append((current, index))
                current = current.primary()
            
            # Now current is the base (no more subscripts)
            # Evaluate it based on its type
            base = None
            current_text = current.getText() if hasattr(current, 'getText') else str(current)
            has_id = hasattr(current, 'ID')
            id_result = current.ID() if has_id else None
            if has_id and id_result:
                var_name = id_result.getText()
                base = self.variables.get(var_name, 0)
            elif hasattr(current, 'NUMBER') and current.NUMBER():
                base = float(current.NUMBER().getText())
            elif hasattr(current, 'STRING') and current.STRING():
                base = current.STRING().getText().strip('"')
            elif hasattr(current, 'exprList') and current.exprList() and text.startswith('['):
                # List literal
                elements = [self.eval_expr(e) for e in current.exprList().expr()]
                base = elements
            else:
                # Fallback: try to evaluate it
                base = self.eval_primary(current)
            
            # DEBUG: commented out for now
            # if base == 0 and current_text != '0':
            #     raise RuntimeError(f"base=0 but current_text='{current_text}', has_id={has_id}, id_result={id_result}, subscripts={subscripts}")
            
            # Apply subscripts in reverse order (since we collected from outer to inner)
            result = base
            for _, index in reversed(subscripts):
                result = result[index]
            
            return result
        
        return 0

    def call_function(self, func_name, args):
        """Call a function (built-in or user-defined)"""
        if func_name == 'print':
            print(*args)
            return None
        elif func_name == 'sample':
            if len(args) > 0 and hasattr(args[0], 'sample'):
                return args[0].sample()
            else:
                raise ValueError("sample() requires a distribution argument")
        elif func_name == 'normal':
            return normal(*args)
        elif func_name == 'bernoulli':
            return bernoulli(*args)
        elif func_name == 'uniform':
            return uniform(*args)
        elif func_name in self.functions:
            func = self.functions[func_name]
            old_vars = self.variables.copy()
            for param, arg in zip(func['params'], args):
                self.variables[param] = arg
            # Execute body
            body_stmts = func['body']
            if body_stmts:
                if isinstance(body_stmts, list):
                    for stmt in body_stmts:
                        self.walk(stmt)
                else:
                    # Single statement
                    self.walk(body_stmts)
            result = self.result
            self.variables = old_vars
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
    
    # First pass: collect all function definitions without executing them
    for stmt_ctx in tree.statement():
        if hasattr(stmt_ctx, 'funcStatement') and stmt_ctx.funcStatement():
            # This is a function definition - extract it without walking the body
            func_ctx = stmt_ctx.funcStatement()
            func_name = func_ctx.ID().getText()
            params = [p.getText() for p in func_ctx.paramList().ID()] if func_ctx.paramList() else []
            body = func_ctx.statement() if hasattr(func_ctx, 'statement') else []
            interpreter.functions[func_name] = {'params': params, 'body': body}
    
    # Second pass: execute non-function statements manually by calling interpreters walk method
    for stmt_ctx in tree.statement():
        if not (hasattr(stmt_ctx, 'funcStatement') and stmt_ctx.funcStatement()):
            # This is not a function definition, execute it
            interpreter.walk(stmt_ctx)
    
    print(f"DEBUG: interpreter.result = {interpreter.result}")
    return interpreter.result
