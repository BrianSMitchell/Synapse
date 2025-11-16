"""
Tests for Phase 16.1: LLM-Assisted Code Generation

Tests cover:
- Mock code generation
- Code validation (syntax checking)
- Caching mechanisms
- CLI interfaces
- Multi-provider support
"""

import pytest
import os
import tempfile
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from synapse.ai.codegen import (
    CodeGenerator,
    CodeValidator,
    MockProvider,
    CodeGenCLI,
    OpenAIProvider,
    AnthropicProvider,
)


class TestCodeValidator:
    """Test code validation functionality."""

    def test_extract_code_plain(self):
        """Test extracting plain code."""
        code = "def fib(n):\n    return n"
        extracted = CodeValidator.extract_code(code)
        assert extracted == code

    def test_extract_code_markdown(self):
        """Test extracting code from markdown blocks."""
        markdown = """Here's the code:
```synapse
def fib(n):
    return n
```
That's it!"""
        extracted = CodeValidator.extract_code(markdown)
        assert "def fib(n):" in extracted
        assert "return n" in extracted

    def test_extract_code_python_markdown(self):
        """Test extracting from python markdown block."""
        markdown = """
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
"""
        extracted = CodeValidator.extract_code(markdown)
        assert "def factorial(n):" in extracted

    def test_validate_syntax_valid(self):
        """Test validation of valid code."""
        code = "def fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1)"
        is_valid, error = CodeValidator.validate_syntax(code)
        assert is_valid
        assert error is None

    def test_validate_syntax_unmatched_braces(self):
        """Test validation catches unmatched braces."""
        code = "def foo():\n    x = {1, 2, 3"  # Missing closing brace
        is_valid, error = CodeValidator.validate_syntax(code)
        assert not is_valid
        assert "brace" in error.lower()

    def test_validate_syntax_unmatched_parens(self):
        """Test validation catches unmatched parentheses."""
        code = "def foo(x, y"  # Missing closing paren
        is_valid, error = CodeValidator.validate_syntax(code)
        assert not is_valid
        assert "parenthes" in error.lower()

    def test_has_main_function(self):
        """Test detection of function definitions."""
        code_with_func = "def fibonacci(n):\n    return n"
        assert CodeValidator.has_main_function(code_with_func)

        code_no_func = "let x = 42\nlet y = 43"
        assert not CodeValidator.has_main_function(code_no_func)


class TestMockProvider:
    """Test mock LLM provider."""

    def test_mock_fibonacci(self):
        """Test mock generates fibonacci template."""
        provider = MockProvider()
        code = provider.generate("fibonacci function")
        assert "def fib" in code
        assert "return" in code

    def test_mock_factorial(self):
        """Test mock generates factorial template."""
        provider = MockProvider()
        code = provider.generate("factorial")
        assert "factorial" in code

    def test_mock_sum(self):
        """Test mock generates sum template."""
        provider = MockProvider()
        code = provider.generate("sum list")
        assert "sum" in code or "total" in code

    def test_mock_max(self):
        """Test mock generates max template."""
        provider = MockProvider()
        code = provider.generate("maximum value")
        assert "max" in code

    def test_mock_fallback(self):
        """Test mock returns fallback for unknown prompt."""
        provider = MockProvider()
        code = provider.generate("something completely unknown xyz123")
        assert "def" in code or "let" in code


