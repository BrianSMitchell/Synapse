# Attrition Logging Standards

**Effective Date:** 2025-11-15
**Last Updated:** 2025-11-15
**Author:** Amp/Team
**Status:** Active

---

## Overview

This document establishes standardized logging practices for the Attrition codebase. All code should follow these standards to maintain consistency, improve debugging, and reduce terminal clutter during development.

---

## Logging Philosophy

1. **Debug logs are for developers** - Remove them before shipping (or gate them)
2. **Warn/Error logs are for all environments** - Always visible, always actionable
3. **Structured data aids debugging** - Include context, not just messages
4. **Security first** - Never log sensitive data (tokens, passwords, PII)
5. **Consistency enables discovery** - Standardized namespaces make filtering easier

---

## Log Levels & When to Use

### `debug()` - Development Information
**Visibility:** Development only (gated by environment variable or build-time)
**Purpose:** Detailed information for developers debugging code flow

**Use Cases:**
- ✅ Variable values during calculation
- ✅ Function entry/exit points
- ✅ State transitions
- ✅ Data structure contents
- ✅ API request/response payloads (non-sensitive fields)

**Example:**
```typescript
logger.debug('Building energy balance calculated', {
  produced: 150,
  consumed: 120,
  balance: 30,
  buildingKey: 'solar_array'
});
```

**Guidelines:**
- Always include contextual data
- Be verbose - developers will gate this
- Never include in production bundles

---

### `info()` - General Information
**Visibility:** All environments (may be gated by configuration)
**Purpose:** Non-critical operational events that are useful to know

**Use Cases:**
- ✅ Service initialization complete
- ✅ Important state changes
- ✅ Configuration applied
- ✅ Feature flags enabled/disabled

**Example:**
```typescript
logger.info('Game loop started', {
  tickRate: 60,
  maxConcurrentOperations: 100,
  timestamp: Date.now()
});
```

**Guidelines:**
- Use for operational awareness
- Keep messages concise
- Include metrics if relevant

---

### `warn()` - Warning Conditions
**Visibility:** All environments (always shown)
**Purpose:** Potentially problematic situations that need attention

**Use Cases:**
- ⚠️ Deprecated feature usage
- ⚠️ Performance degradation
- ⚠️ Fallback to default behavior
- ⚠️ Unusual but recoverable conditions
- ⚠️ Data validation warnings (non-fatal)

**Example:**
```typescript
logger.warn('Fallback behavior triggered', {
  reason: 'Construction capacity not available',
  empire: empireId,
  location: locationCoord,
  fallbackValue: 0
});
```

**Guidelines:**
- Should indicate something needs investigation
- Always include reason or context
- Don't spam for expected conditions

---

### `error()` - Error Conditions
**Visibility:** All environments (always shown)
**Purpose:** Recoverable errors that impact functionality

**Use Cases:**
- ❌ Failed API requests (with retry)
- ❌ Database operation failures (handled)
- ❌ Validation failures (user action)
- ❌ Resource exhaustion (temporary)
- ❌ Unexpected exceptions (caught)

**Example:**
```typescript
logger.error('Failed to fetch base stats', {
  error: error.message,
  code: error.code,
  empire: empireId,
  location: locationCoord,
  attempt: 2,
  willRetry: true
});
```

**Guidelines:**
- Include error message/code
- Include identifying context (IDs, user, etc.)
- Indicate whether retry will occur
- Don't log full error stack (unless needed for debugging)

---

### `fatal()` (Desktop only) - Fatal Errors
**Visibility:** All environments (always shown)
**Purpose:** Unrecoverable errors that crash the application

**Use Cases:**
- 💀 Critical system failure
- 💀 Unrecoverable database error
- 💀 Invalid configuration state
- 💀 Security violation detected

**Example (Desktop):**
```typescript
errorLogger.fatal('Database initialization failed - cannot recover', {
  error: initError.message,
  dataPath: app.getPath('userData'),
  timestamp: Date.now()
});
```

**Guidelines:**
- Only use for truly fatal conditions
- Include all diagnostic information
- Application should shut down after logging

---

## Logging by Package

### Server Package (`packages/server/src/`)

**Logger Import:**
```typescript
import { logger } from '@/utils/logger';
```

**Environment Variable:**
```bash
DEBUG_RESOURCES=true  # Enable debug logs
DEBUG_RESOURCES=false # Disable (default in production)
```

