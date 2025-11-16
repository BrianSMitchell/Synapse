"""Authentication Management for CLI

Handles:
- User login/logout
- Token management
- Credential storage
- Registry authentication
"""

import requests
import json
from typing import Optional, Dict, Any
from .config import CLIConfig, CredentialsManager


class AuthManager:
    """Manages authentication with the registry."""
    
    def __init__(self, config: CLIConfig):
        """Initialize auth manager.
        
        Args:
            config: CLI configuration
        """
        self.config = config
        self.credentials = CredentialsManager(config)
    
    def login(self, username: str, password: str, registry: Optional[str] = None) -> bool:
        """Login to the registry.
        
        Args:
            username: Username
            password: Password
            registry: Registry URL (or use configured)
            
        Returns:
            True if successful, False otherwise
        """
        registry = registry or self.config.registry_url
        
        try:
            # Call registry API
            response = requests.post(
                f"{registry}/api/v1/auth/login",
                json={
                    'username': username,
                    'password': password
                },
                timeout=self.config.connection_timeout_seconds
            )
            
            if response.status_code == 200:
                data = response.json()
                token = data.get('token')
                
                if token:
                    # Store token
                    self.credentials.store_token(registry, token, username)
                    return True
            
            return False
        except requests.RequestException as e:
            print(f"Connection error: {e}")
            return False
    
    def logout(self, registry: Optional[str] = None) -> bool:
        """Logout from the registry.
        
        Args:
            registry: Registry URL (or use configured)
            
        Returns:
            True if successful
        """
        registry = registry or self.config.registry_url
        return self.credentials.delete_token(registry)
    
    def register(self, username: str, password: str, email: str, 
                registry: Optional[str] = None) -> bool:
        """Register a new account.
        
        Args:
            username: Username
            password: Password
            email: Email address
            registry: Registry URL (or use configured)
            
        Returns:
            True if successful, False otherwise
        """
        registry = registry or self.config.registry_url
        
        try:
            response = requests.post(
                f"{registry}/api/v1/auth/register",
                json={
                    'username': username,
                    'password': password,
                    'email': email
                },
                timeout=self.config.connection_timeout_seconds
            )
            
            return response.status_code == 201
        except requests.RequestException as e:
            print(f"Connection error: {e}")
            return False
    
    def get_token(self, registry: Optional[str] = None) -> Optional[str]:
        """Get authentication token for registry.
        
        Args:
            registry: Registry URL (or use configured)
            
        Returns:
            Token if available, None otherwise
        """
        registry = registry or self.config.registry_url
        return self.credentials.get_token(registry)
    
    def is_authenticated(self, registry: Optional[str] = None) -> bool:
        """Check if authenticated with registry.
        
        Args:
            registry: Registry URL (or use configured)
            
        Returns:
            True if token exists, False otherwise
        """
        return self.get_token(registry) is not None
    
    def verify_token(self, registry: Optional[str] = None) -> bool:
        """Verify authentication token with registry.
        
        Args:
            registry: Registry URL (or use configured)
            
        Returns:
            True if token is valid, False otherwise
        """
        registry = registry or self.config.registry_url
        token = self.get_token(registry)
        
        if not token:
            return False
        
        try:
            response = requests.post(
                f"{registry}/api/v1/auth/verify",
                headers={'Authorization': f'Bearer {token}'},
                timeout=self.config.connection_timeout_seconds
            )
            
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def get_headers(self, registry: Optional[str] = None) -> Dict[str, str]:
        """Get HTTP headers with authentication.
        
        Args:
            registry: Registry URL (or use configured)
            
        Returns:
            Dictionary with authorization header if token exists
        """
        headers = {'Content-Type': 'application/json'}
        
        token = self.get_token(registry or self.config.registry_url)
        if token:
            headers['Authorization'] = f'Bearer {token}'
        
        return headers