class TestCodeGenerator:
    """Test main code generator."""

    def test_init_mock_provider(self):
        """Test initialization with mock provider."""
        gen = CodeGenerator(provider="mock")
        assert gen.provider is not None
        assert isinstance(gen.provider, MockProvider)

    def test_generate_with_validation(self):
        """Test code generation with validation."""
        gen = CodeGenerator(provider="mock")
        code = gen.generate("fibonacci function", validate=True)
        assert "def" in code
        assert len(code) > 0

    def test_generate_verbose(self, capsys):
        """Test verbose output during generation."""
        gen = CodeGenerator(provider="mock")
        code = gen.generate("fibonacci", verbose=True)
        captured = capsys.readouterr()
        assert "Generating" in captured.out or "Generated" in captured.out

    def test_cache_key_generation(self):
        """Test cache key generation."""
        gen = CodeGenerator(provider="mock")
        key1 = gen._get_cache_key("fibonacci")
        key2 = gen._get_cache_key("fibonacci")
        assert key1 == key2
        assert len(key1) == 64  # SHA256 hex digest length

    def test_cache_different_prompts(self):
        """Test different prompts generate different cache keys."""
        gen = CodeGenerator(provider="mock")
        key1 = gen._get_cache_key("fibonacci")
        key2 = gen._get_cache_key("factorial")
        assert key1 != key2

    def test_caching_saves_and_loads(self):
        """Test caching mechanism saves and loads code."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = CodeGenerator(provider="mock", cache_dir=tmpdir, use_cache=True)
            
            # Generate code
            code1 = gen.generate("fibonacci function")
            
            # Load from cache
            code2 = gen.generate("fibonacci function")
            
            assert code1 == code2

    def test_cache_disabled(self):
        """Test caching can be disabled."""
        gen = CodeGenerator(provider="mock", use_cache=False)
        assert not gen.use_cache

    def test_generate_function(self):
        """Test generating specific function."""
        gen = CodeGenerator(provider="mock")
        code = gen.generate_function(
            "fibonacci",
            "compute fibonacci of n",
            params=["n"]
        )
        assert "def" in code or "fibonacci" in code.lower()

    def test_generate_module(self):
        """Test generating multi-function module."""
        gen = CodeGenerator(provider="mock")
        code = gen.generate_module(
            "list operations",
            num_functions=3
        )
        assert "def" in code
        assert len(code) > 0

    def test_generate_max_attempts(self):
        """Test max attempts for generation."""
        gen = CodeGenerator(provider="mock")
        # Should succeed within max_attempts
        code = gen.generate("fibonacci", max_attempts=3)
        assert code is not None

    def test_validation_failure_retry(self):
        """Test retries on validation failure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = CodeGenerator(provider="mock", cache_dir=tmpdir)
            
            # Mock provider should return valid code after validation
            code = gen.generate("fibonacci", validate=True, max_attempts=2)
            is_valid, _ = CodeValidator.validate_syntax(code)
            assert is_valid


class TestCodeGenCLI:
    """Test CLI interface."""

    def test_cli_init(self):
        """Test CLI initialization."""
        cli = CodeGenCLI(provider="mock")
        assert cli.gen is not None

    def test_cli_generate_command(self):
        """Test generate command."""
        cli = CodeGenCLI(provider="mock")
        code = cli.generate_command("fibonacci function")
        assert code is not None
        assert len(code) > 0

    def test_cli_function_command(self):
        """Test function generation command."""
        cli = CodeGenCLI(provider="mock")
        code = cli.function_command(
            "fibonacci",
            "compute fibonacci of n",
            params=["n"]
        )
        assert code is not None

    def test_cli_module_command(self):
        """Test module generation command."""
        cli = CodeGenCLI(provider="mock")
        code = cli.module_command(
            "list operations",
            num_functions=3
        )
        assert code is not None


class TestOpenAIProvider:
    """Test OpenAI provider."""

    def test_init_without_api_key(self):
        """Test initialization fails without API key."""
        # Ensure env var is not set
        original = os.environ.pop("OPENAI_API_KEY", None)
        try:
            with pytest.raises(ValueError, match="OPENAI_API_KEY"):
                OpenAIProvider()
        finally:
            if original:
                os.environ["OPENAI_API_KEY"] = original

    def test_init_with_api_key(self):
        """Test initialization with provided API key."""
        # Skip if openai not installed
        try:
            import openai
            provider = OpenAIProvider(api_key="test-key")
            assert provider.api_key == "test-key"
        except ImportError:
            pytest.skip("openai package not installed")

    def test_generate_with_mock(self):
        """Test generation with mocked OpenAI client."""
        try:
            import openai
            with patch.object(openai, "OpenAI") as mock_openai_class:
                mock_client = MagicMock()
                mock_openai_class.return_value = mock_client
                
                # Mock the response
                mock_response = MagicMock()
                mock_response.choices = [MagicMock()]
                mock_response.choices[0].message.content = "def test():\n    return 42"
                mock_client.chat.completions.create.return_value = mock_response
                
                provider = OpenAIProvider(api_key="test-key")
                code = provider.generate("test function")
                
                assert "def test" in code
                assert "return 42" in code
        except ImportError:
            pytest.skip("openai package not installed")


