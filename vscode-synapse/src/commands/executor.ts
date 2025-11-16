import * as vscode from 'vscode';
import * as cp from 'child_process';
import * as path from 'path';
import * as os from 'os';

let outputChannel: vscode.OutputChannel | null = null;

function getOutputChannel(): vscode.OutputChannel {
	if (!outputChannel) {
		outputChannel = vscode.window.createOutputChannel('Synapse');
	}
	return outputChannel;
}

export async function runFile(): Promise<void> {
	const editor = vscode.window.activeTextEditor;
	if (!editor) {
		vscode.window.showErrorMessage('No active editor');
		return;
	}

	const document = editor.document;
	if (document.languageId !== 'synapse') {
		vscode.window.showErrorMessage('Active file is not a Synapse file');
		return;
	}

	if (document.isDirty) {
		await document.save();
	}

	const filePath = document.fileName;
	const outputCh = getOutputChannel();
	outputCh.clear();
	outputCh.show(true);
	outputCh.appendLine(`Running: ${filePath}`);
	outputCh.appendLine('');

	const config = vscode.workspace.getConfiguration('synapse');
	const pythonPath = config.get<string>('pythonPath') || 'python';

	try {
		const cwd = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || os.homedir();
		// Run Synapse interpreter
		const childProcess = cp.spawn(pythonPath, ['-m', 'synapse.repl', filePath], {
			cwd: cwd
		});

		let stdout = '';
		let stderr = '';

		childProcess.stdout?.on('data', (data: Buffer) => {
			stdout += data.toString();
			outputCh.append(data.toString());
		});

		childProcess.stderr?.on('data', (data: Buffer) => {
			stderr += data.toString();
			outputCh.append(data.toString());
		});

		childProcess.on('close', (code: number | null) => {
			if (code === 0) {
				outputCh.appendLine('\n✓ Execution completed successfully');
			} else {
				outputCh.appendLine(`\n✗ Execution failed with code ${code}`);
			}
		});

		childProcess.on('error', (err: Error) => {
			vscode.window.showErrorMessage(`Failed to run Synapse: ${err.message}`);
			outputCh.appendLine(`Error: ${err.message}`);
		});
	} catch (error) {
		vscode.window.showErrorMessage(`Failed to execute file: ${error}`);
	}
}

export async function runSelection(): Promise<void> {
	const editor = vscode.window.activeTextEditor;
	if (!editor) {
		vscode.window.showErrorMessage('No active editor');
		return;
	}

	const selection = editor.selection;
	if (selection.isEmpty) {
		vscode.window.showErrorMessage('No text selected');
		return;
	}

	const code = editor.document.getText(selection);
	const outputCh = getOutputChannel();
	outputCh.clear();
	outputCh.show(true);
	outputCh.appendLine('Running selected code:');
	outputCh.appendLine('');

	const config = vscode.workspace.getConfiguration('synapse');
	const pythonPath = config.get<string>('pythonPath') || 'python';

	// Create a temporary file with the selection
	const fs = require('fs');
	const tmpFile = path.join(os.tmpdir(), `synapse_${Date.now()}.syn`);
	
	try {
		fs.writeFileSync(tmpFile, code);

		const cwd = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || os.homedir();
		const childProcess = cp.spawn(pythonPath, ['-m', 'synapse.repl', tmpFile], {
			cwd: cwd
		});

		childProcess.stdout?.on('data', (data: Buffer) => {
			outputCh.append(data.toString());
		});

		childProcess.stderr?.on('data', (data: Buffer) => {
			outputCh.append(data.toString());
		});

		childProcess.on('close', () => {
			fs.unlinkSync(tmpFile);
		});
	} catch (error) {
		vscode.window.showErrorMessage(`Failed to execute selection: ${error}`);
	}
}

export async function openREPL(): Promise<void> {
	const outputCh = getOutputChannel();
	outputCh.clear();
	outputCh.show(true);
	outputCh.appendLine('Synapse REPL');
	outputCh.appendLine('Type code and press Enter to execute');
	outputCh.appendLine('');

	// Note: Full REPL support would require input handling
	// For now, show a message with instructions
	vscode.window.showInformationMessage(
		'Open terminal and run: python -m synapse.repl',
		'Open Terminal'
	).then(selection => {
		if (selection === 'Open Terminal') {
			const terminal = vscode.window.createTerminal('Synapse REPL');
			terminal.sendText('python -m synapse.repl');
			terminal.show();
		}
	});
}
