"""
Compiler Optimizations for Synapse
Implements dead code elimination, constant folding, and function inlining
"""

from typing import List, Dict, Set, Optional, Tuple, Any
from dataclasses import dataclass
import ast as python_ast
from enum import Enum

from synapse.ai.optimizer_ml import load_model, predict_best_opt


class OptimizationLevel(Enum):
    """Optimization levels"""
    NONE = 0
    BASIC = 1
    AGGRESSIVE = 2
    EXTREME = 3


@dataclass
class OptimizationStats:
    """Track optimization statistics"""
    dead_code_removed: int = 0
    constants_folded: int = 0
    functions_inlined: int = 0
    variables_eliminated: int = 0
    branches_simplified: int = 0
    loops_unrolled: int = 0


class ConstantFolder:
    """Folds constant expressions"""
    
    @staticmethod
    def fold(expr: str) -> Tuple[bool, Any]:
        """Attempt to fold expression into constant"""
        try:
            # Only allow safe builtins
            safe_builtins = {
                '__builtins__': {},
                'abs': abs,
                'len': len,
                'min': min,
                'max': max,
                'sum': sum,
                'int': int,
                'float': float,
                'str': str,
            }
            
            result = eval(expr, safe_builtins)
            return True, result
        except:
            return False, None
    
    @staticmethod
    def is_constant_expr(expr: str) -> bool:
        """Check if expression is purely constant"""
        try:
            python_ast.parse(expr)
            tree = python_ast.parse(expr)
            for node in python_ast.walk(tree):
                if isinstance(node, python_ast.Name):
                    return False
                if isinstance(node, python_ast.Call):
                    return False
            return True
        except:
            return False


class DeadCodeEliminator:
    """Removes unreachable and unused code"""
    
    def __init__(self):
        self.used_vars: Set[str] = set()
        self.used_functions: Set[str] = set()
        self.stats = OptimizationStats()
    
    def eliminate(self, code_lines: List[str]) -> List[str]:
        """Remove dead code from code lines"""
        # First pass: identify used variables and functions
        self._mark_used(code_lines)
        
        # Second pass: remove unused definitions
        result = []
        i = 0
        while i < len(code_lines):
            line = code_lines[i]
            
            # Check for dead variable assignments
            if self._is_dead_assignment(line):
                self.stats.dead_code_removed += 1
                i += 1
                continue
            
            # Check for dead function definitions
            if self._is_dead_function_def(line):
                # Skip entire function
                while i < len(code_lines):
                    i += 1
                    if i < len(code_lines) and code_lines[i].startswith('}'):
                        i += 1
                        break
                self.stats.dead_code_removed += 1
                continue
            
            result.append(line)
            i += 1
        
        return result
    
    def _mark_used(self, code_lines: List[str]) -> None:
        """First pass: identify all used variables and functions"""
        for line in code_lines:
            # Simple heuristic: any identifier in RHS is used
            if '=' in line:
                rhs = line.split('=', 1)[1]
                self._extract_identifiers(rhs, self.used_vars)
                self._extract_function_calls(rhs, self.used_functions)
            elif line.strip().startswith('print('):
                self._extract_identifiers(line, self.used_vars)
                self._extract_function_calls(line, self.used_functions)
            elif line.strip().startswith('if ') or line.strip().startswith('for '):
                self._extract_identifiers(line, self.used_vars)
                self._extract_function_calls(line, self.used_functions)
    
    def _extract_identifiers(self, text: str, target_set: Set[str]) -> None:
        """Extract identifiers from text"""
        # Simple word boundary approach
        import re
        identifiers = re.findall(r'\b[a-zA-Z_]\w*\b', text)
        for ident in identifiers:
            if not self._is_keyword(ident):
                target_set.add(ident)

    def _extract_function_calls(self, text: str, target_set: Set[str]) -> None:
        """Extract function calls f(...)"""
        import re
        calls = re.findall(r'\b[a-zA-Z_]\w*\s*\(', text)
        for call in calls:
            fn_name = call.split('(')[0].strip()
            if not self._is_keyword(fn_name):
                target_set.add(fn_name)
    
    def _is_keyword(self, word: str) -> bool:
        """Check if word is a language keyword"""
        keywords = {'let', 'def', 'if', 'else', 'for', 'in', 'while', 
                   'return', 'print', 'import', 'true', 'false'}
        return word in keywords
    
    def _is_dead_assignment(self, line: str) -> bool:
        """Check if assignment is dead (variable never used)"""
        if not ('let ' in line and '=' in line):
            return False
        
        parts = line.split('=', 1)
        if len(parts) < 2:
            return False
        
        lhs = parts[0].replace('let', '').strip()
        var_name = lhs.split(':')[0].strip()
        
        return var_name not in self.used_vars
    
    def _is_dead_function_def(self, line: str) -> bool:
        """Check if function definition is dead (never called)"""
        if not line.strip().startswith('def '):
            return False
        
        func_name = line.split('(')[0].replace('def', '').strip()
        return func_name not in self.used_functions


