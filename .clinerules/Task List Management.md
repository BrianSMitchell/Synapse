Task List Management Rule

# Task List Management Rule

## Purpose
Maintain task lists as living documents that accurately reflect implementation progress and guide development.

## When This Rule Applies
- Any time working with a task list from a PRD
- During feature implementation
- When tracking progress through defined tasks
- While updating project documentation

---

## Core Principles

### 1. Task Lists Are Source of Truth
- Task list status should always reflect actual code state
- Update task list immediately after completing work
- Never let task list drift from reality

### 2. One Logical Unit at a Time
- Complete one sub-task fully before starting another
- Each sub-task should be independently completable
- Each completion should result in a commit

### 3. Test Before Mark Complete
- All tests must pass before marking task complete
- If tests fail, task is not complete
- Fix failing tests before moving to next task

### 4. Commit Atomically
- Each completed sub-task = one commit
- Each parent task completion = verification commit (if needed)
- Commit messages reference task numbers

---

## Task Status Management

### Sub-Task Lifecycle

markdown
[ ] Not Started → [🚧] In Progress → [x] Complete
                          ↓
                      [⚠️] Blocked (optional)

**Status Indicators:**
- `[ ]` - Not started
- `[🚧]` or `[>]` - Currently working on (optional marker)
- `[x]` - Complete (tests passing, code committed)
- `[⚠️]` - Blocked by dependency or issue (optional)
- `[~]` - Skipped/Deferred (document reason)

### Parent Task Completion

**Parent task marked `[x]` only when:**
1. All sub-tasks are `[x]`
2. All tests pass
3. All code committed
4. Integration verified (if applicable)

---

## Completion Protocol

### When You Complete a Sub-Task

**Required steps in order:**

1. **Verify implementation**
   - Code works as expected
   - Follows acceptance criteria
   - Meets quality standards

2. **Run tests**
   - Execute relevant test suite
   - All tests must pass
   - Fix any failures before proceeding

3. **Clean up**
   - Remove debug code/console.logs
   - Remove temporary files
   - Clean up commented-out code

4. **Stage changes**
   - `git add [files]` (prefer specific files over `.`)
   - Review staged changes (`git diff --staged`)

