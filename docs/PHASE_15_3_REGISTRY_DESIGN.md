# Phase 15.3: Package Manager & Registry - Design Document

**Date:** November 16, 2025  
**Phase:** 15.3 / 35  
**Status:** 🔄 In Progress - Architecture & Implementation  

---

## Executive Summary

Phase 15.3 implements a complete package management system for Synapse, enabling users to publish, discover, and install reusable libraries. The system consists of three integrated components:

1. **Registry Server** - REST API for package storage and metadata
2. **CLI Tools** - Command-line interface for package operations
3. **Dependency Resolver** - Semantic versioning and graph resolution

---

## 1. Architecture Overview

### System Diagram

```
┌─────────────────────────────────────────────────────────┐
│              Synapse Developer                          │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ├─ synapse pkg publish
                   ├─ synapse pkg install <package>@<version>
                   └─ synapse pkg list
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│        Synapse Package CLI (package.py)                 │
│  - Argument parsing & command routing                   │
│  - Local cache management                               │
│  - Dependency resolution integration                    │
└──────────────┬───────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────┐
│     Package Registry REST API (Flask/FastAPI)           │
│  POST   /api/v1/packages                                │
│  GET    /api/v1/packages/{name}                         │
│  GET    /api/v1/packages/{name}/{version}               │
│  GET    /api/v1/search?q=...                            │
│  GET    /api/v1/packages/{name}/versions                │
└──────────────┬───────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────┐
│          Backend Services                               │
│  - PostgreSQL/SQLite Database                           │
│  - File Storage (S3 / Local FS)                         │
│  - Authentication & Rate Limiting                       │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Package Format & Metadata

### synapse.json (Package Manifest)

Every Synapse package includes a manifest file:

```json
{
  "name": "synapse-graph",
  "version": "1.2.3",
  "author": "username",
  "license": "MIT",
  "description": "Graph algorithms for Synapse",
  "keywords": ["graph", "algorithms", "networking"],
  "homepage": "https://github.com/user/synapse-graph",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/synapse-graph.git"
  },
  "main": "src/graph.syn",
  "dependencies": {
    "synapse-math": "^1.0.0",
    "synapse-agents": ">=1.2.0"
  },
  "devDependencies": {
    "synapse-test": "^1.0.0"
  },
  "scripts": {
    "test": "synapse tests/",
    "build": "synapse build ."
  }
}
```

### Package Directory Structure

```
synapse-graph/
├── synapse.json              # Package manifest
├── README.md                 # Documentation
├── src/
│   ├── graph.syn            # Main library code
│   ├── algorithms/
│   │   ├── bfs.syn
│   │   ├── dfs.syn
│   │   └── dijkstra.syn
│   └── utils/
│       └── helpers.syn
├── tests/
│   ├── test_graph.syn
│   └── test_algorithms.syn
├── examples/
│   └── shortest_path.syn
└── LICENSE
```

---

## 3. Registry API Specification

### Base URL
```
https://registry.synapse-lang.dev/api/v1
```

### Endpoints

#### 3.1 Publish Package
```
POST /packages
Content-Type: application/json

{
  "name": "synapse-graph",
  "version": "1.2.3",
  "author": "username",
  "license": "MIT",
  "description": "...",
  "tarball": "<base64-encoded-tarball>",
  "auth_token": "..."
}

Response 201:
{
  "success": true,
  "package": {
    "id": "pkg_abc123",
    "name": "synapse-graph",
    "version": "1.2.3",
    "published_at": "2025-11-16T10:00:00Z",
    "url": "https://registry.synapse-lang.dev/packages/synapse-graph/1.2.3"
  }
}
```

#### 3.2 Get Package Metadata
```
GET /packages/{name}

Response 200:
{
  "name": "synapse-graph",
  "description": "Graph algorithms for Synapse",
  "versions": [
    {
      "version": "1.2.3",
      "published_at": "2025-11-16T10:00:00Z",
      "downloads": 1243,
      "tarball_url": "..."
    },
    {
      "version": "1.2.2",
      "published_at": "2025-11-15T14:30:00Z",
      "downloads": 856,
      "tarball_url": "..."
    }
  ],
  "downloads": {
    "total": 5432,
    "week": 234,
    "month": 1200
  }
}
```

#### 3.3 Get Specific Version
```
GET /packages/{name}/{version}

Response 200:
{
  "name": "synapse-graph",
  "version": "1.2.3",
  "description": "...",
  "author": "username",
  "license": "MIT",
  "dependencies": {
    "synapse-math": "^1.0.0"
  },
  "tarball_url": "https://registry.synapse-lang.dev/tarballs/synapse-graph-1.2.3.tar.gz",
  "published_at": "2025-11-16T10:00:00Z"
}
```

#### 3.4 Search Packages
```
GET /search?q=graph&limit=20&offset=0

