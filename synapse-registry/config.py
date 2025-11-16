"""
Synapse Registry - Configuration
Environment and application configuration

Author: Synapse Team
License: MIT
"""

import os
from pathlib import Path


class Config:
    """Base configuration"""
    
    # Flask
    SECRET_KEY = os.getenv('REGISTRY_SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = False
    TESTING = False
    
    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Upload limits
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB
    
    # Registry
    REGISTRY_PORT = int(os.getenv('REGISTRY_PORT', 8080))
    REGISTRY_HOST = os.getenv('REGISTRY_HOST', '0.0.0.0')
    
    # Storage
    STORAGE_TYPE = os.getenv('REGISTRY_STORAGE_TYPE', 'local')
    STORAGE_PATH = os.getenv('REGISTRY_STORAGE_PATH', './packages')
    
    # S3 configuration (if using S3)
    S3_BUCKET = os.getenv('REGISTRY_S3_BUCKET', '')
    S3_REGION = os.getenv('REGISTRY_S3_REGION', 'us-east-1')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'REGISTRY_DB_URL',
        'sqlite:///synapse_registry.db'
    )
    
    # Security
    CORS_ORIGINS = os.getenv('REGISTRY_CORS_ORIGINS', '*').split(',')
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_DEFAULT = "200 per day, 50 per hour"
    
    # Logging
    LOG_LEVEL = os.getenv('REGISTRY_LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('REGISTRY_LOG_FILE', 'registry.log')
    
    # Cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///synapse_registry_dev.db'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    RATELIMIT_ENABLED = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    
    # Require environment variables in production
    SECRET_KEY = os.getenv('REGISTRY_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('REGISTRY_DB_URL')
    
    if not SECRET_KEY:
        raise ValueError('REGISTRY_SECRET_KEY environment variable not set')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError('REGISTRY_DB_URL environment variable not set')


# Select configuration based on environment
ENV = os.getenv('FLASK_ENV', 'development').lower()

if ENV == 'production':
    config = ProductionConfig()
elif ENV == 'testing':
    config = TestingConfig()
else:
    config = DevelopmentConfig()


# Create storage directory if needed
if config.STORAGE_TYPE == 'local':
    Path(config.STORAGE_PATH).mkdir(parents=True, exist_ok=True)
