"""
CLI command for AI-assisted code generation.

Provides the 'synapse gen' command for generating Synapse code from
natural language descriptions using LLMs.

Usage:
    synapse gen "fibonacci function"
    synapse gen-func fibonacci "compute fibonacci of n" -p n
    synapse gen-module "list operations" -n 3
"""

import argparse
import sys
import os
from typing import Optional

from synapse.ai.codegen import CodeGenerator, CodeGenCLI, CodeValidator


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser for AI code generation commands."""
    parser = argparse.ArgumentParser(
        description="AI-assisted code generation for Synapse",
        prog="synapse gen"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Generation mode")
    
    # Main generation command
    gen = subparsers.add_parser(
        "code",
        aliases=["gen"],
        help="Generate code from description"
    )
    gen.add_argument("description", help="Description of code to generate")
    gen.add_argument(
        "-p", "--provider",
        choices=["openai", "anthropic", "mock"],
        default="mock",
        help="LLM provider (default: mock for testing)"
    )
    gen.add_argument(
        "-k", "--api-key",
        help="API key for provider"
    )
    gen.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    gen.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip validation of generated code"
    )
    gen.add_argument(
        "-c", "--cache-dir",
        help="Cache directory for generated code"
    )
    gen.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable code caching"
    )
    gen.set_defaults(func=cmd_generate)
    
    # Function generation command
    func = subparsers.add_parser(
        "function",
        aliases=["func", "fn"],
        help="Generate a specific function"
    )
    func.add_argument("name", help="Function name")
    func.add_argument("description", help="Function description")
    func.add_argument(
        "-p", "--params",
        nargs="+",
        help="Function parameters"
    )
    func.add_argument(
        "--provider",
        choices=["openai", "anthropic", "mock"],
        default="mock",
        help="LLM provider"
    )
    func.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    func.set_defaults(func=cmd_function)
    
    # Module generation command
    mod = subparsers.add_parser(
        "module",
        aliases=["mod"],
        help="Generate a module with multiple functions"
    )
    mod.add_argument("description", help="Module description")
    mod.add_argument(
        "-n", "--num-functions",
        type=int,
        default=3,
        help="Number of functions to generate (default: 3)"
    )
    mod.add_argument(
        "--provider",
        choices=["openai", "anthropic", "mock"],
        default="mock",
        help="LLM provider"
    )
    mod.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    mod.set_defaults(func=cmd_module)
    
    # Validation command
    val = subparsers.add_parser(
        "validate",
        aliases=["check"],
        help="Validate Synapse code syntax"
    )
    val.add_argument("file", help="Code file or inline code to validate")
    val.add_argument(
        "--inline",
        action="store_true",
        help="Treat input as inline code, not a file"
    )
    val.set_defaults(func=cmd_validate)
    
    return parser


def cmd_generate(args) -> int:
    """Handle 'gen' command."""
    try:
        gen = CodeGenerator(
            provider=args.provider,
            api_key=args.api_key,
            cache_dir=args.cache_dir,
            use_cache=not args.no_cache
        )
        
        code = gen.generate(
            args.description,
            validate=not args.no_validate,
            verbose=args.verbose
        )
        
        print(code)
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_function(args) -> int:
    """Handle 'function' command."""
    try:
        gen = CodeGenerator(provider=args.provider)
        
        code = gen.generate_function(
            args.name,
            args.description,
            params=args.params,
            verbose=args.verbose
        )
        
        print(code)
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_module(args) -> int:
    """Handle 'module' command."""
    try:
        gen = CodeGenerator(provider=args.provider)
        
        code = gen.generate_module(
            args.description,
            num_functions=args.num_functions,
            verbose=args.verbose
        )
        
        print(code)
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_validate(args) -> int:
    """Handle 'validate' command."""
    try:
        if args.inline:
            code = args.file
        else:
            with open(args.file, 'r') as f:
                code = f.read()
        
        is_valid, error = CodeValidator.validate_syntax(code)
        
        if is_valid:
            print("Code is valid (OK)")
            has_func = CodeValidator.has_main_function(code)
            if has_func:
                print("Contains function definitions (OK)")
            return 0
        else:
            print(f"Validation failed: {error}")
            return 1
    
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main(argv: Optional[list] = None) -> int:
    """Main entry point for CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if not hasattr(args, 'func'):
        parser.print_help()
        return 0
    
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
