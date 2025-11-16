import sys
import re
from typing import List, Dict, Set, Tuple, Optional
from synapse.parser.parser import parse_and_execute

# ANSI color codes for syntax highlighting
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


class SyntaxHighlighter:
    """Highlights Synapse syntax with ANSI colors."""
    
    KEYWORDS = {
        'let', 'def', 'if', 'else', 'while', 'for', 'in', 'return', 'import',
        'try', 'catch', 'goal', 'sample', 'morph', 'parallel', 'consensus',
        'agent', 'True', 'False', 'None'
    }
    
    BUILTINS = {
        'print', 'len', 'range', 'int', 'float', 'str', 'bool', 'list', 'dict',
        'sum', 'min', 'max', 'abs', 'round', 'type', 'sample', 'normal',
        'bernoulli', 'categorical'
    }
    
    def __init__(self):
        self.token_patterns = [
            ('STRING', r'"[^"]*"|\'[^\']*\''),
            ('NUMBER', r'\b\d+\.?\d*\b'),
            ('COMMENT', r'#.*'),
            ('KEYWORD', r'\b(' + '|'.join(self.KEYWORDS) + r')\b'),
            ('BUILTIN', r'\b(' + '|'.join(self.BUILTINS) + r')\b'),
            ('OPERATOR', r'[+\-*/%<>=!&|^~]+'),
        ]
    
    def colorize(self, text: str) -> str:
        """Apply syntax highlighting to text."""
        if not isinstance(text, str):
            return str(text)
        
        # Build regex pattern for tokenization
        result = []
        processed = 0
        
        # Try comment first (if present, rest is comment)
        comment_match = re.search(r'#.*', text)
        if comment_match:
            # Highlight part before comment
            before_comment = text[:comment_match.start()]
            result_before = self._highlight_tokens(before_comment)
            # Add comment in gray
            comment_text = text[comment_match.start():]
            return result_before + Colors.BRIGHT_BLACK + comment_text + Colors.RESET
        
        return self._highlight_tokens(text)
    
    def _highlight_tokens(self, text: str) -> str:
        """Tokenize and highlight non-comment text."""
        result = []
        i = 0
        
        while i < len(text):
            # Skip whitespace
            if text[i].isspace():
                result.append(text[i])
                i += 1
                continue
            
            # Try to match each pattern
            matched = False
            
            # Strings
            if text[i] in ('"', "'"):
                quote = text[i]
                j = i + 1
                while j < len(text) and text[j] != quote:
                    j += 1
                if j < len(text):
                    j += 1
                    result.append(Colors.GREEN + text[i:j] + Colors.RESET)
                    i = j
                    matched = True
            
            # Numbers
            if not matched and text[i].isdigit():
                j = i
                while j < len(text) and (text[j].isdigit() or text[j] == '.'):
                    j += 1
                result.append(Colors.CYAN + text[i:j] + Colors.RESET)
                i = j
                matched = True
            
            # Keywords and identifiers
            if not matched and (text[i].isalpha() or text[i] == '_'):
                j = i
                while j < len(text) and (text[j].isalnum() or text[j] == '_'):
                    j += 1
                word = text[i:j]
                
                if word in self.KEYWORDS:
                    result.append(Colors.MAGENTA + Colors.BOLD + word + Colors.RESET)
                elif word in self.BUILTINS:
                    result.append(Colors.YELLOW + word + Colors.RESET)
                else:
                    result.append(word)
                i = j
                matched = True
            
            # Operators
            if not matched and text[i] in '+-*/%<>=!&|^~':
                j = i
                while j < len(text) and text[j] in '+-*/%<>=!&|^~':
                    j += 1
                result.append(Colors.BRIGHT_YELLOW + text[i:j] + Colors.RESET)
                i = j
                matched = True
            
            # Other characters
            if not matched:
                result.append(text[i])
                i += 1
        
        return ''.join(result)


