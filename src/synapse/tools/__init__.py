"""
Synapse tools package - Code generation, documentation, and utilities.
"""

from .docgen import DocumentationGenerator, extract_annotations, generate_api_docs, generate_doc_site

__all__ = [
    'DocumentationGenerator',
    'extract_annotations',
    'generate_api_docs',
    'generate_doc_site'
]
