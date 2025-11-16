"""
Emergent Debugging with AI for Synapse

Analyzes code for bugs introduced by morphing, suggests fixes and improvements,
and integrates with the morphing system for iterative code improvement.

Features:
- Bug detection in morphing-induced code
- AI-powered fix suggestions
- Semantic analysis and type checking
- Performance bottleneck detection
- Integration with code generation (Phase 16.1)
"""

import json
import hashlib
import re
from typing import Optional, Dict, List, Tuple, Any
from abc import ABC, abstractmethod
from enum import Enum
import os


class BugSeverity(Enum):
    """Bug severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class BugType(Enum):
    """Types of bugs that can be detected"""
    SYNTAX_ERROR = "syntax_error"
    TYPE_ERROR = "type_error"
    SCOPE_ERROR = "scope_error"
    UNDEFINED_VARIABLE = "undefined_variable"
    INFINITE_LOOP = "infinite_loop"
    NULL_REFERENCE = "null_reference"
    ARRAY_BOUNDS = "array_bounds"
    LOGIC_ERROR = "logic_error"
    PERFORMANCE_ISSUE = "performance_issue"
    MUTATION_CONFLICT = "mutation_conflict"


class Bug:
    """Represents a detected bug"""
    
    def __init__(
        self,
        bug_type: BugType,
        severity: BugSeverity,
        line: int,
        column: int,
        message: str,
        suggested_fix: Optional[str] = None,
        context: Optional[str] = None
    ):
        self.bug_type = bug_type
        self.severity = severity
        self.line = line
        self.column = column
        self.message = message
        self.suggested_fix = suggested_fix
        self.context = context
        self.id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate unique bug ID"""
        content = f"{self.bug_type.value}{self.line}{self.column}{self.message}"
        return hashlib.md5(content.encode()).hexdigest()[:8]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "type": self.bug_type.value,
            "severity": self.severity.value,
            "line": self.line,
            "column": self.column,
            "message": self.message,
            "suggested_fix": self.suggested_fix,
            "context": self.context
        }
    
    def __repr__(self) -> str:
        return f"Bug({self.bug_type.value}, {self.severity.value}, L{self.line}:C{self.column})"


class DebugProvider(ABC):
    """Abstract base for debug providers (OpenAI, Anthropic, Mock)"""
    
    @abstractmethod
    def analyze(self, code: str, error_context: Optional[str] = None) -> List[Bug]:
        """Analyze code for bugs"""
        pass
    
    @abstractmethod
    def suggest_fix(self, bug: Bug, code: str) -> str:
        """Suggest a fix for a bug"""
        pass