Response 200:
{
  "results": [
    {
      "name": "synapse-graph",
      "version": "1.2.3",
      "description": "Graph algorithms for Synapse",
      "downloads": 5432,
      "score": 0.95
    },
    {
      "name": "synapse-graphql",
      "version": "2.0.1",
      "description": "GraphQL implementation for Synapse",
      "downloads": 1234,
      "score": 0.87
    }
  ],
  "total": 42,
  "limit": 20,
  "offset": 0
}
```

#### 3.5 List All Versions
```
GET /packages/{name}/versions

Response 200:
{
  "name": "synapse-graph",
  "versions": [
    "1.2.3",
    "1.2.2",
    "1.2.1",
    "1.2.0",
    "1.1.5"
  ]
}
```

#### 3.6 Delete Version (authenticated)
```
DELETE /packages/{name}/{version}
Authorization: Bearer <auth_token>

Response 204: No Content
```

---

## 4. Dependency Resolution

### Semantic Versioning Rules

Synapse packages follow **semver** (semantic versioning):

- **Major.Minor.Patch** (e.g., `1.2.3`)
- Version constraints:
  - `^1.2.3` → `>=1.2.3, <2.0.0` (compatible with version)
  - `~1.2.3` → `>=1.2.3, <1.3.0` (patch updates)
  - `1.2.3` → exact version
  - `>=1.0.0` → minimum version
  - `>1.0.0, <2.0.0` → range

### Dependency Resolution Algorithm

```python
Algorithm: ResolveDepencies(root_package)
Input: Package manifest with dependencies
Output: Flat list of {name, version} tuples
Steps:
  1. Parse all dependency constraints
  2. For each dependency:
     a. Query registry for available versions
     b. Find all versions matching constraint
     c. Select highest matching version
     d. Recursively resolve its dependencies
  3. Detect circular dependencies → Error
  4. Detect version conflicts → Error
  5. Return flattened dependency tree
