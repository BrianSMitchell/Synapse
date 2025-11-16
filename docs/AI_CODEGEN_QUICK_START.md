# AI Code Generation - Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies
```bash
# Core only (uses mock provider, no API needed)
pip install synapse

# With OpenAI support
pip install synapse openai

# With Anthropic support  
pip install synapse anthropic
```

### 2. Set API Keys (Optional)
```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Generate Your First Function
```bash
# No API key? Use mock provider (built-in templates)
synapse gen "fibonacci function" -p mock

# With OpenAI
synapse gen "fibonacci function" -p openai

# Verbose output
synapse gen "fibonacci function" -v
```

## Common Tasks

### Generate a Named Function
```bash
synapse gen-func fibonacci "compute fibonacci of n" -p n
synapse gen-func factorial "compute n!" -p n
synapse gen-func is_prime "check if n is prime" -p n
```

### Generate a Module with Multiple Functions
```bash
# List operations (sum, max, min)
synapse gen-module "list utilities" -n 3

# Mathematical functions
synapse gen-module "math helpers" -n 5

# String processing
synapse gen-module "string utilities" -n 4
```

### Validate Your Code
```bash
# Check a file
synapse validate my_code.syn

# Check inline
synapse validate "def foo(): return 42" --inline

# Verbose validation
synapse validate my_code.syn -v
```

## Python API Examples

### Basic Usage
```python
from synapse.ai.codegen import CodeGenerator

# Initialize (no API key needed for mock)
gen = CodeGenerator(provider="mock")

# Generate code
code = gen.generate("fibonacci function")
print(code)
```

### With OpenAI
```python
from synapse.ai.codegen import CodeGenerator

gen = CodeGenerator(provider="openai")
code = gen.generate("fibonacci with memoization")
print(code)
```

### Generate and Validate
```python
from synapse.ai.codegen import CodeGenerator, CodeValidator

gen = CodeGenerator(provider="mock")
code = gen.generate("fibonacci", validate=True)

# Verify it's valid
is_valid, error = CodeValidator.validate_syntax(code)
assert is_valid, f"Code validation failed: {error}"

print("✓ Generated and validated code!")
print(code)
```

### Function Generation
```python
gen = CodeGenerator(provider="mock")

code = gen.generate_function(
    name="fibonacci",
    description="compute fibonacci of n",
    params=["n"]
)
print(code)
```

### Module Generation
```python
gen = CodeGenerator(provider="mock")

code = gen.generate_module(
    description="list operations",
    num_functions=3
)
print(code)
```

## Available Mock Templates

When using `provider="mock"`, you get instant templates for:

- `fibonacci` - Fibonacci sequence computation
- `factorial` - Factorial calculation
- `sum` - Sum a list
- `max` - Find maximum in list

Example:
```bash
synapse gen "fibonacci" -p mock        # ✓ Returns template
synapse gen "sum a list" -p mock       # ✓ Returns template
synapse gen "unknown xyz" -p mock      # Returns fallback
```

## Caching

Generated code is automatically cached by default:

```bash
# First run: Calls LLM API
synapse gen "fibonacci" -p openai

# Second run: Uses cache (instant)
synapse gen "fibonacci" -p openai

# Disable caching
synapse gen "fibonacci" --no-cache
```

Cache location: `$TEMP/synapse_codegen_cache/` (configurable)

## Error Handling

### API Key Not Found
```bash
# Solution: Set environment variable
export OPENAI_API_KEY="sk-..."
synapse gen "fibonacci" -p openai
```

### Invalid Code Generated
- Automatically retried up to 3 times
- Validation checks for syntax errors
- Specify custom max attempts:

```python
code = gen.generate("fibonacci", max_attempts=5)
```

### Rate Limiting
- OpenAI: 3,500 RPM for free tier
- Anthropic: 5 requests per minute free
- Use mock provider for unlimited testing

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "OPENAI_API_KEY not found" | `export OPENAI_API_KEY="sk-..."` |
| "Invalid code generated" | Retries automatically, increase `max_attempts` |
| "Timeout" | Use mock provider or check API status |
| "Unmatched braces error" | LLM generation failed validation, retried automatically |

## Next Steps

### Learn More
- [Full Documentation](./PHASE_16_1_CODEGEN.md)
- [API Reference](./CODEGEN_API.md)
- [Advanced Usage](./AI_CODEGEN_ADVANCED.md)

### Integrate with Your Project
```python
from synapse.ai.codegen import CodeGenerator

def my_app():
    gen = CodeGenerator(provider="openai")
    
    # User describes what they want
    user_input = "function to check if palindrome"
    
    # AI generates code
    code = gen.generate(user_input)
    
    # Use it
    execute_synapse_code(code)
```

### Try Advanced Features
- Multi-function modules
- Custom validation
- Caching control
- Verbose logging

## Tips & Tricks

### Faster Development
1. Use `provider="mock"` for quick iteration
2. Enable `use_cache=True` (default)
3. Use `--no-validate` for speed (not recommended)

### Better Results
1. Be specific: "fibonacci with memoization" vs "fibonacci"
2. Include parameter names: `gen_func(name, "...", params=["n"])`
3. Use verbose mode to see generation progress: `-v`

### Cost Optimization
1. Use mock provider for testing (free)
2. Cache all results (automatic)
3. Test locally before deploying

---

**Ready to generate!** Try: `synapse gen "hello world function" -p mock`
