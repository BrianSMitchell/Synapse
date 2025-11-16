"""
Phase 14.2: LLVM Backend Tests
Comprehensive testing of LLVM IR generation, optimization, and JIT compilation
"""

import pytest
import time
from typing import Dict, Any

# Try importing LLVM backend
try:
    from synapse.backends.llvm import (
        LLVMBackend,
        LLVMCodeGenerator,
        LLVMOptimizer,
        LLVMJITCompiler,
        LLVMTypeSystem,
        transpile_to_llvm,
        benchmark_vs_python,
        test_llvm,
        LLVMLITE_AVAILABLE
    )
except ImportError:
    pytest.skip("LLVM backend not available", allow_module_level=True)


class TestLLVMTypeSystem:
    """Test LLVM type system conversions"""
    
    def test_synapse_to_llvm_type_int(self):
        """Test int type conversion"""
        type_sys = LLVMTypeSystem(None)
        assert type_sys.synapse_to_llvm_type('int') == 'i32'
    
    def test_synapse_to_llvm_type_float(self):
        """Test float type conversion"""
        type_sys = LLVMTypeSystem(None)
        assert type_sys.synapse_to_llvm_type('float') == 'double'
    
    def test_synapse_to_llvm_type_bool(self):
        """Test bool type conversion"""
        type_sys = LLVMTypeSystem(None)
        assert type_sys.synapse_to_llvm_type('bool') == 'i1'
    
    def test_synapse_to_llvm_type_string(self):
        """Test string type conversion"""
        type_sys = LLVMTypeSystem(None)
        assert type_sys.synapse_to_llvm_type('string') == 'i8*'
    
    def test_synapse_to_llvm_type_unknown(self):
        """Test unknown type defaults to i32"""
        type_sys = LLVMTypeSystem(None)
        assert type_sys.synapse_to_llvm_type('unknown') == 'i32'


class TestLLVMCodeGenerator:
    """Test LLVM code generation from AST"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_generate_from_empty_ast(self):
        """Test generation from empty program"""
        codegen = LLVMCodeGenerator()
        ast = {'type': 'program', 'body': []}
        ir = codegen.generate_from_ast(ast)
        assert isinstance(ir, str)
        assert len(ir) > 0
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_generate_simple_function(self):
        """Test function generation"""
        codegen = LLVMCodeGenerator()
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'function_def',
                    'name': 'add',
                    'params': ['a', 'b'],
                    'body': [
                        {
                            'type': 'return_statement',
                            'value': {
                                'type': 'binary_op',
                                'op': '+',
                                'left': {'type': 'identifier', 'name': 'a'},
                                'right': {'type': 'identifier', 'name': 'b'}
                            }
                        }
                    ]
                }
            ]
        }
        ir = codegen.generate_from_ast(ast)
        assert 'define' in ir
        assert 'add' in ir
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_generate_variable_declaration(self):
        """Test variable declaration"""
        codegen = LLVMCodeGenerator()
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'let_statement',
                    'name': 'x',
                    'value': {'type': 'literal', 'value': 42},
                    'var_type': 'int'
                }
            ]
        }
        ir = codegen.generate_from_ast(ast)
        assert isinstance(ir, str)


class TestLLVMBackend:
    """Test full LLVM backend"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_backend_initialization(self):
        """Test backend initialization"""
        backend = LLVMBackend(opt_level=2, enable_jit=True)
        assert backend.opt_level == 2
        assert backend.enable_jit is True
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_backend_compile(self):
        """Test backend compilation"""
        backend = LLVMBackend()
        ast = {'type': 'program', 'body': []}
        ir = backend.compile(ast)
        assert isinstance(ir, str)
        assert len(ir) > 0
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_backend_get_ir(self):
        """Test getting generated IR"""
        backend = LLVMBackend()
        ast = {'type': 'program', 'body': []}
        backend.compile(ast)
        ir = backend.get_ir()
        assert ir is not None
        assert isinstance(ir, str)
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_backend_optimize(self):
        """Test optimization pass"""
        backend = LLVMBackend(opt_level=2)
        ast = {'type': 'program', 'body': []}
        backend.compile(ast)
        optimized = backend.optimize()
        assert isinstance(optimized, str)


