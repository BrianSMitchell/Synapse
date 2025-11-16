"""
Synapse Language Evolution CLI
Phase 16.5: Self-Improving Grammar/Semantics

Usage: python -m synapse.cli.evolve add_keyword:async
"""

import argparse
import os
import subprocess
import difflib
import re
from pathlib import Path

GRAMMAR_PATH = Path("grammar/Synapse.g4")
GENERATED_DIR = Path("src/generated")
NEW_GENERATED_DIR = Path("src/generated_new")
NEW_GRAMMAR_PATH = Path("grammar/Synapse_new.g4")

def load_grammar():
    """Load current grammar"""
    if not GRAMMAR_PATH.exists():
        raise FileNotFoundError(f"Grammar not found: {GRAMMAR_PATH}")
    return GRAMMAR_PATH.read_text()

def mutate_grammar(grammar_text: str, mutation: str) -> str:
    """Apply mutation to grammar"""
    grammar_name = NEW_GRAMMAR_PATH.stem
    
    if mutation.startswith("add_keyword:"):
        kw = mutation.split(":", 1)[1]
        upper_kw = kw.upper()
        new_rule = f"{upper_kw}: '{kw}' ;"
        
        # Update grammar name
        grammar_text = re.sub(r'grammar Synapse;', f'grammar {grammar_name};', grammar_text)
        
        # Find lexer section: after 'grammar ...;' till first parser rule 'program:'
        lexer_match = re.search(r'grammar \w+;\s*(.*?)\s*program:', grammar_text, re.DOTALL)
        if lexer_match:
            lexer_section_end = lexer_match.end(1)
            new_grammar = grammar_text[:lexer_section_end] + "\n" + new_rule + "\n" + grammar_text[lexer_section_end:]
        else:
            # Fallback: insert after grammar declaration
            grammar_end = grammar_text.find(';', grammar_text.find('grammar')) + 1
            new_grammar = grammar_text[:grammar_end] + "\n" + new_rule + "\n" + grammar_text[grammar_end:]
        
        print(f"Added keyword rule: {new_rule}")
        return new_grammar
    
    raise ValueError(f"Unknown mutation: {mutation}")

def generate_new_parser(new_grammar: str):
    """Run ANTLR4 to generate new parser"""
    NEW_GRAMMAR_PATH.write_text(new_grammar)
    
    cmd = [
        "antlr4", str(NEW_GRAMMAR_PATH),
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        "-o", str(NEW_GENERATED_DIR)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ANTLR4 failed:\n{result.stderr}")
    
    print("New parser generated in src/generated_new/")
    return True

def show_diff(original: str, new: str):
    """Show grammar diff"""
    orig_lines = original.splitlines()
    new_lines = new.splitlines()
    diff = difflib.unified_diff(
        orig_lines, new_lines,
        fromfile="Synapse.g4", tofile="Synapse_new.g4",
        lineterm=""
    )
    print("\n".join(diff))

def main():
    parser = argparse.ArgumentParser(description="Evolve Synapse grammar")
    parser.add_argument("mutation", help="Mutation e.g. 'add_keyword:async'")
    args = parser.parse_args()
    
    print("Phase 16.5: Evolving grammar...")
    
    original = load_grammar()
    new_grammar = mutate_grammar(original, args.mutation)
    
    show_diff(original, new_grammar)
    
    NEW_GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    
    success = generate_new_parser(new_grammar)
    
    if success:
        print("✅ Evolution successful! Test new parser next.")
        print("Next: cp src/generated_new/* src/generated/  # Manual for now")
    else:
        print("❌ Evolution failed.")

if __name__ == "__main__":
    main()
