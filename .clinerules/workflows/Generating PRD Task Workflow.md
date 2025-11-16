Universal Task Generation from PRD Workflow
# Task Generation from PRD Workflow

## Purpose
Transform approved Product Requirements Documents (PRDs) into actionable, sequenced implementation task lists.

## When to Use This Workflow
- After PRD approval
- Before starting feature implementation
- When breaking down complex requirements
- For sprint planning from PRD

## Prerequisites
- [ ] Approved PRD document exists
- [ ] PRD contains functional requirements and user stories
- [ ] Access to current codebase for assessment

---

## Phase 1: PRD Analysis & Codebase Assessment

### Goals
Understand requirements and existing infrastructure before planning tasks.

### Step 1: Load and Analyze PRD

**Ask user to provide PRD:**
```markdown
Please provide the PRD file path or name:

Example: `/docs/prds/0001-prd-user-authentication.md`

PRD location: [Wait for response]
markdown

Read and extract:
•  Functional requirements
•  User stories with acceptance criteria
•  Technical considerations
•  Data requirements
•  Non-goals (to avoid scope creep)

Step 2: Assess Current Codebase

Analyze existing infrastructure:
Scanning codebase for relevant patterns...

**Checking for:**
- [ ] Similar existing features to reference
- [ ] Architectural patterns (MVC, services, repositories)
- [ ] Testing framework and conventions
- [ ] Build/deployment scripts
- [ ] Configuration management approach
- [ ] Database/ORM setup
- [ ] API structure and conventions
markdown

Search for key patterns:
# Find similar components/features
grep -r "similar-feature-name" src/

# Identify test framework
cat package.json | grep -E "jest|mocha|vitest|pytest"

# Check project structure
ls -R src/ | head -50

# Find configuration files
find . -name "*config*" -o -name "*.env*" | grep -v node_modules
bash

Step 3: Identify Technical Constraints

Document findings:
## Codebase Assessment

**Architecture Style:** [e.g., REST API, GraphQL, Microservices]
**Frontend Framework:** [e.g., React, Vue, Angular, None]
**Backend Framework:** [e.g., Express, NestJS, Django, Rails]
**Database:** [e.g., PostgreSQL, MongoDB, MySQL]
**Test Framework:** [e.g., Jest, Pytest, RSpec]
**Existing Patterns:**
- Services: [Yes/No - Location]
- Repositories: [Yes/No - Location]
- Middleware: [Yes/No - Location]
- Utilities: [Yes/No - Location]
markdown

Step 4: Map Requirements to Architecture

Create requirement-to-implementation matrix:

| Requirement | Layer Affected | Existing Code | New Code Needed |
|-------------|----------------|---------------|-----------------|
| REQ-001: User login | Auth middleware, API route | auth.middleware.ts | login.route.ts |
| REQ-002: Password validation | Utils, Service | None | validation.service.ts |

Output
Assessment document with codebase patterns and technical approach.



Phase 2: Parent Task Generation

Goals
Create high-level implementation phases.

Task Breakdown Strategy

For different feature types:

User-Facing Feature (UI + Backend):
1. Data model/schema setup
2. Backend API implementation
3. Frontend component development
4. Integration and testing
5. Documentation

Backend/API Only:
1. Data model/schema setup
2. Service layer implementation
3. API routes/endpoints
4. Middleware/validation
5. Testing and documentation

Integration Feature:
1. External API research/setup
2. Integration service layer
3. Error handling and retry logic
4. Data transformation
5. Testing and monitoring

Data Migration/Schema Change:
1. Schema design and migration scripts
2. Data transformation logic
3. Migration testing (dev/staging)
4. Rollback plan
5. Production migration

Step 1: Generate Parent Tasks

Create high-level tasks based on PRD + assessment:
## Proposed High-Level Tasks

Based on PRD analysis and codebase assessment, here are the main implementation phases:

- [ ] 1.0 Database Schema & Models
- [ ] 2.0 Backend Service Layer
- [ ] 3.0 API Endpoints & Validation
- [ ] 4.0 Frontend Components
- [ ] 5.0 Integration & Testing
- [ ] 6.0 Documentation & Deployment

**Estimated Complexity:** [Simple: 1-2 days | Medium: 3-7 days | Complex: 1-2+ weeks]

**Dependencies Identified:**
- External library: [name] (for [purpose])
- Existing service: [name] (modify for [purpose])
- New database table: [name]

Do these parent tasks accurately cover the PRD requirements?
- Type "approve" to proceed to sub-task generation
- Type "modify" to adjust parent tasks
- Type "explain [number]" for clarification on specific task

Your response: [Wait]
markdown

Step 2: Handle Feedback

If user requests modifications:
1. Adjust parent tasks based on feedback
2. Re-present for approval
3. Iterate until approved

Output
Approved parent task list with complexity estimate.



Phase 3: Sub-Task Generation

Goals
Break down each parent task into specific, actionable sub-tasks.

Sub-Task Principles

Each sub-task should:
•  Be completable in < 4 hours
•  Have clear acceptance criteria
•  Be independently testable
•  Follow existing codebase patterns
•  Not require multiple files/changes simultaneously

Sub-task template:
- [ ] X.Y [Action verb] [specific component/file] 
  Details: [What to implement, expected outcome]
  Files: [Specific files to create/modify]
  Tests: [Test requirements]

Step 1: Generate Sub-Tasks Per Parent

For each parent task, create detailed sub-tasks:
### Expanding: 1.0 Database Schema & Models

- [ ] 1.1 Create database migration for `users` table
  - Schema: id, email, password_hash, created_at, updated_at
  - Indexes: email (unique)
  - File: migrations/YYYYMMDD_create_users_table.[ext]

- [ ] 1.2 Create User model/entity
  - Fields matching schema
  - Validation rules: email format, password min length
  - File: models/User.[ext] or entities/User.[ext]
  
- [ ] 1.3 Write model unit tests
  - Test validation rules
  - Test relationships (if any)
  - File: models/User.test.[ext]

Ready for next parent task? (yes/no): [Wait]
markdown

Present sub-tasks incrementally:
•  Generate sub-tasks for one parent task
•  Wait for user approval
•  Move to next parent task
•  Allows course correction if direction is wrong

Step 2: Identify Relevant Files

As sub-tasks are generated, build file list:
## Relevant Files

### New Files to Create
- `models/User.ts` - User entity model with validation
- `models/User.test.ts` - Unit tests for User model
- `services/AuthService.ts` - Authentication business logic
- `services/AuthService.test.ts` - Unit tests for AuthService
- `routes/auth.routes.ts` - Authentication API endpoints
- `migrations/20250122_create_users_table.sql` - Database schema

### Existing Files to Modify
- `app.ts` - Register auth routes
- `config/database.ts` - Add User entity to ORM config
- `types/index.ts` - Add User type definitions

### Testing Strategy
- **Framework:** [Jest/Pytest/RSpec - detected from codebase]
- **Run command:** `[npm test / pytest / bundle exec rspec]`
- **Location:** Tests co-located with source files
markdown

Step 3: Add Task Metadata

Enhance tasks with additional context:
## Task Metadata

**Priority Labels:**
- 🔴 Critical path (blocking other tasks)
- 🟡 Important (needed for feature completion)
- 🟢 Nice-to-have (can be deferred)

**Complexity Estimates:**
- ⚡ Quick (<1 hour)
- ⏱️ Medium (1-4 hours)
- 🔨 Large (4+ hours, consider splitting)

**Dependencies:**
- Task 2.1 depends on 1.1 (needs User model)
- Task 4.1 depends on 3.2 (needs API endpoint)
markdown

Output
Complete task list with all sub-tasks, files, and metadata.



Phase 4: File Organization & Naming

Goals
Determine where to save the task list.

Step 1: Determine Location

Ask user:
Where should I save this task list?

A. Same location as PRD (e.g., `/docs/prds/tasks-[prd-name].md`)
B. Dedicated tasks directory (`/tasks/task-list-[prd-name].md`)
C. Project management directory (`/planning/[prd-name]-tasks.md`)
D. Custom location: [___________]

Your choice: [Wait]
markdown

Step 2: Determine Naming Convention

Ask user:
What naming convention should I use?

A. Match PRD name: `tasks-[prd-filename].md`
B. Feature-based: `tasks-[feature-name]-[date].md`
C. Sequential: `task-list-001.md`
D. Custom: [___________]

Your choice: [Wait]
markdown

Step 3: Generate Final Document

Combine all sections into final format:

# Task List: [Feature Name]

**Source PRD:** [link to PRD file]
**Status:** Not Started | In Progress | Complete
**Created:** [Date]
**Estimated Effort:** [X days/weeks]
**Priority:** Critical | High | Medium | Low

---

## Overview

**Summary:** [Brief description from PRD]

**Success Criteria:**
- [ ] [Criterion 1 from PRD]
- [ ] [Criterion 2 from PRD]

---

## Codebase Context

**Architecture:** [Brief description]
**Key Patterns:** [Conventions to follow]
**Test Framework:** [Name and run command]

---

## Relevant Files

### Files to Create
- `path/to/file1.ts` - [Purpose]
- `path/to/file1.test.ts` - [Test purpose]

### Files to Modify
- `path/to/existing.ts` - [What changes]

### Configuration
- `.env` - Add [ENV_VAR] for [purpose]
- `config/app.config.ts` - Update [setting]

---

## Implementation Tasks

### 1.0 Database Schema & Models 🔴 Critical

- [ ] 1.1 ⚡ Create database migration for users table
  - **Details:** Add users table with fields: id, email, password_hash, created_at, updated_at
  - **Files:** `migrations/YYYYMMDD_create_users.sql`
  - **Tests:** Migration runs without errors, rollback works
  - **Acceptance:** Table created with correct schema

- [ ] 1.2 ⏱️ Create User model/entity
  - **Details:** Implement User class with validation (email format, password min 8 chars)
  - **Files:** `models/User.ts`
  - **Tests:** `models/User.test.ts`
  - **Acceptance:** Model validates correctly, rejects invalid data

### 2.0 Backend Service Layer 🟡 Important

- [ ] 2.1 ⏱️ Implement AuthService
  - **Details:** Methods: register(email, password), login(email, password), hashPassword(password)
  - **Files:** `services/AuthService.ts`
  - **Dependencies:** Requires 1.2 (User model)
  - **Tests:** `services/AuthService.test.ts`
  - **Acceptance:** All methods work, passwords hashed securely

[... continue for all tasks ...]

---

## Testing Checklist

Before marking feature complete:

- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Edge cases tested
- [ ] Error handling verified
- [ ] Performance acceptable
- [ ] Security review done (if applicable)

**Test Command:** `[specific command for this project]`

---

## Deployment Checklist

- [ ] Environment variables configured
- [ ] Database migrations run
- [ ] Documentation updated
- [ ] Stakeholders notified
- [ ] Monitoring/logging verified

---

## Notes

### Implementation Guidelines
- Follow existing code patterns in [directory]
- Use [library] for [purpose] (already in project)
- Avoid [anti-pattern] (common issue in codebase)

### Open Questions
- [ ] Question 1? (Assigned to: [person/team])
- [ ] Question 2? (Assigned to: [person/team])

---

## Progress Tracking

**Last Updated:** [Date]
**Completed Tasks:** 0/[total]
**Estimated Completion:** [Date]

### Changelog
| Date | Task | Status | Notes |
|------|------|--------|-------|
| [Date] | 1.1 | ✅ Complete | Migration successful |
| [Date] | 1.2 | 🚧 In Progress | Model created, tests pending |
````

### Step 4: Save and Present

```markdown
✅ Task list generated successfully!

