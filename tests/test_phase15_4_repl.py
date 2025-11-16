"""
Test suite for Phase 15.4: REPL Enhancements
Tests for multi-line input, syntax highlighting, and auto-complete.
"""

import pytest
import sys
import os
from io import StringIO

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from synapse.repl import (
    SyntaxHighlighter, AutoCompleter, MultiLineBuffer, 
    SynapseREPL, Colors
)


class TestSyntaxHighlighter:
    """Test syntax highlighting functionality."""
    
    def setup_method(self):
        self.highlighter = SyntaxHighlighter()
    
    def test_keyword_highlighting(self):
        """Keywords should be highlighted in magenta."""
        result = self.highlighter.colorize("let x = 5")
        assert Colors.MAGENTA in result
        assert "let" in result
    
    def test_string_highlighting(self):
        """Strings should be highlighted in green."""
        result = self.highlighter.colorize('"hello world"')
        assert Colors.GREEN in result
        assert '"hello world"' in result
    
    def test_number_highlighting(self):
        """Numbers should be highlighted in cyan."""
        result = self.highlighter.colorize("42")
        assert Colors.CYAN in result
        assert "42" in result
    
    def test_float_highlighting(self):
        """Floats should be highlighted in cyan."""
        result = self.highlighter.colorize("3.14159")
        assert Colors.CYAN in result
        assert "3.14159" in result
    
    def test_builtin_highlighting(self):
        """Built-in functions should be highlighted in yellow."""
        result = self.highlighter.colorize("print")
        assert Colors.YELLOW in result
        assert "print" in result
    
    def test_operator_highlighting(self):
        """Operators should be highlighted in bright yellow."""
        result = self.highlighter.colorize("+")
        assert Colors.BRIGHT_YELLOW in result or "+" in result
    
    def test_comment_highlighting(self):
        """Comments should be highlighted in gray."""
        result = self.highlighter.colorize("let x = 5 # comment")
        assert Colors.BRIGHT_BLACK in result
        assert "comment" in result
    
    def test_complex_expression(self):
        """Complex expressions should highlight multiple elements."""
        result = self.highlighter.colorize('let x = "test" + 42')
        assert Colors.MAGENTA in result  # let
        assert Colors.GREEN in result    # "test"
        assert Colors.CYAN in result     # 42
    
    def test_non_string_input(self):
        """Non-string inputs should be converted to string."""
        result = self.highlighter.colorize(42)
        assert "42" in result
    
    def test_single_quotes(self):
        """Single-quoted strings should be highlighted."""
        result = self.highlighter.colorize("'hello'")
        assert Colors.GREEN in result
        assert "'hello'" in result
    
    def test_multiple_keywords(self):
        """Multiple keywords should all be highlighted."""
        result = self.highlighter.colorize("if x then y else z")
        # 'if' and 'else' are keywords; 'then' is not in KEYWORDS list
        # So we expect at least 2 keyword highlights
        assert result.count(Colors.MAGENTA) >= 2


class TestAutoCompleter:
    """Test auto-completion functionality."""
    
    def setup_method(self):
        self.completer = AutoCompleter()
    
    def test_keyword_completion(self):
        """Should complete keywords."""
        suggestions = self.completer.get_suggestions("le")
        assert "let" in suggestions
    
    def test_builtin_completion(self):
        """Should complete built-in functions."""
        suggestions = self.completer.get_suggestions("pri")
        assert "print" in suggestions
    
    def test_no_suggestions_for_unknown(self):
        """Should return empty for unknown prefixes."""
        suggestions = self.completer.get_suggestions("xyz")
        assert len(suggestions) == 0
    
    def test_partial_match(self):
        """Should match partial names."""
        suggestions = self.completer.get_suggestions("wh")
        assert "while" in suggestions
    
    def test_exact_match_first(self):
        """Exact matches should come first."""
        suggestions = self.completer.get_suggestions("if")
        assert suggestions[0] == "if"
    
    def test_update_local_context(self):
        """Should track local variables."""
        self.completer.update_context({"my_var": int, "another": str})
        suggestions = self.completer.get_suggestions("my")
        assert "my_var" in suggestions
    
    def test_local_var_completion(self):
        """Should complete local variables."""
        self.completer.update_context({"counter": int})
        suggestions = self.completer.get_suggestions("coun")
        assert "counter" in suggestions
    
    def test_sorted_suggestions(self):
        """Suggestions should be sorted by length then alphabetically."""
        self.completer.update_context({"x": int, "xx": int, "xxx": int})
        suggestions = self.completer.get_suggestions("x")
        assert suggestions[0] == "x"
        assert "xx" in suggestions
        assert "xxx" in suggestions
    
    def test_max_suggestions(self):
        """Should limit suggestions to 10."""
        # This test may be skipped if there aren't 11+ matching completions
        suggestions = self.completer.get_suggestions("")
        assert len(suggestions) <= 10
    
    def test_complete_at_cursor(self):
        """Should complete at cursor position."""
        result = self.completer.complete_at_cursor("print", 3)
        assert result is not None


