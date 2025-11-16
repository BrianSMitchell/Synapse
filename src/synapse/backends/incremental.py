"""
Incremental Compilation for Synapse
Enables fast recompilation of changed code segments
"""

from typing import Dict, Set, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import time


class ChangeType(Enum):
    """Types of changes detected"""
    MODIFIED = "modified"
    ADDED = "added"
    DELETED = "deleted"
    RENAMED = "renamed"


@dataclass
class FileHash:
    """Track file content hashes for change detection"""
    path: str
    content_hash: str
    modification_time: float
    function_hashes: Dict[str, str]  # function_name -> hash


@dataclass
class CompilationUnit:
    """Represents a compilable unit (file or module)"""
    path: str
    content: str
    dependencies: Set[str]  # paths of imported files
    functions: List[str]  # function names defined
    compiled_output: Optional[str] = None
    compile_time: float = 0.0
    is_dirty: bool = False


class ChangeDetector:
    """Detects changes in source files"""
    
    def __init__(self):
        self.file_hashes: Dict[str, FileHash] = {}
    
    def compute_hash(self, content: str) -> str:
        """Compute SHA256 hash of content"""
        return hashlib.sha256(content.encode()).hexdigest()
    
    def detect_changes(self, files: Dict[str, str]) -> Dict[str, ChangeType]:
        """
        Detect changes between current and previous file states
        Returns: {file_path: change_type}
        """
        changes = {}
        current_paths = set(files.keys())
        previous_paths = set(self.file_hashes.keys())
        
        # Detect added files
        for path in current_paths - previous_paths:
            changes[path] = ChangeType.ADDED
        
        # Detect deleted files
        for path in previous_paths - current_paths:
            changes[path] = ChangeType.DELETED
        
        # Detect modified files
        for path in current_paths & previous_paths:
            current_hash = self.compute_hash(files[path])
            previous_hash = self.file_hashes[path].content_hash
            if current_hash != previous_hash:
                changes[path] = ChangeType.MODIFIED
        
        return changes
    
    def update_hashes(self, files: Dict[str, str]) -> None:
        """Update tracked file hashes"""
        for path, content in files.items():
            content_hash = self.compute_hash(content)
            # Extract function definitions (simple heuristic)
            function_hashes = self._extract_function_hashes(content)
            self.file_hashes[path] = FileHash(
                path=path,
                content_hash=content_hash,
                modification_time=time.time(),
                function_hashes=function_hashes
            )
    
    def _extract_function_hashes(self, content: str) -> Dict[str, str]:
        """Extract and hash individual functions"""
        functions = {}
        lines = content.split('\n')
        current_func = None
        func_lines = []
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('def '):
                # Save previous function
                if current_func:
                    func_content = '\n'.join(func_lines)
                    functions[current_func] = self.compute_hash(func_content)
                
                # Start new function
                parts = stripped.split('(')
                current_func = parts[0].replace('def ', '').strip()
                func_lines = [line]
            elif current_func:
                func_lines.append(line)
        
        # Save last function
        if current_func:
            func_content = '\n'.join(func_lines)
            functions[current_func] = self.compute_hash(func_content)
        
        return functions


class DependencyGraph:
    """Tracks file dependencies for incremental compilation"""
    
    def __init__(self):
        self.graph: Dict[str, Set[str]] = {}  # file -> set of dependencies
        self.reverse_graph: Dict[str, Set[str]] = {}  # file -> set of dependents
    
    def add_dependency(self, source: str, target: str) -> None:
        """Add a dependency: source imports target"""
        if source not in self.graph:
            self.graph[source] = set()
        if target not in self.reverse_graph:
            self.reverse_graph[target] = set()
        
        self.graph[source].add(target)
        self.reverse_graph[target].add(source)
    
    def get_affected_files(self, modified_file: str) -> Set[str]:
        """Get all files affected by a modification"""
        affected = {modified_file}
        to_process = [modified_file]
        
        while to_process:
            current = to_process.pop()
            # Add all dependents
            for dependent in self.reverse_graph.get(current, set()):
                if dependent not in affected:
                    affected.add(dependent)
                    to_process.append(dependent)
        
        return affected
    
    def topological_sort(self) -> List[str]:
        """Return files in topological order for compilation"""
        visited = set()
        result = []
        
        def visit(node: str):
            if node in visited:
                return
            visited.add(node)
            for dep in self.graph.get(node, set()):
                visit(dep)
            result.append(node)
        
        for node in self.graph:
            visit(node)
        
        return result


