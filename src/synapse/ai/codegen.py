"""
LLM-Assisted Code Generation for Synapse

This module provides AI-driven code generation capabilities, allowing Synapse
to generate correct code from natural language descriptions using OpenAI,
Anthropic, or other LLM providers.

Features:
- Generate Synapse functions from natural language descriptions
- Multi-provider support (OpenAI, Anthropic, etc.)
- Code validation and testing
- Caching of generated code
- Fallback strategies and error handling

Example:
    >>> gen = CodeGenerator(provider='openai')
    >>> code = gen.generate("fibonacci function up to n")
    >>> print(code)
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
"""

import json
import hashlib
import re
import os
from typing import Optional, Dict, List, Any
from abc import ABC, abstractmethod
from pathlib import Path
import tempfile


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """
        Generate code from a prompt.
        
        Args:
            prompt: Natural language description of desired code
            max_tokens: Maximum tokens in response
            
        Returns:
            Generated code string
        """
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI API provider for code generation."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize OpenAI provider.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model to use (default: gpt-4)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        try:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError("openai package required: pip install openai")

    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate code using OpenAI API."""
        system_prompt = """You are an expert Synapse programming language assistant.
Generate clean, well-structured Synapse code that:
1. Follows Synapse syntax and idioms
2. Includes helpful comments
3. Handles edge cases properly
4. Uses meaningful variable names

Always return ONLY the code, no explanations or markdown formatting."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.3,  # Lower temperature for more deterministic output
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}")


class AnthropicProvider(LLMProvider):
    """Anthropic Claude API provider for code generation."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-opus-20240229"):
        """
        Initialize Anthropic provider.
        
        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Model to use (default: claude-3-opus)
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model
        
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("anthropic package required: pip install anthropic")

    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate code using Anthropic API."""
        system_prompt = """You are an expert Synapse programming language assistant.
Generate clean, well-structured Synapse code that:
1. Follows Synapse syntax and idioms
2. Includes helpful comments
3. Handles edge cases properly
4. Uses meaningful variable names

Always return ONLY the code, no explanations or markdown formatting."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            raise RuntimeError(f"Anthropic API error: {e}")


class MockProvider(LLMProvider):
    """Mock provider for testing without API calls."""

    def __init__(self):
        """Initialize mock provider."""
        self.templates = {
            "fibonacci": """def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)""",
            
            "factorial": """def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)""",
            
            "sum": """def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    return total""",
            
            "max": """def max_list(lst):
    if len(lst) == 0:
        return nil
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val""",
        }

    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate code using mock templates."""
        prompt_lower = prompt.lower()
        
        for key, template in self.templates.items():
            if key in prompt_lower:
                return template
        
        # Default fallback
        return """def example():
    let x = 42
    return x"""


class CodeValidator:
    """Validates generated Synapse code."""

    @staticmethod
    def extract_code(text: str) -> str:
        """
        Extract code from response (handles markdown wrapping).
        
        Args:
            text: Text potentially containing code blocks
            
        Returns:
            Extracted code
        """
        # Remove markdown code blocks
        if "```" in text:
            parts = text.split("```")
            if len(parts) >= 3:
                # Find synapse or python code block
                for i in range(1, len(parts), 2):
                    content = parts[i].strip()
                    if content.startswith(("synapse", "python")):
                        return "\n".join(parts[i].split("\n")[1:]).strip()
                    else:
                        return content.strip()
        return text.strip()

    @staticmethod
    def validate_syntax(code: str) -> tuple[bool, Optional[str]]:
        """
        Validate Synapse code syntax.
        
        Args:
            code: Code to validate
            
        Returns:
            (is_valid, error_message)
        """
        # Basic syntax checks
        issues = []
        
        # Check for matching braces/parens
        open_braces = code.count("{")
        close_braces = code.count("}")
        if open_braces != close_braces:
            issues.append(f"Unmatched braces: {open_braces} open, {close_braces} close")
        
        open_parens = code.count("(")
        close_parens = code.count(")")
        if open_parens != close_parens:
            issues.append(f"Unmatched parentheses: {open_parens} open, {close_parens} close")
        
        # Check for undefined keywords
        valid_keywords = {
            "def", "let", "if", "else", "for", "while", "return",
            "try", "catch", "import", "goal", "agent", "sample",
            "morph", "consensus", "tensor", "dist"
        }
        
        words = re.findall(r'\b[a-zA-Z_]\w*\b', code)
        suspicious = [w for w in set(words) if w.isupper() and w not in {"True", "False", "None"}]
        
        if issues:
            return False, "; ".join(issues)
        
        return True, None

    @staticmethod
    def has_main_function(code: str) -> bool:
        """Check if code defines a main function."""
        return bool(re.search(r'def\s+\w+\s*\(', code))


class CodeGenerator:
    """Main class for LLM-assisted Synapse code generation."""

    def __init__(
        self,
        provider: str = "openai",
        api_key: Optional[str] = None,
        cache_dir: Optional[str] = None,
        use_cache: bool = True
    ):
        """
        Initialize code generator.
        
        Args:
            provider: LLM provider ('openai', 'anthropic', 'mock')
            api_key: API key for provider
            cache_dir: Directory for caching generated code
            use_cache: Whether to use caching
        """
        self.use_cache = use_cache
        self.cache_dir = Path(cache_dir or tempfile.gettempdir()) / "synapse_codegen_cache"
        
        if self.use_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        if provider == "openai":
            self.provider = OpenAIProvider(api_key=api_key)
        elif provider == "anthropic":
            self.provider = AnthropicProvider(api_key=api_key)
        elif provider == "mock":
            self.provider = MockProvider()
        else:
            raise ValueError(f"Unknown provider: {provider}")
        
        self.validator = CodeValidator()

    def _get_cache_key(self, prompt: str) -> str:
        """Generate cache key from prompt."""
        return hashlib.sha256(prompt.encode()).hexdigest()

    def _load_from_cache(self, cache_key: str) -> Optional[str]:
        """Load cached code if available."""
        if not self.use_cache:
            return None
        
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            try:
                with open(cache_file) as f:
                    data = json.load(f)
                    return data.get("code")
            except Exception:
                pass
        return None

    def _save_to_cache(self, cache_key: str, code: str) -> None:
        """Save code to cache."""
        if not self.use_cache:
            return
        
        cache_file = self.cache_dir / f"{cache_key}.json"
        try:
            with open(cache_file, 'w') as f:
                json.dump({"code": code}, f)
        except Exception:
            pass

    def generate(
        self,
        description: str,
        validate: bool = True,
        max_attempts: int = 3,
        verbose: bool = False
    ) -> str:
        """
        Generate Synapse code from natural language description.
        
        Args:
            description: Natural language description of desired code
            validate: Whether to validate generated code
            max_attempts: Number of retry attempts on validation failure
            verbose: Print generation progress
            
        Returns:
            Generated Synapse code
            
        Raises:
            ValueError: If code generation fails after max attempts
        """
        if verbose:
            print(f"Generating code for: {description}")
        
        # Check cache
        cache_key = self._get_cache_key(description)
        cached = self._load_from_cache(cache_key)
        if cached:
            if verbose:
                print("Using cached result")
            return cached
        
        # Generate with retries
        for attempt in range(max_attempts):
            try:
                prompt = f"""Generate a Synapse function that: {description}
                
