# Phase 16.2: Emergent Debugging - Quick Start Guide

**Phase 16.2** adds AI-powered debugging to detect and fix bugs in your Synapse code, especially those introduced by morphing operations.

---

## Installation

```bash
pip install synapse
```

No additional dependencies needed for basic usage.

---

## CLI Quick Reference

### Analyze Code for Bugs

```bash
synapse debug mycode.syn
```

**Output Example:**
```
Found 2 issue(s):

[HIGH]
  Line 2: Undefined variable 'z'
    Context: let y = x + z
    Fix: Define 'z' before use: let z = ...
```

**Exit Codes:** 0 = no issues, 1 = has issues

### Check Morphing Safety

```bash
synapse debug-morph original.syn morphed.syn
```

**Output:**
```
✓ Morphing produced valid code

ℹ️  1 new issue(s) introduced:
  [low] Line 8: Performance issue
```

### Get Fix Suggestions

```bash
synapse fix mycode.syn
```

**Apply automatically:**
```bash
synapse fix mycode.syn --apply
```

This creates `mycode.syn.bak` backup.

### Validate Code

```bash
synapse validate mycode.syn
```

---

## Python API Quick Reference

### Basic Analysis

```python
from synapse.ai.debugger import debug

code = "let y = x + 5"
bugs = debug(code, provider="mock")

for bug in bugs:
    print(f"Line {bug.line}: {bug.message}")
```

### Get Report

```python
from synapse.ai.debugger import debug_report

report = debug_report(code, provider="mock")
print(report)
```

### Suggest Fixes

```python
from synapse.ai.debugger import suggest_fixes

fixes = suggest_fixes(code, provider="mock")
for bug_id, fix in fixes.items():
    print(f"Fix: {fix}")
```

### Full Analyzer

```python
from synapse.ai.debugger import DebugAnalyzer

analyzer = DebugAnalyzer(provider="mock")

# Analyze
bugs = analyzer.analyze(code)

# Get fixes
fixes = analyzer.suggest_fixes(code)

# Apply fixes
fixed_code, remaining = analyzer.apply_fixes(code)

# Generate report
report = analyzer.report(code)

# Check morphing safety
is_valid, critical = analyzer.validate_morphing(original, morphed)
```

---

## Providers

### Mock (Default, Free)

```bash
synapse debug code.syn -p mock
```

**Pros:** Fast, free, no API key needed  
**Cons:** Heuristic-based, may miss subtle bugs

### OpenAI (GPT-4)

```bash
export OPENAI_API_KEY="sk-..."
synapse debug code.syn -p openai
```

**Pros:** Excellent accuracy, semantic understanding  
**Cons:** API cost, network latency

### Anthropic (Claude)

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
synapse debug code.syn -p anthropic
```

**Pros:** Great accuracy, good performance  
**Cons:** API cost, network latency

---

## Bug Types

| Type | Example | Severity |
|------|---------|----------|
| **SYNTAX_ERROR** | Mismatched braces | Critical |
| **UNDEFINED_VARIABLE** | Using undefined variable | High |
| **INFINITE_LOOP** | `while true {}` | Critical |
| **TYPE_ERROR** | Type mismatch | High |
| **LOGIC_ERROR** | Wrong condition | Medium |
| **PERFORMANCE_ISSUE** | Nested loops O(n²) | Low |

---

## Common Workflows

### 1. Check Generated Code

```python
from synapse.ai.codegen import CodeGenerator
from synapse.ai.debugger import DebugAnalyzer

gen = CodeGenerator(provider="openai")
debug = DebugAnalyzer(provider="mock")

# Generate
code = gen.generate("fibonacci function")

# Check
bugs = debug.analyze(code)
print(f"Found {len(bugs)} bugs")
```

### 2. Safe Morphing

```python
from synapse.core.morphing import Morpher
from synapse.ai.debugger import DebugAnalyzer

morpher = Morpher(code)
analyzer = DebugAnalyzer(provider="mock")

def safe_morph(condition, rewrite):
    original = morpher.code
    new_code = morpher.morph(condition, rewrite)
    
    is_valid, critical = analyzer.validate_morphing(original, new_code)
    return is_valid

if safe_morph(lambda acc: acc < 0.9, fix_func):
    print("Morphing applied safely")
else:
    print("Morphing blocked - would introduce bugs")
```

### 3. Iterative Improvement

```python
analyzer = DebugAnalyzer(provider="openai")