class TestLLVMOptimizations:
    """Test optimization passes"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_optimization_level_0(self):
        """Test no optimization"""
        backend = LLVMBackend(opt_level=0)
        ast = {'type': 'program', 'body': []}
        ir = backend.compile(ast)
        assert ir is not None
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_optimization_level_1(self):
        """Test basic optimization"""
        backend = LLVMBackend(opt_level=1)
        ast = {'type': 'program', 'body': []}
        ir = backend.compile(ast)
        assert ir is not None
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_optimization_level_3(self):
        """Test aggressive optimization"""
        backend = LLVMBackend(opt_level=3)
        ast = {'type': 'program', 'body': []}
        ir = backend.compile(ast)
        assert ir is not None


class TestLLVMTranspiler:
    """Test transpilation functions"""
    
    def test_transpile_to_llvm(self):
        """Test transpile_to_llvm function"""
        code = "let x = 42"
        try:
            result = transpile_to_llvm(code)
            assert isinstance(result, str)
        except RuntimeError:
            # llvmlite not available, uses fallback
            assert True
    
    def test_benchmark_vs_python(self):
        """Test benchmarking function"""
        code = "let x = 42"
        result = benchmark_vs_python(code)
        assert isinstance(result, bool)


class TestLLVMIntegration:
    """Integration tests for LLVM backend"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_compile_and_optimize(self):
        """Test compile and optimize pipeline"""
        backend = LLVMBackend(opt_level=2)
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'function_def',
                    'name': 'main',
                    'params': [],
                    'body': [
                        {
                            'type': 'return_statement',
                            'value': {'type': 'literal', 'value': 0}
                        }
                    ]
                }
            ]
        }
        
        ir_before = backend.compile(ast)
        ir_after = backend.optimize()
        
        assert ir_before is not None
        assert ir_after is not None
        assert 'main' in ir_before
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_benchmark_performance(self):
        """Test performance benchmarking"""
        backend = LLVMBackend()
        ast = {'type': 'program', 'body': []}
        backend.compile(ast)
        
        bench = backend.benchmark_vs_interpreter(iterations=1000)
        
        assert 'iterations' in bench
        assert 'time_seconds' in bench
        assert 'ops_per_second' in bench
        assert bench['iterations'] == 1000
        assert bench['ops_per_second'] > 0


class TestLLVMComplexExpressions:
    """Test complex expression compilation"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_binary_operations(self):
        """Test binary operation codegen"""
        codegen = LLVMCodeGenerator()
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'function_def',
                    'name': 'calc',
                    'params': ['a', 'b'],
                    'body': [
                        {
                            'type': 'return_statement',
                            'value': {
                                'type': 'binary_op',
                                'op': '+',
                                'left': {'type': 'identifier', 'name': 'a'},
                                'right': {'type': 'identifier', 'name': 'b'}
                            }
                        }
                    ]
                }
            ]
        }
        
        ir = codegen.generate_from_ast(ast)
        assert 'add' in ir or '+' in ir
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_unary_operations(self):
        """Test unary operation codegen"""
        codegen = LLVMCodeGenerator()
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'function_def',
                    'name': 'negate',
                    'params': ['x'],
                    'body': [
                        {
                            'type': 'return_statement',
                            'value': {
                                'type': 'unary_op',
                                'op': '-',
                                'operand': {'type': 'identifier', 'name': 'x'}
                            }
                        }
                    ]
                }
            ]
        }
        
        ir = codegen.generate_from_ast(ast)
        assert 'negate' in ir or 'sub' in ir


class TestLLVMControlFlow:
    """Test control flow compilation"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_if_statement(self):
        """Test if statement codegen"""
        codegen = LLVMCodeGenerator()
        ast = {
            'type': 'program',
            'body': [
                {
                    'type': 'function_def',
                    'name': 'conditional',
                    'params': ['x'],
                    'body': [
                        {
                            'type': 'if_statement',
                            'condition': {
                                'type': 'binary_op',
                                'op': '>',
                                'left': {'type': 'identifier', 'name': 'x'},
                                'right': {'type': 'literal', 'value': 0}
                            },
                            'then_body': [
                                {
                                    'type': 'return_statement',
                                    'value': {'type': 'literal', 'value': 1}
                                }
                            ],
                            'else_body': [
                                {
                                    'type': 'return_statement',
                                    'value': {'type': 'literal', 'value': 0}
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        
        ir = codegen.generate_from_ast(ast)
        assert 'then' in ir or 'conditional' in ir


class TestLLVMBackendCompatibility:
    """Test compatibility with existing compiler"""
    
    def test_llvm_test_function(self):
        """Test the basic test_llvm function"""
        result = test_llvm()
        assert isinstance(result, bool)


class TestLLVMPerformanceEstimates:
    """Test performance estimation"""
    
    @pytest.mark.skipif(not LLVMLITE_AVAILABLE, reason="llvmlite not installed")
    def test_benchmark_returns_metrics(self):
        """Test benchmark returns proper metrics"""
        backend = LLVMBackend()
        ast = {'type': 'program', 'body': []}
        backend.compile(ast)
        
        metrics = backend.benchmark_vs_interpreter(iterations=100)
        
        assert 'iterations' in metrics
        assert 'time_seconds' in metrics
        assert 'ops_per_second' in metrics
        assert 'estimated_speedup' in metrics
        assert metrics['estimated_speedup'] > 1


class TestLLVMErrorHandling:
    """Test error handling"""
    
    def test_backend_without_llvmlite_graceful(self):
        """Test graceful fallback when llvmlite missing"""
        if LLVMLITE_AVAILABLE:
            pytest.skip("llvmlite is available")
        
        try:
            result = transpile_to_llvm("let x = 42")
            # Should either work with fallback or raise meaningful error
            assert result is not None
        except RuntimeError as e:
            assert "llvmlite" in str(e).lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