class FunctionInliner:
    """Inlines small functions for performance"""
    
    def __init__(self, size_threshold: int = 3):
        self.size_threshold = size_threshold
        self.stats = OptimizationStats()
    
    def inline(self, code_lines: List[str]) -> List[str]:
        """Inline small functions"""
        # Identify small functions
        functions = self._extract_functions(code_lines)
        
        # Find functions small enough to inline
        to_inline = {}
        for func_name, func_lines in functions.items():
            if len(func_lines) <= self.size_threshold:
                to_inline[func_name] = func_lines
        
        # Replace calls with inlined code
        result = []
        for line in code_lines:
            # Check if line is a function call to be inlined
            inlined = False
            for func_name, func_body in to_inline.items():
                if f'{func_name}(' in line:
                    # Extract arguments and inline
                    result.extend(func_body)
                    self.stats.functions_inlined += 1
                    inlined = True
                    break
            
            if not inlined:
                result.append(line)
        
        return result
    
    def _extract_functions(self, code_lines: List[str]) -> Dict[str, List[str]]:
        """Extract function definitions"""
        functions = {}
        current_func = None
        func_lines = []
        
        for line in code_lines:
            if line.strip().startswith('def '):
                if current_func:
                    functions[current_func] = func_lines
                
                func_name = line.split('(')[0].replace('def', '').strip()
                current_func = func_name
                func_lines = []
            elif current_func:
                if '}' in line:
                    func_lines.append(line)
                    functions[current_func] = func_lines
                    current_func = None
                    func_lines = []
                else:
                    func_lines.append(line)
        
        return functions


class LoopOptimizer:
    """Optimizes loop structures"""
    
    def __init__(self):
        self.stats = OptimizationStats()
    
    def optimize(self, code_lines: List[str]) -> List[str]:
        """Optimize loop structures"""
        result = []
        i = 0
        
        while i < len(code_lines):
            line = code_lines[i]
            
            # Check for simple unrollable loops
            if line.strip().startswith('for ') and self._is_unrollable(code_lines, i):
                # Unroll loop
                unrolled = self._unroll_loop(code_lines, i)
                result.extend(unrolled)
                # Skip original loop
                while i < len(code_lines) and '}' not in code_lines[i]:
                    i += 1
                i += 1
                self.stats.loops_unrolled += 1
            else:
                result.append(line)
                i += 1
        
        return result
    
    def _is_unrollable(self, code_lines: List[str], start_idx: int) -> bool:
        """Check if a loop can be unrolled"""
        # Simple heuristic: very small loops with constant range
        loop_line = code_lines[start_idx]
        
        # Check for 'for i in [1, 2, 3]' pattern
        if '[' in loop_line and ']' in loop_line:
            # Count braces to find loop size
            count = 0
            for i in range(start_idx + 1, min(start_idx + 10, len(code_lines))):
                if '}' in code_lines[i]:
                    count = i - start_idx
                    return count < 5  # Unroll small loops
        
        return False
    
    def _unroll_loop(self, code_lines: List[str], start_idx: int) -> List[str]:
        """Unroll a loop"""
        # Simple implementation: would need actual iteration values
        return [code_lines[start_idx]]