class MockDebugProvider(DebugProvider):
    """Mock debug provider for testing (no API key needed)"""
    
    def analyze(self, code: str, error_context: Optional[str] = None) -> List[Bug]:
        """Analyze code for bugs (mock implementation)"""
        bugs = []
        lines = code.split('\n')
        
        # Check for undefined variables
        defined_vars = set()
        used_vars = set()
        
        for i, line in enumerate(lines, 1):
            # Track variable definitions
            if re.match(r'\s*let\s+(\w+)', line):
                match = re.match(r'\s*let\s+(\w+)', line)
                defined_vars.add(match.group(1))
            
            # Track variable usage
            for match in re.finditer(r'\b([a-zA-Z_]\w*)\b', line):
                var = match.group(1)
                if var not in ['let', 'def', 'if', 'else', 'while', 'for', 'return', 'try', 'catch']:
                    used_vars.add(var)
        
        # Detect undefined variables
        undefined = used_vars - defined_vars
        for var in undefined:
            for i, line in enumerate(lines, 1):
                if var in line:
                    bugs.append(Bug(
                        bug_type=BugType.UNDEFINED_VARIABLE,
                        severity=BugSeverity.HIGH,
                        line=i,
                        column=line.index(var) + 1,
                        message=f"Undefined variable '{var}'",
                        suggested_fix=f"Define '{var}' before use: let {var} = ...",
                        context=line.strip()
                    ))
                    break
        
        # Check for infinite loops (heuristic)
        for i, line in enumerate(lines, 1):
            if 'while' in line and 'true' in line:
                if i + 5 < len(lines):
                    loop_body = '\n'.join(lines[i:min(i+5, len(lines))])
                    if not any(keyword in loop_body for keyword in ['break', 'return', 'raise']):
                        bugs.append(Bug(
                            bug_type=BugType.INFINITE_LOOP,
                            severity=BugSeverity.CRITICAL,
                            line=i,
                            column=1,
                            message="Potential infinite loop detected",
                            suggested_fix="Add a break condition or update loop variable",
                            context=line.strip()
                        ))
        
        # Check for syntax errors
        for i, line in enumerate(lines, 1):
            open_braces = line.count('{') - line.count('}')
            open_parens = line.count('(') - line.count(')')
            open_brackets = line.count('[') - line.count(']')
            
            if open_braces < 0 or open_parens < 0 or open_brackets < 0:
                bugs.append(Bug(
                    bug_type=BugType.SYNTAX_ERROR,
                    severity=BugSeverity.CRITICAL,
                    line=i,
                    column=1,
                    message="Mismatched braces/parentheses/brackets",
                    suggested_fix="Check matching opening/closing delimiters",
                    context=line.strip()
                ))
        
        # Check for mutation conflicts in morphing
        if error_context and 'morph' in error_context.lower():
            # Look for conflicting mutations
            for i, line in enumerate(lines, 1):
                if 'morph' in line:
                    bugs.append(Bug(
                        bug_type=BugType.MUTATION_CONFLICT,
                        severity=BugSeverity.MEDIUM,
                        line=i,
                        column=1,
                        message="Morphing operation may conflict with other mutations",
                        suggested_fix="Ensure morphing conditions are mutually exclusive",
                        context=line.strip()
                    ))
        
        # Check for performance issues
        for i, line in enumerate(lines, 1):
            # Nested loops
            if 'for' in line and i < len(lines):
                nested = lines[i] if i < len(lines) else ""
                if 'for' in nested:
                    bugs.append(Bug(
                        bug_type=BugType.PERFORMANCE_ISSUE,
                        severity=BugSeverity.LOW,
                        line=i,
                        column=1,
                        message="Nested loops detected - may have O(n²) complexity",
                        suggested_fix="Consider optimization or parallelization",
                        context=line.strip()
                    ))
        
        return bugs
    
    def suggest_fix(self, bug: Bug, code: str) -> str:
        """Suggest a fix for a bug"""
        if bug.suggested_fix:
            return bug.suggested_fix
        
        # Generate generic fixes
        fixes = {
            BugType.UNDEFINED_VARIABLE: f"Define the variable before use",
            BugType.INFINITE_LOOP: "Add a break condition to exit the loop",
            BugType.SYNTAX_ERROR: "Check braces, parentheses, and bracket matching",
            BugType.TYPE_ERROR: "Ensure type consistency in operations",
            BugType.SCOPE_ERROR: "Check variable scope and nesting levels",
            BugType.MUTATION_CONFLICT: "Verify morphing conditions don't conflict",
            BugType.PERFORMANCE_ISSUE: "Optimize algorithm or parallelize execution",
        }
        
        return fixes.get(bug.bug_type, "Review code logic and fix manually")


class OpenAIDebugProvider(DebugProvider):
    """OpenAI-based debug provider (requires API key)"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")
        try:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key)
        except ImportError:
            raise ImportError("openai package required for OpenAI provider")
    
    def analyze(self, code: str, error_context: Optional[str] = None) -> List[Bug]:
        """Analyze code for bugs using OpenAI"""
        prompt = f"""Analyze this Synapse code for bugs and issues:

```synapse
{code}
```

{f'Error context: {error_context}' if error_context else ''}

Return a JSON array of bugs with this format:
[
  {{
    "type": "syntax_error|type_error|undefined_variable|logic_error|performance_issue",
    "severity": "critical|high|medium|low",
    "line": <line_number>,
    "column": <column_number>,
    "message": "<description>",
    "suggested_fix": "<fix suggestion>"
  }}
]

