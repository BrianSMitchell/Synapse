# Refactoring Workflow

## Purpose
Guide systematic, safe refactoring of codebases through incremental changes with continuous validation.

## When to Use This Workflow
- Files >500 lines needing modularity
- Post-migration cleanup (e.g., database changes)
- Architectural improvements
- Technical debt reduction
- Code smell remediation requiring structural changes

## Prerequisites
Before starting, ensure:
- [ ] Working test suite exists (or will be created in Phase 2)
- [ ] Changes can be deployed incrementally
- [ ] Clear success criteria defined by user

---

## Phase 1: Assessment & Planning

### Goals
Understand current state, identify risks, establish success metrics.

### Steps

**1. Analyze Target Code**
- Scan file/module for structure, dependencies, and code smells
- Identify logical separation points (services, utilities, domain logic)
- List all dependencies (databases, APIs, external services)

**2. Define Success Criteria**
Ask user to confirm:
- Target metrics (file size, complexity, test coverage)
- Non-negotiables (performance, API compatibility)
- Timeline constraints

**3. Create Refactor Plan**
Generate markdown document with:
- Current structure (file tree/function list)
- Proposed structure (new organization)
- Migration strategy (order of operations)
- Risk assessment (breaking changes, rollback plan)

**4. Get Approval**
Present plan to user and wait for confirmation before proceeding.

### Output
`refactor-plan-[target-name].md` saved in project root or `/docs`

---

## Phase 2: Safety Net (Testing)

### Goals
Establish automated verification to catch regressions.

### Steps

**1. Audit Existing Tests**
- Check test coverage for target code
- Identify gaps in critical paths
- Note dependencies that need mocking

**2. Add Missing Tests**
Priority order:
1. **Characterization tests** - Capture current behavior exactly
2. **Integration tests** - Database/API interactions
3. **Unit tests** - Pure functions and business logic
4. **E2E tests** - Critical user flows (if applicable)

Aim for **>70% coverage** of refactor target before proceeding.

**3. Verify CI/CD**
- Ensure tests run automatically on commits
- Include linting and type checking
- Confirm all tests pass on current code

**4. Checkpoint**
Ask user: "Test suite ready. All tests passing. Proceed to refactoring?"

### Output
- Test files created/updated
- Coverage report showing baseline
- All tests passing ✅

---

## Phase 3: Incremental Execution

### Goals
Make small, verifiable changes iteratively.

### Refactoring Patterns (Apply as Needed)

**Extract Service Layer**
```typescript
// Before: Logic in route handler
app.post('/api/resource', async (req, res) => {
  const result = await db.resources.insert(req.body);
  res.json(result);
});

// After: Service layer separation
app.post('/api/resource', async (req, res) => {
  const result = await ResourceService.create(req.body);
  res.json(result);
});

Extract Utility Functions
// Before: Repeated logic
function processA() { /* calc */ }
function processB() { /* same calc */ }

// After: Shared utility
function sharedCalc() { /* calc */ }
function processA() { return sharedCalc(); }


Dependency Injection
// Before: Hard-coded dependencies
class GameService {
  private db = new Database();
}

// After: Injectable dependencies
class GameService {
  constructor(private db: IDatabase) {}
}

Per-Iteration Process

For Each Chunk:

1. Extract - Move code to new location
2. Update - Fix imports and references
3. Test - Run full test suite
4. Verify - Check metrics (line count, complexity)
5. Commit - Atomic commit with clear message

Commit Message Format:
refactor(scope): brief description

- Specific change 1
- Specific change 2
- Metrics: [old] → [new]

Part of refactor plan: [link to plan]

6. Pause - Ask user: "Chunk [X] complete. Continue to next chunk?"

Iteration Checklist
Code compiles/runs
All tests pass
No new linting errors
Metrics improved (or unchanged)
Committed with descriptive message

Handling Problems

If tests fail:
1. Analyze failure (regression vs. test needs update)
2. Fix immediately if regression
3. Update test if behavior intentionally changed
4. Revert if fix unclear - ask user for guidance

If stuck:
•  Ask user: "Need guidance on [specific issue]"
•  Propose multiple approaches
•  Wait for direction



Phase 4: Validation

Goals
Confirm refactor meets success criteria and performs well.

Steps

1. Full Verification
•  Run complete test suite
•  Check all metrics met (file size, complexity, coverage)
•  Verify no performance regression

2. Documentation Update
•  Update README if structure changed
•  Add/update code comments for complex areas
•  Document new patterns for team reference

3. Final Review
Present summary to user:

## Refactor Complete ✅

### Metrics Achieved
- File size: [before] → [after]
- Complexity: [before] → [after]  
- Test coverage: [before]% → [after]%

### Files Changed
- Created: [list]
- Modified: [list]
- Deleted: [list]

### Next Steps
- Deploy to staging for validation
- Monitor for issues
- Update team documentation

4. Get Approval for Merge
Wait for user confirmation before merging to main branch.



Phase 5: Retrospective (Optional)

Quick Review
Ask user:
•  "Did this refactor achieve your goals?"
•  "Any improvements for next refactor?"

Document lessons learned in project's refactor log.



AI Agent Guidelines

Do's ✅
•  Work incrementally (one chunk at a time)
•  Run tests after EVERY change
•  Commit frequently with clear messages
•  Ask for clarification when uncertain
•  Pause at checkpoints for user approval
•  Preserve exact behavior unless explicitly told otherwise
•  Keep code deployable at all times

Don'ts ❌
•  Don't make multiple large changes simultaneously
•  Don't skip tests "because it's simple"
•  Don't introduce new features during refactoring
•  Don't assume user intent - ask questions
•  Don't proceed if tests fail - investigate first
•  Don't ignore existing code patterns/conventions

Decision Points (Always Ask User)
1. Before starting Phase 3 execution
2. After each major chunk completion
3. When encountering unexpected issues
4. When success criteria seem unrealistic
5. Before final merge to main

Progress Tracking
After each chunk, update the refactor plan markdown:
## Progress
- [x] Phase 1: Assessment ✅
- [x] Phase 2: Testing ✅
- [x] Phase 3: Execution (3/5 chunks complete)
  - [x] Extract database layer
  - [x] Extract business logic
  - [x] Extract utilities
  - [ ] Update tests
  - [ ] Update documentation

Quick Reference: Common Refactor Scenarios

Scenario 1: Large File (>500 lines)
Strategy: Extract by domain/responsibility
1. Identify logical boundaries (services, models, utilities)
2. Extract one boundary at a time
3. Verify imports/exports after each extraction

Scenario 2: Post-Database Migration
Strategy: Isolate data access layer
1. Create service/repository layer
2. Move all DB queries to services
3. Update call sites to use services
4. Add mocks for testing

Scenario 3: High Complexity Functions
Strategy: Break down and extract
1. Identify decision points (if/switch/loops)
2. Extract sub-functions for each responsibility
3. Flatten nesting with early returns
4. Extract constants for magic values

Scenario 4: Code Duplication
Strategy: DRY principle application
1. Find duplicated patterns
2. Extract to shared utility
3. Update all call sites
4. Add tests for utility



Related Guidelines

Reference in conjunction with:
•  Code Quality Standards - Ensure refactored code meets quality criteria
•  Preventing Hardcoding - Avoid introducing new hardcoded values
•  Testing Guidelines - Proper test coverage strategies



Success Indicators

Refactor is successful when:
•  ✅ All tests pass
•  ✅ Metrics improved (or maintained)
•  ✅ Code more readable/maintainable
•  ✅ No performance regression
•  ✅ Documentation updated
•  ✅ Team understands new structure
•  ✅ Deployable to production