class SynapseOptimizer:
    """Main optimizer orchestrator"""
    
    def __init__(self, level: OptimizationLevel = OptimizationLevel.BASIC, use_ml: bool = False):
        self.level = level
        self.use_ml = use_ml
        self.ml_model = None
        if use_ml:
            self._load_ml_model()
        self.stats = OptimizationStats()
        self.constant_folder = ConstantFolder()
        self.dead_code_eliminator = DeadCodeEliminator()
        self.inliner = FunctionInliner()
        self.loop_optimizer = LoopOptimizer()
    
    def _load_ml_model(self):
        """Load ML model for optimization guidance"""
        self.ml_model = load_model()
    
    def optimize(self, code: str) -> str:
        """Optimize Synapse code"""
        if self.use_ml and self.ml_model:
            pred_level, _ = predict_best_opt(code)
            self.level = OptimizationLevel(min(pred_level, 3))
        
        code_lines = code.split('\n')
        
        if self.level == OptimizationLevel.NONE:
            return code
        
        # Apply optimizations
        if self.level.value >= OptimizationLevel.BASIC.value:
            code_lines = self._fold_constants(code_lines)
            code_lines = self.dead_code_eliminator.eliminate(code_lines)
        
        if self.level.value >= OptimizationLevel.AGGRESSIVE.value:
            code_lines = self.inliner.inline(code_lines)
            code_lines = self.loop_optimizer.optimize(code_lines)
        
        # Merge stats
        self.stats.constants_folded = self.constant_folder.__dict__.get('folded', 0)
        self.stats.dead_code_removed = self.dead_code_eliminator.stats.dead_code_removed
        self.stats.functions_inlined = self.inliner.stats.functions_inlined
        self.stats.loops_unrolled = self.loop_optimizer.stats.loops_unrolled
        
        return '\n'.join(code_lines)
    
    def _fold_constants(self, code_lines: List[str]) -> List[str]:
        """Fold constant expressions"""
        result = []
        folded_count = 0
        
        for line in code_lines:
            if '=' in line and 'def ' not in line:
                parts = line.split('=', 1)
                if len(parts) == 2:
                    lhs = parts[0]
                    rhs = parts[1].strip()
                    
                    if self.constant_folder.is_constant_expr(rhs):
                        success, value = self.constant_folder.fold(rhs)
                        if success:
                            # Replace with folded constant
                            line = f"{lhs}= {value}"
                            folded_count += 1
            
            result.append(line)
        
        self.stats.constants_folded += folded_count
        return result
    
    def get_stats(self) -> dict:
        """Get optimization statistics"""
        return {
            'dead_code_removed': self.stats.dead_code_removed,
            'constants_folded': self.stats.constants_folded,
            'functions_inlined': self.stats.functions_inlined,
            'variables_eliminated': self.stats.variables_eliminated,
            'branches_simplified': self.stats.branches_simplified,
            'loops_unrolled': self.stats.loops_unrolled,
        }


def test_optimizer():
    """Test the optimizer"""
    code = '''
let x = 10
let y = 20
let z = x + y

def add(a, b) {
    a + b
}

let result = add(5, 3)

let unused = 42

if z > 25 {
    print(z)
}
'''
    
    print("=== Original Code ===")
    print(code)
    
    optimizer = SynapseOptimizer(OptimizationLevel.BASIC)
    optimized = optimizer.optimize(code)
    
    print("\n=== Optimized Code ===")
    print(optimized)
    
    print("\n=== Optimization Stats ===")
    for key, value in optimizer.get_stats().items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    test_optimizer()