5. **Commit with descriptive message**
   ```bash
   git commit -m "type(scope): summary" -m "- Detail 1" -m "- Detail 2" -m "Refs: Task X.Y"

•  type: feat, fix, refactor, test, docs, chore
•  scope: Component/module affected
•  summary: What was accomplished
•  details: Key changes (use multiple -m flags)
•  refs: Link to task number and PRD
6. Update task list
◦  Mark sub-task [x]
◦  Update "Relevant Files" section if files added/modified
◦  Update progress metadata (if present)
7. Check parent task
◦  If all sibling sub-tasks [x], mark parent [x]
◦  Update task list file
◦  Commit task list update separately (optional)

When You Complete a Parent Task

Additional verification:

1. Integration check
◦  If parent task has dependencies, verify integration
◦  Run broader test suite if available
2. Review checklist
◦  All acceptance criteria met
◦  No TODO comments left
◦  Documentation updated (if required)
3. Update metadata
◦  Update completion counts
◦  Update last modified date
◦  Update status if tracked



Task Discovery & Adjustment

When You Discover New Tasks

Scenarios:
•  Implementation reveals additional work needed
•  Bug found that needs fixing
•  Refactoring opportunity identified
•  Missing edge case discovered

Protocol:
1. Pause current work
2. Document new task - Add to task list with details
3. Assess priority:
◦  Blocking current task? → Do immediately
◦  Related but not blocking? → Add as sub-task
◦  Unrelated? → Add to separate parent task
4. Get user approval if significant scope change
5. Update task estimates if timeline affected

Format for new tasks:
- [ ] X.Y [NEW] [Description of discovered task]
  - Added: [Date]
  - Reason: [Why this is needed]
  - Priority: [Critical/High/Medium/Low]
markdown

When Tasks Need Adjustment

Common adjustments:
•  Split large task into smaller ones
•  Merge related tasks
•  Reorder tasks due to dependencies
•  Skip task (document reason)
•  Defer task to later phase

Always document changes:
### Task Adjustments Log
- [Date] Split task 2.3 into 2.3a and 2.3b (too large)
- [Date] Skipped task 3.2 (covered by existing component)
- [Date] Added task 4.5 (discovered during implementation)
markdown


File Management

Relevant Files Section

Keep this section updated:
## Relevant Files

### Created
- `src/services/AuthService.ts` - Authentication business logic [Task 2.1]
- `src/services/AuthService.test.ts` - Unit tests for AuthService [Task 2.2]

### Modified
- `src/app.ts` - Registered auth routes [Task 3.1]
- `README.md` - Added authentication documentation [Task 6.1]

### Configuration
- `.env.example` - Added AUTH_SECRET placeholder [Task 1.3]
markdown

Update immediately when:
•  Creating new file
•  Modifying existing file
•  Deleting file
•  Moving/renaming file

Include:
•  File path (relative to project root)
•  Brief description of purpose/contents
•  Task number that created/modified it



Progress Tracking

Update Metadata Regularly

If task list includes progress section, update:
## Progress Tracking

**Last Updated:** [Date and time]
**Completed Tasks:** X/Y parent tasks, XX/YY sub-tasks
**Current Task:** Task X.Y - [Description]
**Estimated Completion:** [Date]
**Blockers:** [Any blockers or none]

### Recent Activity
- [Time] Completed Task 2.3 - Implemented password hashing
- [Time] Started Task 2.4 - Building login endpoint
- [Time] Discovered issue with [X], added Task 2.5
markdown


User Interaction Guidelines

When to Pause for User Approval

Always pause after:
•  Completing a sub-task (wait for "continue" or "next")
•  Discovering significant new work
•  Encountering a blocker
•  Test failures that require direction
•  Before making architectural decisions

How to pause:
✅ Completed Task 2.3: Implemented password hashing

**Changes:**
- Added bcrypt hashing to AuthService
- All tests passing (12/12)
- Committed: abc123f

**Next:** Task 2.4 - Implement login endpoint

Continue? (yes/no/review):
markdown

Don't pause for:
•  Minor file updates
•  Test file creation alongside implementation
•  Obvious next steps within same sub-task

When to Ask Questions

Ask user when:
•  Acceptance criteria unclear
•  Multiple valid implementation approaches
•  Discovered scope change
•  Technical blocker encountered
•  Existing code conflicts with task approach

Format questions clearly:
❓ Question about Task 3.2:

**Context:** Implementing user authentication endpoint

**Issue:** Existing middleware uses JWT but task specs mention sessions

**Options:**
A. Use JWT (matches existing pattern)
B. Implement sessions (matches PRD spec)
C. Support both (more complex)

Which approach should I take?
markdown


Error Handling

When Tests Fail

Protocol:

1. Stop immediately - Do not mark task complete
2. Analyze failure:
◦  Regression (broke existing functionality)?
◦  Test needs update (behavior intentionally changed)?
◦  Implementation bug?
3. Fix appropriately:
◦  Regression → Fix code
◦  Test needs update → Update test after confirming with user
◦  Implementation bug → Debug and fix
4. Re-run all tests
5. Only then mark complete

Never:
•  Skip failing tests
•  Comment out failing tests
•  Mark task complete with failing tests
•  Move to next task without resolving

When You Get Stuck

Options:

1. Document the blocker:
   - [⚠️] 3.2 Implement login endpoint
     - BLOCKED: Unclear if should use JWT or sessions
     - Question: [Describe question]
     - Waiting for: User clarification
markdown

2. Ask specific question (see above)
3. Propose alternative:
   Task 3.2 blocked. Alternative approaches:
   
   A. Skip 3.2 for now, continue with 3.3 (non-blocking)
   B. Implement temporary solution, refactor later
   C. Research [topic] and propose solution
   
   What would you prefer?
markdown


Quality Standards Integration

Apply During Task Execution

Reference these rules while working:
•  Code Quality Standards - Ensure no code smells introduced
•  Preventing Hardcoding - Extract constants as you code
•  Debugging Workflow - If bugs arise during task

Before marking any task complete:
Code meets quality standards
No hardcoded values
Tests comprehensive
Documentation updated (if required)
No console.logs or debug code
Linting passes



Commit Message Format

Template
git commit -m "type(scope): brief summary" \
  -m "- Detail point 1" \
  -m "- Detail point 2" \
  -m "- Detail point 3" \
  -m "Refs: Task X.Y from PRD-ZZZZ"
bash

Types
•  feat: New feature or functionality
•  fix: Bug fix
•  refactor: Code restructuring (no behavior change)
•  test: Adding or updating tests
•  docs: Documentation changes
•  chore: Maintenance (deps, config, etc.)
•  style: Code style/formatting only

Examples

Good:
git commit -m "feat(auth): implement password hashing" \
  -m "- Add bcrypt hashing to AuthService.hashPassword()" \
  -m "- Salt rounds set to 10" \
  -m "- Add comparePassword method for validation" \
  -m "- All tests passing (12/12)" \
  -m "Refs: Task 2.3 from PRD-0001-authentication"
bash

Poor:
git commit -m "update auth"
bash


Success Indicators

Task list management is effective when:
•  ✅ Task list status matches actual code state
•  ✅ Every commit references a task
•  ✅ Tests pass before marking tasks complete
•  ✅ Progress is visible at a glance
•  ✅ New tasks are discovered and documented
•  ✅ Blockers are clearly marked
•  ✅ File changes are tracked accurately
•  ✅ User can resume work easily from task list state



Related Guidelines

Apply in conjunction with:
•  Task Generation from PRD Workflow - Creates the initial task list
•  Code Quality Standards - Quality checks during implementation
•  Debugging Workflow - When issues arise during tasks
•  Refactoring Workflow - If tasks involve refactoring