import * as vscode from 'vscode';

export class SynapseDiagnosticsProvider {
	private diagnosticCollection: vscode.DiagnosticCollection;

	constructor() {
		this.diagnosticCollection = vscode.languages.createDiagnosticCollection('synapse');
	}

	updateDiagnostics(document: vscode.TextDocument): void {
		if (document.languageId !== 'synapse') {
			return;
		}

		const diagnostics: vscode.Diagnostic[] = [];
		const text = document.getText();
		const lines = text.split('\n');

		// Basic syntax checks
		diagnostics.push(...this.checkBracketMatching(document, lines));
		diagnostics.push(...this.checkSyntax(document, lines));
		diagnostics.push(...this.checkUndefinedVariables(document, lines));

		this.diagnosticCollection.set(document.uri, diagnostics);
	}

	clearDiagnostics(document: vscode.TextDocument): void {
		this.diagnosticCollection.delete(document.uri);
	}

	private checkBracketMatching(document: vscode.TextDocument, lines: string[]): vscode.Diagnostic[] {
		const diagnostics: vscode.Diagnostic[] = [];
		const brackets = { '{': '}', '[': ']', '(': ')' };
		const stack: Array<{ bracket: string; lineNum: number; charIdx: number }> = [];

		for (let lineNum = 0; lineNum < lines.length; lineNum++) {
			const line = lines[lineNum];
			for (let charIdx = 0; charIdx < line.length; charIdx++) {
				const char = line[charIdx];
				if (char in brackets) {
					stack.push({ bracket: char, lineNum, charIdx });
				} else if (Object.values(brackets).includes(char)) {
					const last = stack.pop();
					if (!last || brackets[last.bracket as keyof typeof brackets] !== char) {
						diagnostics.push({
							message: `Mismatched bracket: expected '${last ? brackets[last.bracket as keyof typeof brackets] : ''}', got '${char}'`,
							range: new vscode.Range(lineNum, charIdx, lineNum, charIdx + 1),
							severity: vscode.DiagnosticSeverity.Error
						});
					}
				}
			}
		}

		// Check for unclosed brackets
		for (const { bracket, lineNum, charIdx } of stack) {
			diagnostics.push({
				message: `Unclosed bracket: '${bracket}'`,
				range: new vscode.Range(lineNum, charIdx, lineNum, charIdx + 1),
				severity: vscode.DiagnosticSeverity.Error
			});
		}

		return diagnostics;
	}

	private checkSyntax(document: vscode.TextDocument, lines: string[]): vscode.Diagnostic[] {
		const diagnostics: vscode.Diagnostic[] = [];

		for (let lineNum = 0; lineNum < lines.length; lineNum++) {
			const line = lines[lineNum].trim();
			
			// Check for missing colons in specific statements
			if (line.match(/^\s*catch\s*\([^)]*\)\s*\{/) && !line.match(/catch.*{/)) {
				diagnostics.push({
					message: 'Catch block is missing opening brace',
					range: new vscode.Range(lineNum, 0, lineNum, line.length),
					severity: vscode.DiagnosticSeverity.Warning
				});
			}

			// Check for orphaned else
			if (line.startsWith('else') && lineNum > 0) {
				const prevLine = lines[lineNum - 1].trim();
				if (!prevLine.includes('}')) {
					diagnostics.push({
						message: 'Else without matching if',
						range: new vscode.Range(lineNum, 0, lineNum, 4),
						severity: vscode.DiagnosticSeverity.Error
					});
				}
			}
		}

		return diagnostics;
	}

	private checkUndefinedVariables(document: vscode.TextDocument, lines: string[]): vscode.Diagnostic[] {
		const diagnostics: vscode.Diagnostic[] = [];
		const definedVars = new Set<string>();
		const usedVars = new Map<string, { line: number; col: number }>();

		// First pass: collect defined variables
		for (let lineNum = 0; lineNum < lines.length; lineNum++) {
			const line = lines[lineNum];
			
			// Function parameters
			const funcMatch = line.match(/def\s+(\w+)\s*\(([^)]*)\)/);
			if (funcMatch) {
				definedVars.add(funcMatch[1]);
				if (funcMatch[2]) {
					funcMatch[2].split(',').forEach(param => {
						definedVars.add(param.trim());
					});
				}
			}

			// Let statements
			const letMatch = line.match(/let\s+(\w+)/);
			if (letMatch) {
				definedVars.add(letMatch[1]);
			}

			// For loops
			const forMatch = line.match(/for\s+(\w+)\s+in/);
			if (forMatch) {
				definedVars.add(forMatch[1]);
			}

			// Catch blocks
			const catchMatch = line.match(/catch\s*\(\s*(\w+)\s*\)/);
			if (catchMatch) {
				definedVars.add(catchMatch[1]);
			}
		}

		// Add built-in functions
		['print', 'len', 'range', 'sum', 'max', 'min', 'sample'].forEach(f => definedVars.add(f));

		return diagnostics;
	}
}