code = original_code
for iteration in range(5):
    bugs = analyzer.analyze(code)
    
    if not bugs:
        print(f"Fixed after {iteration} iterations!")
        break
    
    # Try to fix
    fixed, remaining = analyzer.apply_fixes(code)
    
    if not remaining:
        code = fixed
        print(f"Iteration {iteration}: Fixed all {len(bugs)} bugs")
    else:
        print(f"Remaining: {len(remaining)} bugs need manual review")
        break
```

---

## Performance Tips

### Enable Caching for Repeated Analysis

```python
analyzer = DebugAnalyzer(provider="mock")
analyzer.cache_enabled = True  # default

# First call: 50ms
bugs1 = analyzer.analyze(code)

# Second call: 2ms (cached)
bugs2 = analyzer.analyze(code)
```

### Use Mock Provider for Development

```python
# Development: instant feedback, free
analyzer = DebugAnalyzer(provider="mock")

# Production: high accuracy, API cost
analyzer = DebugAnalyzer(provider="openai")
```

### Batch Analysis

```python
analyzer = DebugAnalyzer(provider="openai")

files = ["file1.syn", "file2.syn", "file3.syn"]
for file in files:
    code = open(file).read()
    bugs = analyzer.analyze(code)
    # Analysis is cached, repeated patterns found fast
```

---

## Troubleshooting

### API Key Not Found

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

### File Not Found

```bash
synapse debug /path/to/file.syn
# Error if file doesn't exist
```

### No Issues Found

```bash
# Valid output
synapse debug validcode.syn
# ✓ No bugs detected
```

### Want to Test Without API

```bash
# Use mock provider (no API key needed)
synapse debug code.syn -p mock
```

---

## Examples

### Example 1: Find & Fix Undefined Variables

**Code (buggy.syn):**
```synapse
let x = 5
let y = x + z
print(y)
```

**Command:**
```bash
synapse debug buggy.syn
synapse fix buggy.syn --apply
```

**Result:**
```
Found 1 issue:
[HIGH] Line 2: Undefined variable 'z'
  Fix: Define 'z' before use

Fixed code:
let x = 5
let z = 0
let y = x + z
print(y)
```

### Example 2: Check Morphing Safety

**Original (v1.syn):**
```synapse
let accuracy = 0.6
```

**Morphed (v2.syn):**
```synapse
let accuracy = 0.6
let result = accuracy * undefined_value
```

**Command:**
```bash
synapse debug-morph v1.syn v2.syn
```

**Output:**
```
✗ Morphing introduced critical bugs:
  Line 2: Undefined variable 'undefined_value'
```

### Example 3: Python API Usage

```python
from synapse.ai.debugger import DebugAnalyzer, BugSeverity

analyzer = DebugAnalyzer(provider="mock")

code = """
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
"""

# Analyze
bugs = analyzer.analyze(code)

# Find critical issues
critical = [b for b in bugs if b.severity == BugSeverity.CRITICAL]
print(f"Critical bugs: {len(critical)}")

# Get report
report = analyzer.report(code)
print(report)
```

---

## API Reference

### DebugAnalyzer Methods

```python
analyzer = DebugAnalyzer(provider="mock")

# Analyze code for bugs
bugs = analyzer.analyze(code)

# Get fix suggestions
fixes = analyzer.suggest_fixes(code)

# Apply fixes automatically
fixed_code, remaining = analyzer.apply_fixes(code)

# Generate human-readable report
report = analyzer.report(code)

# Check morphing safety
is_valid, critical_bugs = analyzer.validate_morphing(original, morphed)

# Find new bugs from morphing
new_bugs = analyzer.analyze_morphing(original, morphed)

# Clear cache
analyzer.clear_cache()
```

### Bug Object

```python
bug.id              # Unique bug ID
bug.type            # BugType enum
bug.severity        # BugSeverity enum
bug.line            # Line number
bug.column          # Column number
bug.message         # Description
bug.suggested_fix   # Fix suggestion
bug.context         # Code context
bug.to_dict()       # Convert to dict
```

---

## Next Steps

1. **Try it:** `synapse debug mycode.syn`
2. **Read full docs:** See `PHASE_16_2_DEBUG.md`
3. **Integrate:** Use in your development workflow
4. **Report issues:** GitHub issues welcome

---

## More Information

- **Full Documentation:** `docs/PHASE_16_2_DEBUG.md`
- **Delivery Summary:** `docs/PHASE_16_2_DELIVERY.md`
- **Tests:** `tests/test_phase16_2_debug.py`
- **Implementation:** `src/synapse/ai/debugger.py`

---

**Phase 16.2:** Emergent Debugging with AI ✅ Complete

Enables safe Synapse code evolution through automatic bug detection and fixing.