📁 **Location:** [filepath]
📊 **Total Tasks:** [parent count] parent tasks, [subtask count] subtasks
⏱️ **Estimated Effort:** [time estimate]

**Next Steps:**
1. Review task list for accuracy
2. Use "PRD Task List Management" workflow during implementation
3. Update task status as work progresses

Would you like me to:
A. Make changes to this task list
B. Start implementation of first task
C. Export to project management tool format
D. Save and exit

Your choice: [Wait]


Phase 5: Task List Refinement (Optional)

Goals
Adjust task list based on user feedback.

Refinement Options

User can request:
1. Reorder tasks - Change execution sequence
2. Split tasks - Break large tasks into smaller ones
3. Merge tasks - Combine related sub-tasks
4. Add tasks - Include missing implementation steps
5. Remove tasks - Eliminate unnecessary work
6. Adjust estimates - Update complexity/time estimates

For each change:
•  Update task list
•  Show what changed
•  Re-save file
•  Update task count/estimates



AI Agent Guidelines

Do's ✅
•  Analyze codebase before generating tasks
•  Match existing project patterns and conventions
•  Create testable, specific sub-tasks
•  Include file paths for clarity
•  Estimate complexity realistically
•  Wait for user approval between phases
•  Adapt to discovered constraints
•  Reference PRD requirements explicitly