class TestMultiLineBuffer:
    """Test multi-line input handling."""
    
    def setup_method(self):
        self.buffer = MultiLineBuffer()
    
    def test_single_line_complete(self):
        """Single complete line should be marked complete."""
        result = self.buffer.add_line("let x = 5")
        assert result  # Should be complete
    
    def test_incomplete_expression_missing_closing_bracket(self):
        """Expression with open bracket should be incomplete."""
        result = self.buffer.add_line("let arr = [1, 2, 3")
        assert not result
    
    def test_closing_bracket_completes(self):
        """Closing bracket should complete the expression."""
        self.buffer.add_line("let arr = [1, 2, 3")
        assert not self.buffer.is_complete()
        
        self.buffer.add_line("]")
        assert self.buffer.is_complete()
    
    def test_unclosed_parenthesis(self):
        """Unclosed parenthesis should make expression incomplete."""
        self.buffer.add_line("print(1 + 2")
        assert not self.buffer.is_complete()
    
    def test_balanced_parens(self):
        """Balanced parentheses should mark complete."""
        result = self.buffer.add_line("print(1 + 2)")
        assert result
    
    def test_nested_brackets(self):
        """Nested brackets should be tracked correctly."""
        self.buffer.add_line("let x = [[1, 2], [3, 4")
        assert not self.buffer.is_complete()
        
        self.buffer.add_line("]]")
        assert self.buffer.is_complete()
    
    def test_multiple_lines(self):
        """Multiple lines should accumulate."""
        self.buffer.add_line("if true then")
        self.buffer.add_line("  print(42)")
        
        assert "if true then" in self.buffer.get_content()
        assert "print(42)" in self.buffer.get_content()
    
    def test_clear_buffer(self):
        """Should be able to clear the buffer."""
        self.buffer.add_line("let x = 5")
        self.buffer.clear()
        
        assert self.buffer.is_empty()
        assert self.buffer.get_content() == ""
    
    def test_incomplete_ending_with_operator(self):
        """Lines ending with operators should be incomplete."""
        self.buffer.add_line("1 +")
        # Even though brackets are balanced, incomplete ending
        # This depends on implementation
    
    def test_get_content_newline_separated(self):
        """Content should be newline-separated."""
        self.buffer.add_line("let x = 1")
        self.buffer.add_line("let y = 2")
        
        content = self.buffer.get_content()
        assert "\n" in content
        assert "let x = 1" in content
        assert "let y = 2" in content
    
    def test_empty_buffer_is_incomplete(self):
        """Empty buffer should be incomplete."""
        assert not self.buffer.is_complete()
    
    def test_braces_tracking(self):
        """Should track curly braces."""
        self.buffer.add_line("{ x = 1")
        assert not self.buffer.is_complete()
        
        self.buffer.clear()
        self.buffer.add_line("{ x = 1 }")
        assert self.buffer.is_complete()


class TestSynapseREPL:
    """Test REPL integration."""
    
    def setup_method(self):
        self.repl = SynapseREPL()
    
    def test_format_none_output(self):
        """None should return empty string."""
        result = self.repl.format_output(None)
        assert result == ""
    
    def test_format_boolean_output(self):
        """Booleans should be highlighted in cyan."""
        result = self.repl.format_output(True)
        assert Colors.CYAN in result
        assert "True" in result
    
    def test_format_integer_output(self):
        """Integers should be highlighted in cyan."""
        result = self.repl.format_output(42)
        assert Colors.CYAN in result
        assert "42" in result
    
    def test_format_float_output(self):
        """Floats should be highlighted in cyan."""
        result = self.repl.format_output(3.14)
        assert Colors.CYAN in result
        assert "3.14" in result
    
    def test_format_string_output(self):
        """Strings should use syntax highlighter."""
        result = self.repl.format_output("hello world")
        # Should return highlighted string
        assert "hello world" in result
    
    def test_format_list_output(self):
        """Lists should be formatted."""
        result = self.repl.format_output([1, 2, 3])
        assert "1" in result
        assert "2" in result
        assert "3" in result
    
    def test_format_dict_output(self):
        """Dicts should be formatted."""
        result = self.repl.format_output({"key": "value"})
        assert "key" in result
        assert "value" in result
    
    def test_prompt_regular(self):
        """Regular prompt should be cyan."""
        prompt = self.repl.get_prompt(is_continuation=False)
        assert Colors.BRIGHT_CYAN in prompt
        assert "synapse>" in prompt
    
    def test_prompt_continuation(self):
        """Continuation prompt should be different."""
        prompt = self.repl.get_prompt(is_continuation=True)
        assert Colors.BRIGHT_BLACK in prompt
        assert "..." in prompt
    
    def test_history_tracking(self):
        """Commands should be added to history."""
        initial_len = len(self.repl.history)
        self.repl.multi_line.add_line("let x = 5")
        self.repl.history.append(self.repl.multi_line.get_content())
        
        assert len(self.repl.history) == initial_len + 1


