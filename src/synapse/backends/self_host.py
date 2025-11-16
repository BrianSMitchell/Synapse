"""
Self-Hosted Synapse Compiler
Implements lexer, parser, and codegen in Synapse itself
"""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import json

class TokenType(Enum):
    """Token types for Synapse lexer"""
    # Literals
    NUMBER = "NUMBER"
    STRING = "STRING"
    ID = "ID"
    
    # Keywords
    LET = "LET"
    DEF = "DEF"
    IF = "IF"
    ELSE = "ELSE"
    FOR = "FOR"
    IN = "IN"
    WHILE = "WHILE"
    TRY = "TRY"
    CATCH = "CATCH"
    IMPORT = "IMPORT"
    RETURN = "RETURN"
    SAMPLE = "SAMPLE"
    MORPH = "MORPH"
    CONSENSUS = "CONSENSUS"
    PRINT = "PRINT"
    
    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    STAR = "STAR"
    SLASH = "SLASH"
    PERCENT = "PERCENT"
    EQUAL = "EQUAL"
    EQUAL_EQUAL = "EQUAL_EQUAL"
    BANG_EQUAL = "BANG_EQUAL"
    LESS = "LESS"
    LESS_EQUAL = "LESS_EQUAL"
    GREATER = "GREATER"
    GREATER_EQUAL = "GREATER_EQUAL"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    
    # Delimiters
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    LBRACKET = "LBRACKET"
    RBRACKET = "RBRACKET"
    COMMA = "COMMA"
    DOT = "DOT"
    COLON = "COLON"
    SEMICOLON = "SEMICOLON"
    ARROW = "ARROW"
    
    # Special
    EOF = "EOF"
    NEWLINE = "NEWLINE"

@dataclass
class Token:
    """Represents a single token"""
    type: TokenType
    lexeme: str
    literal: Any
    line: int
    column: int

class SynapseLexer:
    """Lexer for Synapse language"""
    
    KEYWORDS = {
        'let': TokenType.LET,
        'def': TokenType.DEF,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'for': TokenType.FOR,
        'in': TokenType.IN,
        'while': TokenType.WHILE,
        'try': TokenType.TRY,
        'catch': TokenType.CATCH,
        'import': TokenType.IMPORT,
        'return': TokenType.RETURN,
        'sample': TokenType.SAMPLE,
        'morph': TokenType.MORPH,
        'consensus': TokenType.CONSENSUS,
        'print': TokenType.PRINT,
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
    }
    
    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """Tokenize the source code"""
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line, self.column))
        return self.tokens
    
    def is_at_end(self) -> bool:
        return self.current >= len(self.source)
    
    def peek(self, offset: int = 0) -> Optional[str]:
        pos = self.current + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]
    
    def advance(self) -> str:
        char = self.source[self.current]
        self.current += 1
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char
    
    def scan_token(self):
        """Scan a single token"""
        char = self.peek()
        
        if char is None:
            return
        
        # Whitespace
        if char in ' \t\n\r':
            self.advance()
            if char == '\n':
                self.add_token(TokenType.NEWLINE)
            return
        
        # Comments
        if char == '/' and self.peek(1) == '/':
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()
            return
        
        # Strings
        if char == '"' or char == "'":
            self.string(char)
            return
        
        # Numbers
        if char.isdigit():
            self.number()
            return
        
        # Identifiers and keywords
        if char.isalpha() or char == '_':
            self.identifier()
            return
        
        # Operators and delimiters
        self.advance()
        
        if char == '+':
            self.add_token(TokenType.PLUS)
        elif char == '-':
            if self.peek() == '>':
                self.advance()
                self.add_token(TokenType.ARROW)
            else:
                self.add_token(TokenType.MINUS)
        elif char == '*':
            self.add_token(TokenType.STAR)
        elif char == '/':
            self.add_token(TokenType.SLASH)
        elif char == '%':
            self.add_token(TokenType.PERCENT)
        elif char == '=':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)
        elif char == '!':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.NOT)
        elif char == '<':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif char == '>':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        elif char == '(':
            self.add_token(TokenType.LPAREN)
        elif char == ')':
            self.add_token(TokenType.RPAREN)
        elif char == '{':
            self.add_token(TokenType.LBRACE)
        elif char == '}':
            self.add_token(TokenType.RBRACE)
        elif char == '[':
            self.add_token(TokenType.LBRACKET)
        elif char == ']':
            self.add_token(TokenType.RBRACKET)
        elif char == ',':
            self.add_token(TokenType.COMMA)
        elif char == '.':
            self.add_token(TokenType.DOT)
        elif char == ':':
            self.add_token(TokenType.COLON)
        elif char == ';':
            self.add_token(TokenType.SEMICOLON)
    
    def string(self, quote: str):
        """Parse a string literal"""
        start_line = self.line
        start_col = self.column
        self.advance()  # Opening quote
        
        value = ""
        while self.peek() != quote and not self.is_at_end():
            value += self.advance()
        
        if self.is_at_end():
            raise SyntaxError(f"Unterminated string at line {start_line}, col {start_col}")
        
        self.advance()  # Closing quote
        self.add_token(TokenType.STRING, value)
    
    def number(self):
        """Parse a numeric literal"""
        while self.peek() and self.peek().isdigit():
            self.advance()
        
        if self.peek() == '.' and self.peek(1) and self.peek(1).isdigit():
            self.advance()  # Consume '.'
            while self.peek() and self.peek().isdigit():
                self.advance()
        
        lexeme = self.source[self.start:self.current]
        value = float(lexeme) if '.' in lexeme else int(lexeme)
        self.add_token(TokenType.NUMBER, value)
    
    def identifier(self):
        """Parse an identifier or keyword"""
        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            self.advance()
        
        lexeme = self.source[self.start:self.current]
        token_type = self.KEYWORDS.get(lexeme, TokenType.ID)
        self.add_token(token_type)
    
    def add_token(self, token_type: TokenType, literal: Any = None):
        """Add a token to the list"""
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, lexeme, literal, self.line, self.column))


