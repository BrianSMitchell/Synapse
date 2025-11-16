"""Utility Functions for CLI

Handles:
- Progress bars
- Colored output
- Formatting helpers
"""

import sys
import os
from typing import Optional, Dict, Any


class ProgressBar:
    """Simple progress bar for downloads/uploads."""
    
    def __init__(self, total: int, prefix: str = '', width: int = 50):
        """Initialize progress bar.
        
        Args:
            total: Total number of items
            prefix: Prefix text
            width: Progress bar width in characters
        """
        self.total = total
        self.prefix = prefix
        self.width = width
        self.current = 0
    
    def update(self, amount: int = 1) -> None:
        """Update progress.
        
        Args:
            amount: Amount to increment
        """
        self.current = min(self.current + amount, self.total)
        self._display()
    
    def set_total(self, new_total: int) -> None:
        """Update total.
        
        Args:
            new_total: New total value
        """
        self.total = new_total
    
    def _display(self) -> None:
        """Display progress bar."""
        if self.total == 0:
            percent = 100
        else:
            percent = int(100 * self.current / self.total)
        
        filled = int(self.width * self.current / max(self.total, 1))
        bar = '█' * filled + '░' * (self.width - filled)
        
        # Use carriage return to overwrite line
        print(f"\r{self.prefix} [{bar}] {percent}%", end='', flush=True)
    
    def finish(self) -> None:
        """Mark progress as complete."""
        self.current = self.total
        self._display()
        print()  # New line after completion


def colorize(text: str, color: str) -> str:
    """Add ANSI color codes to text.
    
    Args:
        text: Text to colorize
        color: Color name (red, green, yellow, blue, cyan, gray)
        
    Returns:
        Colored text (or original if colors disabled)
    """
    if os.environ.get('NO_COLOR') or not sys.stdout.isatty():
        return text
    
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'gray': '\033[90m',
    }
    
    reset = '\033[0m'
    color_code = colors.get(color, '')
    
    if color_code:
        return f"{color_code}{text}{reset}"
    return text


def print_success(message: str) -> None:
    """Print success message.
    
    Args:
        message: Message to print
    """
    print(colorize(message, 'green'))


def print_error(message: str) -> None:
    """Print error message.
    
    Args:
        message: Message to print
    """
    print(colorize(f"✗ {message}", 'red'), file=sys.stderr)


def print_warning(message: str) -> None:
    """Print warning message.
    
    Args:
        message: Message to print
    """
    print(colorize(f"⚠ {message}", 'yellow'))


def print_info(message: str) -> None:
    """Print info message.
    
    Args:
        message: Message to print
    """
    print(colorize(f"ℹ {message}", 'cyan'))


def format_size(bytes_: int) -> str:
    """Format byte size to human readable string.
    
    Args:
        bytes_: Size in bytes
        
    Returns:
        Formatted size string (e.g., '1.5 MB')
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_ < 1024:
            return f"{bytes_:.1f} {unit}"
        bytes_ /= 1024
    return f"{bytes_:.1f} PB"


def format_number(num: int) -> str:
    """Format number with thousands separator.
    
    Args:
        num: Number to format
        
    Returns:
        Formatted number string
    """
    return f"{num:,}"


def format_package_info(pkg: Dict[str, Any]) -> str:
    """Format package information for display.
    
    Args:
        pkg: Package dictionary
        
    Returns:
        Formatted information string
    """
    name = pkg.get('name', 'Unknown')
    version = pkg.get('version', 'Unknown')
    description = pkg.get('description', 'No description')
    
    # Truncate description
    if len(description) > 60:
        description = description[:57] + '...'
    
    return f"{name}@{version}: {description}"


def truncate(text: str, max_length: int, suffix: str = '...') -> str:
    """Truncate text to maximum length.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to append if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def format_table(headers: list, rows: list) -> str:
    """Format data as a simple table.
    
    Args:
        headers: List of header strings
        rows: List of row lists
        
    Returns:
        Formatted table string
    """
    # Calculate column widths
    widths = [len(h) for h in headers]
    
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Create separator
    separator = '+' + '+'.join(['-' * (w + 2) for w in widths]) + '+'
    
    # Create header row
    header_row = '|' + '|'.join([
        f" {h:<{w}} " for h, w in zip(headers, widths)
    ]) + '|'
    
    # Create data rows
    data_rows = []
    for row in rows:
        data_row = '|' + '|'.join([
            f" {str(cell):<{w}} " for cell, w in zip(row, widths)
        ]) + '|'
        data_rows.append(data_row)
    
    # Assemble table
    table_lines = [separator, header_row, separator] + data_rows + [separator]
    return '\n'.join(table_lines)


def prompt(message: str, default: Optional[str] = None) -> str:
    """Prompt user for input.
    
    Args:
        message: Prompt message
        default: Default value if user presses Enter
        
    Returns:
        User input or default
    """
    if default:
        prompt_text = f"{message} [{default}]: "
    else:
        prompt_text = f"{message}: "
    
    response = input(prompt_text).strip()
    return response or default or ''


def confirm(message: str, default: bool = False) -> bool:
    """Prompt user for confirmation.
    
    Args:
        message: Confirmation message
        default: Default answer if user presses Enter
        
    Returns:
        True if confirmed, False otherwise
    """
    default_text = 'Y/n' if default else 'y/N'
    response = input(f"{message} [{default_text}]: ").strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes']
