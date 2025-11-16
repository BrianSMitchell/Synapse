# VS Code Extension Development Guide

## Architecture Overview

The Synapse VS Code extension is built with TypeScript and integrates with the Synapse language runtime.

### Components

```
src/
├── extension.ts              # Main entry point, activates providers/commands
├── providers/
│   ├── completionProvider.ts # IntelliSense/autocomplete
│   └── diagnosticsProvider.ts # Real-time error checking
└── commands/
    └── executor.ts           # Run file, selection, REPL commands
```

### Key Files

- **package.json** - Extension metadata, VSCode API configuration
- **tsconfig.json** - TypeScript compilation settings
- **syntaxes/synapse.tmLanguage.json** - TextMate grammar for syntax highlighting
- **snippets/synapse.json** - Code snippet definitions

## Development Workflow

### 1. Setup

```bash
git clone https://github.com/BrianSMitchell/Synapse
cd vscode-synapse
npm install
```

### 2. Development Mode

Open the extension folder in VS Code and press **F5** to start debugging:

```bash
npm run watch    # In terminal: compile on file changes
```

This will:
- Compile TypeScript on save
- Open a new VS Code window with the extension loaded
- Allow you to debug and test in real-time

### 3. Testing

```bash
npm run test
```

## Adding Features

### Adding a New Command

1. Define in `package.json` under `contributes.commands`:
```json
{
  "command": "synapse.myNewCommand",
  "title": "Synapse: My New Command"
}
```

2. Implement in `src/commands/executor.ts`:
```typescript
export async function myNewCommand(): Promise<void> {
  // Implementation
}
```

3. Register in `src/extension.ts`:
```typescript
context.subscriptions.push(
  vscode.commands.registerCommand('synapse.myNewCommand', () => myNewCommand())
);
```

### Extending IntelliSense

Edit `src/providers/completionProvider.ts`:

```typescript
// Add to SynapseCompletionProvider class
private myNewCategory = ['item1', 'item2'];

// In provideCompletionItems()
for (const item of this.myNewCategory) {
  const completion = new vscode.CompletionItem(item, vscode.CompletionItemKind.Keyword);
  completions.push(completion);
}
```

### Adding Diagnostics Rules

Edit `src/providers/diagnosticsProvider.ts`:

```typescript
private checkMyRule(document: vscode.TextDocument, lines: string[]): vscode.Diagnostic[] {
  const diagnostics: vscode.Diagnostic[] = [];
  // Implementation
  return diagnostics;
}

// Call in updateDiagnostics()
diagnostics.push(...this.checkMyRule(document, lines));
```

## TextMate Grammar (Syntax Highlighting)

The file `syntaxes/synapse.tmLanguage.json` uses TextMate syntax. To modify:

1. Add patterns to the `repository` section
2. Use regex patterns to match tokens
3. Map to VSCode color tokens (scopes)

Example scope names:
- `keyword.control.synapse` - Control keywords (if, else, for)
- `keyword.other.synapse` - Other keywords (let, def)
- `storage.type.synapse` - Type keywords
- `string.quoted.double.synapse` - String literals
- `comment.line.double-slash.synapse` - Line comments

## Debugging Tips

1. **Enable debug output**: Add `console.log()` in TypeScript
2. **Check diagnostics**: Open the "Problems" panel (Ctrl+Shift+M)
3. **View extension logs**: Run "Developer: Show Logs" command
4. **Breakpoints**: Set in VS Code and press F5 to debug

## Performance Considerations

- **Diagnostics**: Runs on every file change, keep light
- **IntelliSense**: Scans document for variables, optimize regex
- **File execution**: Spawns Python process, handle async properly

## Code Style

- Use TypeScript strict mode
- Follow VS Code extension best practices
- Add JSDoc comments for public APIs
- Test with various Synapse code patterns

## Testing Checklist

Before submitting:

```
[ ] Syntax highlighting works on various code samples
[ ] Code completion triggers appropriately
[ ] Diagnostics catch errors
[ ] File execution works
[ ] REPL command opens correctly
[ ] No TypeScript compilation errors
[ ] No runtime exceptions in console
```

## Building for Release

```bash
npm run vscode:prepublish
npx vsce package
```

This generates a `.vsix` file for manual installation or publishing to the Marketplace.

## References

- [VS Code Extension API](https://code.visualstudio.com/api)
- [TextMate Grammar](https://macromates.com/manual/en/language_grammars)
- [TSLint Rules](https://www.typescriptlang.org/tsconfig)
