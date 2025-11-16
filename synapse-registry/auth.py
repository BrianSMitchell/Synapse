"""
Synapse Registry - Authentication Module
Token generation, password hashing, and auth utilities

Author: Synapse Team
License: MIT
"""

import jwt
import os
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional
from functools import wraps

SECRET_KEY = os.getenv('REGISTRY_SECRET_KEY', 'dev-secret-key')
TOKEN_EXPIRY_DAYS = 30


def hash_password(password: str) -> str:
    """Hash password using PBKDF2 with salt"""
    salt = secrets.token_hex(16)
    iterations = 100000
    hash_obj = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        iterations
    )
    return f"pbkdf2_sha256${iterations}${salt}${hash_obj.hex()}"


def verify_password(password: str, password_hash: str) -> bool:
    """Verify password against hash"""
    try:
        parts = password_hash.split('$')
        if len(parts) != 4:
            return False
        
        algorithm, iterations, salt, stored_hash = parts
        if algorithm != 'pbkdf2_sha256':
            return False
        
        iterations = int(iterations)
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            iterations
        )
        return hash_obj.hex() == stored_hash
    except (ValueError, IndexError):
        return False


def generate_token(user_id: int) -> str:
    """Generate JWT authentication token"""
    payload = {
        'user_id': user_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=TOKEN_EXPIRY_DAYS),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token: str) -> Optional[int]:
    """Verify JWT token and return user_id"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload.get('user_id')
    except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
        return None


def generate_api_key(user_id: int) -> str:
    """Generate random API key for CLI authentication"""
    prefix = f"syn_{user_id}_"
    random_part = secrets.token_urlsafe(32)
    return prefix + random_part


def validate_api_key_format(api_key: str) -> bool:
    """Validate API key format"""
    return api_key.startswith('syn_') and len(api_key) > 50


class TokenManager:
    """Manage JWT tokens and expiry"""
    
    def __init__(self, secret_key: str = SECRET_KEY):
        self.secret_key = secret_key
    
    def create_token(
        self,
        user_id: int,
        expires_in_days: int = TOKEN_EXPIRY_DAYS,
        extra_claims: dict = None
    ) -> str:
        """Create JWT token with optional extra claims"""
        payload = {
            'user_id': user_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=expires_in_days),
        }
        if extra_claims:
            payload.update(extra_claims)
        
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    
    def decode_token(self, token: str) -> Optional[dict]:
        """Decode and validate JWT token"""
        try:
            return jwt.decode(token, self.secret_key, algorithms=['HS256'])
        except jwt.InvalidTokenError:
            return None
    
    def get_user_id(self, token: str) -> Optional[int]:
        """Extract user_id from token"""
        payload = self.decode_token(token)
        return payload.get('user_id') if payload else None
    
    def is_token_expired(self, token: str) -> bool:
        """Check if token is expired"""
        payload = self.decode_token(token)
        return payload is None


class PasswordValidator:
    """Validate password strength"""
    
    MIN_LENGTH = 8
    REQUIRE_UPPERCASE = True
    REQUIRE_DIGITS = True
    REQUIRE_SPECIAL = True
    
    @classmethod
    def validate(cls, password: str) -> tuple[bool, str]:
        """Validate password and return (valid, reason)"""
        if len(password) < cls.MIN_LENGTH:
            return False, f'Password must be at least {cls.MIN_LENGTH} characters'
        
        if cls.REQUIRE_UPPERCASE and not any(c.isupper() for c in password):
            return False, 'Password must contain at least one uppercase letter'
        
        if cls.REQUIRE_DIGITS and not any(c.isdigit() for c in password):
            return False, 'Password must contain at least one digit'
        
        if cls.REQUIRE_SPECIAL and not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
            return False, 'Password must contain at least one special character'
        
        return True, 'Password is valid'


# Global token manager instance
_token_manager = TokenManager()


def get_token_manager() -> TokenManager:
    """Get global token manager instance"""
    return _token_manager
