"""
Documentation Generator for Synapse

Automatically extracts documentation from Synapse code using annotations and comments,
generates API documentation in Markdown, and builds a complete static documentation site.

Features:
- Extract function/module metadata from code annotations
- Parse inline comments as documentation
- Type-aware documentation with parameter descriptions
- Generate Markdown API docs with cross-references
- Build complete HTML documentation site
- Support for examples and usage patterns
- TOC generation and navigation
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict, field
from datetime import datetime


@dataclass
class Parameter:
    """Function parameter documentation."""
    name: str
    type_hint: str = ""
    description: str = ""
    default: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class Function:
    """Function documentation."""
    name: str
    description: str = ""
    parameters: List[Parameter] = field(default_factory=list)
    return_type: str = ""
    return_description: str = ""
    examples: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    source_file: str = ""
    line_number: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'parameters': [p.to_dict() for p in self.parameters],
            'return_type': self.return_type,
            'return_description': self.return_description,
            'examples': self.examples,
            'tags': self.tags,
            'source_file': self.source_file,
            'line_number': self.line_number,
        }


@dataclass
class Module:
    """Module documentation."""
    name: str
    description: str = ""
    functions: List[Function] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    file_path: str = ""
    version: str = "1.0"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'functions': [f.to_dict() for f in self.functions],
            'tags': self.tags,
            'file_path': self.file_path,
            'version': self.version,
        }


class AnnotationParser:
    """Parse Synapse code comments and annotations for documentation."""

    # Regex patterns for parsing
    FUNCTION_DEF = re.compile(r'def\s+(\w+)\s*\((.*?)\)')
    COMMENT_BLOCK = re.compile(r'^//\s*(.*)$', re.MULTILINE)
    ANNOTATION = re.compile(r'@(\w+)\s*:\s*(.+)')
    PARAMETER_DOC = re.compile(r'@param\s+(\w+)\s*:\s*(.+)')
    RETURN_DOC = re.compile(r'@return\s*:\s*(.+)')
    EXAMPLE_DOC = re.compile(r'@example\s*:\s*(.+)')
    TYPE_HINT = re.compile(r'(\w+)\s*:\s*(\w+)')

    def __init__(self, code: str, file_path: str = ""):
        """Initialize parser with code and optional file path."""
        self.code = code
        self.file_path = file_path
        self.lines = code.split('\n')

    def extract_module_metadata(self) -> Tuple[str, str]:
        """Extract module name and description from header comments."""
        name = Path(self.file_path).stem if self.file_path else "unnamed"
        
        # Look for module-level comments at the start
        description_lines = []
        in_header = True
        
        for line in self.lines:
            line = line.strip()
            if in_header and line.startswith('//'):
                # Extract comment content
                comment = line[2:].strip()
                if comment and not comment.startswith('='):
                    description_lines.append(comment)
            elif in_header and line == '':
                continue
            elif in_header and line and not line.startswith('//'):
                in_header = False
                break
        
        description = '\n'.join(description_lines).strip()
        return name, description

    def extract_functions(self) -> List[Function]:
        """Extract all function definitions with their documentation."""
        functions = []
        i = 0
        
        while i < len(self.lines):
            line = self.lines[i]
            
            # Check for function definition
            match = self.FUNCTION_DEF.search(line)
            if match:
                func_name = match.group(1)
                params_str = match.group(2)
                
                # Extract preceding comments as documentation
                comments = self._extract_preceding_comments(i)
                description = comments.get('description', '')
                
                # Parse parameters
                parameters = self._parse_parameters(params_str)
                
                # Extract additional metadata from comments
                return_type = comments.get('return_type', '')
                return_desc = comments.get('return_description', '')
                examples = comments.get('examples', [])
                tags = comments.get('tags', [])
                
                # Create function object
                func = Function(
                    name=func_name,
                    description=description,
                    parameters=parameters,
                    return_type=return_type,
                    return_description=return_desc,
                    examples=examples,
                    tags=tags,
                    source_file=self.file_path,
                    line_number=i + 1
                )
                functions.append(func)
            
            i += 1
        
        return functions

    def _extract_preceding_comments(self, func_line: int) -> Dict[str, Any]:
        """Extract comments preceding a function definition."""
        metadata = {
            'description': '',
            'return_type': '',
            'return_description': '',
            'examples': [],
            'tags': []
        }
        
        # Look backward from function line
        comment_lines = []
        i = func_line - 1
        
        while i >= 0:
            line = self.lines[i].strip()
            if line.startswith('//'):
                # Extract comment (remove // prefix)
                comment = line[2:].strip()
                if comment and not comment.startswith('='):
                    comment_lines.insert(0, comment)
            elif line == '' or line.startswith('def'):
                break
            else:
                break
            i -= 1
        
        # Parse extracted comments
        full_comment = '\n'.join(comment_lines)
        
        # Extract main description (first paragraph)
        parts = full_comment.split('@')
        if parts:
            metadata['description'] = parts[0].strip()
        
        # Extract tagged metadata
        for part in parts[1:]:
            lines = part.split('\n')
            if not lines:
                continue
            
            tag_line = lines[0].strip()
            
            if tag_line.startswith('param'):
                # @param name: description
                match = re.match(r'param\s+(\w+)\s*:\s*(.*)', tag_line)
                if match:
                    param_name = match.group(1)
                    param_desc = match.group(2).strip()
                    # Find matching parameter and update description
                    # (will be done in _parse_parameters)
            elif tag_line.startswith('return'):
                # @return: description
                match = re.match(r'return\s*:\s*(.*)', tag_line)
                if match:
                    metadata['return_description'] = match.group(1).strip()
            elif tag_line.startswith('example'):
                # @example: code or description
                match = re.match(r'example\s*:\s*(.*)', tag_line)
                if match:
                    example_text = match.group(1).strip()
                    # Append remaining lines as part of example
                    if len(lines) > 1:
                        example_text += '\n' + '\n'.join(lines[1:])
                    metadata['examples'].append(example_text)
            elif tag_line.startswith('tag'):
                # @tag: value
                match = re.match(r'tag\s*:\s*(.*)', tag_line)
                if match:
                    metadata['tags'].append(match.group(1).strip())
        
        return metadata

    def _parse_parameters(self, params_str: str) -> List[Parameter]:
        """Parse function parameter list."""
        parameters = []
        
        if not params_str.strip():
            return parameters
        
        # Split by comma (simple approach)
        params = params_str.split(',')
        
        for param in params:
            param = param.strip()
            if not param:
                continue
            
            # Try to extract type hint
            type_match = self.TYPE_HINT.match(param)
            if type_match:
                name = type_match.group(1)
                type_hint = type_match.group(2)
                parameters.append(Parameter(name=name, type_hint=type_hint))
            else:
                # No type hint
                parameters.append(Parameter(name=param))
        
        return parameters


class DocumentationGenerator:
    """Main documentation generator for Synapse projects."""

    def __init__(self, project_root: str = "."):
        """Initialize generator with project root directory."""
        self.project_root = Path(project_root)
        self.modules: List[Module] = []
        self.output_dir = self.project_root / "docs" / "api"

    def scan_directory(self, directory: str = "stdlib", extensions: List[str] = None) -> None:
        """Scan directory for Synapse files and extract documentation."""
        if extensions is None:
            extensions = ['.syn']
        
        target_dir = self.project_root / directory
        if not target_dir.exists():
            print(f"Warning: Directory {target_dir} does not exist")
            return
        
        for file_path in target_dir.rglob('*'):
            if file_path.is_file() and file_path.suffix in extensions:
                self._process_file(file_path)

    def _process_file(self, file_path: Path) -> None:
        """Process a single Synapse file and extract documentation."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            parser = AnnotationParser(code, str(file_path))
            
            # Extract module metadata
            module_name, module_desc = parser.extract_module_metadata()
            
            # Extract functions
            functions = parser.extract_functions()
            
            # Create module object
            module = Module(
                name=module_name,
                description=module_desc,
                functions=functions,
                file_path=str(file_path)
            )
            
            self.modules.append(module)
            print(f"[OK] Processed {file_path.name}: {len(functions)} functions")
            
        except Exception as e:
            print(f"[ERROR] Error processing {file_path}: {e}")

    def generate_markdown_docs(self, output_file: str = None) -> str:
        """Generate Markdown API documentation."""
        if output_file is None:
            output_file = str(self.output_dir / "API.md")
        
        lines = []
        lines.append("# Synapse API Documentation\n")
        lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        
        # Table of contents
        lines.append("## Table of Contents\n")
        for module in self.modules:
            lines.append(f"- [{module.name}](#{module.name.lower()})")
            for func in module.functions:
                lines.append(f"  - [{func.name}](#{func.name.lower()})")
        lines.append("")
        
        # Generate documentation for each module
        for module in self.modules:
            lines.extend(self._module_to_markdown(module))
        
        # Write to file
        self.output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"[OK] Generated Markdown docs: {output_file}")
        return '\n'.join(lines)

    def _module_to_markdown(self, module: Module) -> List[str]:
        """Convert module to Markdown format."""
        lines = []
        
        lines.append(f"\n## {module.name}\n")
        
        if module.description:
            lines.append(f"{module.description}\n")
        
        if module.tags:
            lines.append(f"**Tags:** {', '.join(module.tags)}\n")
        
        # Functions
        if module.functions:
            lines.append("### Functions\n")
            for func in module.functions:
                lines.extend(self._function_to_markdown(func))
        
        return lines

    def _function_to_markdown(self, func: Function) -> List[str]:
        """Convert function to Markdown format."""
        lines = []
        
        # Function signature
        params_str = ', '.join([f"`{p.name}`" for p in func.parameters])
        lines.append(f"#### `{func.name}({params_str})`\n")
        
        if func.description:
            lines.append(f"{func.description}\n")
        
        # Parameters
        if func.parameters:
            lines.append("**Parameters:**\n")
            for param in func.parameters:
                if param.type_hint:
                    lines.append(f"- `{param.name}` ({param.type_hint})")
                else:
                    lines.append(f"- `{param.name}`")
                if param.description:
                    lines.append(f"  - {param.description}")
            lines.append("")
        
        # Return type
        if func.return_type:
            lines.append(f"**Returns:** `{func.return_type}`")
            if func.return_description:
                lines.append(f"  - {func.return_description}")
            lines.append("")
        
        # Examples
        if func.examples:
            lines.append("**Examples:**\n")
            for example in func.examples:
                lines.append("```synapse")
                lines.append(example)
                lines.append("```\n")
        
        # Tags
        if func.tags:
            lines.append(f"*Tags: {', '.join(func.tags)}*\n")
        
        lines.append("")
        return lines

    def generate_json_docs(self, output_file: str = None) -> str:
        """Generate JSON documentation (machine-readable)."""
        if output_file is None:
            output_file = str(self.output_dir / "api.json")
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        docs = {
            'generated': datetime.now().isoformat(),
            'modules': [m.to_dict() for m in self.modules],
            'total_functions': sum(len(m.functions) for m in self.modules),
            'total_modules': len(self.modules)
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(docs, f, indent=2)
        
        print(f"[OK] Generated JSON docs: {output_file}")
        return json.dumps(docs, indent=2)

    def generate_html_site(self, output_dir: str = None, template: str = None) -> None:
        """Generate complete HTML documentation site."""
        if output_dir is None:
            output_dir = str(self.output_dir)
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate index page
        self._generate_index_html(output_path)
        
        # Generate module pages
        for module in self.modules:
            self._generate_module_html(module, output_path)
        
        # Generate CSS
        self._generate_css(output_path)
        
        print(f"[OK] Generated HTML documentation site: {output_dir}")

    def _generate_index_html(self, output_path: Path) -> None:
        """Generate index.html for the documentation site."""
        html = self._get_html_template_start(
            title="Synapse API Documentation",
            description="Complete API documentation for the Synapse language"
        )
        
        html += "<div class='container'>\n"
        html += "<h1>Synapse API Documentation</h1>\n"
        html += f"<p class='timestamp'>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>\n"
        
        # Module list
        html += "<div class='modules'>\n"
        html += f"<h2>Modules ({len(self.modules)})</h2>\n"
        html += "<ul>\n"
        
        for module in self.modules:
            html += f"<li><a href='{module.name.lower()}.html'>{module.name}</a>"
            html += f" ({len(module.functions)} functions)</li>\n"
        
        html += "</ul>\n"
        html += "</div>\n"
        html += self._get_html_template_end()
        
        with open(output_path / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)

    def _generate_module_html(self, module: Module, output_path: Path) -> None:
        """Generate HTML page for a single module."""
        html = self._get_html_template_start(
            title=f"{module.name} - Synapse API",
            description=module.description
        )
        
        html += "<div class='container'>\n"
        html += f"<h1>{module.name}</h1>\n"
        
        if module.description:
            html += f"<div class='module-description'>{module.description}</div>\n"
        
        html += f"<p class='function-count'>{len(module.functions)} functions</p>\n"
        
        # Functions
        for func in module.functions:
            html += self._function_to_html(func)
        
        html += "<p class='back-link'><a href='index.html'>← Back to index</a></p>\n"
        html += "</div>\n"
        html += self._get_html_template_end()
        
        filename = output_path / f"{module.name.lower()}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def _function_to_html(self, func: Function) -> str:
        """Convert function to HTML."""
        html = ""
        
        html += "<div class='function'>\n"
        html += f"<h3><code>{func.name}()</code></h3>\n"
        
        if func.description:
            html += f"<p class='description'>{func.description}</p>\n"
        
        # Parameters
        if func.parameters:
            html += "<div class='parameters'>\n"
            html += "<strong>Parameters:</strong>\n"
            html += "<ul>\n"
            for param in func.parameters:
                if param.type_hint:
                    html += f"<li><code>{param.name}</code> ({param.type_hint})"
                else:
                    html += f"<li><code>{param.name}</code>"
                if param.description:
                    html += f" - {param.description}"
                html += "</li>\n"
            html += "</ul>\n"
            html += "</div>\n"
        
        # Return type
        if func.return_type:
            html += f"<p><strong>Returns:</strong> <code>{func.return_type}</code>"
            if func.return_description:
                html += f" - {func.return_description}"
            html += "</p>\n"
        
        # Examples
        if func.examples:
            html += "<div class='examples'>\n"
            html += "<strong>Examples:</strong>\n"
            for example in func.examples:
                html += "<pre><code>"
                html += example.replace('<', '&lt;').replace('>', '&gt;')
                html += "</code></pre>\n"
            html += "</div>\n"
        
        html += "</div>\n"
        return html

    def _generate_css(self, output_path: Path) -> None:
        """Generate CSS stylesheet for documentation."""
        css = """
/* Synapse API Documentation Styles */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
    background: white;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1 {
    color: #222;
    margin-bottom: 10px;
    font-size: 2.5em;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 10px;
}

h2 {
    color: #333;
    margin-top: 30px;
    margin-bottom: 15px;
    font-size: 1.8em;
    border-left: 4px solid #0066cc;
    padding-left: 10px;
}

h3 {
    color: #0066cc;
    margin-top: 20px;
    margin-bottom: 10px;
    font-size: 1.3em;
}

code {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 0.9em;
}

pre {
    background: #2d2d2d;
    color: #f8f8f2;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    margin: 10px 0;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
}

.timestamp {
    color: #999;
    font-size: 0.9em;
    margin-bottom: 20px;
}

.function {
    background: #fafafa;
    padding: 20px;
    margin: 20px 0;
    border-left: 4px solid #0066cc;
    border-radius: 4px;
}

.function-count {
    color: #666;
    font-size: 1.1em;
    margin-bottom: 30px;
}

.description {
    margin: 10px 0;
    color: #555;
}

.parameters,
.examples {
    margin: 15px 0;
    padding: 10px 0;
}

.parameters ul,
.modules ul {
    margin-left: 20px;
}

.parameters li,
.modules li {
    margin: 8px 0;
}

.back-link {
    margin-top: 30px;
    border-top: 1px solid #ddd;
    padding-top: 20px;
}

.back-link a {
    color: #0066cc;
    text-decoration: none;
}

.back-link a:hover {
    text-decoration: underline;
}

/* Responsive */
@media (max-width: 600px) {
    .container {
        padding: 20px 10px;
    }
    
    h1 {
        font-size: 1.8em;
    }
    
    h2 {
        font-size: 1.3em;
    }
}
"""
        
        with open(output_path / "style.css", 'w', encoding='utf-8') as f:
            f.write(css)

    def _get_html_template_start(self, title: str = "Synapse API", description: str = "") -> str:
        """Get HTML template start."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="style.css">
</head>
<body>
"""

    def _get_html_template_end(self) -> str:
        """Get HTML template end."""
        return """
</body>
</html>
"""


def extract_annotations(code: str, file_path: str = "") -> Dict[str, Any]:
    """
    Extract all annotations and metadata from Synapse code.
    
    Args:
        code: Synapse source code
        file_path: Optional path to source file
    
    Returns:
        Dictionary containing extracted metadata
    """
    parser = AnnotationParser(code, file_path)
    module_name, module_desc = parser.extract_module_metadata()
    functions = parser.extract_functions()
    
    return {
        'module_name': module_name,
        'module_description': module_desc,
        'functions': [f.to_dict() for f in functions],
        'function_count': len(functions)
    }


def generate_api_docs(source_dir: str, output_file: str = None) -> str:
    """
    Generate API documentation for a directory of Synapse files.
    
    Args:
        source_dir: Directory containing .syn files
        output_file: Output Markdown file path
    
    Returns:
        Generated Markdown documentation
    """
    gen = DocumentationGenerator()
    gen.scan_directory(source_dir)
    return gen.generate_markdown_docs(output_file)


def generate_doc_site(source_dir: str, output_dir: str = None) -> None:
    """
    Generate complete HTML documentation site.
    
    Args:
        source_dir: Directory containing .syn files
        output_dir: Output directory for HTML site
    """
    gen = DocumentationGenerator()
    gen.scan_directory(source_dir)
    gen.generate_html_site(output_dir)


if __name__ == "__main__":
    # Demo usage
    import sys
    
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = "stdlib"
    
    print(f"Generating documentation for {source_dir}...")
    
    # Create generator
    gen = DocumentationGenerator()
    gen.scan_directory(source_dir)
    
    # Generate all formats
    gen.generate_markdown_docs()
    gen.generate_json_docs()
    gen.generate_html_site()
    
    print("✓ Documentation generation complete!")
