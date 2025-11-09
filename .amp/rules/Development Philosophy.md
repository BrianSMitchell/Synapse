# Development Philosophy

## Purpose
Core principles that guide how all work is approached, regardless of specific workflow or task.

## Core Principles

### 1. Incremental Progress
**Make the smallest meaningful change at a time.**

- Break large tasks into atomic steps
- Each step should be independently verifiable
- Complete one step fully before starting the next
- Never attempt multiple substantial changes simultaneously

**Why:** Reduces risk, enables rollback, makes debugging easier

**Examples:**
- ✅ Extract one function to new file → Test → Commit
- ❌ Refactor entire module in one commit

---

### 2. Continuous Verification
**Validate after every change.**

- Run tests after each modification
- Verify behavior hasn't changed unexpectedly
- Don't assume changes work—prove it
- Use automated tests + manual spot checks

**Why:** Catch issues immediately when context is fresh

**Examples:**
- ✅ Change code → Run tests → Verify → Commit
- ❌ Make 10 changes → Run tests once → Debug for hours

---

### 3. Explicit Documentation
**Document what, why, and how with each change.**

- Commit messages explain the change and reasoning
- Update task lists to reflect current state
- Track files modified with purpose
- Leave code better documented than you found it

**Why:** Future you (and others) will need context

**Examples:**
- ✅ `feat(auth): add password hashing with bcrypt (REQ-002)`
- ❌ `git commit -m "update auth"`

---

### 4. User Checkpoints
**Pause for approval at decision points.**

- Wait for confirmation after completing sub-tasks
- Ask questions when multiple approaches exist
- Present plans before execution
- Don't assume user intent—verify it

**Why:** Keeps work aligned with user goals, prevents wasted effort

**Examples:**
- ✅ "Completed Task 2.3. Continue to 2.4?"
- ❌ Implementing 5 tasks without checkpoints

---

### 5. Quality Over Speed
**Do it right, not fast.**

- Follow code quality standards always
- Don't skip tests to save time
- Refactor incrementally rather than accumulating debt
- Fix problems properly, not with quick hacks

**Why:** Technical debt compounds; quality work goes faster long-term

**Examples:**
- ✅ Extract constants properly, even if it takes 5 extra minutes
- ❌ Hardcode values "just for now" (they'll stay forever)

---

### 6. Simplicity First
**Choose the simplest solution that works.**

- Avoid over-engineering
- Don't add flexibility "for the future"
- Prefer boring, proven patterns over clever ones
- YAGNI (You Aren't Gonna Need It)

**Why:** Simple code is maintainable code

**Examples:**
- ✅ Use existing utility function
- ❌ Build elaborate framework for one use case

---

## How These Principles Apply

### During PRD Generation
- ✅ Ask clarifying questions incrementally
- ✅ Validate understanding before generating document
- ✅ Iterate based on feedback

### During Task Generation
- ✅ Break requirements into small, actionable tasks
- ✅ Get parent task approval before sub-tasks
- ✅ Document file changes explicitly

### During Implementation (Task List Management)
- ✅ One sub-task at a time
- ✅ Test after each sub-task
- ✅ Commit with descriptive messages
- ✅ Pause for user approval

### During Refactoring
- ✅ Small chunks, verified incrementally
- ✅ Tests pass after every change
- ✅ Commit atomically
- ✅ Checkpoint after each chunk

### During Debugging
- ✅ Bottom-up layer verification
- ✅ Isolate variables (change one thing)
- ✅ Document findings
- ✅ Minimal fixes, not rewrites

---

## When to Adapt These Principles

### Exceptions (Rare)
You may deviate when:
- **Hotfix scenarios** - Speed critical, but still document
- **Prototyping** - Exploration phase, but mark as prototype
- **User explicitly requests** - "Skip tests, just show me something"

**Always mention when deviating and why.**

---

## Anti-Patterns to Avoid

- ❌ "I'll clean this up later" (no you won't)
- ❌ "Just one more thing..." (scope creep)
- ❌ "This is too small to test" (famous last words)
- ❌ "I'll document it when done" (never happens)
- ❌ "Let me try 5 things and see what works" (chaos)

---

## Success Indicators

Work aligns with these principles when:
- ✅ Each commit is small, focused, and documented
- ✅ Tests pass continuously, not just "at the end"
- ✅ You can explain what each change does and why
- ✅ User is never surprised by what you've done
- ✅ Codebase improves with each change
- ✅ Bugs are caught early, not during deployment

---

## Related Guidelines

These principles are reflected in:
- **All Workflows** - Built into execution steps
- **All Rules** - Inform how rules are applied
- **Task List Management** - Operationalizes these principles
- **Code Quality Standards** - Quality aspects of these principles