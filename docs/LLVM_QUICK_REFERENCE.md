# LLVM Backend Quick Reference

## Installation

```bash
pip install llvmlite
```

## Basic Usage

```python
from synapse.backends.llvm import LLVMBackend
from synapse.backends.self_host import SelfHostedCompiler

# 1. Parse Synapse code
compiler = SelfHostedCompiler()
ast = compiler.compile_to_ast("def add(x, y) { return x + y }")

# 2. Create backend
backend = LLVMBackend(opt_level=2, enable_jit=True)

# 3. Compile to LLVM IR
ir = backend.compile(ast)

# 4. Optimize
optimized_ir = backend.optimize()

# 5. JIT compile
functions = backend.jit_compile()

# 6. Call native function
if 'add' in functions:
    result = functions['add'](5, 3)
```

## Optimization Levels

```python
# No optimization (fastest compilation)
backend = LLVMBackend(opt_level=0)

# Basic (constant merge, dead arg elimination)
backend = LLVMBackend(opt_level=1)

# Standard (default - recommended)
backend = LLVMBackend(opt_level=2)

# Aggressive (slowest compilation, fastest execution)
backend = LLVMBackend(opt_level=3)
```

## Common Patterns

### Pattern 1: IR Generation Only

```python
backend = LLVMBackend(enable_jit=False)
ir = backend.compile(ast)
print(ir)  # Print LLVM IR
```

### Pattern 2: Maximum Performance

```python
backend = LLVMBackend(opt_level=3, enable_jit=True)
backend.compile(ast)
optimized = backend.optimize()
functions = backend.jit_compile()
```

### Pattern 3: Benchmarking

```python
backend = LLVMBackend()
backend.compile(ast)
metrics = backend.benchmark_vs_interpreter(iterations=100000)
print(f"Speedup: {metrics['estimated_speedup']:.1f}x")
```

## Type Mapping

| Synapse | LLVM IR |
|---------|---------|
| `int` | `i32` |
| `float` | `double` |
| `bool` | `i1` |
| `string` | `i8*` |

## Supported Operators

### Arithmetic
- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
- `%` (modulo)

### Comparison
- `==` (equal)
- `!=` (not equal)
- `<` (less than)
- `<=` (less or equal)
- `>` (greater than)
- `>=` (greater or equal)

### Logical
- `and` (logical AND)
- `or` (logical OR)
- `not` (logical NOT)

## Supported Statements

- `let x = value` (variable declaration)
- `x = value` (assignment)
- `if (cond) { } else { }` (conditional)
- `while (cond) { }` (loop)
- `return value` (return)
- `print(value)` (output)

## Performance Tips

1. **Use opt_level=2 by default** - Good balance of speed and compilation time
2. **Enable JIT for repeated calls** - Pays off after 5+ invocations
3. **Benchmark your specific workload** - Performance varies by code pattern
4. **Use opt_level=3 for production** - Maximum runtime performance
5. **Profile with multiple iterations** - Use 100k+ iterations for benchmarking

## Troubleshooting

### "llvmlite not installed"
```bash
pip install llvmlite
```

### "Failed to initialize JIT"
```python
# Use IR-only mode to debug
backend = LLVMBackend(enable_jit=False)
ir = backend.compile(ast)
print(ir)
```

### "Optimization failed"
```python
# Try lower optimization level
backend = LLVMBackend(opt_level=1)
```

## API Cheat Sheet

```python
# Create backend
backend = LLVMBackend(opt_level=2, enable_jit=True)

# Compile AST to LLVM IR
ir_code = backend.compile(ast)

# Apply optimizations
optimized = backend.optimize()

# JIT compile to native code
functions = backend.jit_compile()

# Get IR string
ir = backend.get_ir()

# Benchmark performance
metrics = backend.benchmark_vs_interpreter(iterations=10000)

# Access results
print(metrics['ops_per_second'])
print(metrics['estimated_speedup'])
```

## Example Programs

### Fibonacci
```synapse
def fib(n) {
    if (n <= 1) return n
    return fib(n - 1) + fib(n - 2)
}
```

### Factorial
```synapse
def factorial(n) {
    if (n <= 1) return 1
    return n * factorial(n - 1)
}
```

### Sum Array
```synapse
def sum_array(arr) {
    let sum = 0
    for i in arr {
        sum = sum + arr[i]
    }
    return sum
}
```

## Performance Expectations

| Operation | Native (JIT) | Bytecode VM | Python |
|-----------|--------------|-------------|--------|
| Integer arithmetic | 1-2 ns | 3.5 ns | 100 ns |
| Function call | 5-10 ns | 50 ns | 500 ns |
| Array access | 2-3 ns | 5 ns | 200 ns |
| **Overall speedup** | **15-20x** | **30x** | **1x** |

## Components Reference

### LLVMBackend (Main)
High-level orchestrator for compilation pipeline

### LLVMCodeGenerator
AST → LLVM IR conversion

### LLVMOptimizer
Applies LLVM optimization passes

### LLVMJITCompiler
IR → Native code compilation

### LLVMTypeSystem
Type conversions and utilities

## Documentation Links

- Full Guide: `docs/LLVM_BACKEND_GUIDE.md`
- Phase Summary: `docs/PHASE_14_2_SUMMARY.md`
- Test Examples: `tests/test_phase14_2_llvm.py`

---

**Last Updated:** November 16, 2025