**Namespace Pattern:**
```typescript
const log = logger.withNamespace('ServiceName');
log.debug('message', { data });
```

**Example:**
```typescript
// In packages/server/src/services/structuresService.ts
import { logger } from '../utils/logger';

class StructuresService {
  async start(empireId: string, buildingKey: string) {
    const log = logger.withNamespace('StructuresService.start');
    
    log.debug('Starting construction', { empireId, buildingKey });
    
    try {
      // ... implementation
      log.debug('Construction validated', { 
        creditsCost, 
        estimatedMinutes: 45 
      });
    } catch (error) {
      log.error('Failed to start construction', {
        error: error.message,
        code: error.code,
        empireId,
        buildingKey
      });
      throw error;
    }
  }
}
```

**Server Logger Behavior:**
- `debug()` and `info()` - Only logged when `DEBUG_RESOURCES=true`
- `warn()` and `error()` - Always logged
- Namespace automatically prefixed: `[ServiceName]`
- Console methods patched if `initLogger()` called at startup

---

### Client Package (`packages/client/src/`)

**Logger Import:**
```typescript
import Logger from '@/services/Logger';
```

**Environment Variable:**
```
No environment variable needed. Client uses build-time detection:
- Development: Logger.debug() calls included
- Production: Logger.debug() calls compiled out (zero overhead)
```

**Namespace Pattern (new):**
```typescript
const log = Logger.withNamespace?.('ComponentName') || Logger;
log.debug('message', { component: 'ComponentName', data });
```

**Example:**
```typescript
// In packages/client/src/stores/gameStore.ts
import Logger from '@/services/Logger';

export const useGameStore = create<GameState>((set, get) => {
  const log = Logger.withNamespace?.('GameStore') || Logger;
  
  return {
    updateLocation: (coord, location) => {
      log.debug('Updating location', { coord, structure: location });
      set(state => ({
        locations: new Map(state.locations).set(coord, location),
      }));
    },
  };
});
```

**Client Logger Behavior:**
- `debug()` calls **completely stripped** in production builds
- `info()`, `warn()`, `error()` included in production
- History automatically tracked (accessible via `Logger.getHistory()`)
- No performance impact in production

---

### Desktop Package (`packages/desktop/src/`)

**Logger Import (Errors):**
```typescript
import errorLogger from '@/services/errorLoggingService';
```

**For Debug Logging:**
Use simple patterns or leverage client logger if available. Desktop error logger is for errors, not debug.

**Example:**
```typescript
// In packages/desktop/src/main.ts
import errorLogger from '@/services/errorLoggingService';

try {
  initializeApp();
  errorLogger.info('Application initialized');
} catch (error) {
  errorLogger.error('Failed to initialize application', error as Error, {
    timestamp: Date.now(),
    platform: process.platform
  });
  app.quit();
}
```

**Desktop Logger Behavior:**
- Optimized for **error logging**, not debug
- Logs to file, database, and console
- Automatically redacts sensitive data
- File rotation at 10 MB (keeps 5 files)
- `ENABLE_ERROR_SYNC=true` syncs errors to server (use cautiously)

---

## Namespace Naming Convention

Namespaces help identify log origin and enable filtering. Use one of these patterns:

### Pattern 1: Class/Service Name (Recommended for Services)
```typescript
const log = logger.withNamespace('StructuresService');
const log = logger.withNamespace('TechService');
const log = logger.withNamespace('BaseStatsService');
```

### Pattern 2: Component Name (Recommended for React Components)
```typescript
const log = Logger.withNamespace('BaseDetailHeader');
const log = Logger.withNamespace('MapCanvas');
const log = Logger.withNamespace('EmpirePanel');
```

### Pattern 3: Module Path (Recommended for Utilities)
```typescript
const log = logger.withNamespace('utils:resourceCalculation');
const log = logger.withNamespace('middleware:auth');
```

### Pattern 4: Feature/Domain (Recommended for Multi-File Features)
```typescript
const log = logger.withNamespace('Feature:BuildingQueue');
const log = logger.withNamespace('Feature:ResearchTree');
```

**Guidelines:**
- Keep namespace concise (1-2 words if possible)
- Use CamelCase for class/component names
- Use lowercase with colons for module paths
- Namespaces appear in logs as: `[NamespaceName] Your message`

