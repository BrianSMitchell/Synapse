#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate documentation for Synapse stdlib."""

from synapse.tools.docgen import DocumentationGenerator

if __name__ == "__main__":
    print("[*] Generating Synapse documentation...")
    print()
    
    gen = DocumentationGenerator('.')
    gen.scan_directory('stdlib')
    
    print()
    print("[*] Generating Markdown documentation...")
    gen.generate_markdown_docs('docs/api/API.md')
    
    print("[*] Generating JSON documentation...")
    gen.generate_json_docs('docs/api/api.json')
    
    print("[*] Generating HTML documentation site...")
    gen.generate_html_site('docs/api')
    
    print()
    print("[OK] Documentation generation complete!")
    print(f"[*] Generated documentation for {len(gen.modules)} module(s)")
    for module in gen.modules:
        print(f"   - {module.name}: {len(module.functions)} functions")
