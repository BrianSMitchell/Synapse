import * as vscode from 'vscode';

export class SynapseCompletionProvider implements vscode.CompletionItemProvider {
	private keywords = [
		'def', 'let', 'if', 'else', 'for', 'in', 'while',
		'try', 'catch', 'import', 'morph', 'goal', 'sample'
	];

	private builtins = [
		'print', 'len', 'range', 'sum', 'max', 'min',
		'append', 'pop', 'reverse', 'sort'
	];

	private types = [
		'int', 'float', 'string', 'list'
	];

	private distributions = [
		'normal', 'bernoulli', 'uniform', 'exponential',
		'poisson', 'gamma', 'beta'
	];

	provideCompletionItems(
		document: vscode.TextDocument,
		position: vscode.Position,
		token: vscode.CancellationToken,
		context: vscode.CompletionContext
	): vscode.CompletionItem[] {
		const completions: vscode.CompletionItem[] = [];

		// Keywords
		for (const keyword of this.keywords) {
			const item = new vscode.CompletionItem(keyword, vscode.CompletionItemKind.Keyword);
			item.detail = `Keyword`;
			item.sortText = `0_${keyword}`; // Prioritize keywords
			completions.push(item);
		}

		// Built-in functions
		for (const builtin of this.builtins) {
			const item = new vscode.CompletionItem(builtin, vscode.CompletionItemKind.Function);
			item.detail = `Built-in function`;
			item.sortText = `1_${builtin}`;
			completions.push(item);
		}

		// Types
		for (const type of this.types) {
			const item = new vscode.CompletionItem(type, vscode.CompletionItemKind.Class);
			item.detail = `Type`;
			item.sortText = `2_${type}`;
			completions.push(item);
		}

		// Distributions (for sample context)
		const line = document.lineAt(position.line);
		const linePrefix = line.text.substr(0, position.character);
		if (linePrefix.includes('sample')) {
			for (const dist of this.distributions) {
				const item = new vscode.CompletionItem(dist, vscode.CompletionItemKind.Method);
				item.detail = `Distribution`;
				completions.push(item);
			}
		}

		// Local variables and functions (scan document)
		const scanner = new VariableScanner(document);
		const localSymbols = scanner.scan();
		
		for (const symbol of localSymbols) {
			const item = new vscode.CompletionItem(symbol.name, symbol.kind);
			item.detail = symbol.detail;
			item.sortText = `3_${symbol.name}`;
			completions.push(item);
		}

		return completions;
	}

	resolveCompletionItem?(
		item: vscode.CompletionItem,
		token: vscode.CancellationToken
	): vscode.CompletionItem {
		return item;
	}
}

interface LocalSymbol {
	name: string;
	kind: vscode.CompletionItemKind;
	detail: string;
}

class VariableScanner {
	constructor(private document: vscode.TextDocument) {}

	scan(): LocalSymbol[] {
		const symbols: LocalSymbol[] = [];
		const text = this.document.getText();

		// Match function definitions
		const funcRegex = /def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g;
		let match;
		while ((match = funcRegex.exec(text)) !== null) {
			symbols.push({
				name: match[1],
				kind: vscode.CompletionItemKind.Function,
				detail: 'Function definition'
			});
		}

		// Match let statements
		const letRegex = /let\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=/g;
		while ((match = letRegex.exec(text)) !== null) {
			symbols.push({
				name: match[1],
				kind: vscode.CompletionItemKind.Variable,
				detail: 'Variable'
			});
		}

		// Remove duplicates
		const seen = new Set<string>();
		return symbols.filter(s => {
			if (seen.has(s.name)) return false;
			seen.add(s.name);
			return true;
		});
	}
}
