# Synapse VS Code Extension - Quick Start Guide

Get up and running with Synapse language support in VS Code in 5 minutes.

## Installation

### Option 1: Build from Source (Development)
```bash
cd vscode-synapse
npm install
npm run compile
```

Then in VS Code: **F5** to start debugging with the extension.

### Option 2: Install Pre-built (When Available)
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Synapse"
4. Click Install

## Creating Your First Synapse File

1. Create a new file: `hello.syn`
2. Type the following:
```synapse
let greeting = "Hello, Synapse!"
print(greeting)
```

3. Press **Ctrl+Shift+E** to run
4. See output in the "Synapse" output channel

## Quick Features

### Code Completion (Ctrl+Space)
Start typing keywords and press Ctrl+Space to see suggestions:
- `def` - Define a function
- `let` - Declare a variable
- `if`, `for`, `while` - Control flow
- `print` - Output text

### Hover Help
Hover over any keyword to see documentation.

### Code Snippets
Type a keyword and press Tab to expand snippets:
- `def` + Tab → Function template
- `let` + Tab → Variable template
- `if` + Tab → If statement
- `for` + Tab → For loop

### Error Detection
Syntax errors appear as you type:
- Unclosed brackets
- Missing parentheses
- Invalid syntax

### Run Code
- **Ctrl+Shift+E** - Run entire file
- Select code + right-click → "Synapse: Run Selection"
- **Ctrl+Shift+`** - Open Synapse REPL

## Example Programs

### Variables and Functions
```synapse
def greet(name) {
    let greeting = "Hello, " 
    greeting
}

print(greet("World"))
```

### Loops and Conditionals
```synapse
for i in [1, 2, 3, 4, 5] {
    if i > 2 {
        print(i)
    }
}
```

### Error Handling
```synapse
try {
    let x = 10 / 0
} catch (err) {
    print("Caught error!")
}
```

### Lists and Indexing
```synapse
let arr = [10, 20, 30]
print(arr[0])

let matrix = [[1, 2], [3, 4]]
print(matrix[1][1])
```

### Probabilistic Code
```synapse
let x = sample(normal)
print(x)
```

## Configuration

Edit your **VS Code settings** (Ctrl+,) and add:

```json
{
  "synapse.pythonPath": "python3",
  "synapse.enableDiagnostics": true,
  "synapse.enableAutocomplete": true
}
```

## Troubleshooting

### "Synapse executable not found"
Make sure you have Python 3.8+ installed and configured:
```bash
python --version
```

### Completion not working
- Press **Ctrl+Space** to trigger manually
- Ensure `enableAutocomplete` is true in settings

### No output when running file
- Check the "Synapse" output channel (View → Output)
- Ensure the Synapse runtime is installed
- Look for error messages in the output

### Extension not activating
- Reload VS Code window: **Ctrl+Shift+P** → "Reload Window"
- Check Extension panel for errors

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Run file | Ctrl+Shift+E |
| Open REPL | Ctrl+Shift+` |
| Trigger completion | Ctrl+Space |
| Go to definition | F12 |
| Quick fix | Ctrl+. |
| Format document | Alt+Shift+F |

## Next Steps

1. **Learn the Language**: Read [Synapse Documentation](https://github.com/BrianSMitchell/Synapse)
2. **Explore Examples**: Check out `/examples` directory
3. **Join Community**: GitHub discussions and issues
4. **Write Code**: Start building with Synapse!

## Features Overview

✅ **Syntax Highlighting** - Beautiful code formatting  
✅ **IntelliSense** - Smart code completion  
✅ **Diagnostics** - Real-time error detection  
✅ **Snippets** - Quick code templates  
✅ **Execution** - Run code directly from editor  
✅ **REPL** - Interactive development environment  
✅ **Documentation** - Hover help for keywords  

## Getting Help

- **GitHub Issues**: Report bugs and request features
- **Documentation**: See README.md for complete guide
- **Examples**: Check `/examples` for sample code
- **Development**: See DEVELOPMENT.md for architecture

---

**Happy Coding with Synapse!** 🚀

For more information, visit: https://github.com/BrianSMitchell/Synapse
