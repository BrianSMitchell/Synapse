"""
CLI commands for AI-assisted debugging

Commands:
- synapse debug <file> - Analyze code for bugs
- synapse debug-morph <file> - Check for morphing-induced bugs
- synapse fix <file> - Suggest and apply fixes
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from synapse.ai.debugger import (
    DebugAnalyzer, 
    BugSeverity,
    debug,
    debug_report,
    suggest_fixes
)


def debug_command(args):
    """synapse debug <file> - Analyze code for bugs"""
    
    if not args.file:
        print("Error: No file specified")
        sys.exit(1)
    
    file_path = Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
    
    # Read code
    try:
        code = file_path.read_text()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Analyze
    analyzer = DebugAnalyzer(provider=args.provider)
    
    if args.verbose:
        print(f"Analyzing {args.file} with {args.provider} provider...")
    
    report = analyzer.report(code)
    print(report)
    
    # Exit with error code if critical bugs found
    bugs = analyzer.analyze(code)
    critical_count = sum(1 for b in bugs if b.severity == BugSeverity.CRITICAL)
    
    if critical_count > 0:
        print(f"\n⚠️  {critical_count} critical issue(s) found")
        sys.exit(1)
    else:
        if args.verbose:
            print("✓ No critical issues")
        sys.exit(0)


def debug_morph_command(args):
    """synapse debug-morph <original> <morphed> - Check for morphing-induced bugs"""
    
    if not args.original or not args.morphed:
        print("Error: Both original and morphed files required")
        sys.exit(1)
    
    original_path = Path(args.original)
    morphed_path = Path(args.morphed)
    
    if not original_path.exists():
        print(f"Error: Original file not found: {args.original}")
        sys.exit(1)
    
    if not morphed_path.exists():
        print(f"Error: Morphed file not found: {args.morphed}")
        sys.exit(1)
    
    # Read codes
    try:
        original_code = original_path.read_text()
        morphed_code = morphed_path.read_text()
    except Exception as e:
        print(f"Error reading files: {e}")
        sys.exit(1)
    
    # Analyze
    analyzer = DebugAnalyzer(provider=args.provider)
    
    if args.verbose:
        print(f"Comparing morphing changes...")
    
    # Check validity
    is_valid, critical_bugs = analyzer.validate_morphing(original_code, morphed_code)
    
    if is_valid:
        print("✓ Morphing produced valid code")
        
        # Show new bugs at other severity levels
        new_bugs = analyzer.analyze_morphing(original_code, morphed_code)
        if new_bugs:
            print(f"\nℹ️  {len(new_bugs)} new issue(s) introduced:")
            for bug in new_bugs:
                print(f"  [{bug.severity.value}] Line {bug.line}: {bug.message}")
    else:
        print("✗ Morphing introduced critical bugs:")
        for bug in critical_bugs:
            print(f"  Line {bug.line}: {bug.message}")
            if bug.suggested_fix:
                print(f"    Fix: {bug.suggested_fix}")
        sys.exit(1)


def fix_command(args):
    """synapse fix <file> - Suggest and apply fixes"""
    
    if not args.file:
        print("Error: No file specified")
        sys.exit(1)
    
    file_path = Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
    
    # Read code
    try:
        code = file_path.read_text()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Analyze and fix
    analyzer = DebugAnalyzer(provider=args.provider)
    
    if args.verbose:
        print(f"Analyzing {args.file}...")
    
    bugs = analyzer.analyze(code)
    
    if not bugs:
        print("✓ No bugs detected")
        sys.exit(0)
    
    print(f"Found {len(bugs)} issue(s)\n")
    
    # Get fix suggestions
    fixes = analyzer.suggest_fixes(code)
    
    for bug in bugs:
        print(f"[{bug.severity.value.upper()}] Line {bug.line}: {bug.message}")
        if bug.id in fixes:
            print(f"  Suggestion: {fixes[bug.id]}")
        print()
    
    # Optionally apply fixes
    if args.apply:
        print("Applying fixes...")
        fixed_code, remaining_bugs = analyzer.apply_fixes(code)
        
        # Write fixed code
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        backup_path.write_text(code)
        file_path.write_text(fixed_code)
        
        print(f"✓ Fixed code written to {file_path}")
        print(f"  Backup saved to {backup_path}")
        
        if remaining_bugs:
            print(f"⚠️  {len(remaining_bugs)} issue(s) require manual review:")
            for bug in remaining_bugs:
                print(f"  [{bug.severity.value}] Line {bug.line}: {bug.message}")
    
    sys.exit(0 if not bugs else 1)


def validate_command(args):
    """synapse validate <file> - Check code validity"""
    
    if not args.file:
        print("Error: No file specified")
        sys.exit(1)
    
    file_path = Path(args.file)
    
    if not file_path.exists():
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
    
    # Read code
    try:
        code = file_path.read_text()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Analyze
    analyzer = DebugAnalyzer(provider=args.provider)
    bugs = analyzer.analyze(code)
    
    if not bugs:
        print(f"✓ {args.file} is valid")
        sys.exit(0)
    else:
        print(f"✗ {args.file} has {len(bugs)} issue(s)")
        for bug in bugs:
            print(f"  [{bug.severity.value}] Line {bug.line}: {bug.message}")
        sys.exit(1)


def setup_debug_subparsers(subparsers):
    """Setup debug-related subcommands"""
    
    # debug command
    debug_parser = subparsers.add_parser(
        'debug',
        help='Analyze code for bugs'
    )
    debug_parser.add_argument('file', nargs='?', help='File to analyze')
    debug_parser.add_argument(
        '-p', '--provider',
        choices=['mock', 'openai', 'anthropic'],
        default='mock',
        help='AI provider (default: mock)'
    )
    debug_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    debug_parser.set_defaults(func=debug_command)
    
    # debug-morph command
    debug_morph_parser = subparsers.add_parser(
        'debug-morph',
        help='Check for morphing-induced bugs'
    )
    debug_morph_parser.add_argument('original', nargs='?', help='Original file')
    debug_morph_parser.add_argument('morphed', nargs='?', help='Morphed file')
    debug_morph_parser.add_argument(
        '-p', '--provider',
        choices=['mock', 'openai', 'anthropic'],
        default='mock',
        help='AI provider (default: mock)'
    )
    debug_morph_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    debug_morph_parser.set_defaults(func=debug_morph_command)
    
    # fix command
    fix_parser = subparsers.add_parser(
        'fix',
        help='Suggest and apply fixes'
    )
    fix_parser.add_argument('file', nargs='?', help='File to fix')
    fix_parser.add_argument(
        '-p', '--provider',
        choices=['mock', 'openai', 'anthropic'],
        default='mock',
        help='AI provider (default: mock)'
    )
    fix_parser.add_argument(
        '-a', '--apply',
        action='store_true',
        help='Apply fixes automatically'
    )
    fix_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    fix_parser.set_defaults(func=fix_command)
    
    # validate command
    validate_parser = subparsers.add_parser(
        'validate',
        help='Check code validity'
    )
    validate_parser.add_argument('file', nargs='?', help='File to validate')
    validate_parser.add_argument(
        '-p', '--provider',
        choices=['mock', 'openai', 'anthropic'],
        default='mock',
        help='AI provider (default: mock)'
    )
    validate_parser.set_defaults(func=validate_command)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Synapse AI Debugging')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    setup_debug_subparsers(subparsers)
    
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