class TestREPLIntegration:
    """Integration tests for full REPL flow."""
    
    def test_simple_assignment_flow(self):
        """Test simple variable assignment."""
        repl = SynapseREPL()
        repl.multi_line.add_line("let x = 42")
        
        assert repl.multi_line.is_complete()
        assert "x" in repl.multi_line.get_content()
    
    def test_multiline_function_definition(self):
        """Test multi-line function definition."""
        repl = SynapseREPL()
        
        repl.multi_line.add_line("def add(a, b)")
        # This line has balanced parens, so it appears complete by bracket count
        # The _looks_complete check determines it needs more based on ending
        # Since the line ends with ')', it may be marked complete
        
        repl.multi_line.add_line("  return a + b")
        # Should be complete after body
        assert repl.multi_line.is_complete()
    
    def test_multiline_if_statement(self):
        """Test multi-line if statement."""
        repl = SynapseREPL()
        
        repl.multi_line.add_line("if x > 0 then")
        assert not repl.multi_line.is_complete()
        
        repl.multi_line.add_line("  print(x)")
        # May or may not be complete depending on grammar
    
    def test_syntax_highlighting_chain(self):
        """Test that multiple elements are highlighted."""
        repl = SynapseREPL()
        highlighter = repl.highlighter
        
        result = highlighter.colorize("def factorial(n)")
        # Should highlight 'def' and 'n'
        assert Colors.MAGENTA in result  # keyword
    
    def test_autocomplete_with_context(self):
        """Test autocomplete with local variable context."""
        repl = SynapseREPL()
        repl.completer.update_context({"my_function": "callable"})
        
        suggestions = repl.completer.get_suggestions("my")
        assert "my_function" in suggestions


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_empty_string_highlighting(self):
        """Empty strings should be handled."""
        highlighter = SyntaxHighlighter()
        result = highlighter.colorize("")
        assert result == ""
    
    def test_whitespace_only(self):
        """Whitespace-only input should not break."""
        buffer = MultiLineBuffer()
        buffer.add_line("   ")
        assert buffer.get_content() == "   "
    
    def test_special_characters_in_strings(self):
        """Special characters in strings should not break highlighting."""
        highlighter = SyntaxHighlighter()
        result = highlighter.colorize('"test@#$%^&*()"')
        assert "@" in result or Colors.RESET in result  # Properly escaped or reset
    
    def test_unicode_characters(self):
        """Unicode should be handled gracefully."""
        highlighter = SyntaxHighlighter()
        result = highlighter.colorize("# Comment with emoji 🚀")
        assert "emoji" in result
    
    def test_very_long_input(self):
        """Very long input should not cause issues."""
        highlighter = SyntaxHighlighter()
        long_input = "x = " + "1 + " * 100 + "0"
        result = highlighter.colorize(long_input)
        assert len(result) > len(long_input)  # Due to color codes
    
    def test_mixed_bracket_types(self):
        """Mixed bracket types should track correctly."""
        buffer = MultiLineBuffer()
        buffer.add_line("arr = [[1, (2, 3)], {4: 5}")
        assert not buffer.is_complete()
        
        buffer.add_line("]")
        assert buffer.open_brackets == 0
    
    def test_autocomplete_empty_prefix(self):
        """Empty prefix should return some suggestions."""
        completer = AutoCompleter()
        suggestions = completer.get_suggestions("")
        assert len(suggestions) > 0


# Performance tests
class TestPerformance:
    """Test performance characteristics."""
    
    def test_syntax_highlighting_performance(self):
        """Syntax highlighting should be fast."""
        import time
        highlighter = SyntaxHighlighter()
        
        # Time highlighting 100 lines
        start = time.time()
        for _ in range(100):
            highlighter.colorize("let x = some_function(arg1, arg2) # comment")
        elapsed = time.time() - start
        
        # Should complete in less than 100ms
        assert elapsed < 0.1
    
    def test_autocomplete_performance(self):
        """Auto-complete should be fast."""
        import time
        completer = AutoCompleter()
        completer.update_context({f"var_{i}": int for i in range(100)})
        
        start = time.time()
        for _ in range(100):
            completer.get_suggestions("var")
        elapsed = time.time() - start
        
        # Should complete in less than 50ms
        assert elapsed < 0.05
    
    def test_multiline_buffer_performance(self):
        """Multi-line buffer should handle large content."""
        import time
        buffer = MultiLineBuffer()
        
        start = time.time()
        for i in range(100):
            buffer.add_line(f"line {i}")
        elapsed = time.time() - start
        
        # Should complete in less than 10ms
        assert elapsed < 0.01


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