---

## Structured Data Best Practices

### ✅ DO: Include Relevant Context

```typescript
// Good: Includes context for debugging
logger.debug('Calculating energy balance', {
  produced: 150,
  consumed: 120,
  balance: 30,
  buildings: ['solar_array', 'nuclear_plant'],
  planetType: 'desert'
});
```

### ❌ DON'T: Dump Entire Objects

```typescript
// Bad: Too much data, hard to parse
logger.debug('Building object:', { building });

// Good: Specific fields only
logger.debug('Building updated', {
  buildingId: building.id,
  level: building.level,
  isActive: building.is_active,
  constructionTime: building.construction_completed
});
```

### ❌ DON'T: Log Sensitive Data

```typescript
// Bad: Logs passwords and tokens
logger.info('User authenticated', { 
  email: user.email,
  password: user.password,
  token: authToken
});

// Good: Safe user identification
logger.info('User authenticated', {
  userId: user.id,
  email: user.email
  // NO: password, token, sessionSecret, etc.
});
```

### ✅ DO: Use Consistent Field Names

```typescript
// Consistent: Makes logs searchable
logger.debug('Processing empire', { empireId, userId, status });
logger.debug('Building started', { empireId, locationCoord, buildingKey });

// Inconsistent: Hard to filter
logger.debug('Processing', { id: empire.id, user: user.id });
logger.debug('Building', { empire, location, building });
```

---

## Common Scenarios

### Scenario 1: Calculation or Computation

```typescript
const log = logger.withNamespace('CapacityCalculation');

log.debug('Starting capacity calculation', {
  empireId,
  locationCoord,
  buildingCount: buildings.length
});

const result = calculateCapacity(buildings);

log.debug('Capacity calculation complete', {
  construction: result.construction,
  population: result.population,
  area: result.area,
  processTimeMs: Date.now() - startTime
});
```

### Scenario 2: Service Method with Validation

```typescript
const log = logger.withNamespace('StructuresService.start');

log.debug('Start construction requested', {
  empireId,
  locationCoord,
  buildingKey,
  creditsCost
});

// Validation checks
if (availableCredits < creditsCost) {
  log.warn('Insufficient credits', {
    required: creditsCost,
    available: availableCredits,
    shortfall: creditsCost - availableCredits
  });
  return { success: false, reason: 'INSUFFICIENT_CREDITS' };
}

log.debug('Validation passed', { 
  credits: 'OK',
  energy: 'OK',
  population: 'OK'
});
```

### Scenario 3: API Request/Response

```typescript
const log = logger.withNamespace('GameApi.fetchBaseStats');

log.debug('Fetching base stats', {
  baseCoord,
  timeout: 5000
});

try {
  const response = await fetch(`/api/bases/${baseCoord}/stats`);
  const data = await response.json();
  
  log.debug('Base stats received', {
    statusCode: response.status,
    population: data.population,
    energy: data.energy,
    area: data.area,
    responseTimeMs: Date.now() - requestTime
  });
  
  return data;
} catch (error) {
  log.error('Failed to fetch base stats', {
    error: error.message,
    code: error.code,
    baseCoord,
    willRetry: true
  });
  // Retry logic...
}
```

### Scenario 4: Error Handling with Recovery

```typescript
const log = logger.withNamespace('BuildingService.scheduleNextQueued');

try {
  // Main logic
} catch (error) {
  // Check if recoverable
  if (isTemporaryError(error)) {
    log.warn('Temporary error, will retry', {
      error: error.message,
      attempt: retryCount,
      nextRetryMs: backoffMs,
      buildingId
    });
    scheduleRetry();
  } else {
    log.error('Unrecoverable error', {
      error: error.message,
      code: error.code,
      buildingId,
      empireId,
      willShutdown: true
    });
    throw error;
  }
}
```

---

## Migration Examples

### Migration Pattern 1: Simple console.log → logger.debug

```typescript
// Before
console.log(`[StructuresService.start] key=${buildingKey} delta=${delta} produced=${produced}`);

// After
const log = logger.withNamespace('StructuresService.start');
log.debug('Energy balance calculated', {
  key: buildingKey,
  delta,
  produced,
  consumed,
  balance,
  reserved: reservedNegative,
  projectedEnergy
});
```

