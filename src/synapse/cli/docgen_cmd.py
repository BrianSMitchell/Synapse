"""
Documentation Generator Command for Synapse CLI

Handles:
- synapse doc generate <source> [--output] [--format]
- synapse doc serve <source> [--port]

Features:
- Generate Markdown API documentation
- Generate JSON documentation
- Generate static HTML site
- Auto-discovery of Synapse files
"""

import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
import json

from synapse.tools.docgen import DocumentationGenerator, generate_api_docs, generate_doc_site


class DocumentationCommand:
    """Handle documentation generation commands."""
    
    def __init__(self, config=None):
        """Initialize documentation command.
        
        Args:
            config: CLI configuration object (optional)
        """
        self.config = config
    
    def handle_generate(self, args) -> int:
        """Handle 'synapse doc generate' command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code (0 for success, 1 for failure)
        """
        source_dir = args.source or "stdlib"
        output_dir = args.output or "docs/api"
        output_format = args.format or "all"
        
        try:
            print(f"📚 Generating documentation from: {source_dir}")
            print(f"📝 Output directory: {output_dir}")
            print(f"📋 Format: {output_format}")
            print()
            
            # Create documentation generator
            gen = DocumentationGenerator()
            
            # Scan directory
            print(f"🔍 Scanning {source_dir}...")
            gen.scan_directory(source_dir)
            
            if not gen.modules:
                print("❌ No modules found in the specified directory")
                return 1
            
            print(f"✓ Found {len(gen.modules)} module(s)")
            print()
            
            # Generate selected formats
            if output_format in ["all", "markdown"]:
                self._generate_markdown(gen, output_dir)
            
            if output_format in ["all", "json"]:
                self._generate_json(gen, output_dir)
            
            if output_format in ["all", "html"]:
                self._generate_html(gen, output_dir)
            
            print()
            print("✅ Documentation generation complete!")
            print(f"📂 Output: {output_dir}")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return 1
    
    def handle_serve(self, args) -> int:
        """Handle 'synapse doc serve' command.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code
        """
        source_dir = args.source or "stdlib"
        port = args.port or 8000
        output_dir = "docs/api"
        
        try:
            print(f"📚 Generating and serving documentation...")
            
            # Generate documentation
            gen = DocumentationGenerator()
            gen.scan_directory(source_dir)
            
            if not gen.modules:
                print("❌ No modules found")
                return 1
            
            gen.generate_html_site(output_dir)
            
            # Try to start simple HTTP server
            self._start_server(output_dir, port)
            
            return 0
            
        except Exception as e:
            print(f"❌ Error: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return 1
    
    def handle_validate(self, args) -> int:
        """Handle 'synapse doc validate' command.
        
        Validates that all functions have proper documentation.
        
        Args:
            args: Parsed command arguments
            
        Returns:
            Exit code
        """
        source_dir = args.source or "stdlib"
        min_coverage = args.coverage or 0.8
        
        try:
            print(f"🔍 Validating documentation in: {source_dir}")
            
            gen = DocumentationGenerator()
            gen.scan_directory(source_dir)
            
            if not gen.modules:
                print("❌ No modules found")
                return 1
            
            # Calculate documentation coverage
            total_functions = 0
            documented_functions = 0
            
            for module in gen.modules:
                for func in module.functions:
                    total_functions += 1
                    if func.description:
                        documented_functions += 1
            
            if total_functions == 0:
                print("❌ No functions found")
                return 1
            
            coverage = documented_functions / total_functions
            coverage_percent = coverage * 100
            
            print()
            print(f"📊 Documentation Coverage: {coverage_percent:.1f}%")
            print(f"   {documented_functions}/{total_functions} functions documented")
            
            if coverage >= min_coverage:
                print(f"✅ Meets minimum coverage requirement ({min_coverage*100:.0f}%)")
                return 0
            else:
                print(f"⚠️  Below minimum coverage requirement ({min_coverage*100:.0f}%)")
                
                # List undocumented functions
                print()
                print("Undocumented functions:")
                for module in gen.modules:
                    for func in module.functions:
                        if not func.description:
                            print(f"  - {module.name}.{func.name}()")
                
                return 1
            
        except Exception as e:
            print(f"❌ Error: {e}")
            if args.verbose:
                import traceback
                traceback.print_exc()
            return 1
    
    def _generate_markdown(self, gen: DocumentationGenerator, output_dir: str) -> None:
        """Generate Markdown documentation."""
        output_file = os.path.join(output_dir, "API.md")
        print(f"📝 Generating Markdown documentation...")
        gen.generate_markdown_docs(output_file)
        print(f"  ✓ {output_file}")
    
    def _generate_json(self, gen: DocumentationGenerator, output_dir: str) -> None:
        """Generate JSON documentation."""
        output_file = os.path.join(output_dir, "api.json")
        print(f"📊 Generating JSON documentation...")
        gen.generate_json_docs(output_file)
        print(f"  ✓ {output_file}")
    
    def _generate_html(self, gen: DocumentationGenerator, output_dir: str) -> None:
        """Generate HTML documentation site."""
        print(f"🌐 Generating HTML documentation site...")
        gen.generate_html_site(output_dir)
        print(f"  ✓ {output_dir}/index.html")
        print(f"  ✓ {output_dir}/style.css")
        for module in gen.modules:
            print(f"  ✓ {output_dir}/{module.name.lower()}.html")
    
    def _start_server(self, directory: str, port: int) -> None:
        """Start a simple HTTP server.
        
        Args:
            directory: Directory to serve
            port: Port to listen on
        """
        import http.server
        import socketserver
        
        os.chdir(directory)
        
        class Handler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                print(f"  {format % args}")
        
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print()
                print(f"🚀 Server running at: http://localhost:{port}")
                print("   Press Ctrl+C to stop")
                print()
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n✓ Server stopped")


def create_parser_docgen(subparsers) -> None:
    """Create parser for documentation commands.
    
    Args:
        subparsers: Parent subparsers object from argparse
    """
    # Main 'doc' command parser
    doc_parser = subparsers.add_parser(
        'doc',
        help='Generate and manage documentation'
    )
    
    doc_subparsers = doc_parser.add_subparsers(
        dest='doc_command',
        help='Documentation subcommands'
    )
    
    # 'synapse doc generate' command
    generate_parser = doc_subparsers.add_parser(
        'generate',
        help='Generate API documentation'
    )
    
    generate_parser.add_argument(
        'source',
        nargs='?',
        default='stdlib',
        help='Source directory containing .syn files (default: stdlib)'
    )
    
    generate_parser.add_argument(
        '--output', '-o',
        type=str,
        default='docs/api',
        help='Output directory (default: docs/api)'
    )
    
    generate_parser.add_argument(
        '--format', '-f',
        type=str,
        choices=['all', 'markdown', 'json', 'html'],
        default='all',
        help='Output format(s) (default: all)'
    )
    
    generate_parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    # 'synapse doc serve' command
    serve_parser = doc_subparsers.add_parser(
        'serve',
        help='Generate and serve documentation locally'
    )
    
    serve_parser.add_argument(
        'source',
        nargs='?',
        default='stdlib',
        help='Source directory (default: stdlib)'
    )
    
    serve_parser.add_argument(
        '--port', '-p',
        type=int,
        default=8000,
        help='Server port (default: 8000)'
    )
    
    serve_parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    # 'synapse doc validate' command
    validate_parser = doc_subparsers.add_parser(
        'validate',
        help='Validate documentation coverage'
    )
    
    validate_parser.add_argument(
        'source',
        nargs='?',
        default='stdlib',
        help='Source directory (default: stdlib)'
    )
    
    validate_parser.add_argument(
        '--coverage', '-c',
        type=float,
        default=0.8,
        help='Minimum documentation coverage (0.0-1.0, default: 0.8)'
    )
    
    validate_parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )


def handle_doc_command(args, config=None) -> int:
    """Handle documentation command dispatch.
    
    Args:
        args: Parsed command arguments
        config: CLI configuration
        
    Returns:
        Exit code
    """
    cmd = DocumentationCommand(config)
    
    if args.doc_command == 'generate':
        return cmd.handle_generate(args)
    elif args.doc_command == 'serve':
        return cmd.handle_serve(args)
    elif args.doc_command == 'validate':
        return cmd.handle_validate(args)
    else:
        print("❌ Unknown documentation command")
        return 1


if __name__ == "__main__":
    # Simple test runner
    import argparse
    
    parser = argparse.ArgumentParser(description="Synapse Documentation Generator")
    create_parser_docgen(parser.add_subparsers())
    
    args = parser.parse_args()
    sys.exit(handle_doc_command(args))
