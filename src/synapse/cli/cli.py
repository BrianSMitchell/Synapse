"""Synapse Package Manager CLI - Main Entry Point

Handles command routing and parsing for:
- synapse pkg publish <package>
- synapse pkg install <package>
- synapse pkg search <query>
- synapse pkg info <package>
- synapse pkg list
- synapse pkg login
- synapse pkg logout
- synapse pkg update <package>
"""

import argparse
import sys
import os
from typing import Optional, List, Dict, Any

from .auth import AuthManager
from .publish import PublishCommand
from .install import InstallCommand
from .search import SearchCommand
from .info import InfoCommand
from .list import ListCommand
from .config import CLIConfig


class SynapseCLI:
    """Main CLI application for Synapse package manager."""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        """Initialize the CLI application."""
        self.config = CLIConfig()
        self.auth_manager = AuthManager(self.config)
        
        # Command handlers
        self.commands = {
            'publish': PublishCommand(self.config, self.auth_manager),
            'install': InstallCommand(self.config, self.auth_manager),
            'search': SearchCommand(self.config),
            'info': InfoCommand(self.config),
            'list': ListCommand(self.config),
            'login': None,  # Special handler
            'logout': None,  # Special handler
            'update': InstallCommand(self.config, self.auth_manager),
        }
    
    def create_parser(self) -> argparse.ArgumentParser:
        """Create and configure argument parser.
        
        Returns:
            Configured ArgumentParser instance
        """
        parser = argparse.ArgumentParser(
            prog='synapse pkg',
            description='Synapse Package Manager CLI',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self._get_epilog()
        )
        
        parser.add_argument(
            '--version',
            action='version',
            version=f'%(prog)s {self.VERSION}'
        )
        
        parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Enable verbose output'
        )
        
        parser.add_argument(
            '--registry',
            type=str,
            default=os.environ.get('SYNAPSE_REGISTRY', 'https://registry.synapse.sh'),
            help='Registry URL (default: https://registry.synapse.sh)'
        )
        
        # Subcommands
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Publish command
        publish_parser = subparsers.add_parser(
            'publish',
            help='Publish a package to the registry'
        )
        publish_parser.add_argument(
            'package',
            type=str,
            help='Path to package directory or tarball'
        )
        publish_parser.add_argument(
            '--token',
            type=str,
            help='Authentication token (or use login)'
        )
        publish_parser.add_argument(
            '--force',
            action='store_true',
            help='Force publish even if version exists'
        )
        
        # Install command
        install_parser = subparsers.add_parser(
            'install',
            help='Install a package'
        )
        install_parser.add_argument(
            'packages',
            nargs='*',
            help='Package names with optional version (e.g., mylib@1.0.0)'
        )
        install_parser.add_argument(
            '--global', '-g',
            action='store_true',
            help='Install globally'
        )
        install_parser.add_argument(
            '--save', '-S',
            action='store_true',
            help='Save to synapse.json'
        )
        install_parser.add_argument(
            '--save-dev', '-D',
            action='store_true',
            help='Save as dev dependency'
        )
        
        # Update command (alias for install with existing packages)
        update_parser = subparsers.add_parser(
            'update',
            help='Update packages'
        )
        update_parser.add_argument(
            'packages',
            nargs='*',
            help='Package names to update (empty = all)'
        )
        
        # Search command
        search_parser = subparsers.add_parser(
            'search',
            help='Search for packages'
        )
        search_parser.add_argument(
            'query',
            type=str,
            help='Search query'
        )
        search_parser.add_argument(
            '--limit',
            type=int,
            default=10,
            help='Limit results (default: 10)'
        )
        search_parser.add_argument(
            '--sort',
            type=str,
            choices=['relevance', 'downloads', 'recently-updated'],
            default='relevance',
            help='Sort order'
        )
        
        # Info command
        info_parser = subparsers.add_parser(
            'info',
            help='Show package information'
        )
        info_parser.add_argument(
            'package',
            type=str,
            help='Package name'
        )
        info_parser.add_argument(
            '--version',
            type=str,
            help='Specific version (default: latest)'
        )
        
        # List command
        list_parser = subparsers.add_parser(
            'list',
            help='List installed packages'
        )
        list_parser.add_argument(
            '--global', '-g',
            action='store_true',
            help='List global packages'
        )
        list_parser.add_argument(
            '--depth',
            type=int,
            default=0,
            help='Dependency depth (0 = direct only)'
        )
        
        # Login command
        login_parser = subparsers.add_parser(
            'login',
            help='Login to the registry'
        )
        login_parser.add_argument(
            '--username', '-u',
            type=str,
            help='Username'
        )
        login_parser.add_argument(
            '--password', '-p',
            type=str,
            help='Password'
        )
        login_parser.add_argument(
            '--registry',
            type=str,
            help='Registry URL'
        )
        
        # Logout command
        logout_parser = subparsers.add_parser(
            'logout',
            help='Logout from the registry'
        )
        logout_parser.add_argument(
            '--registry',
            type=str,
            help='Registry URL'
        )
        
        return parser
    
    def run(self, args: Optional[List[str]] = None) -> int:
        """Run the CLI application.
        
        Args:
            args: Command line arguments (or sys.argv if None)
            
        Returns:
            Exit code (0 = success, non-zero = error)
        """
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)
        
        # Handle global options
        if parsed_args.verbose:
            os.environ['SYNAPSE_VERBOSE'] = '1'
        
        if hasattr(parsed_args, 'registry'):
            self.config.registry_url = parsed_args.registry
        
        # Route command
        if not parsed_args.command:
            parser.print_help()
            return 0
        
        try:
            if parsed_args.command == 'login':
                return self._handle_login(parsed_args)
            elif parsed_args.command == 'logout':
                return self._handle_logout(parsed_args)
            elif parsed_args.command in self.commands:
                command = self.commands[parsed_args.command]
                return command.execute(parsed_args)
            else:
                print(f"Unknown command: {parsed_args.command}", file=sys.stderr)
                return 1
        except KeyboardInterrupt:
            print("\nAborted by user", file=sys.stderr)
            return 130
        except Exception as e:
            if os.environ.get('SYNAPSE_VERBOSE'):
                import traceback
                traceback.print_exc()
            else:
                print(f"Error: {e}", file=sys.stderr)
            return 1
    
    def _handle_login(self, args: argparse.Namespace) -> int:
        """Handle login command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        import getpass
        
        username = args.username
        password = args.password
        
        if not username:
            username = input("Username: ")
        
        if not password:
            password = getpass.getpass("Password: ")
        
        registry = args.registry if hasattr(args, 'registry') else self.config.registry_url
        
        success = self.auth_manager.login(username, password, registry)
        
        if success:
            print(f"✓ Successfully logged in to {registry}")
            return 0
        else:
            print("✗ Login failed", file=sys.stderr)
            return 1
    
    def _handle_logout(self, args: argparse.Namespace) -> int:
        """Handle logout command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code
        """
        registry = args.registry if hasattr(args, 'registry') else self.config.registry_url
        
        success = self.auth_manager.logout(registry)
        
        if success:
            print(f"✓ Successfully logged out from {registry}")
            return 0
        else:
            print("✗ Logout failed", file=sys.stderr)
            return 1
    
    @staticmethod
    def _get_epilog() -> str:
        """Get epilog text for help.
        
        Returns:
            Epilog string
        """
        return """
Examples:
  synapse pkg publish ./mylib                # Publish local package
  synapse pkg install mylib                  # Install package
  synapse pkg install mylib@1.2.3            # Install specific version
  synapse pkg search machine-learning        # Search for packages
  synapse pkg info mylib                     # Show package info
  synapse pkg list                           # List installed packages
  synapse pkg login                          # Login to registry

For more help on a command:
  synapse pkg <command> -h

Documentation: https://docs.synapse.sh
Report issues: https://github.com/BrianSMitchell/Synapse
"""


def main() -> int:
    """Entry point for the Synapse package manager CLI.
    
    Returns:
        Exit code
    """
    cli = SynapseCLI()
    return cli.run()


if __name__ == '__main__':
    sys.exit(main())