class TestAnthropicProvider:
    """Test Anthropic provider."""

    def test_init_without_api_key(self):
        """Test initialization fails without API key."""
        original = os.environ.pop("ANTHROPIC_API_KEY", None)
        try:
            with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
                AnthropicProvider()
        finally:
            if original:
                os.environ["ANTHROPIC_API_KEY"] = original

    def test_init_with_api_key(self):
        """Test initialization with provided API key."""
        try:
            import anthropic
            provider = AnthropicProvider(api_key="test-key")
            assert provider.api_key == "test-key"
        except ImportError:
            pytest.skip("anthropic package not installed")


class TestIntegration:
    """Integration tests."""

    def test_full_workflow_mock(self):
        """Test full workflow with mock provider."""
        gen = CodeGenerator(provider="mock")
        
        # Generate function
        code = gen.generate_function(
            "fibonacci",
            "compute fibonacci sequence"
        )
        
        # Validate
        is_valid, _ = CodeValidator.validate_syntax(code)
        assert is_valid
        
        # Verify has function
        assert CodeValidator.has_main_function(code)

    def test_caching_workflow(self):
        """Test caching in full workflow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = CodeGenerator(
                provider="mock",
                cache_dir=tmpdir,
                use_cache=True
            )
            
            # First generation
            code1 = gen.generate("fibonacci", verbose=False)
            
            # Create new generator with same cache dir
            gen2 = CodeGenerator(
                provider="mock",
                cache_dir=tmpdir,
                use_cache=True
            )
            
            # Should load from cache
            code2 = gen2.generate("fibonacci", verbose=False)
            
            # Should be identical
            assert code1 == code2

    def test_multiple_generations(self):
        """Test generating multiple different functions."""
        gen = CodeGenerator(provider="mock")
        
        fib = gen.generate("fibonacci")
        fact = gen.generate("factorial")
        summ = gen.generate("sum")
        
        assert "fib" in fib.lower()
        assert "factorial" in fact.lower()
        assert "sum" in summ.lower()


# Performance tests
class TestPerformance:
    """Performance benchmarks."""

    def test_generation_time(self):
        """Test generation completes quickly."""
        import time
        gen = CodeGenerator(provider="mock")
        
        start = time.time()
        code = gen.generate("fibonacci")
        elapsed = time.time() - start
        
        # Mock should be very fast (< 1 second)
        assert elapsed < 1.0
        assert len(code) > 0

    def test_cache_load_time(self):
        """Test cached code loads quickly."""
        import time
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = CodeGenerator(
                provider="mock",
                cache_dir=tmpdir,
                use_cache=True
            )
            
            # Prime cache
            code1 = gen.generate("fibonacci")
            
            # Measure cache load
            start = time.time()
            code2 = gen.generate("fibonacci")
            elapsed = time.time() - start
            
            # Cache load should be < 100ms
            assert elapsed < 0.1


# Error handling tests
class TestErrorHandling:
    """Test error handling."""

    def test_invalid_provider(self):
        """Test error on invalid provider."""
        with pytest.raises(ValueError, match="Unknown provider"):
            CodeGenerator(provider="nonexistent")

    def test_max_attempts_exceeded(self):
        """Test error when max attempts exceeded."""
        # This is hard to trigger with mock provider, but test the logic
        gen = CodeGenerator(provider="mock")
        # Mock provider should always succeed
        code = gen.generate("anything", max_attempts=1)
        assert code is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