If no bugs found, return an empty array: []
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000
            )
            
            response_text = response.choices[0].message.content
            
            # Extract JSON from response
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                bug_list = json.loads(json_match.group())
                bugs = []
                for bug_data in bug_list:
                    try:
                        bugs.append(Bug(
                            bug_type=BugType[bug_data.get('type', 'logic_error').upper()],
                            severity=BugSeverity[bug_data.get('severity', 'medium').upper()],
                            line=bug_data.get('line', 0),
                            column=bug_data.get('column', 0),
                            message=bug_data.get('message', ''),
                            suggested_fix=bug_data.get('suggested_fix')
                        ))
                    except (KeyError, ValueError):
                        continue
                return bugs
        except Exception as e:
            # Fall back to mock provider on error
            print(f"OpenAI debug failed: {e}, falling back to mock")
        
        return MockDebugProvider().analyze(code, error_context)
    
    def suggest_fix(self, bug: Bug, code: str) -> str:
        """Suggest a fix using OpenAI"""
        prompt = f"""Fix this bug in Synapse code:

Bug: {bug.message}
Type: {bug.bug_type.value}
Line: {bug.line}
Context: {bug.context}

Code:
```synapse
{code}
```

Provide only the corrected code block without explanation. Output format:
```synapse
<corrected_code>
```
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=500
            )
            
            response_text = response.choices[0].message.content
            
            # Extract code from response
            code_match = re.search(r'```synapse\s*(.*?)\s*```', response_text, re.DOTALL)
            if code_match:
                return code_match.group(1)
        except Exception as e:
            print(f"OpenAI fix failed: {e}")
        
        return bug.suggested_fix or "See bug report for details"


class AnthropicDebugProvider(DebugProvider):
    """Anthropic-based debug provider (requires API key)"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("anthropic package required for Anthropic provider")
    
    def analyze(self, code: str, error_context: Optional[str] = None) -> List[Bug]:
        """Analyze code for bugs using Anthropic"""
        prompt = f"""Analyze this Synapse code for bugs and issues:

```synapse
{code}
```

{f'Error context: {error_context}' if error_context else ''}

Return a JSON array of bugs. Return only JSON, no other text:
[
  {{
    "type": "syntax_error|type_error|undefined_variable|logic_error",
    "severity": "critical|high|medium|low",
    "line": <line_number>,
    "column": <column_number>,
    "message": "<description>",
    "suggested_fix": "<fix>"
  }}
]

Empty array if no bugs: []
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            # Extract JSON from response
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                bug_list = json.loads(json_match.group())
                bugs = []
                for bug_data in bug_list:
                    try:
                        bugs.append(Bug(
                            bug_type=BugType[bug_data.get('type', 'logic_error').upper()],
                            severity=BugSeverity[bug_data.get('severity', 'medium').upper()],
                            line=bug_data.get('line', 0),
                            column=bug_data.get('column', 0),
                            message=bug_data.get('message', ''),
                            suggested_fix=bug_data.get('suggested_fix')
                        ))
                    except (KeyError, ValueError):
                        continue
                return bugs
        except Exception as e:
            print(f"Anthropic debug failed: {e}, falling back to mock")
        
        return MockDebugProvider().analyze(code, error_context)
    
    def suggest_fix(self, bug: Bug, code: str) -> str:
        """Suggest a fix using Anthropic"""
        prompt = f"""Fix this bug in Synapse code:

Bug: {bug.message}
Type: {bug.bug_type.value}

Code:
```synapse
{code}
```