class AutoCompleter:
    """Provides context-aware auto-completion for REPL."""
    
    def __init__(self):
        self.local_vars: Dict[str, type] = {}
        self.completions: Set[str] = self._build_completions()
    
    def _build_completions(self) -> Set[str]:
        """Build set of all available completions."""
        completions = set()
        
        # Keywords
        completions.update([
            'let', 'def', 'if', 'else', 'while', 'for', 'in', 'return', 'import',
            'try', 'catch', 'goal', 'sample', 'morph', 'parallel', 'consensus',
            'agent', 'True', 'False', 'None'
        ])
        
        # Built-in functions
        completions.update([
            'print', 'len', 'range', 'int', 'float', 'str', 'bool', 'list', 'dict',
            'sum', 'min', 'max', 'abs', 'round', 'type', 'sample', 'normal',
            'bernoulli', 'categorical', 'exit', 'help'
        ])
        
        # Standard library modules
        completions.update(['math', 'agents', 'ml'])
        
        return completions
    
    def update_context(self, local_vars: Dict[str, type]):
        """Update completion context with local variables."""
        self.local_vars = local_vars.copy()
    
    def get_suggestions(self, prefix: str) -> List[str]:
        """Get completion suggestions for given prefix."""
        all_options = self.completions | set(self.local_vars.keys())
        
        # Filter by prefix
        suggestions = [s for s in all_options if s.startswith(prefix)]
        
        # Sort: exact matches first, then by length, then alphabetically
        suggestions.sort(key=lambda x: (x != prefix, len(x), x))
        
        return suggestions[:10]  # Return top 10
    
    def complete_at_cursor(self, line: str, cursor_pos: int) -> Optional[str]:
        """Get best completion at cursor position."""
        # Extract word being completed
        word_start = cursor_pos
        while word_start > 0 and (line[word_start-1].isalnum() or line[word_start-1] == '_'):
            word_start -= 1
        
        prefix = line[word_start:cursor_pos]
        suggestions = self.get_suggestions(prefix)
        
        return suggestions[0] if suggestions else None


class MultiLineBuffer:
    """Handles multi-line input with bracket/parenthesis matching."""
    
    def __init__(self):
        self.buffer: List[str] = []
        self.open_brackets = 0
        self.open_parens = 0
        self.open_braces = 0
    
    def add_line(self, line: str) -> bool:
        """
        Add line to buffer. Return True if expression is complete, False if incomplete.
        """
        self.buffer.append(line)
        self._update_bracket_count(line)
        
        # Check if expression is complete
        return self.is_complete()
    
    def _update_bracket_count(self, line: str):
        """Track open/close brackets."""
        for char in line:
            if char == '[':
                self.open_brackets += 1
            elif char == ']':
                self.open_brackets -= 1
            elif char == '(':
                self.open_parens += 1
            elif char == ')':
                self.open_parens -= 1
            elif char == '{':
                self.open_braces += 1
            elif char == '}':
                self.open_braces -= 1
    
    def is_complete(self) -> bool:
        """Check if buffered expression is syntactically complete."""
        return (self.open_brackets == 0 and 
                self.open_parens == 0 and 
                self.open_braces == 0 and
                self._looks_complete())
    
    def _looks_complete(self) -> bool:
        """Check if the expression looks semantically complete."""
        if not self.buffer:
            return False
        
        full_text = '\n'.join(self.buffer).strip()
        
        # Check for incomplete expressions
        incomplete_endings = [':', '+', '-', '*', '/', '%', '=', 'and', 'or', 'if', 'else', 'then']
        for ending in incomplete_endings:
            if full_text.endswith(ending):
                return False
        
        return True
    
    def get_content(self) -> str:
        """Get the buffered content."""
        return '\n'.join(self.buffer)
    
    def clear(self):
        """Clear the buffer."""
        self.buffer.clear()
        self.open_brackets = 0
        self.open_parens = 0
        self.open_braces = 0
    
    def is_empty(self) -> bool:
        """Check if buffer is empty."""
        return len(self.buffer) == 0


