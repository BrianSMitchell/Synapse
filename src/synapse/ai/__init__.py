"""
AI integration module for Synapse.

This module provides AI-driven capabilities for code generation,
optimization, debugging, and language evolution.

Phases:
- Phase 16.1: LLM-Assisted Code Generation
- Phase 16.2: Emergent Debugging with AI
"""

from .codegen import (
    CodeGenerator,
    CodeValidator,
    LLMProvider,
    OpenAIProvider,
    AnthropicProvider,
    MockProvider,
    CodeGenCLI,
)

from .debugger import (
    DebugAnalyzer,
    Bug,
    BugType,
    BugSeverity,
    DebugProvider,
    MockDebugProvider,
    OpenAIDebugProvider,
    AnthropicDebugProvider,
    debug,
    debug_report,
    suggest_fixes,
)

__all__ = [
    # Code Generation (Phase 16.1)
    "CodeGenerator",
    "CodeValidator",
    "LLMProvider",
    "OpenAIProvider",
    "AnthropicProvider",
    "MockProvider",
    "CodeGenCLI",
    # Debugging (Phase 16.2)
    "DebugAnalyzer",
    "Bug",
    "BugType",
    "BugSeverity",
    "DebugProvider",
    "MockDebugProvider",
    "OpenAIDebugProvider",
    "AnthropicDebugProvider",
    "debug",
    "debug_report",
    "suggest_fixes",
]

__version__ = "1.1.0"
