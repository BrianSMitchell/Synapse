import * as vscode from 'vscode';
import { SynapseCompletionProvider } from './providers/completionProvider';
import { SynapseDiagnosticsProvider } from './providers/diagnosticsProvider';
import { runFile, runSelection, openREPL } from './commands/executor';

export function activate(context: vscode.ExtensionContext) {
	console.log('Synapse extension is now active');

	// Register completion provider for IntelliSense
	context.subscriptions.push(
		vscode.languages.registerCompletionItemProvider(
			'synapse',
			new SynapseCompletionProvider(),
			'.'
		)
	);

	// Register diagnostics provider
	const diagnosticsProvider = new SynapseDiagnosticsProvider();
	context.subscriptions.push(
		vscode.workspace.onDidOpenTextDocument(doc => diagnosticsProvider.updateDiagnostics(doc)),
		vscode.workspace.onDidChangeTextDocument(event => diagnosticsProvider.updateDiagnostics(event.document)),
		vscode.workspace.onDidCloseTextDocument(doc => diagnosticsProvider.clearDiagnostics(doc))
	);

	// Register commands
	context.subscriptions.push(
		vscode.commands.registerCommand('synapse.runFile', () => runFile()),
		vscode.commands.registerCommand('synapse.runSelection', () => runSelection()),
		vscode.commands.registerCommand('synapse.openREPL', () => openREPL())
	);

	// Hover provider for documentation
	context.subscriptions.push(
		vscode.languages.registerHoverProvider('synapse', {
			provideHover(document, position) {
				const range = document.getWordRangeAtPosition(position);
				const word = document.getText(range);
				
				// Keywords documentation
				const docs: { [key: string]: string } = {
					'def': 'Define a function: `def name(params) { body }`',
					'let': 'Declare a variable: `let x = value`',
					'if': 'Conditional statement: `if condition { body }`',
					'else': 'Else clause: `} else { body }`',
					'for': 'Loop statement: `for item in iterable { body }`',
					'in': 'In operator for iteration',
					'try': 'Try block: `try { } catch (err) { }`',
					'catch': 'Catch block for error handling',
					'import': 'Import module: `import "file.syn"`',
					'morph': 'Self-modification: `morph name { body }`',
					'goal': 'Goal declaration: `goal: expression`',
					'sample': 'Sample from distribution: `sample(distribution)`',
					'print': 'Print output: `print(expression)`',
					'and': 'Logical AND operator',
					'or': 'Logical OR operator',
					'not': 'Logical NOT operator'
				};

				if (docs[word]) {
					return new vscode.Hover(new vscode.MarkdownString(docs[word]));
				}
				return null;
			}
		})
	);
}

export function deactivate() {
	console.log('Synapse extension is now deactivated');
}