class ASTNode:
    """Base class for AST nodes"""
    pass

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

@dataclass
class LetStmt(ASTNode):
    name: str
    type_hint: Optional[str]
    value: ASTNode

@dataclass
class FuncDef(ASTNode):
    name: str
    params: List[str]
    body: List[ASTNode]

@dataclass
class IfStmt(ASTNode):
    condition: ASTNode
    then_branch: List[ASTNode]
    else_branch: Optional[List[ASTNode]]

@dataclass
class ForStmt(ASTNode):
    var: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class WhileStmt(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class TryStmt(ASTNode):
    try_body: List[ASTNode]
    catch_var: str
    catch_body: List[ASTNode]

@dataclass
class ReturnStmt(ASTNode):
    value: Optional[ASTNode]

@dataclass
class ExprStmt(ASTNode):
    expr: ASTNode

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    op: str
    operand: ASTNode

@dataclass
class CallExpr(ASTNode):
    callee: ASTNode
    args: List[ASTNode]

@dataclass
class ArrayAccess(ASTNode):
    array: ASTNode
    index: ASTNode

@dataclass
class Literal(ASTNode):
    value: Any

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class ArrayLiteral(ASTNode):
    elements: List[ASTNode]


class SynapseParser:
    """Parser for Synapse language"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def parse(self) -> Program:
        """Parse tokens into an AST"""
        statements = []
        while not self.is_at_end():
            # Skip newlines at statement level
            while self.check(TokenType.NEWLINE):
                self.advance()
            
            if not self.is_at_end():
                stmt = self.statement()
                if stmt:
                    statements.append(stmt)
        
        return Program(statements)
    
    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF
    
    def peek(self) -> Token:
        return self.tokens[self.current]
    
    def peek_back(self) -> Token:
        return self.tokens[self.current - 1] if self.current > 0 else self.peek()
    
    def advance(self) -> Token:
        token = self.peek()
        if not self.is_at_end():
            self.current += 1
        return token
    
    def check(self, token_type: TokenType) -> bool:
        return self.peek().type == token_type
    
    def match(self, *types: TokenType) -> bool:
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False
    
    def statement(self) -> Optional[ASTNode]:
        """Parse a statement"""
        if self.match(TokenType.LET):
            return self.let_statement()
        elif self.match(TokenType.DEF):
            return self.func_definition()
        elif self.match(TokenType.IF):
            return self.if_statement()
        elif self.match(TokenType.FOR):
            return self.for_statement()
        elif self.match(TokenType.WHILE):
            return self.while_statement()
        elif self.match(TokenType.TRY):
            return self.try_statement()
        elif self.match(TokenType.RETURN):
            return self.return_statement()
        else:
            return self.expression_statement()
    
    def let_statement(self) -> LetStmt:
        """Parse let statement: let x: type = expr"""
        name_token = self.advance()
        if name_token.type != TokenType.ID:
            raise SyntaxError(f"Expected identifier, got {name_token.type}")
        name = name_token.lexeme
        
        type_hint = None
        if self.match(TokenType.COLON):
            type_token = self.advance()
            type_hint = type_token.lexeme
        
        if not self.match(TokenType.EQUAL):
            raise SyntaxError("Expected '=' in let statement")
        
        value = self.expression()
        return LetStmt(name, type_hint, value)
    
    def func_definition(self) -> FuncDef:
        """Parse function definition: def name(params) { body }"""
        name_token = self.advance()
        if name_token.type != TokenType.ID:
            raise SyntaxError(f"Expected function name, got {name_token.type}")
        name = name_token.lexeme
        
        if not self.match(TokenType.LPAREN):
            raise SyntaxError("Expected '(' after function name")
        
        params = []
        if not self.check(TokenType.RPAREN):
            while True:
                param = self.advance()
                if param.type != TokenType.ID:
                    raise SyntaxError(f"Expected parameter name, got {param.type}")
                params.append(param.lexeme)
                if not self.match(TokenType.COMMA):
                    break
        
        if not self.match(TokenType.RPAREN):
            raise SyntaxError("Expected ')' after parameters")
        
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' before function body")
        
        body = self.block()
        
        return FuncDef(name, params, body)
    
    def if_statement(self) -> IfStmt:
        """Parse if statement: if condition { body } else { body }"""
        condition = self.expression()
        
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' after if condition")
        
        then_branch = self.block()
        
        else_branch = None
        if self.match(TokenType.ELSE):
            if not self.match(TokenType.LBRACE):
                raise SyntaxError("Expected '{' after else")
            else_branch = self.block()
        
        return IfStmt(condition, then_branch, else_branch)
    
    def for_statement(self) -> ForStmt:
        """Parse for statement: for var in iterable { body }"""
        var_token = self.advance()
        if var_token.type != TokenType.ID:
            raise SyntaxError(f"Expected variable name in for loop")
        var = var_token.lexeme
        
        if not self.match(TokenType.IN):
            raise SyntaxError("Expected 'in' in for loop")
        
        iterable = self.expression()
        
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' after for clause")
        
        body = self.block()
        return ForStmt(var, iterable, body)
    
    def while_statement(self) -> WhileStmt:
        """Parse while statement: while condition { body }"""
        condition = self.expression()
        
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' after while condition")
        
        body = self.block()
        return WhileStmt(condition, body)
    
    def try_statement(self) -> TryStmt:
        """Parse try-catch statement"""
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' after try")
        
        try_body = self.block()
        
        if not self.match(TokenType.CATCH):
            raise SyntaxError("Expected 'catch' after try block")
        
        if not self.match(TokenType.LPAREN):
            raise SyntaxError("Expected '(' after catch")
        
        catch_var = self.advance().lexeme
        
        if not self.match(TokenType.RPAREN):
            raise SyntaxError("Expected ')' after catch variable")
        
        if not self.match(TokenType.LBRACE):
            raise SyntaxError("Expected '{' for catch block")
        
        catch_body = self.block()
        
        return TryStmt(try_body, catch_var, catch_body)
    
    def return_statement(self) -> ReturnStmt:
        """Parse return statement"""
        value = None
        if not self.check(TokenType.NEWLINE) and not self.check(TokenType.RBRACE):
            value = self.expression()
        return ReturnStmt(value)
    
    def expression_statement(self) -> ExprStmt:
        """Parse expression statement"""
        expr = self.expression()
        return ExprStmt(expr)
    
    def expression(self) -> ASTNode:
        """Parse expression (assignment or logical or)"""
        return self.logical_or()
    
    def logical_or(self) -> ASTNode:
        """Parse logical or expression"""
        left = self.logical_and()
        
        while self.match(TokenType.OR):
            op = self.peek_back().lexeme
            right = self.logical_and()
            left = BinaryOp(left, op, right)
        
        return left
    
    def logical_and(self) -> ASTNode:
        """Parse logical and expression"""
        left = self.equality()
        
        while self.match(TokenType.AND):
            op = self.peek_back().lexeme
            right = self.equality()
            left = BinaryOp(left, op, right)
        
        return left
    
    def equality(self) -> ASTNode:
        """Parse equality expression"""
        left = self.comparison()
        
        while self.match(TokenType.EQUAL_EQUAL, TokenType.BANG_EQUAL):
            op = self.peek_back().lexeme
            right = self.comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def comparison(self) -> ASTNode:
        """Parse comparison expression"""
        left = self.additive()
        
        while self.match(TokenType.LESS, TokenType.LESS_EQUAL, 
                          TokenType.GREATER, TokenType.GREATER_EQUAL):
            op = self.peek_back().lexeme
            right = self.additive()
            left = BinaryOp(left, op, right)
        
        return left
    
    def additive(self) -> ASTNode:
        """Parse additive expression"""
        left = self.multiplicative()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = self.peek_back().lexeme
            right = self.multiplicative()
            left = BinaryOp(left, op, right)
        
        return left
    
    def multiplicative(self) -> ASTNode:
        """Parse multiplicative expression"""
        left = self.unary()
        
        while self.match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.peek_back().lexeme
            right = self.unary()
            left = BinaryOp(left, op, right)
        
        return left
    
    def unary(self) -> ASTNode:
        """Parse unary expression"""
        if self.match(TokenType.NOT, TokenType.MINUS):
            op = self.peek_back().lexeme
            expr = self.unary()
            return UnaryOp(op, expr)
        
        return self.call()
    
    def call(self) -> ASTNode:
        """Parse function call"""
        expr = self.primary()
        
        while True:
            if self.match(TokenType.LPAREN):
                expr = self.finish_call(expr)
            elif self.match(TokenType.LBRACKET):
                index = self.expression()
                if not self.match(TokenType.RBRACKET):
                    raise SyntaxError("Expected ']' after array index")
                expr = ArrayAccess(expr, index)
            else:
                break
        
        return expr
    
    def finish_call(self, callee: ASTNode) -> CallExpr:
        """Finish parsing a function call"""
        args = []
        
        if not self.check(TokenType.RPAREN):
            while True:
                args.append(self.expression())
                if not self.match(TokenType.COMMA):
                    break
        
        if not self.match(TokenType.RPAREN):
            raise SyntaxError("Expected ')' after arguments")
        
        return CallExpr(callee, args)
    
    def primary(self) -> ASTNode:
        """Parse primary expression"""
        if self.match(TokenType.NUMBER):
            return Literal(self.peek_back().literal)
        
        if self.match(TokenType.STRING):
            return Literal(self.peek_back().literal)
        
        if self.match(TokenType.PRINT):
            # print is treated as a function call
            return Identifier('print')
        
        if self.match(TokenType.ID):
            return Identifier(self.peek_back().lexeme)
        
        if self.match(TokenType.LBRACKET):
            elements = []
            if not self.check(TokenType.RBRACKET):
                while True:
                    elements.append(self.expression())
                    if not self.match(TokenType.COMMA):
                        break
            
            if not self.match(TokenType.RBRACKET):
                raise SyntaxError("Expected ']' after array elements")
            
            return ArrayLiteral(elements)
        
        if self.match(TokenType.LPAREN):
            expr = self.expression()
            if not self.match(TokenType.RPAREN):
                raise SyntaxError("Expected ')' after expression")
            return expr
        
        raise SyntaxError(f"Unexpected token: {self.peek()}")
    
    def block(self) -> List[ASTNode]:
        """Parse a block of statements"""
        statements = []
        
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            # Skip newlines
            while self.check(TokenType.NEWLINE):
                self.advance()
            
            if not self.check(TokenType.RBRACE):
                stmt = self.statement()
                if stmt:
                    statements.append(stmt)
        
        if not self.match(TokenType.RBRACE):
            raise SyntaxError("Expected '}' after block")
        
        return statements


class CodeGenerator:
    """Generates Python code from Synapse AST"""
    
    def __init__(self):
        self.indent_level = 0
        self.code = []
        self.locals = set()
    
    def generate(self, ast: Program) -> str:
        """Generate Python code from AST"""
        for stmt in ast.statements:
            self.generate_stmt(stmt)
        
        return '\n'.join(self.code)
    
    def generate_stmt(self, stmt: ASTNode) -> None:
        """Generate code for a statement"""
        if isinstance(stmt, LetStmt):
            self.gen_let(stmt)
        elif isinstance(stmt, FuncDef):
            self.gen_func(stmt)
        elif isinstance(stmt, IfStmt):
            self.gen_if(stmt)
        elif isinstance(stmt, ForStmt):
            self.gen_for(stmt)
        elif isinstance(stmt, WhileStmt):
            self.gen_while(stmt)
        elif isinstance(stmt, TryStmt):
            self.gen_try(stmt)
        elif isinstance(stmt, ReturnStmt):
            self.gen_return(stmt)
        elif isinstance(stmt, ExprStmt):
            self.gen_expr(stmt)
    
    def gen_let(self, stmt: LetStmt) -> None:
        """Generate let statement"""
        value_code = self.generate_expr(stmt.value)
        self.emit(f"{stmt.name} = {value_code}")
        self.locals.add(stmt.name)
    
    def gen_func(self, stmt: FuncDef) -> None:
        """Generate function definition"""
        params = ', '.join(stmt.params)
        self.emit(f"def {stmt.name}({params}):")
        
        self.indent_level += 1
        for body_stmt in stmt.body:
            self.generate_stmt(body_stmt)
        self.indent_level -= 1
    
    def gen_if(self, stmt: IfStmt) -> None:
        """Generate if statement"""
        condition = self.generate_expr(stmt.condition)
        self.emit(f"if {condition}:")
        
        self.indent_level += 1
        for then_stmt in stmt.then_branch:
            self.generate_stmt(then_stmt)
        self.indent_level -= 1
        
        if stmt.else_branch:
            self.emit("else:")
            self.indent_level += 1
            for else_stmt in stmt.else_branch:
                self.generate_stmt(else_stmt)
            self.indent_level -= 1
    
    def gen_for(self, stmt: ForStmt) -> None:
        """Generate for loop"""
        iterable = self.generate_expr(stmt.iterable)
        self.emit(f"for {stmt.var} in {iterable}:")
        
        self.indent_level += 1
        for body_stmt in stmt.body:
            self.generate_stmt(body_stmt)
        self.indent_level -= 1
    
    def gen_while(self, stmt: WhileStmt) -> None:
        """Generate while loop"""
        condition = self.generate_expr(stmt.condition)
        self.emit(f"while {condition}:")
        
        self.indent_level += 1
        for body_stmt in stmt.body:
            self.generate_stmt(body_stmt)
        self.indent_level -= 1
    
    def gen_try(self, stmt: TryStmt) -> None:
        """Generate try-catch"""
        self.emit("try:")
        
        self.indent_level += 1
        for try_stmt in stmt.try_body:
            self.generate_stmt(try_stmt)
        self.indent_level -= 1
        
        self.emit(f"except Exception as {stmt.catch_var}:")
        self.indent_level += 1
        for catch_stmt in stmt.catch_body:
            self.generate_stmt(catch_stmt)
        self.indent_level -= 1
    
    def gen_return(self, stmt: ReturnStmt) -> None:
        """Generate return statement"""
        if stmt.value:
            value = self.generate_expr(stmt.value)
            self.emit(f"return {value}")
        else:
            self.emit("return None")
    
    def gen_expr(self, stmt: ExprStmt) -> None:
        """Generate expression statement"""
        expr = self.generate_expr(stmt.expr)
        self.emit(expr)
    
    def generate_expr(self, expr: ASTNode) -> str:
        """Generate code for an expression"""
        if isinstance(expr, Literal):
            if isinstance(expr.value, str):
                return f'"{expr.value}"'
            return str(expr.value)
        
        elif isinstance(expr, Identifier):
            return expr.name
        
        elif isinstance(expr, BinaryOp):
            left = self.generate_expr(expr.left)
            right = self.generate_expr(expr.right)
            # Map Synapse operators to Python
            op_map = {
                '==': '==', '!=': '!=', '<': '<', '<=': '<=',
                '>': '>', '>=': '>=', 'and': 'and', 'or': 'or',
                '+': '+', '-': '-', '*': '*', '/': '/', '%': '%'
            }
            op = op_map.get(expr.op, expr.op)
            return f"({left} {op} {right})"
        
        elif isinstance(expr, UnaryOp):
            operand = self.generate_expr(expr.operand)
            op_map = {'not': 'not', '-': '-'}
            op = op_map.get(expr.op, expr.op)
            return f"({op} {operand})"
        
        elif isinstance(expr, CallExpr):
            callee = self.generate_expr(expr.callee)
            args = ', '.join(self.generate_expr(arg) for arg in expr.args)
            return f"{callee}({args})"
        
        elif isinstance(expr, ArrayAccess):
            array = self.generate_expr(expr.array)
            index = self.generate_expr(expr.index)
            return f"{array}[{index}]"
        
        elif isinstance(expr, ArrayLiteral):
            elements = ', '.join(self.generate_expr(e) for e in expr.elements)
            return f"[{elements}]"
        
        return ""
    
    def emit(self, code: str) -> None:
        """Emit a line of code"""
        indent = "    " * self.indent_level
        self.code.append(f"{indent}{code}")


class SelfHostedCompiler:
    """Self-hosted Synapse compiler"""
    
    def __init__(self):
        pass
    
    def compile_to_python(self, synapse_code: str) -> str:
        """Compile Synapse code to Python"""
        # Lexical analysis
        lexer = SynapseLexer(synapse_code)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = SynapseParser(tokens)
        ast = parser.parse()
        
        # Code generation
        codegen = CodeGenerator()
        python_code = codegen.generate(ast)
        
        return python_code
    
    def compile_to_ast(self, synapse_code: str) -> Program:
        """Compile Synapse code to AST"""
        lexer = SynapseLexer(synapse_code)
        tokens = lexer.tokenize()
        parser = SynapseParser(tokens)
        return parser.parse()
    
    def compile_to_bytecode(self, synapse_code: str) -> List[Dict[str, Any]]:
        """Compile Synapse code to bytecode (simple IR)"""
        ast = self.compile_to_ast(synapse_code)
        bytecode = []
        self._gen_bytecode(ast.statements, bytecode)
        return bytecode
    
    def _gen_bytecode(self, stmts: List[ASTNode], bytecode: List[Dict]) -> None:
        """Generate bytecode from statements"""
        for stmt in stmts:
            if isinstance(stmt, LetStmt):
                bytecode.append({
                    'op': 'let',
                    'name': stmt.name,
                    'value': self._expr_to_bytecode(stmt.value)
                })
            elif isinstance(stmt, ExprStmt):
                bytecode.append({
                    'op': 'expr',
                    'expr': self._expr_to_bytecode(stmt.expr)
                })
    
    def _expr_to_bytecode(self, expr: ASTNode) -> Dict[str, Any]:
        """Convert expression to bytecode"""
        if isinstance(expr, Literal):
            return {'op': 'literal', 'value': expr.value}
        elif isinstance(expr, Identifier):
            return {'op': 'var', 'name': expr.name}
        elif isinstance(expr, BinaryOp):
            return {
                'op': 'binop',
                'operator': expr.op,
                'left': self._expr_to_bytecode(expr.left),
                'right': self._expr_to_bytecode(expr.right)
            }
        return {'op': 'unknown'}


def test_compiler():
    """Test the self-hosted compiler"""
    code = """
    let x = 42
    let y = 10
    let z = x + y
    """
    
    compiler = SelfHostedCompiler()
    python_code = compiler.compile_to_python(code)
    print("Generated Python:")
    print(python_code)
    
    # Test bytecode
    bytecode = compiler.compile_to_bytecode(code)
    print("\nGenerated Bytecode:")
    for instr in bytecode:
        print(instr)


if __name__ == "__main__":
    test_compiler()
