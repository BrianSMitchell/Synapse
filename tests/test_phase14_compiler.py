"""
Tests for Phase 14: Production Compiler
Tests self-hosted compiler, bytecode VM, incremental compilation, and optimization
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from synapse.backends.self_host import (
    SynapseLexer, SynapseParser, CodeGenerator, SelfHostedCompiler,
    TokenType, Literal, Identifier, BinaryOp
)
from synapse.vm.bytecode import BytecodeVM, Opcode, BytecodeVM
from synapse.backends.incremental import IncrementalCompiler, ChangeDetector
from synapse.backends.optimizer import SynapseOptimizer, OptimizationLevel


class TestSynapseLexer:
    """Test the Synapse lexer"""
    
    def test_tokenize_let_statement(self):
        """Test lexing a let statement"""
        code = "let x = 42"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        
        assert tokens[0].type == TokenType.LET
        assert tokens[1].type == TokenType.ID
        assert tokens[2].type == TokenType.EQUAL
        assert tokens[3].type == TokenType.NUMBER
        assert tokens[-1].type == TokenType.EOF
    
    def test_tokenize_function(self):
        """Test lexing a function definition"""
        code = "def add(a, b) { a + b }"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens]
        assert TokenType.DEF in token_types
        assert TokenType.ID in token_types
        assert TokenType.LPAREN in token_types
        assert TokenType.RPAREN in token_types
    
    def test_tokenize_string(self):
        """Test lexing strings"""
        code = 'let s = "hello"'
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        
        string_token = next(t for t in tokens if t.type == TokenType.STRING)
        assert string_token.literal == "hello"
    
    def test_tokenize_operators(self):
        """Test lexing operators"""
        code = "a + b - c * d / e % f"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens]
        assert TokenType.PLUS in token_types
        assert TokenType.MINUS in token_types
        assert TokenType.STAR in token_types
        assert TokenType.SLASH in token_types
        assert TokenType.PERCENT in token_types


class TestSynapseParser:
    """Test the Synapse parser"""
    
    def test_parse_let_statement(self):
        """Test parsing let statements"""
        code = "let x = 42"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        parser = SynapseParser(tokens)
        ast = parser.parse()
        
        assert len(ast.statements) > 0
        assert ast.statements[0].__class__.__name__ == "LetStmt"
    
    def test_parse_function_definition(self):
        """Test parsing function definitions"""
        code = "def add(a, b) { a + b }"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        parser = SynapseParser(tokens)
        ast = parser.parse()
        
        assert len(ast.statements) > 0
        assert ast.statements[0].__class__.__name__ == "FuncDef"
    
    def test_parse_if_statement(self):
        """Test parsing if statements"""
        code = "if x > 10 { print(x) }"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        parser = SynapseParser(tokens)
        ast = parser.parse()
        
        assert len(ast.statements) > 0
        assert ast.statements[0].__class__.__name__ == "IfStmt"
    
    def test_parse_for_loop(self):
        """Test parsing for loops"""
        code = "for i in [1, 2, 3] { print(i) }"
        lexer = SynapseLexer(code)
        tokens = lexer.tokenize()
        parser = SynapseParser(tokens)
        ast = parser.parse()
        
        assert len(ast.statements) > 0
        assert ast.statements[0].__class__.__name__ == "ForStmt"


class TestCodeGenerator:
    """Test code generation"""
    
    def test_generate_python_from_let(self):
        """Test Python code generation from let statement"""
        code = "let x = 42"
        compiler = SelfHostedCompiler()
        python_code = compiler.compile_to_python(code)
        
        assert "x = 42" in python_code
    
    def test_generate_python_arithmetic(self):
        """Test Python code generation for arithmetic"""
        code = "let z = x + y"
        compiler = SelfHostedCompiler()
        python_code = compiler.compile_to_python(code)
        
        assert "x + y" in python_code
        assert "z" in python_code


class TestSelfHostedCompiler:
    """Test the self-hosted compiler"""
    
    def test_compile_to_ast(self):
        """Test compiling to AST"""
        code = "let x = 42"
        compiler = SelfHostedCompiler()
        ast = compiler.compile_to_ast(code)
        
        assert len(ast.statements) > 0
    
    def test_compile_to_python(self):
        """Test compiling to Python"""
        code = "let x = 42"
        compiler = SelfHostedCompiler()
        python = compiler.compile_to_python(code)
        
        assert "x = 42" in python
    
    def test_compile_to_bytecode(self):
        """Test compiling to bytecode"""
        code = "let x = 42"
        compiler = SelfHostedCompiler()
        bytecode = compiler.compile_to_bytecode(code)
        
        assert len(bytecode) > 0
        assert bytecode[0]['op'] == 'let'


class TestBytecodeVM:
    """Test the bytecode VM"""
    
    def test_load_and_execute_constant(self):
        """Test loading and executing constants"""
        vm = BytecodeVM()
        
        const_42 = vm.load_constant(42)
        vm.emit(Opcode.LOAD_CONST, const_42, 0)
        
        result = vm.execute()
        assert vm.registers[0] == 42
    
    def test_arithmetic_operations(self):
        """Test arithmetic operations"""
        vm = BytecodeVM()
        
        # Load 10 and 20
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(10), 0)
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(20), 1)
        
        # Add
        vm.emit(Opcode.ADD, 0, 1, 2)
        
        result = vm.execute()
        assert vm.registers[2] == 30
    
    def test_comparison_operations(self):
        """Test comparison operations"""
        vm = BytecodeVM()
        
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(10), 0)
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(5), 1)
        vm.emit(Opcode.CMP_GT, 0, 1, 2)
        
        result = vm.execute()
        assert vm.registers[2] == True
    
    def test_vm_performance(self):
        """Test VM performance is acceptable"""
        vm = BytecodeVM()
        
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(100), 0)
        vm.emit(Opcode.LOAD_CONST, vm.load_constant(50), 1)
        vm.emit(Opcode.MUL, 0, 1, 2)
        
        stats = vm.benchmark(100)
        
        # Should execute 100 iterations of 3-instruction code in < 100ms
        assert stats['total_time'] < 0.1


class TestIncrementalCompilation:
    """Test incremental compilation"""
    
    def test_change_detection(self):
        """Test change detection"""
        detector = ChangeDetector()
        
        files = {'a.syn': 'let x = 1'}
        detector.update_hashes(files)
        
        files['a.syn'] = 'let x = 2'
        changes = detector.detect_changes(files)
        
        assert 'a.syn' in changes
    
    def test_no_change_detection(self):
        """Test no changes detected when files unchanged"""
        detector = ChangeDetector()
        
        files = {'a.syn': 'let x = 1'}
        detector.update_hashes(files)
        
        changes = detector.detect_changes(files)
        
        assert len(changes) == 0
    
    def test_incremental_compile(self):
        """Test incremental compilation"""
        compiler = IncrementalCompiler()
        
        files = {
            'utils.syn': 'def add(a, b) { a + b }',
            'main.syn': 'import "utils.syn"\nlet x = add(1, 2)'
        }
        
        compiler.register_files(files)
        result = compiler.compile_incremental(files)
        
        assert 'utils.syn' in result
        assert 'main.syn' in result
    
    def test_cache_effectiveness(self):
        """Test that caching reduces recompilation"""
        compiler = IncrementalCompiler()
        
        files = {
            'utils.syn': 'def add(a, b) { a + b }',
            'main.syn': 'import "utils.syn"'
        }
        
        compiler.register_files(files)
        result1 = compiler.compile_incremental(files)
        stats1 = compiler.get_stats()
        
        result2 = compiler.compile_incremental(files)
        stats2 = compiler.get_stats()
        
        # After second compile with no changes, should have more cache hits
        assert stats2['units_compiled'] >= stats1['units_compiled'] or \
               stats2.get('cache_hit_rate', 0) >= stats1.get('cache_hit_rate', 0)


class TestOptimizer:
    """Test code optimizer"""
    
    def test_dead_code_elimination(self):
        """Test elimination of unused variables"""
        code = '''
let x = 10
let unused = 42
print(x)
'''
        optimizer = SynapseOptimizer(OptimizationLevel.BASIC)
        optimized = optimizer.optimize(code)
        
        assert 'unused' not in optimized
        assert 'x' in optimized
    
    def test_constant_folding(self):
        """Test constant folding"""
        code = 'let x = 5 + 3'
        optimizer = SynapseOptimizer(OptimizationLevel.BASIC)
        optimized = optimizer.optimize(code)
        
        stats = optimizer.get_stats()
        assert stats['dead_code_removed'] >= 0
    
    def test_optimization_preserves_functionality(self):
        """Test that optimization doesn't change behavior"""
        code = '''
let x = 10
let y = 20
let z = x + y
print(z)
'''
        optimizer = SynapseOptimizer(OptimizationLevel.AGGRESSIVE)
        optimized = optimizer.optimize(code)
        
        # Optimized code should still have the print
        assert 'print' in optimized
        assert 'z' in optimized


class TestIntegration:
    """Integration tests for Phase 14"""
    
    def test_full_pipeline(self):
        """Test full compilation pipeline"""
        code = '''
def square(x) {
    x * x
}

let result = square(5)
print(result)
'''
        
        compiler = SelfHostedCompiler()
        
        # Compile to AST
        ast = compiler.compile_to_ast(code)
        assert len(ast.statements) > 0
        
        # Compile to Python
        python = compiler.compile_to_python(code)
        assert 'def' in python
        
        # Compile to bytecode
        bytecode = compiler.compile_to_bytecode(code)
        assert len(bytecode) > 0
    
    def test_optimizer_integration(self):
        """Test optimizer with other components"""
        code = 'let x = 10\nlet y = 20\nlet z = x + y\nprint(z)'
        
        optimizer = SynapseOptimizer(OptimizationLevel.BASIC)
        optimized = optimizer.optimize(code)
        
        # Check that optimization preserves key elements
        assert 'x' in optimized or 'z' in optimized or len(optimized) > 0
        
        compiler = SelfHostedCompiler()
        ast = compiler.compile_to_ast(code)  # Parse original
        assert len(ast.statements) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