Don'ts ❌
•  Don't assume project structure without checking
•  Don't create tasks without codebase context
•  Don't make sub-tasks too large (>4 hours)
•  Don't skip testing tasks
•  Don't ignore existing similar code
•  Don't proceed without parent task approval
•  Don't hardcode test frameworks or tools

Task Quality Checklist

Good tasks:
•  ✅ Specific action and target file
•  ✅ Clear acceptance criteria
•  ✅ Realistic time estimate
•  ✅ Dependencies identified
•  ✅ Testing requirements included

Poor tasks:
•  ❌ "Implement feature" (too vague)
•  ❌ "Fix all bugs" (unmeasurable)
•  ❌ Tasks requiring multiple files simultaneously
•  ❌ No testing mentioned
•  ❌ No acceptance criteria



Examples

Good Task
- [ ] 2.3 ⏱️ Implement password hashing in AuthService
  - **Details:** Use bcrypt library (already in dependencies), salt rounds = 10
  - **Files:** `services/AuthService.ts` (add hashPassword and comparePassword methods)
  - **Tests:** `services/AuthService.test.ts` (verify hash != plain, compare works)
  - **Acceptance:** Passwords hashed securely, compare function validates correctly
markdown

Poor Task
- [ ] 2.3 Do authentication stuff
markdown

