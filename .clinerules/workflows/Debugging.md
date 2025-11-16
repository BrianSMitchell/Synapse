Universal Debugging Workflow

# Systematic Debugging Workflow

## Purpose
Structured approach to identify and fix bugs efficiently by eliminating possibilities systematically rather than randomly trying solutions.

## When to Use This Workflow
- Feature not working as expected
- Intermittent failures
- "It works in X but not Y" scenarios
- Data appearing incorrect or missing
- Authentication/authorization issues
- Integration problems between layers

---

## Core Debugging Principles

### The Golden Rules
1. **Never guess** - Verify assumptions with evidence
2. **Work bottom-up** - Start at data layer, move toward UI
3. **Isolate variables** - Change one thing at a time
4. **Document findings** - Track what you've tested
5. **Compare working vs broken** - Find the difference

### Common Anti-Patterns (Avoid These)
- ❌ Making multiple changes simultaneously
- ❌ Assuming "it can't be X" without checking
- ❌ Fixing symptoms instead of root cause
- ❌ Skipping layers (jumping straight to frontend debugging)
- ❌ Not reproducing the bug reliably first

---

## Phase 1: Problem Definition (5-10 minutes)

### Goals
Clearly articulate what's broken vs. what's working.

### Steps

**1. Describe Expected vs. Actual Behavior**
```markdown
## Bug Report Template
**Expected:** [What should happen]
**Actual:** [What is happening]
**Frequency:** [Always / Sometimes / Rarely]
**Environment:** [Dev / Staging / Production]
**Recent Changes:** [What changed before bug appeared]
markdown

2. Establish Reproduction Steps
Create minimal steps to reproduce:
1. Navigate to [page]
2. Click [button]
3. Observe [incorrect behavior]

3. Identify Scope
Ask clarifying questions:
•  Does it happen for all users or specific ones?
•  All data or specific records?
•  All browsers/devices or specific ones?
•  All environments or just production/dev?

4. Find Similar Working Functionality
Identify a similar feature that DOES work - this becomes your control group.

Output
Clear problem statement and reliable reproduction steps.



Phase 2: Layer Identification (2-5 minutes)

Goals
Map which system layers are involved.

Common Application Layers
┌─────────────────────┐
│   Frontend/UI       │ ← User sees problem here
├─────────────────────┤
│   API/Routes        │ ← HTTP requests/responses
├─────────────────────┤
│   Business Logic    │ ← Services, controllers
├─────────────────────┤
│   Data Access       │ ← Database queries, ORM
├─────────────────────┤
│   Database/Storage  │ ← Raw data
└─────────────────────┘

Step: List Involved Layers
For your bug, which layers are involved?
Database/Storage
Data access (queries/ORM)
Business logic (services)
API/Routes
Authentication/Authorization
Frontend rendering
External services/APIs

Output
List of layers to verify, starting from bottom.



Phase 3: Bottom-Up Verification (15-45 minutes)

Goals
Verify each layer independently, starting from the data layer.

Layer 1: Database/Storage

Verify data exists and is correct:
-- SQL example
SELECT * FROM [table] WHERE [condition];

-- Check data quality
SELECT COUNT(*), [column] 
FROM [table] 
GROUP BY [column];
sql

# NoSQL example (MongoDB)
db.collection.find({ condition })

# Check for records
db.collection.countDocuments({ condition })
bash
Checklist:
Data exists in database
Data has expected values
Foreign keys/references valid
No NULL/undefined critical fields
Timestamps indicate recent activity

If data is wrong, stop here - Problem is data integrity/creation.



Layer 2: Data Access (Queries/ORM)

Verify queries return correct data:
// Add logging to database queries
console.log('Query:', query);
console.log('Parameters:', params);
const result = await db.query(query, params);
console.log('Result count:', result.length);
console.log('First result:', result[0]);
javascript
Common issues at this layer:
•  Incorrect WHERE clauses
•  JOINs missing required tables
•  Pagination skipping records
•  Sorting causing unexpected order
•  Case sensitivity in queries
•  Timezone conversions

Checklist:
Query syntax correct
Query returns expected number of records
Filtering logic matches requirements
No accidental duplicates/omissions

If queries return wrong data, stop here - Problem is query logic.



Layer 3: Business Logic (Services)

Verify processing logic:
// Add logging to service methods
async function processData(input) {
  console.log('Input:', input);
  
  const step1 = await transform(input);
  console.log('After transform:', step1);
  
  const step2 = await validate(step1);
  console.log('After validate:', step2);
  
  return step2;
}
javascript
Common issues at this layer:
•  Incorrect transformations
•  Failed validations
•  Permission checks failing
•  Business rules applied incorrectly
•  State mutations not persisting

Checklist:
Input data has expected format
Transformations produce correct output
Validations pass when they should
Error handling not swallowing issues
State changes persist correctly

If logic produces wrong results, stop here - Problem is business logic.



Layer 4: API/Routes

Verify HTTP layer:
# Test API directly (bypassing frontend)
curl -X GET 'http://localhost:3000/api/resource' \
  -H 'Authorization: Bearer TOKEN' \
  -H 'Content-Type: application/json'

# Or use tools like Postman, Insomnia, HTTPie
bash

// Add logging to route handlers
app.get('/api/resource', async (req, res) => {
  console.log('Headers:', req.headers);
  console.log('Query params:', req.query);
  console.log('Body:', req.body);
  
  const result = await service.getData(req.query);
  console.log('Response:', result);
  
  res.json(result);
});
javascript

Common issues at this layer:
•  Wrong HTTP method
•  Missing/incorrect headers
•  Body not parsed correctly
•  Query parameters malformed
•  Response not serialized properly
•  CORS issues

Checklist:
API endpoint accessible
Request format correct
Response status code correct (200, not 500)
Response body has expected structure
Headers included (auth, content-type)

If API returns wrong data, stop here - Problem is API layer.



Layer 5: Authentication/Authorization

Verify permissions and identity:
// Log authentication state
console.log('User:', req.user);
console.log('Token:', req.headers.authorization);
console.log('Permissions:', req.user?.permissions);
console.log('Session:', req.session);

// Verify token validity
const decoded = jwt.verify(token, secret);
console.log('Decoded token:', decoded);
javascript

Common issues at this layer:
•  Token expired/invalid
•  Wrong user context
•  Permissions not granted
•  Session not persisting
•  Cookie issues (domain/path)
•  Token not sent in request

Checklist:
User authenticated
Token valid and not expired
User has required permissions
User ID matches expected
Session data correct

If auth fails, stop here - Problem is authentication/authorization.



Layer 6: Frontend

Verify UI receives and displays data:
// Log in component/page
console.log('Props received:', props);
console.log('State:', state);
console.log('API response:', data);

// Check API calls
console.log('Fetching with:', {
  url,
  headers,
  body
});

fetch(url, options)
  .then(res => {
    console.log('Response status:', res.status);
    return res.json();
  })
  .then(data => {
    console.log('Parsed data:', data);
  });
javascript

Common issues at this layer:
•  Wrong API endpoint called
•  Headers not included (auth token)
•  Response not handled correctly
•  Conditional rendering hiding data
•  Incorrect props passed to components
•  State not updating after API call

Checklist:
API call made to correct endpoint
Request includes authentication
Response received successfully
Data stored in state correctly
Component renders with data
No conditional logic hiding elements



Phase 4: Isolation & Comparison (10-30 minutes)

Goals
Isolate the broken component and compare with working equivalent.

Technique 1: Create Minimal Reproduction

Build isolated test:
// Create standalone test file
// isolated-test.js

// Copy just the broken function
async function brokenFunction(input) {
  // ... function code
}

// Test with known inputs
const result = await brokenFunction(testInput);
console.log('Result:', result);
console.log('Expected:', expectedOutput);
javascript

Technique 2: Side-by-Side Comparison

Compare working vs broken:
## Working Feature (User Profile)
- API: GET /api/user/:id
- Returns: User object with all fields
- Auth: Token in Authorization header

## Broken Feature (User Posts)
- API: GET /api/posts/:userId
- Returns: Empty array (should have posts)
- Auth: Token in Authorization header

## DIFFERENCE FOUND:
- Working: Uses `req.user.id` from token
- Broken: Uses `req.params.userId` from URL
- Root cause: Token not being decoded properly
markdown

Technique 3: Binary Search Approach

For complex flows, bisect:
1. Add logging at midpoint of execution
2. Check if data correct at midpoint
3. If correct → problem is after midpoint
4. If wrong → problem is before midpoint
5. Repeat until narrowed to single function


Phase 5: Root Cause Analysis (5-15 minutes)

Goals
Identify the root cause, not just symptoms.

Ask "The 5 Whys"
Bug: User can't see their posts

Why? → API returns empty array
Why? → Database query returns no results  
Why? → Query uses wrong user ID
Why? → User ID from token is undefined
Why? → Token not being decoded in middleware
ROOT CAUSE: Auth middleware not applied to this route
Common Root Causes by Category

Data Issues:
•  Missing database records
•  Incorrect foreign keys
•  Data type mismatches
•  Null/undefined values

Logic Issues:
•  Off-by-one errors
•  Incorrect conditionals
•  Wrong operators (= vs ===, && vs ||)
•  Missing edge case handling

Authentication Issues:
•  Token not sent/received
•  Token expired
•  Wrong scope/permissions
•  Session not maintained

Configuration Issues:
•  Environment variables missing
•  Wrong API URLs (dev vs prod)
•  CORS misconfigured
•  Database connection issues

Timing Issues:
•  Race conditions
•  Async/await missing
•  Promises not resolved
•  State updates not reflected



Phase 6: Solution Implementation (10-60 minutes)

Goals
Fix root cause with minimal changes.

Principles

1. Minimal Viable Fix
Change only what's necessary:
// ❌ Bad - Rewriting entire function
function getBrokenFeature() {
  // 100 lines of new code...
}

// ✅ Good - Minimal change to fix issue
function getFeature() {
  // existing code...
  const userId = req.user?.id || req.params.userId; // ← Added fallback
  // existing code...
}
javascript

2. Verify Fix at Each Layer
After fixing, verify bottom-up again:
1. Database query returns correct data ✓
2. Service processes correctly ✓
3. API returns expected response ✓
4. Frontend displays correctly ✓

3. Add Tests to Prevent Regression
// test/feature.test.js
describe('User Posts', () => {
  it('should return posts for authenticated user', async () => {
    const token = generateToken({ userId: 123 });
    const response = await request(app)
      .get('/api/posts/123')
      .set('Authorization', `Bearer ${token}`);
    
    expect(response.status).toBe(200);
    expect(response.body).toHaveLength(5);
  });
});
javascript
4. Document the Fix
## Fix: User Posts Not Loading

**Root Cause:** Auth middleware not applied to /api/posts/:userId route

**Solution:** Added authMiddleware to route definition

**Files Changed:**
- routes/posts.js (added middleware)

**Testing:** Verified with authenticated requests in Postman
markdown


Phase 7: Prevention & Documentation (5-10 minutes)

Goals
Learn from the bug and prevent similar issues.

Create Bug Postmortem
## Bug Postmortem: [Feature] Not Working

**Date:** [Date discovered]
**Severity:** [Critical / High / Medium / Low]
**Time to Fix:** [Hours]

### What Happened
[Brief description]

### Root Cause
[Specific cause identified]

### How It Was Found
[Which debugging technique revealed it]

### Fix Applied
[Changes made]

### Prevention Measures
- [ ] Added test coverage for this scenario
- [ ] Updated documentation
- [ ] Added linting rule to catch similar issues
- [ ] Refactored to make issue impossible

### Lessons Learned
[What we learned from this bug]
markdown

Add Defensive Code

Prevent similar bugs:
// Add assertions
function processUser(user) {
  if (!user?.id) {
    throw new Error('User ID required');
  }
  // ... rest of function
}

// Add logging for critical paths
logger.info('Processing user', { userId: user.id, action: 'update' });

// Add validation
const schema = z.object({
  userId: z.string().uuid(),
  // ... other fields
});
javascript

Update Documentation

Add to project docs:
•  Common gotchas discovered
•  Debugging tips for this feature
•  Known edge cases
•  Testing requirements



Quick Reference: Debugging Commands

Database Inspection
-- Check record exists
SELECT * FROM [table] WHERE id = '[id]';

-- Check relationships
SELECT a.*, b.* 
FROM [table_a] a 
LEFT JOIN [table_b] b ON a.id = b.foreign_key;

-- Count records
SELECT COUNT(*) FROM [table] WHERE [condition];
sql

API Testing
# PowerShell (Windows)
Invoke-WebRequest -Uri "http://localhost:3000/api/resource" `
  -Headers @{"Authorization"="Bearer TOKEN"} `
  -Method GET

# cURL (cross-platform)
curl -H "Authorization: Bearer TOKEN" http://localhost:3000/api/resource
bash

Log Analysis
// Structured logging
logger.debug('Function entry', { input, context });
logger.info('Operation complete', { result, duration });
logger.error('Operation failed', { error, stack: error.stack });
javascript

Network Debugging
// Browser DevTools
// 1. Open Network tab
// 2. Filter by API endpoint
// 3. Check request headers, payload
// 4. Check response status, body
// 5. Look for failed requests (red)
javascript


Decision Tree: Where to Start?

Is data in database correct?
├─ NO → Fix data creation/migration
└─ YES → Do queries return correct data?
   ├─ NO → Fix query logic
   └─ YES → Does API return correct data?
      ├─ NO → Fix API/business logic
      └─ YES → Does frontend receive data?
         ├─ NO → Fix API call/auth
         └─ YES → Fix rendering logic


AI Agent Instructions for Debugging

When user reports a bug:

1. Ask for problem definition
◦  Expected vs actual behavior
◦  Reproduction steps
◦  Environment details
2. Identify layers involved
◦  Present layer diagram
◦  Ask which layers user suspects
3. Propose verification plan
◦  Bottom-up layer checks
◦  Specific commands to run
◦  Wait for user to execute and report results
4. Narrow down based on results
◦  Eliminate verified layers
◦  Focus on problematic layer
◦  Suggest isolation techniques
5. Analyze root cause
◦  Compare with working functionality
◦  Ask "5 whys" questions
◦  Identify specific line/function
6. Propose minimal fix
◦  Single targeted change
◦  Explain why it fixes root cause
◦  Wait for approval before implementing
7. Add tests and documentation
◦  Prevent regression
◦  Document for future reference

Do NOT:
•  Jump to solutions without verification
•  Make multiple changes at once
•  Assume auth is always the problem
•  Skip layer verification
•  Implement fixes without user approval



Success Metrics

Debugging is successful when:
•  ✅ Bug reproduced reliably
•  ✅ Root cause identified (not just symptoms)
•  ✅ Fix tested at all layers
•  ✅ Tests added to prevent regression
•  ✅ Similar bugs prevented through patterns learned