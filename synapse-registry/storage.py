"""
Synapse Registry - Storage Backend
Handles tarball storage and retrieval

Author: Synapse Team
License: MIT
"""

import os
import tarfile
import json
import gzip
import io
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
import hashlib

logger = logging.getLogger(__name__)


class StorageBackend(ABC):
    """Abstract base class for storage backends"""
    
    @abstractmethod
    def save_tarball(self, name: str, version: str, data: bytes) -> str:
        """Save tarball and return storage path"""
        pass
    
    @abstractmethod
    def load_tarball(self, path: str) -> bytes:
        """Load tarball data"""
        pass
    
    @abstractmethod
    def delete_tarball(self, path: str) -> None:
        """Delete tarball"""
        pass
    
    @abstractmethod
    def exists(self, path: str) -> bool:
        """Check if tarball exists"""
        pass


class LocalStorage(StorageBackend):
    """File system storage backend"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def save_tarball(self, name: str, version: str, data: bytes) -> str:
        """Save tarball to disk"""
        # Create package directory
        pkg_dir = self.base_path / name
        pkg_dir.mkdir(parents=True, exist_ok=True)
        
        # Save file
        filename = f'{name}-{version}.tar.gz'
        path = pkg_dir / filename
        
        with open(path, 'wb') as f:
            f.write(data)
        
        logger.info(f'Saved tarball: {path}')
        return str(path)
    
    def load_tarball(self, path: str) -> bytes:
        """Load tarball from disk"""
        with open(path, 'rb') as f:
            return f.read()
    
    def delete_tarball(self, path: str) -> None:
        """Delete tarball from disk"""
        p = Path(path)
        if p.exists():
            p.unlink()
            logger.info(f'Deleted tarball: {path}')
    
    def exists(self, path: str) -> bool:
        """Check if tarball exists"""
        return Path(path).exists()


class S3Storage(StorageBackend):
    """AWS S3 storage backend"""
    
    def __init__(self, bucket: str, region: str = 'us-east-1'):
        try:
            import boto3
            self.s3_client = boto3.client('s3', region_name=region)
            self.bucket = bucket
        except ImportError:
            raise RuntimeError('boto3 is required for S3 storage')
    
    def save_tarball(self, name: str, version: str, data: bytes) -> str:
        """Save tarball to S3"""
        key = f'packages/{name}/{name}-{version}.tar.gz'
        
        self.s3_client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=data,
            ContentType='application/gzip'
        )
        
        logger.info(f'Saved tarball to S3: s3://{self.bucket}/{key}')
        return f's3://{self.bucket}/{key}'
    
    def load_tarball(self, path: str) -> bytes:
        """Load tarball from S3"""
        # Parse S3 path: s3://bucket/key
        parts = path.replace('s3://', '').split('/', 1)
        bucket = parts[0]
        key = parts[1]
        
        response = self.s3_client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()
    
    def delete_tarball(self, path: str) -> None:
        """Delete tarball from S3"""
        parts = path.replace('s3://', '').split('/', 1)
        bucket = parts[0]
        key = parts[1]
        
        self.s3_client.delete_object(Bucket=bucket, Key=key)
        logger.info(f'Deleted tarball from S3: {path}')
    
    def exists(self, path: str) -> bool:
        """Check if tarball exists in S3"""
        parts = path.replace('s3://', '').split('/', 1)
        bucket = parts[0]
        key = parts[1]
        
        try:
            self.s3_client.head_object(Bucket=bucket, Key=key)
            return True
        except:
            return False


def validate_package_tarball(data: bytes) -> None:
    """Validate tarball contents and structure"""
    try:
        # Check magic number for gzip
        if data[:2] != b'\x1f\x8b':
            raise ValueError('Invalid tarball: not gzip format')
        
        # Try to open as tar
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tar:
            # Check for required synapse.json
            members = tar.getmembers()
            has_manifest = any(m.name.endswith('synapse.json') for m in members)
            
            if not has_manifest:
                raise ValueError('Package must contain synapse.json manifest')
            
            # Validate manifest
            for member in members:
                if member.name.endswith('synapse.json'):
                    f = tar.extractfile(member)
                    manifest = json.load(f)
                    
                    # Required fields
                    required = ['name', 'version', 'description']
                    for field in required:
                        if field not in manifest:
                            raise ValueError(f'synapse.json missing required field: {field}')
                    
                    # Validate name format
                    name = manifest['name'].lower()
                    if not (name and all(c.isalnum() or c in '-_' for c in name)):
                        raise ValueError('Invalid package name in synapse.json')
                    
                    # Validate version format
                    version = manifest['version']
                    import re
                    if not re.match(r'^\d+\.\d+\.\d+', version):
                        raise ValueError('Invalid version format in synapse.json')
                    
                    break
            
            # Check tarball size
            if len(data) > 100 * 1024 * 1024:  # 100MB limit
                raise ValueError('Tarball exceeds maximum size of 100MB')
    
    except tarfile.TarError as e:
        raise ValueError(f'Invalid tarball: {str(e)}')


def extract_package_manifest(data: bytes) -> dict:
    """Extract and parse synapse.json from tarball"""
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tar:
            for member in tar.getmembers():
                if member.name.endswith('synapse.json'):
                    f = tar.extractfile(member)
                    return json.load(f)
    except Exception as e:
        logger.error(f'Error extracting manifest: {e}')
    
    return {}


def create_package_tarball(
    package_dir: str,
    output_path: Optional[str] = None
) -> bytes:
    """Create tarball from package directory"""
    package_name = Path(package_dir).name
    output_path = output_path or f'{package_name}.tar.gz'
    
    with tarfile.open(output_path, 'w:gz') as tar:
        tar.add(package_dir, arcname=package_name)
    
    with open(output_path, 'rb') as f:
        data = f.read()
    
    return data


class PackageIndex:
    """In-memory package index for quick lookups"""
    
    def __init__(self):
        self.packages = {}  # name -> {versions: [], metadata: {}}
    
    def add_package(self, name: str, version: str, metadata: dict) -> None:
        """Add package version to index"""
        if name not in self.packages:
            self.packages[name] = {
                'versions': [],
                'metadata': metadata
            }
        
        if version not in self.packages[name]['versions']:
            self.packages[name]['versions'].append(version)
            # Sort versions (simplified - doesn't handle semver properly)
            self.packages[name]['versions'].sort(reverse=True)
    
    def has_version(self, name: str, version: str) -> bool:
        """Check if version exists"""
        return (
            name in self.packages and
            version in self.packages[name]['versions']
        )
    
    def get_latest_version(self, name: str) -> Optional[str]:
        """Get latest version of package"""
        if name in self.packages:
            versions = self.packages[name]['versions']
            return versions[0] if versions else None
        return None
    
    def list_versions(self, name: str) -> list:
        """List all versions of package"""
        if name in self.packages:
            return self.packages[name]['versions']
        return []
    
    def save(self, path: str) -> None:
        """Save index to file"""
        with open(path, 'w') as f:
            json.dump(self.packages, f, indent=2)
    
    def load(self, path: str) -> None:
        """Load index from file"""
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.packages = json.load(f)
