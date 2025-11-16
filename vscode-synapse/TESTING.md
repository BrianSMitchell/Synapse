# VS Code Extension Testing Guide

## Manual Testing Checklist

### Syntax Highlighting
- [ ] Keywords are colored correctly (def, let, if, for, try, etc.)
- [ ] Operators are highlighted differently from keywords
- [ ] Strings are in distinct color
- [ ] Numbers are highlighted
- [ ] Comments are styled correctly

Test file: Create `test.syn`
```synapse
// This is a comment
let x = 42
def add(a, b) {
    a + b
}
```

### Code Completion (IntelliSense)

**Trigger with Ctrl+Space and verify:**

- [ ] Keywords appear when typing first letter
- [ ] Built-in functions (print, len, etc.) show up
- [ ] Types (int, float, list, string) are suggested
- [ ] Local variables defined with `let` appear in suggestions
- [ ] Local functions defined with `def` appear in suggestions
- [ ] Sort order is correct (keywords first, then functions, variables)

Test scenarios:
```synapse
let myVar = 5
def myFunc() { }
pr...      // Should suggest "print"
def...     // Should suggest "def"
myV...     // Should suggest "myVar"
```

### Diagnostics (Error Detection)

- [ ] Unclosed brackets are flagged: `{ [ (`
- [ ] Mismatched brackets trigger errors: `} ]`
- [ ] Orphaned else statements are detected
- [ ] Errors show correct line numbers
- [ ] Error messages are clear

Test cases:
```synapse
// Missing closing bracket
if x > 5 {
    print("hello")
// Error expected here

// Mismatched brackets
let arr = [1, 2, 3}  // Error expected

// Orphaned else
print("test")
else {
    // Error expected
}
```

### Hover Tooltips

- [ ] Hovering over keywords shows documentation
- [ ] Tooltips are helpful and clear
- [ ] Supported keywords: def, let, if, else, for, print, sample, goal, morph

Test: Hover over the keyword `def`
Expected: See documentation for function definitions

### Commands

#### Run File (Ctrl+Shift+E)
1. Create a simple `.syn` file with `print("Hello")`
2. Press Ctrl+Shift+E
3. Verify:
   - [ ] Output channel opens
   - [ ] File executes
   - [ ] Output appears in channel
   - [ ] Success/failure message shown

#### Run Selection
1. Create `.syn` file with multiple statements
2. Select a few lines
3. Run with context menu "Synapse: Run Selection"
4. Verify:
   - [ ] Only selected code executes
   - [ ] Output appears
   - [ ] Temp file is cleaned up

#### Open REPL
1. Press Ctrl+Shift+`
2. Verify:
   - [ ] Terminal opens with Synapse REPL started
   - [ ] Can input commands
   - [ ] Output is visible

### Snippets

Test each snippet:

- [ ] `def` - Creates function template
- [ ] `let` - Creates variable declaration
- [ ] `if` - Creates if statement
- [ ] `ifelse` - Creates if-else block
- [ ] `for` - Creates for loop
- [ ] `try` - Creates try-catch block
- [ ] `goal` - Creates goal declaration
- [ ] `morph` - Creates morph block
- [ ] `print` - Creates print statement
- [ ] `sample` - Creates sample statement
- [ ] `import` - Creates import statement

## Automated Testing

### Unit Tests

```bash
npm run test
```

Current test coverage areas:
- [ ] Completion item generation
- [ ] Diagnostic rule detection
- [ ] Command execution

### Integration Tests

Create test scenarios that exercise multiple components:

1. **Full Workflow Test**
   - Open file with errors
   - Check diagnostics appear
   - Run file
   - Verify output

2. **Completion Pipeline**
   - Type code
   - Trigger completion
   - Select item
   - Verify insertion

## Performance Testing

### IntelliSense Response Time
- Create large `.syn` file (1000+ lines)
- Trigger completion multiple times
- Expected: < 100ms response time

### Diagnostics Response Time
- Edit large file
- Expected: Diagnostics update < 500ms

Test with:
```bash
# Monitor CPU and memory in Task Manager while editing
```

## Browser-based Testing

For future WASM target:

- [ ] Extension works in VS Code Web
- [ ] File execution works in browser environment
- [ ] Output is displayed correctly

## Error Scenarios

Test error handling:

- [ ] Missing Synapse runtime shows helpful error
- [ ] Invalid Python path shows error message
- [ ] Malformed code shows diagnostics
- [ ] Execution timeout doesn't hang UI
- [ ] Large outputs don't crash extension

## Testing Matrix

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Syntax highlighting | ✓ | ✓ | ✓ |
| Completion | ✓ | ✓ | ✓ |
| Diagnostics | ✓ | ✓ | ✓ |
| Run file | ✓ | ✓ | ✓ |
| REPL | ✓ | ✓ | ✓ |

## Regression Testing

When making changes, retest:

1. Syntax highlighting on all token types
2. Completion ranking and filtering
3. All diagnostic rules
4. All commands with edge cases
5. Performance with large files

## Known Issues to Test

Document any known issues:

```markdown
## Known Issues

1. REPL input requires terminal mode
   - Status: Planned for v0.2
   - Workaround: Use terminal directly

2. Some scoping issues not detected
   - Status: Complex analysis needed
   - Impact: May not catch all errors
```

## Test Report Template

```markdown
# Test Report - [Date]

## Environment
- VS Code: [version]
- OS: [OS and version]
- Python: [version]
- Extension: [version]

## Test Results

### Syntax Highlighting
- Passed: Y/N
- Issues: [list any issues]

### Code Completion
- Passed: Y/N
- Issues: [list any issues]

[... continue for each feature ...]

## Overall Status
- [PASS] / [FAIL]
- Notes: [any observations]
```

---

Run these tests before every release.
