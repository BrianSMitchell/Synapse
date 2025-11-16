# Synapse Language Support for VS Code

Official VS Code extension for the **Synapse** programming language - an AI-driven, probabilistic language with self-evolution capabilities.

## Features

### 🎨 Syntax Highlighting
- Full syntax highlighting for Synapse code
- Support for all Synapse keywords, operators, and literals
- Clear distinction between different token types

### 🔍 IntelliSense & Code Completion
- Keyword completion (def, let, if, for, try, etc.)
- Built-in function suggestions (print, len, sample, etc.)
- Type suggestions (int, float, string, list)
- Local variable and function recognition
- Distribution completion for probabilistic code

### 📋 Code Snippets
Quick templates for common patterns:
- `def` - Function definitions
- `let` - Variable declarations
- `if` / `ifelse` - Conditional statements
- `for` - Loop statements
- `try` - Error handling
- `goal` - Goal declarations
- `morph` - Self-modification blocks
- And more...

### ⚠️ Real-time Diagnostics
- Bracket matching validation
- Syntax error detection
- Undefined variable warnings (basic)
- Error highlighting with line numbers

### 🎯 Hover Documentation
- Hover over keywords for instant documentation
- Built-in function descriptions
- Type information

### ▶️ Quick Execution
- **Ctrl+Shift+E** - Run current Synapse file
- **Ctrl+Shift+`** - Open Synapse REPL
- Run selection with right-click menu

### 🔌 Debugger Integration (Coming Soon)
- Breakpoint support
- Step through execution
- Variable inspection
- Call stack viewing

## Installation

1. Install from VS Code Marketplace: [Synapse Language Support](https://marketplace.visualstudio.com/items?itemName=BrianSMitchell.synapse)
2. Alternatively, clone the repository and run:
   ```bash
   npm install
   npm run compile
   npm run package
   ```
3. Install the generated `.vsix` file in VS Code

## Configuration

Add to your VS Code `settings.json`:

```json
{
  "synapse.synapseExecutablePath": "synapse",
  "synapse.pythonPath": "python",
  "synapse.enableAutocomplete": true,
  "synapse.enableDiagnostics": true
}
```

## Requirements

- VS Code 1.85.0 or higher
- Python 3.8+ (for running Synapse files)
- Synapse language runtime

## Usage

### Basic Example
Create a file `hello.syn`:
```synapse
let message = "Hello, Synapse!"
print(message)
```

Run with **Ctrl+Shift+E** to see output in the Synapse output channel.

### Function Definition
```synapse
def add(a, b) {
    a + b
}

let result = add(5, 3)
print(result)
```

### Control Flow
```synapse
let x = 10
if x > 5 {
    print("x is greater than 5")
} else {
    print("x is less than or equal to 5")
}
```

### Loops
```synapse
for i in [1, 2, 3, 4, 5] {
    print(i)
}
```

### Error Handling
```synapse
try {
    let result = risky_operation()
    print(result)
} catch (err) {
    print("Error occurred!")
}
```

## Development

### Setup
```bash
npm install
npm run compile
```

### Watch Mode
```bash
npm run watch
```

### Testing
```bash
npm run test
```

### Building the Extension
```bash
npm run vscode:prepublish
```

## Architecture

The extension consists of:

- **extension.ts** - Main extension entry point, manages providers and commands
- **completionProvider.ts** - IntelliSense suggestions and code completion
- **diagnosticsProvider.ts** - Real-time error detection and validation
- **executor.ts** - Command execution (run file, selection, REPL)

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Roadmap

- [x] Syntax highlighting
- [x] Basic code completion
- [x] Code snippets
- [x] Error diagnostics
- [ ] Full debugger integration
- [ ] Symbol navigation (Go to Definition)
- [ ] Rename refactoring
- [ ] Advanced type checking
- [ ] Performance profiling integration

## Known Issues

- REPL input requires terminal mode (full interactive REPL coming in v0.2)
- Some advanced scoping issues not detected
- Debugger integration not yet implemented

## License

MIT - See LICENSE file for details

## Support

For issues, questions, or suggestions, visit:
- [GitHub Issues](https://github.com/BrianSMitchell/Synapse/issues)
- [Synapse Documentation](https://github.com/BrianSMitchell/Synapse/docs)

---

**Version:** 0.1.0  
**Last Updated:** November 16, 2025