Provide corrected code in a synapse code block:
```synapse
<corrected_code>
```
"""
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_text = response.content[0].text
            
            # Extract code from response
            code_match = re.search(r'```synapse\s*(.*?)\s*```', response_text, re.DOTALL)
            if code_match:
                return code_match.group(1)
        except Exception as e:
            print(f"Anthropic fix failed: {e}")
        
        return bug.suggested_fix or "See bug report for details"


class DebugAnalyzer:
    """
    Main debugger that analyzes code for bugs and suggests improvements.
    Integrates with morphing system and code generation.
    """
    
    def __init__(self, provider: str = "mock"):
        """
        Initialize debugger with specified provider
        
        Args:
            provider: "mock", "openai", or "anthropic"
        """
        self.provider_name = provider
        
        if provider == "mock":
            self.provider = MockDebugProvider()
        elif provider == "openai":
            self.provider = OpenAIDebugProvider()
        elif provider == "anthropic":
            self.provider = AnthropicDebugProvider()
        else:
            raise ValueError(f"Unknown provider: {provider}")
        
        self.cache: Dict[str, List[Bug]] = {}
        self.cache_enabled = True
    
    def _get_cache_key(self, code: str, error_context: Optional[str] = None) -> str:
        """Generate cache key for code analysis"""
        content = f"{code}|{error_context or ''}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def analyze(self, code: str, error_context: Optional[str] = None) -> List[Bug]:
        """
        Analyze code for bugs
        
        Args:
            code: Synapse code to analyze
            error_context: Optional error message or context
        
        Returns:
            List of detected bugs
        """
        # Check cache
        cache_key = self._get_cache_key(code, error_context)
        if self.cache_enabled and cache_key in self.cache:
            return self.cache[cache_key]
        
        # Analyze
        bugs = self.provider.analyze(code, error_context)
        
        # Cache results
        if self.cache_enabled:
            self.cache[cache_key] = bugs
        
        return bugs
    
    def suggest_fixes(self, code: str, error_context: Optional[str] = None) -> Dict[str, str]:
        """
        Analyze code and suggest fixes for all bugs
        
        Args:
            code: Synapse code to analyze
            error_context: Optional error context
        
        Returns:
            Dictionary mapping bug IDs to suggested fixes
        """
        bugs = self.analyze(code, error_context)
        fixes = {}
        
        for bug in bugs:
            fix = self.provider.suggest_fix(bug, code)
            fixes[bug.id] = fix
        
        return fixes
    
    def apply_fixes(self, code: str, error_context: Optional[str] = None) -> Tuple[str, List[Bug]]:
        """
        Analyze code and attempt to apply fixes
        
        Args:
            code: Synapse code to fix
            error_context: Optional error context
        
        Returns:
            Tuple of (fixed_code, remaining_bugs)
        """
        bugs = self.analyze(code, error_context)
        fixed_code = code
        remaining_bugs = []
        
        # Sort by line number (highest first) to preserve line numbers when editing
        bugs_by_line = sorted(bugs, key=lambda b: b.line, reverse=True)
        
        lines = fixed_code.split('\n')
        
        for bug in bugs_by_line:
            if bug.line > 0 and bug.line <= len(lines):
                # Try to apply simple fixes
                if bug.bug_type == BugType.UNDEFINED_VARIABLE and bug.suggested_fix:
                    # Insert variable definition
                    var_match = re.search(r"'(\w+)'", bug.message)
                    if var_match:
                        var_name = var_match.group(1)
                        lines.insert(bug.line - 1, f"let {var_name} = 0")
                elif bug.bug_type == BugType.SYNTAX_ERROR:
                    # Try to fix matching issues
                    line = lines[bug.line - 1]
                    open_braces = line.count('{') - line.count('}')
                    if open_braces > 0:
                        lines[bug.line - 1] += '}' * open_braces
                    remaining_bugs.append(bug)
                else:
                    remaining_bugs.append(bug)
            else:
                remaining_bugs.append(bug)
        
        fixed_code = '\n'.join(lines)
        return fixed_code, remaining_bugs
    
    def report(self, code: str, error_context: Optional[str] = None) -> str:
        """
        Generate a human-readable bug report
        
        Args:
            code: Synapse code to analyze
            error_context: Optional error context
        
        Returns:
            Formatted bug report
        """
        bugs = self.analyze(code, error_context)
        lines = code.split('\n')
        
        if not bugs:
            return "✓ No bugs detected"
        
        report = f"Found {len(bugs)} issue(s):\n\n"
        
        # Group by severity
        by_severity = {}
        for bug in bugs:
            severity = bug.severity.value
            if severity not in by_severity:
                by_severity[severity] = []
            by_severity[severity].append(bug)
        
        # Severity order
        severity_order = ["critical", "high", "medium", "low", "info"]
        
        for severity in severity_order:
            if severity in by_severity:
                report += f"[{severity.upper()}]\n"
                for bug in by_severity[severity]:
                    report += f"  Line {bug.line}: {bug.message}\n"
                    if bug.context:
                        report += f"    Context: {bug.context}\n"
                    if bug.suggested_fix:
                        report += f"    Fix: {bug.suggested_fix}\n"
                    report += "\n"
        
        return report
    
    def analyze_morphing(self, original_code: str, morphed_code: str) -> List[Bug]:
        """
        Analyze code after morphing to detect new bugs
        
        Args:
            original_code: Original code before morphing
            morphed_code: Code after morphing
        
        Returns:
            List of new bugs introduced by morphing
        """
        # Analyze both versions
        original_bugs = set(b.id for b in self.analyze(original_code))
        morphed_bugs = self.analyze(morphed_code, "Morphing operation")
        
        # Find new bugs
        new_bugs = [b for b in morphed_bugs if b.id not in original_bugs]
        return new_bugs
    
    def validate_morphing(self, original_code: str, morphed_code: str) -> Tuple[bool, List[Bug]]:
        """
        Check if morphing introduced critical bugs
        
        Args:
            original_code: Original code
            morphed_code: Morphed code
        
        Returns:
            Tuple of (is_valid, critical_bugs)
        """
        new_bugs = self.analyze_morphing(original_code, morphed_code)
        critical_bugs = [b for b in new_bugs if b.severity == BugSeverity.CRITICAL]
        
        return len(critical_bugs) == 0, critical_bugs
    
    def clear_cache(self):
        """Clear analysis cache"""
        self.cache.clear()


# Convenience functions
def debug(code: str, provider: str = "mock") -> List[Bug]:
    """Quick debug analysis"""
    analyzer = DebugAnalyzer(provider)
    return analyzer.analyze(code)


def debug_report(code: str, provider: str = "mock") -> str:
    """Quick debug report"""
    analyzer = DebugAnalyzer(provider)
    return analyzer.report(code)


def suggest_fixes(code: str, provider: str = "mock") -> Dict[str, str]:
    """Quick fix suggestions"""
    analyzer = DebugAnalyzer(provider)
    return analyzer.suggest_fixes(code)