### Migration Pattern 2: Conditional console.log → logger.debug

```typescript
// Before
if (process.env.DEBUG_RESOURCES === 'true') {
  console.log(`[StructuresService] idempotent existing queued for identityKey=${identityKey}`);
}

// After
const log = logger.withNamespace('StructuresService');
log.debug('Idempotent construction already queued', { identityKey });
// No if statement needed! Logger handles the gating.
```

### Migration Pattern 3: console.table → logger.debug

```typescript
// Before
console.table(buildings.map(b => ({
  id: b.id,
  type: b.type,
  level: b.level,
  isActive: b.is_active
})));

// After
const log = logger.withNamespace('BaseStructures');
log.debug('Base structures', {
  count: buildings.length,
  structures: buildings.map(b => ({
    id: b.id,
    type: b.type,
    level: b.level,
    isActive: b.is_active
  }))
});
```

### Migration Pattern 4: console.warn → logger.warn

```typescript
// Before
console.warn("[StructuresService.start] skip: missing catalogKey _id=%s", b._id?.toString?.());

// After
const log = logger.withNamespace('StructuresService.start');
log.warn('Skipping building with missing catalogKey', {
  buildingId: b._id?.toString?.()
});
```

### Migration Pattern 5: console.error → logger.error

```typescript
// Before
console.error(`[StructuresService.start] upsert failed:`, upsertError);

// After
const log = logger.withNamespace('StructuresService.start');
log.error('Failed to create building', {
  error: upsertError.message,
  code: upsertError.code,
  empireId,
  buildingKey,
  upsertDetails: {
    onConflict: 'identity_key',
    ignoreDuplicates: false
  }
});
```

---

## Production Behavior

### Server Production
```bash
# Production: DEBUG_RESOURCES not set (defaults to false)
npm run build && npm start

# Result:
# - debug() calls: NOT logged ✅
# - info() calls: NOT logged (safe to remove if development-only)
# - warn() calls: LOGGED ✅
# - error() calls: LOGGED ✅
```

### Client Production
```bash
# Production: Build-time stripping via Vite
npm run build

# Result:
# - Logger.debug() calls: Compiled out completely ✅ (0 bytes)
# - Logger.info() calls: LOGGED ✅
# - Logger.warn() calls: LOGGED ✅
# - Logger.error() calls: LOGGED ✅
```

### Desktop Production
```
errorLogger.debug() → Logged only if debug level enabled
errorLogger.info() → Logged
errorLogger.warn() → Logged
errorLogger.error() → Logged
errorLogger.fatal() → Logged + file + database
```

---

## Troubleshooting

### Problem: Debug logs appearing in production

**Server:**
```bash
# Check env var
echo $DEBUG_RESOURCES  # Should be unset or 'false'

# Or during deployment
# Ensure DEBUG_RESOURCES not set in production environment
```

**Client:**
```bash
# Build should strip them automatically
npm run build
# Check bundle size - should be smaller with debug stripped

# If still appearing:
# 1. Clear node_modules: rm -rf node_modules
# 2. Clear dist: rm -rf dist
# 3. Rebuild: npm run build
```

### Problem: Important logs not appearing

**Check:**
1. Are you using the correct logger? (server vs client vs desktop)
2. Is the namespace correct?
3. Is the log level appropriate? (debug not shown in prod)
4. Is there an error being swallowed? (add try/catch)

---

## Checklist for Code Review

When reviewing code, check for:

- [ ] Raw `console.log/table/debug/warn/error` replaced with logger
- [ ] Appropriate log level used (debug vs warn vs error)
- [ ] Namespace is descriptive and consistent
- [ ] No sensitive data logged (tokens, passwords, PII)
- [ ] Context data is specific, not entire objects
- [ ] Error logs include error message and identifying context
- [ ] Log levels follow conventions (debug = dev only, warn/error = all envs)

---

## Related Documents

- **Task List:** `/tasks/task-list-0001-centralized-logger-cleanup.md`
- **Migration Guide:** `/tasks/MIGRATION-GUIDE.md` (next)
- **Audit Report:** `/tasks/1.1-LOGGER-AUDIT-REPORT.md`

---

## Questions & Updates

**Last reviewed:** 2025-11-15
**Next review:** After Phase 3 migration complete

Have questions about logging standards? Check the audit report or migration guide, then ask the team.