```

### Lock File (synapse.lock)

After resolution, generate deterministic lock file:

```json
{
  "lockfileVersion": 1,
  "packages": {
    "synapse-graph@1.2.3": {
      "version": "1.2.3",
      "resolved": "https://registry.synapse-lang.dev/tarballs/synapse-graph-1.2.3.tar.gz",
      "dependencies": {
        "synapse-math": "synapse-math@1.0.5"
      }
    },
    "synapse-math@1.0.5": {
      "version": "1.0.5",
      "resolved": "https://registry.synapse-lang.dev/tarballs/synapse-math-1.0.5.tar.gz",
      "dependencies": {}
    }
  }
}
```

---

## 5. Local Package Cache

### Cache Structure

```
~/.synapse/
├── cache/
│   ├── packages/
│   │   ├── synapse-graph-1.2.3.tar.gz
│   │   ├── synapse-math-1.0.5.tar.gz
│   │   └── ...
│   └── index.json          # Local package index
├── credentials.json         # Auth tokens
└── config.json             # Registry URL, proxy settings
```

### Cache Operations

- **Fetch & Cache**: Download tarball if not in cache
- **Validate**: Verify checksum (SHA256)
- **Expire**: Purge old versions (keep last N)
- **Offline Mode**: Use cache if network unavailable

---

## 6. CLI Commands

### 6.1 Publish Package
```bash
synapse pkg publish
# Reads synapse.json, validates, uploads to registry
```

### 6.2 Install Package
```bash
synapse pkg install synapse-graph@1.2.3
synapse pkg install synapse-graph  # Latest
synapse pkg install               # All from synapse.json
```

### 6.3 Update Package
```bash
synapse pkg update synapse-graph
synapse pkg update                # All packages
```

### 6.4 Uninstall Package
```bash
synapse pkg uninstall synapse-graph
```

### 6.5 List Installed
```bash
synapse pkg list
# Output:
# synapse-graph@1.2.3
# synapse-math@1.0.5
# synapse-agents@2.1.0
```

### 6.6 Search Registry
```bash
synapse pkg search graph
synapse pkg search --limit 50 "algorithms"
```

### 6.7 Show Package Info
```bash
synapse pkg info synapse-graph
synapse pkg info synapse-graph@1.2.3
```

### 6.8 Authentication
```bash
synapse pkg login
synapse pkg logout
```

---

## 7. Implementation Plan

### Phase 15.3.1: Registry Server (Week 1)

**Files:**
- `synapse-registry/app.py` - Flask REST API server
- `synapse-registry/models.py` - Database models (SQLAlchemy)
- `synapse-registry/storage.py` - File storage abstraction
- `synapse-registry/auth.py` - Token-based authentication
- `synapse-registry/search.py` - Full-text search
- `tests/test_registry_api.py` - API tests (50+ tests)

**Deliverables:**
- ✅ REST API with 6 endpoints
- ✅ PostgreSQL/SQLite support
- ✅ Package upload/download
- ✅ Full-text search
- ✅ Rate limiting
- ✅ Docker configuration

**Code Lines:** ~1,200 lines

### Phase 15.3.2: CLI Tools (Week 2)

**Files:**
- `src/synapse/cli/package.py` - Package management CLI
- `src/synapse/cli/auth.py` - Authentication helpers
- `src/synapse/cli/cache.py` - Local cache management

**Deliverables:**
- ✅ 8 CLI commands
- ✅ Progress bars for uploads/downloads
- ✅ Error handling and validation
- ✅ Configuration management

**Code Lines:** ~600 lines

### Phase 15.3.3: Dependency Resolver (Week 3)

**Files:**
- `src/synapse/resolver/semver.py` - Semantic versioning
- `src/synapse/resolver/graph.py` - Dependency graph resolution
- `src/synapse/resolver/lock.py` - Lock file generation
- `tests/test_resolver.py` - Resolver tests (30+ tests)

**Deliverables:**
- ✅ Semver constraint parsing
- ✅ Version selection algorithm
- ✅ Circular dependency detection
- ✅ Lock file generation
- ✅ Conflict resolution

**Code Lines:** ~500 lines

---

## 8. Testing Strategy

### Unit Tests
- Registry API endpoints (mock HTTP)
- Semantic version parsing
- Dependency resolution algorithms
- Cache operations

### Integration Tests
- End-to-end CLI workflows
- Registry server + CLI interaction
- Lock file generation

### Performance Tests
- Large dependency graphs (100+ packages)
- Concurrent registry requests
- Search performance

**Target:** 80+ tests, 95%+ coverage

---

## 9. Security Considerations

1. **Authentication**
   - Token-based (JWT)
   - Stored in `~/.synapse/credentials.json`
   - API rate limiting (100 req/min per IP)

2. **Package Verification**
   - SHA256 checksums
   - GPG signature validation (optional)

3. **Input Validation**
   - Package name validation (alphanumeric + hyphens)
   - Version format validation
   - Tarball size limits (100MB max)

4. **Access Control**
   - Publish: authenticated users only
   - Read: public
   - Delete: package owner only

---

## 10. Documentation

### User Documentation
- `docs/PACKAGE_MANAGER_GUIDE.md` - User guide
- `docs/PUBLISHING_GUIDE.md` - How to publish packages
- `docs/SYNAPSE_JSON_SPEC.md` - Manifest format spec

### Developer Documentation
- `synapse-registry/README.md` - Registry setup & deployment
- `src/synapse/cli/README.md` - CLI development guide
- `src/synapse/resolver/README.md` - Resolver internals

---

## 11. Deployment & Infrastructure

### Registry Server Deployment
- Docker container (Python 3.10+)
- PostgreSQL database
- S3 or local storage for tarballs
- Nginx reverse proxy
- SSL/TLS with Let's Encrypt

### Environment Variables
```bash
REGISTRY_DB_URL=postgresql://user:pass@localhost/synapse_registry
REGISTRY_STORAGE=s3://synapse-packages
REGISTRY_SECRET_KEY=...
REGISTRY_PORT=8080
```

---

## 12. Success Criteria

✅ Phase 15.3 is complete when:

1. Registry server deployed and operational
   - All 6 API endpoints functional
   - Package upload/download working
   - Search working with 100+ packages

2. CLI tools complete
   - All 8 commands implemented
   - Full error handling
   - Progress feedback

3. Dependency resolver operational
   - Resolves complex dependency graphs
   - Generates correct lock files
   - Detects conflicts

4. Test coverage
   - 80+ tests, 95%+ coverage
   - Integration tests passing

5. Documentation
   - Complete user guide
   - API documentation
   - Deployment guide

---

## 13. Timeline

| Week | Tasks | Status |
|------|-------|--------|
| **Week 1** | Registry server (API, DB, storage) | 🔄 In Progress |
| **Week 2** | CLI tools (publish, install, search) | 📋 Ready |
| **Week 3** | Dependency resolver & lock files | 📋 Ready |

**Total Effort:** 3 weeks  
**Expected Code:** 2,300+ lines  
**Expected Tests:** 80+ tests

---

## Next Steps

1. ✅ Design complete (this document)
2. 🔄 Implement Registry Server
3. Implement CLI Tools
4. Implement Dependency Resolver
5. Integration testing & documentation

---

**Document Status:** Complete - Ready for Implementation  
**Last Updated:** November 16, 2025