class IncrementalCompiler:
    """Performs incremental compilation"""
    
    def __init__(self):
        self.change_detector = ChangeDetector()
        self.dependency_graph = DependencyGraph()
        self.compilation_units: Dict[str, CompilationUnit] = {}
        self.cache: Dict[str, str] = {}  # compiled output cache
        self.compilation_stats = {
            'total_time': 0.0,
            'units_compiled': 0,
            'cache_hits': 0,
            'cache_misses': 0,
        }
    
    def register_files(self, files: Dict[str, str]) -> None:
        """Register source files for incremental compilation"""
        for path, content in files.items():
            unit = CompilationUnit(
                path=path,
                content=content,
                dependencies=self._extract_dependencies(content),
                functions=self._extract_functions(content),
            )
            self.compilation_units[path] = unit
            
            # Add to dependency graph
            for dep in unit.dependencies:
                self.dependency_graph.add_dependency(path, dep)
        
        # Initial hashes
        self.change_detector.update_hashes(files)
    
    def compile_incremental(self, files: Dict[str, str]) -> Dict[str, str]:
        """
        Compile files incrementally, only recompiling changed units
        Returns: {file_path: compiled_output}
        """
        start_time = time.time()
        
        # On first call, mark all as dirty
        first_call = len(self.cache) == 0
        
        # Detect changes
        changes = self.change_detector.detect_changes(files)
        
        if not changes and not first_call:
            # No changes
            return {path: (unit.compiled_output or "") for path, unit in 
                    self.compilation_units.items()}
        
        # Update units
        for path, content in files.items():
            if path in self.compilation_units:
                unit = self.compilation_units[path]
                unit.content = content
                if path in changes:
                    unit.is_dirty = True
            else:
                # New file
                unit = CompilationUnit(
                    path=path,
                    content=content,
                    dependencies=self._extract_dependencies(content),
                    functions=self._extract_functions(content),
                )
                self.compilation_units[path] = unit
                for dep in unit.dependencies:
                    self.dependency_graph.add_dependency(path, dep)
                unit.is_dirty = True
        
        # Mark affected files as dirty
        dirty_files = set()
        for changed_file in changes:
            affected = self.dependency_graph.get_affected_files(changed_file)
            dirty_files.update(affected)
        
        # Compile dirty units in dependency order
        compile_order = self.dependency_graph.topological_sort()
        results = {}
        
        for path in compile_order:
            if path in self.compilation_units:
                unit = self.compilation_units[path]
                if unit.is_dirty or path not in self.cache:
                    # Compile
                    output = self._compile_unit(unit) or ""
                    self.cache[path] = output
                    unit.compiled_output = output
                    unit.is_dirty = False
                    self.compilation_stats['units_compiled'] += 1
                    self.compilation_stats['cache_misses'] += 1
                else:
                    # Use cached
                    unit.compiled_output = self.cache.get(path, "")
                    self.compilation_stats['cache_hits'] += 1
                
                results[path] = unit.compiled_output or ""
        
        # Update hashes
        self.change_detector.update_hashes(files)
        
        elapsed = time.time() - start_time
        self.compilation_stats['total_time'] += elapsed
        
        return results
    
    def _compile_unit(self, unit: CompilationUnit) -> str:
        """Compile a single compilation unit"""
        start_time = time.time()
        
        # Placeholder: actual compilation would use parser/codegen
        # For now, just return the content with a marker
        output = f"// Compiled from {unit.path}\n{unit.content}\n"
        
        unit.compile_time = time.time() - start_time
        return output if output else ""
    
    def _extract_dependencies(self, content: str) -> Set[str]:
        """Extract import statements"""
        dependencies = set()
        for line in content.split('\n'):
            stripped = line.strip()
            if stripped.startswith('import '):
                # Simple heuristic: import path
                parts = stripped.split()
                if len(parts) > 1:
                    path = parts[1].strip('"\'')
                    dependencies.add(path)
        return dependencies
    
    def _extract_functions(self, content: str) -> List[str]:
        """Extract function definitions"""
        functions = []
        for line in content.split('\n'):
            stripped = line.strip()
            if stripped.startswith('def '):
                parts = stripped.split('(')
                func_name = parts[0].replace('def ', '').strip()
                functions.append(func_name)
        return functions
    
    def get_stats(self) -> Dict[str, any]:
        """Get compilation statistics"""
        stats = self.compilation_stats.copy()
        total_units = len(self.compilation_units)
        stats['total_units'] = total_units
        if stats['cache_hits'] + stats['cache_misses'] > 0:
            hit_rate = stats['cache_hits'] / (stats['cache_hits'] + stats['cache_misses'])
            stats['cache_hit_rate'] = hit_rate
        return stats


def test_incremental_compiler():
    """Test incremental compilation"""
    compiler = IncrementalCompiler()
    
    # Register initial files
    files = {
        'utils.syn': '''
def add(a, b) {
    a + b
}

def multiply(a, b) {
    a * b
}
''',
        'main.syn': '''
import "utils.syn"

let x = add(5, 3)
let y = multiply(x, 2)
print(y)
''',
    }
    
    compiler.register_files(files)
    
    print("=== First Compilation (Full) ===")
    result1 = compiler.compile_incremental(files)
    for path, output in result1.items():
        print(f"\n{path}:")
        if output:
            print(output[:100] + "..." if len(output) > 100 else output)
        else:
            print("(no output)")
    print("\nStats:", compiler.get_stats())
    
    # Modify only main.syn
    files['main.syn'] = '''
import "utils.syn"

let x = add(10, 5)
let y = multiply(x, 3)
print(y)
'''
    
    print("\n=== Second Compilation (Incremental) ===")
    result2 = compiler.compile_incremental(files)
    print("Stats:", compiler.get_stats())
    
    # No changes
    print("\n=== Third Compilation (No Changes) ===")
    result3 = compiler.compile_incremental(files)
    print("Stats:", compiler.get_stats())


if __name__ == "__main__":
    test_incremental_compiler()
