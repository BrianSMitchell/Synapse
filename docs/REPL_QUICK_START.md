# Synapse REPL - Quick Start Guide

## Starting the REPL

```bash
python -m synapse.repl
```

Or from Python:
```python
from synapse.repl import main
main()
```

---

## Basic Commands

### Simple Expressions
```
synapse> let x = 42
42
synapse> print(x)
42
synapse> x + 8
50
```

### Variables and Functions
```
synapse> let name = "Synapse"
"Synapse"
synapse> def greet(n)
    ...   print("Hello, " + n)
    ...
synapse> greet(name)
Hello, Synapse
```

### Multi-Line Input
```
synapse> if x > 0 then
    ...   print("positive")
    ... else
    ...   print("non-positive")
    ...
positive
```

**Tip:** Press Enter twice or until all brackets are balanced to execute.

---

## Special Commands

| Command | Action |
|---------|--------|
| `exit` | Exit REPL |
| `help` | Show help |
| `clear` | Clear input buffer |

---

## Syntax Highlighting

The REPL automatically highlights:
- **Keywords** (magenta): `let`, `def`, `if`, `while`, etc.
- **Built-ins** (yellow): `print`, `len`, `range`, etc.
- **Strings** (green): `"hello"`, `'world'`
- **Numbers** (cyan): `42`, `3.14`
- **Operators** (bright yellow): `+`, `-`, `*`, `/`
- **Comments** (gray): `# comment`

---

## Auto-Complete

Type a prefix and get suggestions for:
- Keywords: `le` → `let`, `def` → no match
- Functions: `pri` → `print`, `ran` → `range`
- Variables: `my` → `my_var` (if defined)

**Note:** Auto-complete is computed but not interactive in this version. Future versions will support Tab completion.

---

## Examples

### Example 1: Calculate Factorial
```
synapse> def factorial(n)
    ...   if n <= 1 then
    ...     return 1
    ...   else
    ...     return n * factorial(n - 1)
    ...
synapse> factorial(5)
120
```

### Example 2: Array Operations
```
synapse> let arr = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
synapse> let squared = [x * x for x in arr]
[1, 4, 9, 16, 25]
```

### Example 3: Probabilistic Code
```
synapse> let coin = bernoulli(0.5)
0.5
synapse> if sample(coin) then
    ...   print("Heads!")
    ... else
    ...   print("Tails!")
    ...
Heads!
```

### Example 4: Multi-Line with Nesting
```
synapse> let matrix = [
    ...   [1, 2, 3],
    ...   [4, 5, 6],
    ...   [7, 8, 9]
    ... ]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
synapse> print(matrix[0][1])
2
```

---

## Tips & Tricks

### 1. Check Variable Type
```
synapse> type(x)
<class 'int'>
```

### 2. Get Help on Built-ins
```
synapse> help
# Shows REPL commands and syntax highlighting info
```

### 3. Clear After Mistakes
```
synapse> if x > 0 then    # Oops, forgot closing
    ...   clear           # Type 'clear' to reset
synapse> # Now start over
```

### 4. Multi-line with Comments
```
synapse> def add(a, b)
    ...   # Add two numbers
    ...   return a + b
    ...
synapse> add(2, 3)
5
```

### 5. Use Command History
Previously entered commands are tracked in `.history`. You can review them after exiting.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+C | Interrupt current input |
| Ctrl+D | Exit REPL (or type `exit`) |
| Backspace | Delete character |
| Return | Execute or continue |

---

## Common Errors

### Missing Closing Bracket
```
synapse> let arr = [1, 2, 3
    ...   # Type ] to close
    ...   ]
[1, 2, 3]
```

### Undefined Variable
```
synapse> print(undefined)
Error: undefined is not defined
```

### Syntax Error
```
synapse> let 123x = 5
Error: Invalid variable name
```

---

## Supported Data Types

- **Numbers:** integers, floats (`42`, `3.14`)
- **Strings:** single or double quotes (`"hello"`, `'world'`)
- **Booleans:** `True`, `False`
- **Lists:** array literals (`[1, 2, 3]`)
- **Dictionaries:** key-value pairs
- **Distributions:** `bernoulli(p)`, `normal(μ, σ)`, etc.

---

## Advanced Features

### Sampling from Distributions
```
synapse> let x = normal(0, 1)
0.523  # Random sample
synapse> sample(x)  # Another sample
-1.204
```

### Goal-Driven Programming
```
synapse> goal: find_pattern(data)
    ...   # AI agent explores solutions
    ...
```

### Code Morphing
```
synapse> morph my_function
    ...   # Runtime code modification
    ...
```

### Parallel Agents
```
synapse> parallel
    ...   agent_1(task1)
    ...   agent_2(task2)
    ...
```

---

## Troubleshooting

**Issue:** Colors not showing?
- Some terminals don't support ANSI colors. Check terminal settings.

**Issue:** Multi-line not working?
- Make sure all brackets `[]`, parentheses `()`, and braces `{}` are balanced.

**Issue:** Auto-complete not available?
- Auto-complete is computed internally. Full interactive Tab completion coming soon.

---

## Next Steps

- Read `PHASE_15_4_REPL_ENHANCEMENTS.md` for detailed architecture
- Check `Synapse PRD.md` for language design
- Explore examples in `examples/` directory

---

*Synapse REPL - Interactive Development at the Speed of Thought*