Good Parent Task Structure
### 3.0 API Endpoints & Validation 🟡 Important

- [ ] 3.1 Create auth routes file
- [ ] 3.2 Implement POST /api/auth/register endpoint
- [ ] 3.3 Implement POST /api/auth/login endpoint
- [ ] 3.4 Add request validation middleware
- [ ] 3.5 Write API integration tests
- [ ] 3.6 Update API documentation
markdown

Poor Parent Task Structure
### 3.0 Make the API work
- [ ] 3.1 Do all the endpoints
markdown


Success Indicators

Task list is complete when:
•  ✅ All PRD functional requirements covered
•  ✅ Tasks follow existing codebase patterns
•  ✅ Each task has clear acceptance criteria
•  ✅ Testing included for all components
•  ✅ Dependencies between tasks identified
•  ✅ File paths and names specified
•  ✅ Complexity estimates provided
•  ✅ User approves task breakdown



Related Workflows

Use this workflow after:
•  PRD Generation Workflow - Creates the input PRD

Use these workflows during implementation:
•  PRD Task List Management - Track progress through tasks
•  Debugging Workflow - When issues arise
•  Refactoring Workflow - If code quality suffers
•  Code Quality Standards - Ensure quality during implementation

Integration points:
•  Task list feeds into sprint planning
•  Tasks reference PRD requirements
•  Progress tracked in task list management workflow