class SynapseREPL:
    """Enhanced REPL with multi-line support, highlighting, and auto-complete."""
    
    def __init__(self):
        self.highlighter = SyntaxHighlighter()
        self.completer = AutoCompleter()
        self.multi_line = MultiLineBuffer()
        self.history: List[str] = []
        self.history_index = -1
    
    def format_output(self, result) -> str:
        """Format output with syntax highlighting."""
        if result is None:
            return ""
        
        # Format different types
        if isinstance(result, str):
            return self.highlighter.colorize(result)
        elif isinstance(result, bool):
            return Colors.CYAN + str(result) + Colors.RESET
        elif isinstance(result, (int, float)):
            return Colors.CYAN + str(result) + Colors.RESET
        elif isinstance(result, list):
            return Colors.BRIGHT_WHITE + str(result) + Colors.RESET
        elif isinstance(result, dict):
            return Colors.BRIGHT_WHITE + str(result) + Colors.RESET
        else:
            return str(result)
    
    def get_prompt(self, is_continuation: bool = False) -> str:
        """Get REPL prompt."""
        if is_continuation:
            return Colors.BRIGHT_BLACK + "    ... " + Colors.RESET
        else:
            return Colors.BRIGHT_CYAN + "synapse> " + Colors.RESET
    
    def read_line(self, is_continuation: bool = False) -> str:
        """Read a line from user with prompt."""
        try:
            prompt = self.get_prompt(is_continuation)
            return input(prompt)
        except EOFError:
            raise
        except KeyboardInterrupt:
            raise
    
    def run(self):
        """Main REPL loop."""
        print(Colors.BRIGHT_GREEN + "Synapse REPL - A Language for Emergent Intelligence" + Colors.RESET)
        print(Colors.BRIGHT_GREEN + "Type 'exit' to quit, 'help' for commands." + Colors.RESET)
        print()
        
        while True:
            try:
                # Read input (multi-line if needed)
                self.multi_line.clear()
                
                while True:
                    line = self.read_line(is_continuation=not self.multi_line.is_empty())
                    
                    # Handle special commands
                    if line.strip() == "exit":
                        print(Colors.BRIGHT_GREEN + "Goodbye!" + Colors.RESET)
                        return
                    
                    if line.strip() == "help":
                        self._show_help()
                        break
                    
                    if line.strip() == "clear":
                        self.multi_line.clear()
                        break
                    
                    if line.strip() == "":
                        if not self.multi_line.is_empty():
                            # Empty line signals end of multi-line input
                            break
                        else:
                            # Skip empty input
                            continue
                    
                    # Add line to multi-line buffer
                    self.multi_line.add_line(line)
                    
                    # Check if expression is complete
                    if self.multi_line.is_complete():
                        break
                
                # Skip if nothing was entered
                if self.multi_line.is_empty():
                    continue
                
                # Execute the command
                source_code = self.multi_line.get_content()
                self.history.append(source_code)
                
                result = parse_and_execute(source_code)
                
                if result is not None:
                    formatted = self.format_output(result)
                    if formatted:
                        print(formatted)
                
            except KeyboardInterrupt:
                print()
                continue
            except EOFError:
                print(Colors.BRIGHT_GREEN + "Goodbye!" + Colors.RESET)
                break
            except Exception as e:
                print(Colors.BRIGHT_RED + f"Error: {e}" + Colors.RESET)
    
    def _show_help(self):
        """Display help information."""
        help_text = """
Synapse REPL Commands:
  exit              - Exit the REPL
  help              - Show this help message
  clear             - Clear the input buffer
  
Multi-line Input:
  Press Enter twice or until all brackets are balanced to execute.
  
Syntax Highlighting:
  Keywords (magenta), builtins (yellow), strings (green), numbers (cyan)
  
Auto-complete:
  Suggestions available for keywords, functions, and variables.
        """
        print(Colors.BRIGHT_CYAN + help_text + Colors.RESET)


def main():
    """Entry point for REPL."""
    repl = SynapseREPL()
    repl.run()


if __name__ == "__main__":
    main()
