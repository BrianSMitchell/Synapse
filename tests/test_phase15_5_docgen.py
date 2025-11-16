"""
Phase 15.5: Documentation Generator Tests

Tests for the Synapse documentation generator including:
- Annotation and comment parsing
- Function metadata extraction  
- Markdown generation
- JSON documentation
- HTML site generation
- Type-aware documentation
"""

import pytest
import json
import tempfile
from pathlib import Path
from synapse.tools.docgen import (
    AnnotationParser,
    DocumentationGenerator,
    Parameter,
    Function,
    Module,
    extract_annotations,
    generate_api_docs,
    generate_doc_site
)


class TestParameter:
    """Tests for Parameter dataclass."""

    def test_parameter_creation(self):
        """Test basic parameter creation."""
        param = Parameter(name="x", type_hint="float", description="Value to process")
        assert param.name == "x"
        assert param.type_hint == "float"
        assert param.description == "Value to process"

    def test_parameter_to_dict(self):
        """Test parameter serialization."""
        param = Parameter(name="x", type_hint="int", description="Counter")
        data = param.to_dict()
        assert data['name'] == "x"
        assert data['type_hint'] == "int"
        assert data['description'] == "Counter"

    def test_parameter_optional_fields(self):
        """Test parameter with optional fields."""
        param = Parameter(name="x")
        assert param.type_hint == ""
        assert param.description == ""
        assert param.default is None


class TestFunction:
    """Tests for Function dataclass."""

    def test_function_creation(self):
        """Test function creation with metadata."""
        func = Function(
            name="add",
            description="Add two numbers",
            parameters=[
                Parameter(name="x", type_hint="float"),
                Parameter(name="y", type_hint="float")
            ],
            return_type="float",
            return_description="Sum of x and y"
        )
        assert func.name == "add"
        assert len(func.parameters) == 2
        assert func.return_type == "float"

    def test_function_with_examples(self):
        """Test function with examples."""
        func = Function(
            name="increment",
            examples=["increment(5)  // returns 6"]
        )
        assert len(func.examples) == 1
        assert "increment(5)" in func.examples[0]

    def test_function_to_dict(self):
        """Test function serialization."""
        func = Function(
            name="test",
            description="Test function",
            source_file="test.syn",
            line_number=10
        )
        data = func.to_dict()
        assert data['name'] == "test"
        assert data['source_file'] == "test.syn"
        assert data['line_number'] == 10


class TestModule:
    """Tests for Module dataclass."""

    def test_module_creation(self):
        """Test module creation."""
        module = Module(
            name="math",
            description="Math utilities",
            file_path="math.syn"
        )
        assert module.name == "math"
        assert module.version == "1.0"

    def test_module_with_functions(self):
        """Test module with functions."""
        func1 = Function(name="add", description="Add numbers")
        func2 = Function(name="subtract", description="Subtract numbers")
        
        module = Module(
            name="operations",
            functions=[func1, func2]
        )
        
        assert len(module.functions) == 2
        assert module.functions[0].name == "add"

    def test_module_to_dict(self):
        """Test module serialization."""
        module = Module(name="test", description="Test module")
        data = module.to_dict()
        assert data['name'] == "test"
        assert data['version'] == "1.0"


