# Preventing Hardcoding & Magic Values

## Purpose
Eliminate hardcoded values to improve maintainability, configurability, and reduce duplication.

## Core Principle
**Before writing ANY literal value, ask: "Could this change? Does this exist elsewhere?"**

If the answer to either is "yes" → Don't hardcode it.

---

## Detection: What Counts as Hardcoding?

### 🔴 Always Extract (Critical)

**1. Configuration Values**
```javascript
// ❌ Bad
const apiUrl = 'https://api.example.com';
const maxRetries = 3;

// ✅ Good
const apiUrl = process.env.API_URL;
const maxRetries = config.network.maxRetries;

2. Magic Numbers

// ❌ Bad
if (users.length > 100) { ... }
timeout = 5000;

// ✅ Good
const MAX_USERS = 100;
const TIMEOUT_MS = 5000;
if (users.length > MAX_USERS) { ... }
javascript

3. Repeated Strings

// ❌ Bad
log('user-created');
log('user-created'); // Duplicated!

// ✅ Good
const EVENT_USER_CREATED = 'user-created';
log(EVENT_USER_CREATED);
javascript

4. API Endpoints/Routes

// ❌ Bad
fetch('/api/users');
fetch('/api/users'); // Duplicated!

// ✅ Good
const ENDPOINTS = {
  users: '/api/users',
  posts: '/api/posts'
};
fetch(ENDPOINTS.users);
javascript

5. Error Messages

// ❌ Bad
throw new Error('User not found');

// ✅ Good
const ERROR_MESSAGES = {
  userNotFound: 'User not found'
};
throw new Error(ERROR_MESSAGES.userNotFound);
javascript

🟡 Consider Extracting (Context-Dependent)

6. Business Logic Constants

// Depends on likelihood of change
const TAX_RATE = 0.07; // Extract if changes per region/time
const DAYS_IN_WEEK = 7; // Universal constant, can inline
javascript

7. Display Strings
// Extract if internationalization planned
const WELCOME_MESSAGE = 'Welcome!';
javascript


Prevention Strategy: 4-Step Process

Step 1: Scan Before Writing
When starting any code task, first search the codebase for:
•  Existing constants files (constants.ts, config.js, etc.)
•  Environment variables (.env, process.env)
•  Configuration files (config.json, settings.yaml)
•  Enums or type definitions

Search queries to run:
# Find existing constant files
grep -r "const.*=" src/ | grep -i "constant\|config\|enum"

# Find similar values
grep -r "specific-value-you-need"
bash

Step 2: Reuse or Create
Decision tree:
Does this value exist? → YES → Use existing reference
                      ↓ NO
                      ↓
Will it be reused? → YES → Create named constant
                   ↓ NO
                   ↓
Could it change? → YES → Use config/env
                 ↓ NO
                 ↓
               Use inline (rare!)

Step 3: Choose the Right Location

Environment Variables - For deployment/environment-specific values
// .env
API_KEY=abc123
DATABASE_URL=postgres://...

// code
const apiKey = process.env.API_KEY;
javascript

Config Files - For application settings
// config/app.config.ts
export const appConfig = {
  pagination: {
    defaultPageSize: 20,
    maxPageSize: 100
  }
};
javascript

Constants Files - For business logic constants
// constants/user.constants.ts
export const USER_ROLES = {
  ADMIN: 'admin',
  USER: 'user'
} as const;

export const MAX_USERNAME_LENGTH = 50;
javascript

Enums - For related sets of values
// types/status.enum.ts
export enum OrderStatus {
  PENDING = 'pending',
  PROCESSING = 'processing',
  COMPLETED = 'completed'
}
typescript

Step 4: Document and Justify
When creating new constants, add context:
// ✅ Good - Explains why and source
/**
 * Maximum file upload size in bytes (5MB).
 * Based on AWS S3 multipart upload requirements.
 * See: https://docs.aws.amazon.com/...
 */
export const MAX_FILE_SIZE = 5 * 1024 * 1024;
javascript


AI Agent Implementation Checklist

Before submitting any code, verify:

Pre-Code Generation
Searched codebase for existing constants/configs
Identified which values need extraction
Planned where new constants will live
Checked for duplicates across files

During Code Generation
All literal values justified (inline or extracted)
Naming follows project conventions
Constants grouped logically
Added JSDoc comments for non-obvious values

Post-Code Generation
No magic numbers in business logic
No duplicate string literals
Configuration values in appropriate location
Tests use constants (not re-hardcoding)



Common Patterns by Language/Framework

Node.js/TypeScript
// constants/app.constants.ts
export const APP_CONFIG = {
  PORT: process.env.PORT || 3000,
  ENV: process.env.NODE_ENV || 'development'
} as const;

// Use throughout app
import { APP_CONFIG } from '@/constants/app.constants';
typescript

React/Frontend
// constants/routes.constants.ts
export const ROUTES = {
  HOME: '/',
  LOGIN: '/login',
  DASHBOARD: '/dashboard'
} as const;

// Usage
<Link to={ROUTES.DASHBOARD}>Dashboard</Link>
typescript

Python/Django
# settings.py or constants.py
MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_FILE_TYPES = ['.jpg', '.png', '.pdf']

# Usage
from .constants import MAX_UPLOAD_SIZE
python

Database-Related
// Never hardcode table names or queries
// ❌ Bad
const users = await db.query('SELECT * FROM users');

// ✅ Good
const TABLES = {
  USERS: 'users',
  POSTS: 'posts'
} as const;
const users = await db.query(`SELECT * FROM ${TABLES.USERS}`);
typescript


Project Adaptation Guidelines

First Time in a Codebase?
Run this discovery process:

1. Find existing patterns:
   # Search for constant files
   find . -name "*constant*" -o -name "*config*" -o -name "*enum*"
   
   # Check environment variables
   cat .env .env.example
   
   # Look for configuration
   find . -name "*.config.*" -o -name "settings.*"
bash

2. Analyze naming conventions:
◦  UPPER_SNAKE_CASE vs camelCase vs PascalCase?
◦  File organization: /constants/, /config/, /utils/?
◦  Grouping strategy: By feature, by type, or single file?
3. Adopt existing patterns:
◦  Match the project's style
◦  Don't introduce new patterns without discussing
◦  When in doubt, ask user for preferred approach



Exceptions: When Hardcoding is OK

Acceptable Inline Values
1. Universal constants: const PI = 3.14159, const MONTHS = 12
2. Array indices: array[0], slice(1, 3)
3. Boolean literals: isActive = true
4. Null/undefined checks: if (value === null)
5. Type constraints: minLength: 1, maxLength: 255 in schemas

Test Files
// Tests can use inline values for clarity
it('should validate email', () => {
  expect(validate('test@example.com')).toBe(true);
  // ✅ OK - Test data doesn't need extraction
});
javascript


Red Flags to Watch For

🚨 Immediate Action Required
•  Same string/number appears 3+ times
•  URLs or endpoints directly in code
•  Credentials or API keys inline
•  File paths hardcoded
•  Version numbers scattered across files

Detection Commands
# Find repeated strings
grep -r '"some-string"' src/ | wc -l

# Find magic numbers in code
grep -rE '\b[0-9]{2,}\b' src/ --include="*.ts" --include="*.js"

# Find potential API keys
grep -rE '[A-Z0-9]{32,}' src/
bash


Integration with Other Rules

Apply this rule BEFORE:
•  Code Quality Standards - Hardcoding violates DRY principle
•  Refactoring Guidelines - Extract constants during refactors

Reference during:
•  PRD Task Implementation - Plan constants upfront
•  Code Reviews - Check for hardcodes before approval



Success Metrics

Code is hardcode-free when:
•  ✅ Can change config without touching code
•  ✅ No duplicate string literals
•  ✅ Magic numbers explained via constants
•  ✅ Environment-specific values in .env
•  ✅ Easy to internationalize (no English hardcoded)
•  ✅ Tests don't break when constants change