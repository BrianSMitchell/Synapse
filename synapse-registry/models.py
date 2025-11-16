"""
Synapse Registry - Database Models
SQLAlchemy ORM models for package management

Author: Synapse Team
License: MIT
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from typing import Optional
import jwt
import os

db = SQLAlchemy()


class User(db.Model):
    """User account model"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    packages = db.relationship('Package', backref='owner', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def verify_password(self, password: str) -> bool:
        """Verify password against hash"""
        from auth import verify_password
        return verify_password(password, self.password_hash)


class Package(db.Model):
    """Package metadata model"""
    __tablename__ = 'packages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(216), unique=True, nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(255), nullable=True)
    license = db.Column(db.String(50), default='MIT')
    homepage = db.Column(db.String(512), nullable=True)
    repository = db.Column(db.String(512), nullable=True)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    versions = db.relationship('PackageVersion', backref='package', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Package {self.name}>'
    
    def get_latest_version(self) -> Optional['PackageVersion']:
        """Get latest published version"""
        return PackageVersion.query.filter_by(
            package_id=self.id
        ).order_by(PackageVersion.published_at.desc()).first()


class PackageVersion(db.Model):
    """Package version model"""
    __tablename__ = 'package_versions'
    
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'), nullable=False, index=True)
    version = db.Column(db.String(50), nullable=False)
    
    # Metadata
    checksum = db.Column(db.String(64), nullable=False)  # SHA256
    tarball_path = db.Column(db.String(512), nullable=False)
    tarball_size = db.Column(db.Integer, nullable=False)
    
    # Dependencies and keywords
    dependencies_json = db.Column(db.Text, nullable=True, default='{}')
    keywords_json = db.Column(db.Text, nullable=True, default='[]')
    
    # Statistics
    download_count = db.Column(db.Integer, default=0)
    
    # Timestamps
    published_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Unique constraint
    __table_args__ = (db.UniqueConstraint('package_id', 'version', name='uq_package_version'),)
    
    # Relationships
    downloads = db.relationship('Download', backref='package_version', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<PackageVersion {self.package.name}@{self.version}>'


class Download(db.Model):
    """Package download tracking"""
    __tablename__ = 'downloads'
    
    id = db.Column(db.Integer, primary_key=True)
    package_version_id = db.Column(db.Integer, db.ForeignKey('package_versions.id'), nullable=False, index=True)
    ip_address = db.Column(db.String(45), nullable=True)
    downloaded_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    user_agent = db.Column(db.String(512), nullable=True)
    
    def __repr__(self):
        return f'<Download {self.package_version.package.name}@{self.package_version.version}>'


class APIToken(db.Model):
    """API access tokens"""
    __tablename__ = 'api_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    token = db.Column(db.String(500), unique=True, nullable=False, index=True)
    name = db.Column(db.String(255), nullable=True)
    last_used = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationships
    user = db.relationship('User', backref='api_tokens')
    
    def __repr__(self):
        return f'<APIToken {self.name}>'


class SearchIndex(db.Model):
    """Full-text search index"""
    __tablename__ = 'search_index'
    
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'), nullable=False, index=True)
    version_id = db.Column(db.Integer, db.ForeignKey('package_versions.id'), nullable=False, index=True)
    
    # Search fields
    name = db.Column(db.String(216), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    keywords = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(255), nullable=True, index=True)
    
    # Relevance scoring
    popularity_score = db.Column(db.Float, default=0.0)  # Based on downloads
    relevance_score = db.Column(db.Float, default=0.0)   # TF-IDF or similar
    
    indexed_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    package = db.relationship('Package', backref='search_entries')
    version = db.relationship('PackageVersion', backref='search_entry')
    
    def __repr__(self):
        return f'<SearchIndex {self.name}>'