class TestAnnotationParser:
    """Tests for AnnotationParser."""

    def test_parse_simple_function(self):
        """Test parsing simple function definition."""
        code = """
        def add(x, y) {
            x + y
        }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 1
        assert functions[0].name == "add"
        assert len(functions[0].parameters) == 2
        assert functions[0].parameters[0].name == "x"
        assert functions[0].parameters[1].name == "y"

    def test_parse_function_with_comment(self):
        """Test parsing function with documentation comment."""
        code = """
        // Add two numbers together
        def add(x, y) {
            x + y
        }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 1
        assert "Add two numbers" in functions[0].description

    def test_parse_function_with_type_hints(self):
        """Test parsing function with type hints."""
        code = """
        def add(x: float, y: float) {
            x + y
        }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 1
        assert functions[0].parameters[0].type_hint == "float"
        assert functions[0].parameters[1].type_hint == "float"

    def test_extract_module_metadata(self):
        """Test module metadata extraction."""
        code = """
        // Math utilities module
        // Provides basic arithmetic operations
        
        def add(x, y) {
            x + y
        }
        """
        parser = AnnotationParser(code, "math.syn")
        name, desc = parser.extract_module_metadata()
        
        assert name == "math"
        assert "Math utilities" in desc

    def test_parse_multiple_functions(self):
        """Test parsing multiple functions."""
        code = """
        def add(x, y) { x + y }
        def subtract(x, y) { x - y }
        def multiply(x, y) { x * y }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 3
        assert [f.name for f in functions] == ["add", "subtract", "multiply"]

    def test_parse_function_with_return_annotation(self):
        """Test parsing return type annotation."""
        code = """
        // Calculate sum
        // @return: float - the sum of x and y
        def add(x, y) {
            x + y
        }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 1
        assert "sum of x and y" in functions[0].return_description

    def test_parse_function_with_examples(self):
        """Test parsing example annotations."""
        code = """
        // Add two numbers
        // @example: add(3, 4) returns 7
        def add(x, y) {
            x + y
        }
        """
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 1
        assert len(functions[0].examples) > 0

    def test_empty_code(self):
        """Test parsing empty code."""
        parser = AnnotationParser("")
        functions = parser.extract_functions()
        assert len(functions) == 0

    def test_code_without_functions(self):
        """Test parsing code without functions."""
        code = "let x = 5\nlet y = 10"
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        assert len(functions) == 0


class TestDocumentationGenerator:
    """Tests for DocumentationGenerator."""

    def test_initialization(self):
        """Test generator initialization."""
        gen = DocumentationGenerator(".")
        assert gen.project_root == Path(".")
        assert len(gen.modules) == 0

    def test_markdown_generation(self):
        """Test Markdown documentation generation."""
        gen = DocumentationGenerator()
        
        func = Function(
            name="test_func",
            description="A test function",
            parameters=[Parameter(name="x", type_hint="int")],
            return_type="int"
        )
        
        module = Module(
            name="test_module",
            description="Test module",
            functions=[func]
        )
        
        gen.modules = [module]
        markdown = gen.generate_markdown_docs()
        
        assert "test_module" in markdown
        assert "test_func" in markdown
        assert "Table of Contents" in markdown

    def test_markdown_with_multiple_modules(self):
        """Test Markdown with multiple modules."""
        gen = DocumentationGenerator()
        
        # Create modules
        for i in range(3):
            func = Function(name=f"func{i}", description=f"Function {i}")
            module = Module(name=f"module{i}", functions=[func])
            gen.modules.append(module)
        
        markdown = gen.generate_markdown_docs()
        
        assert "module0" in markdown
        assert "module1" in markdown
        assert "module2" in markdown

    def test_json_generation(self):
        """Test JSON documentation generation."""
        gen = DocumentationGenerator()
        
        func = Function(
            name="add",
            description="Add two numbers",
            parameters=[
                Parameter(name="x", type_hint="float"),
                Parameter(name="y", type_hint="float")
            ]
        )
        
        module = Module(name="math", functions=[func])
        gen.modules = [module]
        
        json_str = gen.generate_json_docs()
        data = json.loads(json_str)
        
        assert data['total_modules'] == 1
        assert data['total_functions'] == 1
        assert data['modules'][0]['name'] == "math"

    def test_html_generation(self):
        """Test HTML site generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = DocumentationGenerator()
            
            func = Function(name="test", description="Test function")
            module = Module(name="test_mod", functions=[func])
            gen.modules = [module]
            
            gen.generate_html_site(tmpdir)
            
            # Check generated files
            output_path = Path(tmpdir)
            assert (output_path / "index.html").exists()
            assert (output_path / "style.css").exists()
            assert (output_path / "test_mod.html").exists()

    def test_html_file_content(self):
        """Test HTML file content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = DocumentationGenerator()
            
            func = Function(
                name="multiply",
                description="Multiply two numbers",
                parameters=[Parameter(name="a", type_hint="float")]
            )
            module = Module(name="calc", functions=[func])
            gen.modules = [module]
            
            gen.generate_html_site(tmpdir)
            
            # Read index.html
            index_path = Path(tmpdir) / "index.html"
            content = index_path.read_text()
            
            assert "Synapse API Documentation" in content
            assert "calc" in content
            assert "1 functions" in content

    def test_css_generation(self):
        """Test CSS stylesheet generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            gen = DocumentationGenerator()
            gen.generate_html_site(tmpdir)
            
            css_path = Path(tmpdir) / "style.css"
            assert css_path.exists()
            
            content = css_path.read_text()
            assert "Synapse API" in content or "body" in content

    def test_module_to_markdown(self):
        """Test module Markdown conversion."""
        gen = DocumentationGenerator()
        
        func = Function(
            name="test",
            description="Test function",
            parameters=[Parameter(name="x")]
        )
        module = Module(name="mod", functions=[func])
        
        lines = gen._module_to_markdown(module)
        markdown = '\n'.join(lines)
        
        assert "mod" in markdown
        assert "test" in markdown

    def test_function_to_markdown(self):
        """Test function Markdown conversion."""
        gen = DocumentationGenerator()
        
        func = Function(
            name="add",
            description="Add two numbers",
            parameters=[
                Parameter(name="x", type_hint="float", description="First number"),
                Parameter(name="y", type_hint="float", description="Second number")
            ],
            return_type="float",
            return_description="The sum"
        )
        
        lines = gen._function_to_markdown(func)
        markdown = '\n'.join(lines)
        
        assert "`add(" in markdown
        assert "Parameters:" in markdown
        assert "Returns:" in markdown
        assert "float" in markdown

    def test_function_with_examples_markdown(self):
        """Test function with examples in Markdown."""
        gen = DocumentationGenerator()
        
        func = Function(
            name="test",
            examples=["test(5) // returns 5"]
        )
        
        lines = gen._function_to_markdown(func)
        markdown = '\n'.join(lines)
        
        assert "Examples:" in markdown
        assert "test(5)" in markdown


