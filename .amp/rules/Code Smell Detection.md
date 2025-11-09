# Code Quality Standards & Smell Detection

## Purpose
Maintain high code quality by proactively detecting and preventing code smells during development. Apply these standards to ALL code generation and modification tasks.

## Core Principles

### 1. Detect Before You Write
Before generating code, analyze the task for potential code smells:
- Will this create duplication?
- Does this add unnecessary complexity?
- Are we mixing concerns (business logic + infrastructure)?
- Could this be more maintainable?

### 2. Quality Gates (Apply in Order)

#### Development Phase (Immediate)
- **Avoid console.log abuse** - Use proper logging libraries
- **Limit function complexity** - Max 10-15 decision points per function
- **Separation of concerns** - Keep routes/controllers thin, move logic to services
- **Modern patterns** - Prefer async/await over callbacks/promise chains
- **Consistent patterns** - Match existing codebase conventions

#### Pre-commit Phase (Before Saving)
- **Run existing linters** - Check for eslint, prettier, or similar tools in the project
- **Verify tests pass** - Run relevant test suites
- **Self-review** - Check generated code against these principles

#### Integration Phase (After Implementation)
- **Suggest quality tooling** - Recommend linters, formatters, or quality checks if missing
- **Document patterns** - Note reusable patterns for future reference

## Common Code Smells to Detect & Fix

### 🔴 Critical (Always Fix)

**1. Excessive Logging**
```javascript
// ❌ Bad - Debug noise
console.log('step 1');
console.log('step 2'); 
console.log('step 3');
console.log('step 4');

// ✅ Good - Structured logging
logger.info('Process completed', { steps: 4, duration: 120 });

2. Mixed Concerns
// ❌ Bad - Business logic in route
app.post('/users', async (req, res) => {
  const user = await db.users.insert(req.body);
  await sendEmail(user.email);
  res.json(user);
});

// ✅ Good - Service layer separation
app.post('/users', async (req, res) => {
  const user = await UserService.create(req.body);
  res.json(user);
});

3. Legacy Async Patterns
// ❌ Bad - Promise chains
getData().then(processData).then(saveData).catch(handleError);

// ✅ Good - Modern async/await
try {
  const data = await getData();
  const processed = await processData(data);
  await saveData(processed);
} catch (error) {
  handleError(error);
}

🟡 Warning (Address When Practical)

4. High Complexity

// ❌ Bad - Deeply nested conditionals
if (a) {
  if (b) {
    if (c) {
      if (d) {
        // complex logic
      }
    }
  }
}

// ✅ Good - Early returns & flattened logic
if (!a || !b || !c || !d) return;
// simpler logic

5. Magic Numbers/Strings
// ❌ Bad - Hardcoded values
if (status === 'active' && count > 5) { ... }

// ✅ Good - Named constants
const STATUS_ACTIVE = 'active';
const MAX_RETRY_COUNT = 5;
if (status === STATUS_ACTIVE && count > MAX_RETRY_COUNT) { ... }

6. Code Duplication
// ❌ Bad - Repeated patterns
function getUser(id) { return db.users.findById(id); }
function getPost(id) { return db.posts.findById(id); }
function getComment(id) { return db.comments.findById(id); }

// ✅ Good - Generic utility
function getById(collection, id) { return db[collection].findById(id); }

AI Agent Implementation Checklist

When generating or modifying code, verify:

No excessive logging - Max 3-5 debug statements, use proper logger
Complexity check - Functions have single responsibility, <50 lines ideal
Async patterns - Using modern async/await, not callbacks
Separation verified - Business logic separate from routes/controllers
No magic values - Constants extracted and named
DRY principle - No obvious duplication
Consistent with codebase - Matches existing patterns and conventions
Linter-ready - Would pass standard linting (ESLint, Pylint, etc.)
Testable - Pure functions where possible, dependencies injectable

Project-Specific Adaptations

When working in a new codebase:

1. Scan for existing quality tools
◦  Look for .eslintrc, prettier.config, pyproject.toml, etc.
◦  Check package.json scripts for lint, format, test
◦  Review pre-commit hooks (.husky/, .git/hooks/)
2. Learn the patterns
◦  Find similar components/functions
◦  Identify logging approach (console, winston, pino, etc.)
◦  Note ID generation method (UUID, ObjectId, auto-increment, etc.)
◦  Understand service/repository patterns in use
3. Suggest improvements when appropriate
◦  If no linter exists, suggest adding one
◦  If quality issues are systemic, flag for user awareness
◦  Don't block on improvements, but document them

When to Override These Rules

You may skip these checks when:
•  User explicitly requests quick prototype/POC code
•  Working in a test/example file clearly marked as such
•  Matching deliberately simplified existing patterns for consistency
•  User provides specific instructions that conflict (always ask for clarification first)

Always mention when you're overriding quality standards and why.

Success Metrics

Good code quality means:
•  ✅ Code is readable without extensive comments
•  ✅ Functions have single, clear purposes
•  ✅ Changes are localized (touch few files)
•  ✅ Tests are easy to write
•  ✅ New developers can understand quickly
•  ✅ Bugs are caught early (linting, types, tests)

Related Rules & Workflows

Reference these rules and workflow in conjunction:
•  "Preventing Hardcoding" - For constants and configuration management
•  "Refactor Workflow" - When code smells require broader refactoring
•  "Debugging Workflow" - When code smells cause issues