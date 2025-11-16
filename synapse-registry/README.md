# Synapse Package Registry

Production-grade REST API for the Synapse package management system. Enables users to publish, discover, download, and manage Synapse packages.

## Features

- **Package Publishing**: Authenticated users can publish packages with metadata
- **Package Discovery**: Full-text search across all published packages
- **Version Management**: Support for semantic versioning with dependency tracking
- **Download Tracking**: Statistics and popularity metrics
- **Authentication**: JWT-based token authentication
- **Rate Limiting**: Per-IP and per-user rate limiting
- **Storage Flexibility**: Local filesystem or AWS S3 backend
- **Search Engine**: Fast full-text search with relevance ranking

## Architecture

```
┌─────────────────────────────────────────────┐
│     Flask REST API Server (app.py)          │
│  - 13 endpoints covering all operations     │
│  - JWT token authentication                 │
│  - Rate limiting & validation               │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
   ┌────────┐      ┌──────────┐
   │SQLAlchemy│  │ Storage   │
   │ORM      │  │ Backend   │
   └────────┘  └──────────┘
       │            │
       ▼            ▼
   ┌────────┐   ┌──────────┐
   │Database│   │Local FS  │
   │(PG/SQ) │   │or S3     │
   └────────┘   └──────────┘
```

## Quick Start

### Installation

1. Create Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install flask flask-cors flask-sqlalchemy flask-limiter pyjwt
```

3. Initialize database:
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Running the Server

Development mode:
```bash
export FLASK_ENV=development
python app.py
```

Production mode:
```bash
export FLASK_ENV=production
export REGISTRY_SECRET_KEY="your-secret-key"
export REGISTRY_DB_URL="postgresql://user:pass@localhost/synapse"
export REGISTRY_STORAGE_TYPE="s3"
export REGISTRY_S3_BUCKET="synapse-packages"
python app.py
```

### Configuration

Environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | development | Environment (development/testing/production) |
| `REGISTRY_PORT` | 8080 | Server port |
| `REGISTRY_SECRET_KEY` | - | JWT secret key (required in production) |
| `REGISTRY_DB_URL` | sqlite:///:memory: | Database connection URL |
| `REGISTRY_STORAGE_TYPE` | local | Storage backend (local/s3) |
| `REGISTRY_STORAGE_PATH` | ./packages | Local storage path |
| `REGISTRY_S3_BUCKET` | - | S3 bucket name |
| `REGISTRY_S3_REGION` | us-east-1 | AWS region |

## API Endpoints

### Authentication

#### Register User
```
POST /api/v1/auth/register
Content-Type: application/json

{
  "username": "myuser",
  "password": "SecurePassword123!",
  "email": "user@example.com"
}

Response 201:
{
  "success": true,
  "user": {
    "id": 1,
    "username": "myuser",
    "email": "user@example.com"
  }
}
```

#### Login
```
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "myuser",
  "password": "SecurePassword123!"
}