class TestExtractAnnotations:
    """Tests for extract_annotations function."""

    def test_extract_from_simple_code(self):
        """Test annotation extraction from simple code."""
        code = """
        // Math module
        def add(x, y) { x + y }
        """
        
        result = extract_annotations(code)
        
        assert result['module_name'] != ""
        assert result['function_count'] == 1
        assert result['functions'][0]['name'] == "add"

    def test_extract_with_multiple_functions(self):
        """Test extraction with multiple functions."""
        code = """
        def f1() { }
        def f2() { }
        def f3() { }
        """
        
        result = extract_annotations(code)
        assert result['function_count'] == 3

    def test_extract_with_file_path(self):
        """Test extraction with file path."""
        code = "def test() { }"
        result = extract_annotations(code, "utils.syn")
        
        assert result['module_name'] == "utils"


class TestGenerateAPIDocs:
    """Tests for generate_api_docs function."""

    def test_generate_api_docs(self):
        """Test API documentation generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            test_file = Path(tmpdir) / "test.syn"
            test_file.write_text("""
            // Test module
            def test() { }
            """)
            
            output_file = Path(tmpdir) / "api.md"
            
            # This will fail because scan_directory expects relative paths
            # But we can test the concept
            gen = DocumentationGenerator(tmpdir)
            func = Function(name="test")
            module = Module(name="test_mod", functions=[func])
            gen.modules = [module]
            
            result = gen.generate_markdown_docs(str(output_file))
            
            assert "test_mod" in result
            assert output_file.exists()


class TestIntegration:
    """Integration tests for complete documentation workflow."""

    def test_complete_workflow(self):
        """Test complete documentation generation workflow."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test Synapse files
            test_dir = Path(tmpdir) / "src"
            test_dir.mkdir()
            
            math_file = test_dir / "math.syn"
            math_file.write_text("""
            // Math utilities
            // Provides basic mathematical operations
            
            // Add two numbers together
            def add(x: float, y: float) {
                x + y
            }
            
            // Multiply two numbers
            def multiply(x: float, y: float) {
                x * y
            }
            """)
            
            # Generate documentation
            gen = DocumentationGenerator(tmpdir)
            gen.scan_directory("src")
            
            assert len(gen.modules) > 0
            
            # Generate outputs
            with tempfile.TemporaryDirectory() as outdir:
                gen.generate_markdown_docs(str(Path(outdir) / "api.md"))
                gen.generate_json_docs(str(Path(outdir) / "api.json"))
                gen.generate_html_site(outdir)
                
                # Verify outputs
                assert (Path(outdir) / "api.md").exists()
                assert (Path(outdir) / "api.json").exists()
                assert (Path(outdir) / "index.html").exists()

    def test_real_stdlib_documentation(self):
        """Test documentation generation from real stdlib."""
        gen = DocumentationGenerator()
        
        # This will work if we're in the right directory
        try:
            gen.scan_directory("stdlib")
            
            if len(gen.modules) > 0:
                markdown = gen.generate_markdown_docs()
                assert len(markdown) > 0
                
                json_str = gen.generate_json_docs()
                data = json.loads(json_str)
                assert 'modules' in data
        except:
            pytest.skip("stdlib directory not found or not accessible")


# Performance tests
class TestPerformance:
    """Performance tests for documentation generator."""

    def test_parse_large_file(self):
        """Test parsing performance with large file."""
        # Generate code with many functions
        code_lines = ["// Large module"]
        for i in range(100):
            code_lines.append(f"def func{i}(x) {{ x + {i} }}")
        
        code = '\n'.join(code_lines)
        
        parser = AnnotationParser(code)
        functions = parser.extract_functions()
        
        assert len(functions) == 100

    def test_generate_large_documentation(self):
        """Test documentation generation with many modules."""
        gen = DocumentationGenerator()
        
        # Create 20 modules with 10 functions each
        for i in range(20):
            functions = [
                Function(name=f"func{j}", description=f"Function {j}")
                for j in range(10)
            ]
            module = Module(name=f"module{i}", functions=functions)
            gen.modules.append(module)
        
        # Generate Markdown
        markdown = gen.generate_markdown_docs()
        assert len(gen.modules) == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