Requirements:
- Return ONLY valid Synapse code
- Include a main function or primary function definition
- Add comments explaining logic
- Handle edge cases"""
                
                code = self.provider.generate(prompt)
                code = self.validator.extract_code(code)
                
                if validate:
                    is_valid, error = self.validator.validate_syntax(code)
                    if not is_valid:
                        if verbose:
                            print(f"Attempt {attempt + 1}: Validation failed - {error}")
                        if attempt < max_attempts - 1:
                            continue
                        raise ValueError(f"Generated invalid code: {error}")
                
                # Save to cache
                self._save_to_cache(cache_key, code)
                
                if verbose:
                    print(f"Generated {len(code.split())} tokens of code")
                
                return code
            
            except Exception as e:
                if verbose:
                    print(f"Attempt {attempt + 1}: {e}")
                if attempt == max_attempts - 1:
                    raise ValueError(f"Failed to generate code after {max_attempts} attempts: {e}")
        
        raise ValueError("Unexpected error in code generation")

    def generate_function(
        self,
        name: str,
        description: str,
        params: Optional[List[str]] = None,
        **kwargs
    ) -> str:
        """
        Generate a specific Synapse function.
        
        Args:
            name: Function name
            description: What the function should do
            params: List of parameter names
            **kwargs: Additional arguments to generate()
            
        Returns:
            Generated function code
        """
        param_str = f" with parameters {', '.join(params)}" if params else ""
        full_desc = f"Create a function named '{name}' that {description}{param_str}"
        return self.generate(full_desc, **kwargs)

    def generate_module(
        self,
        description: str,
        num_functions: int = 3,
        **kwargs
    ) -> str:
        """
        Generate a Synapse module with multiple functions.
        
        Args:
            description: Overall module description
            num_functions: Number of functions to generate
            **kwargs: Additional arguments to generate()
            
        Returns:
            Generated module code
        """
        full_desc = f"""Create a Synapse module for: {description}
Include {num_functions} related functions that work together."""
        return self.generate(full_desc, **kwargs)


class CodeGenCLI:
    """CLI interface for code generation."""

    def __init__(self, provider: str = "mock"):
        self.gen = CodeGenerator(provider=provider)

    def generate_command(self, description: str, verbose: bool = False) -> str:
        """CLI command: synapse gen <description>"""
        return self.gen.generate(description, verbose=verbose)

    def function_command(
        self,
        name: str,
        description: str,
        params: Optional[List[str]] = None
    ) -> str:
        """CLI command: synapse gen-func <name> <description> [params]"""
        return self.gen.generate_function(name, description, params)

    def module_command(self, description: str, num_functions: int = 3) -> str:
        """CLI command: synapse gen-module <description> [-n NUM_FUNCTIONS]"""
        return self.gen.generate_module(description, num_functions)


if __name__ == "__main__":
    # Example usage
    print("Synapse Code Generation Examples")
    print("=" * 50)
    
    # Create generator with mock provider (no API needed)
    gen = CodeGenerator(provider="mock")
    
    # Example 1: Generate fibonacci
    print("\n1. Fibonacci Function:")
    print("-" * 50)
    fib_code = gen.generate("fibonacci function up to n", verbose=True)
    print(fib_code)
    
    # Example 2: Generate factorial
    print("\n2. Factorial Function:")
    print("-" * 50)
    fact_code = gen.generate_function("factorial", "compute factorial of n")
    print(fact_code)
    
    # Example 3: List operations module
    print("\n3. List Operations Module:")
    print("-" * 50)
    module_code = gen.generate_module("list operations with sum, max, min", num_functions=3)
    print(module_code)
