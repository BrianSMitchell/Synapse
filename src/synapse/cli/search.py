"""Search Command - Find packages in the registry

Handles:
- Query parsing
- Registry search requests
- Result formatting
- Caching
"""

import json
import requests
from typing import List, Dict, Any, Optional
import argparse
from .config import CLIConfig
from .utils import print_success, print_error, format_package_info


class SearchCommand:
    """Handles package searching."""
    
    def __init__(self, config: CLIConfig):
        """Initialize search command.
        
        Args:
            config: CLI configuration
        """
        self.config = config
    
    def execute(self, args: argparse.Namespace) -> int:
        """Execute search command.
        
        Args:
            args: Parsed arguments
            
        Returns:
            Exit code (0 = success, non-zero = error)
        """
        query = args.query
        limit = args.limit
        sort = args.sort
        
        try:
            results = self._search(query, limit, sort)
            
            if not results:
                print(f"No packages found matching '{query}'")
                return 0
            
            self._display_results(results, query)
            return 0
        
        except Exception as e:
            print_error(f"Search failed: {e}")
            return 1
    
    def _search(self, query: str, limit: int = 10, sort: str = 'relevance') -> List[Dict[str, Any]]:
        """Search registry.
        
        Args:
            query: Search query
            limit: Result limit
            sort: Sort order (relevance, downloads, recently-updated)
            
        Returns:
            List of package results
        """
        # Check cache first
        cache_key = f"search_{query}_{sort}"
        cache_file = self.config.get_cache_path(cache_key)
        
        if cache_file.exists() and not self.config.is_cache_expired(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                pass
        
        try:
            params = {
                'q': query,
                'limit': limit,
                'sort': sort
            }
            
            response = requests.get(
                f"{self.config.registry_url}/api/v1/search",
                params=params,
                timeout=self.config.connection_timeout_seconds
            )
            
            if response.status_code == 200:
                results = response.json().get('packages', [])
                
                # Cache results
                cache_file.parent.mkdir(parents=True, exist_ok=True)
                with open(cache_file, 'w') as f:
                    json.dump(results, f)
                
                return results
            
            return []
        
        except requests.RequestException:
            return []
    
    def _display_results(self, results: List[Dict[str, Any]], query: str) -> None:
        """Display search results.
        
        Args:
            results: Search results
            query: Original query
        """
        print(f"\nResults for '{query}': {len(results)} packages\n")
        
        for i, pkg in enumerate(results, 1):
            name = pkg.get('name', 'Unknown')
            version = pkg.get('latest_version', '0.0.0')
            description = pkg.get('description', 'No description')
            downloads = pkg.get('total_downloads', 0)
            author = pkg.get('author', 'Unknown')
            
            # Truncate description
            if len(description) > 60:
                description = description[:57] + '...'
            
            # Format line
            print(f"{i}. {name}@{version}")
            print(f"   {description}")
            print(f"   Author: {author} | Downloads: {downloads}")
            print()