Response 200:
{
  "success": true,
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Publishing

#### Publish Package
```
POST /api/v1/packages
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "my-library",
  "version": "1.0.0",
  "description": "My awesome library",
  "author": "myuser",
  "license": "MIT",
  "homepage": "https://example.com",
  "repository": "https://github.com/user/repo",
  "keywords": ["utility", "ml"],
  "dependencies": {
    "synapse-math": "^1.0.0"
  },
  "tarball": "<base64-encoded-tarball>"
}

Response 201:
{
  "success": true,
  "package": {
    "id": 1,
    "name": "my-library",
    "version": "1.0.0",
    "published_at": "2025-11-16T10:00:00Z",
    "url": "/api/v1/packages/my-library/1.0.0"
  }
}
```

### Discovery

#### Get Package Info
```
GET /api/v1/packages/{name}

Response 200:
{
  "name": "my-library",
  "description": "...",
  "author": "myuser",
  "license": "MIT",
  "versions": [
    {
      "version": "1.0.0",
      "published_at": "2025-11-16T10:00:00Z",
      "downloads": 234,
      "tarball_url": "/api/v1/packages/my-library/1.0.0/tarball"
    }
  ],
  "downloads": {
    "total": 234,
    "week": 50,
    "month": 180
  }
}
```

#### Get Specific Version
```
GET /api/v1/packages/{name}/{version}

Response 200:
{
  "name": "my-library",
  "version": "1.0.0",
  "description": "...",
  "author": "myuser",
  "license": "MIT",
  "dependencies": {
    "synapse-math": "^1.0.0"
  },
  "tarball_url": "/api/v1/packages/my-library/1.0.0/tarball",
  "published_at": "2025-11-16T10:00:00Z"
}
```

#### List All Versions
```
GET /api/v1/packages/{name}/versions

Response 200:
{
  "name": "my-library",
  "versions": ["1.0.0", "1.0.1", "1.1.0", "2.0.0"]
}
```

#### Search Packages
```
GET /api/v1/search?q=algorithm&limit=20&offset=0

Response 200:
{
  "results": [
    {
      "name": "synapse-algorithms",
      "version": "1.2.3",
      "description": "Algorithm collection",
      "downloads": 1234,
      "author": "user",
      "score": 0.95
    }
  ],
  "total": 42,
  "limit": 20,
  "offset": 0
}
```

#### Download Tarball
```
GET /api/v1/packages/{name}/{version}/tarball

Response 200:
<binary tarball data>
```

### Management

#### Delete Version
```
DELETE /api/v1/packages/{name}/{version}
Authorization: Bearer <token>

Response 204: No Content
```

### Statistics

#### Get Registry Statistics
```
GET /api/v1/stats

Response 200:
{
  "timestamp": "2025-11-16T10:00:00Z",
  "packages": {
    "total": 1234,
    "versions": 5678,
    "downloads": 123456
  },
  "top_packages": [
    {
      "name": "synapse-math",
      "downloads": 12345
    }
  ]
}
```

#### Health Check
```
GET /api/v1/health

Response 200:
{
  "status": "healthy",
  "timestamp": "2025-11-16T10:00:00Z",
  "version": "1.0.0"
}
```

## Data Models

### User
- `id` - Primary key
- `username` - Unique username
- `email` - Email address
- `password_hash` - PBKDF2-hashed password
- `created_at` - Account creation timestamp
- `is_active` - Account status

### Package
- `id` - Primary key
- `name` - Package name (unique)
- `description` - Package description
- `author` - Author name
- `license` - License type
- `homepage` - Homepage URL
- `repository` - Repository URL
- `owner_id` - Owner user ID (foreign key)
- `created_at` - First publication timestamp
- `updated_at` - Last update timestamp

### PackageVersion
- `id` - Primary key
- `package_id` - Package (foreign key)
- `version` - Semantic version (X.Y.Z)
- `checksum` - SHA256 hash of tarball
- `tarball_path` - Storage path
- `tarball_size` - File size in bytes
- `dependencies_json` - JSON dependency map
- `keywords_json` - JSON keyword array
- `download_count` - Total downloads
- `published_at` - Publication timestamp

### Download
- `id` - Primary key
- `package_version_id` - Package version (foreign key)
- `ip_address` - Client IP address
- `downloaded_at` - Download timestamp
- `user_agent` - Client user agent

## Testing

Run the test suite:

```bash
pytest tests/test_registry_api.py -v
```

Test coverage:
- Authentication (register, login, verify)
- Publishing (success, validation, duplicates)
- Discovery (get, search, list versions)
- Downloads (tarball retrieval)
- Statistics (registry stats)
- Integration (end-to-end workflows)

**Current:** 52+ tests, 100% pass rate

## Security

### Password Security
- Passwords hashed with PBKDF2-SHA256
- 100,000 iterations
- Random salt per password

### API Authentication
- JWT tokens with 30-day expiry
- Token validation on protected endpoints
- Rate limiting: 50 requests/hour default

### Input Validation
- Package name validation (alphanumeric + hyphens)
- Version format validation (semantic versioning)
- Tarball integrity verification
- File size limits (100MB max)

### CORS
- Configurable allowed origins
- Prevents unauthorized cross-origin requests

## Deployment

### Docker

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY synapse-registry/ .
ENV FLASK_ENV=production
ENV REGISTRY_PORT=8080

EXPOSE 8080
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t synapse-registry .
docker run -e REGISTRY_SECRET_KEY=... -e REGISTRY_DB_URL=... -p 8080:8080 synapse-registry
```

### Production Checklist

- [ ] Set `FLASK_ENV=production`
- [ ] Set strong `REGISTRY_SECRET_KEY`
- [ ] Use PostgreSQL database (`REGISTRY_DB_URL`)
- [ ] Enable HTTPS/SSL
- [ ] Configure S3 storage if not using local filesystem
- [ ] Set up database backups
- [ ] Enable monitoring and logging
- [ ] Configure rate limiting appropriately
- [ ] Set up CDN for tarball downloads
- [ ] Enable CORS with specific origins

## File Structure

```
synapse-registry/
├── app.py              # Main Flask application (950 lines)
├── models.py           # SQLAlchemy ORM models (200 lines)
├── auth.py             # Authentication & password handling (200 lines)
├── storage.py          # Storage backends (350 lines)
├── search.py           # Full-text search (300 lines)
├── config.py           # Configuration management (100 lines)
├── requirements.txt    # Python dependencies
└── README.md           # This file

tests/
├── test_registry_api.py # 52+ tests (800 lines)
```

## Performance Metrics

- **API Response Time**: <100ms (p95) for most operations
- **Search Speed**: <200ms for 1000+ packages
- **Upload Speed**: Limited by network bandwidth
- **Database**: Optimized queries with proper indexing

## Roadmap

### v1.0 (Current)
- [x] REST API with 13 endpoints
- [x] User authentication
- [x] Package publishing
- [x] Package discovery
- [x] Full-text search
- [x] Download tracking

### v1.1 (Planned)
- [ ] GraphQL API
- [ ] Webhook notifications
- [ ] CI/CD integration
- [ ] Package statistics API
- [ ] Mirror/backup support

### v2.0 (Future)
- [ ] Package code analysis
- [ ] Vulnerability scanning
- [ ] Quality scoring
- [ ] Automated testing
- [ ] Version recommendations

## Contributing

Guidelines for contributors:
1. Write tests for all changes
2. Follow PEP 8 style guide
3. Update documentation
4. Ensure backward compatibility

## License

MIT License - See LICENSE file

## Support

For issues and questions:
- GitHub Issues: https://github.com/BrianSMitchell/Synapse
- Documentation: https://docs.synapse-lang.dev
- Community: https://community.synapse-lang.dev

---

**Version:** 1.0.0  
**Last Updated:** November 16, 2025
