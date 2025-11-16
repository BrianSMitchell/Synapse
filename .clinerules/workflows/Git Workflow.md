Git Workflow

Purpose
Guide proper version control practices for tracking changes, collaborating, and maintaining code history.

When to Use This Workflow
•  Starting work on a new feature
•  Making changes to existing code
•  Preparing to share code with others
•  Resolving merge conflicts
•  Rolling back problematic changes



Core Git Principles

The Golden Rules
1. Commit often - Small, atomic commits are easier to understand and revert
2. Write clear messages - Future you needs to know what and why
3. Test before committing - Never commit broken code
4. Branch for features - Keep main branch stable
5. Pull before push - Stay synchronized with remote

Common Anti-Patterns (Avoid These)
•  ❌ Committing directly to main without testing
•  ❌ Vague commit messages ("fix stuff", "updates")
•  ❌ Committing generated files (node_modules, build artifacts)
•  ❌ Making unrelated changes in one commit
•  ❌ Force pushing without understanding consequences



Branch Strategy

Branch Types

main (or master)
•  Production-ready code
•  Always deployable
•  Protected from direct commits

feature/[name]
•  New features or enhancements
•  Example: feature/user-authentication
•  Merged to main when complete

fix/[name]
•  Bug fixes
•  Example: fix/login-timeout
•  Merged to main when tested

refactor/[name]
•  Code restructuring without behavior change
•  Example: refactor/split-game-logic
•  Merged to main when tested

hotfix/[name]
•  Emergency production fixes
•  Created from main, merged back immediately
•  Example: hotfix/security-patch



Phase 1: Starting New Work

Step 1: Ensure Clean State

Check current status:
# See what branch you're on and any uncommitted changes
git status

# See recent commits
git log --oneline -5
pwsh

If you have uncommitted changes:
# Option A: Commit them first (if related to current work)
git add .
git commit -m "type: description"

# Option B: Stash them (save for later)
git stash save "WIP: description of what I was doing"

# Later, restore stashed changes
git stash pop
pwsh

Step 2: Update Main Branch
# Switch to main branch
git checkout main

# Get latest changes from remote
git pull origin main

# Verify you're up-to-date
git status
pwsh

Step 3: Create Feature Branch
# Create and switch to new branch
git checkout -b feature/your-feature-name

# Verify you're on the new branch
git branch
# (current branch shows with asterisk *)
pwsh

Branch naming conventions:
•  Use lowercase
•  Separate words with hyphens
•  Include type prefix (feature/, fix/, etc.)
•  Be descriptive but concise

Examples:
•  ✅ feature/password-reset
•  ✅ fix/navbar-mobile-menu
•  ✅ refactor/extract-auth-service
•  ❌ my-branch
•  ❌ updates
•  ❌ feature



Phase 2: Making Changes

Work in Small Increments

Follow this cycle for each sub-task:

1. Make code changes
2. Test the changes
3. Review what changed
4. Stage specific files
5. Commit with message
6. Repeat

Step 1: Review Changes Before Staging
# See what files changed
git status

# See actual changes in files
git diff

# See changes in specific file
git diff path/to/file.ts
pwsh

Step 2: Stage Files Selectively
# Stage specific files (preferred)
git add src/services/AuthService.ts
git add src/services/AuthService.test.ts

# Stage all files in directory
git add src/services/

# Stage all changes (use cautiously)
git add .

# Unstage a file if you added it by mistake
git restore --staged path/to/file.ts
pwsh

💡 Tip: Stage only related changes in each commit. If you fixed two unrelated bugs, make two separate commits.

Step 3: Review Staged Changes
# See what's about to be committed
git diff --staged

# If something shouldn't be included, unstage it
git restore --staged path/to/file.ts
pwsh

Step 4: Commit with Descriptive Message

Commit message format:
type(scope): brief summary (50 chars or less)

- Detailed point 1
- Detailed point 2
- Detailed point 3

Refs: Task X.Y from PRD-ZZZZ

PowerShell command (use multiple -m flags):
git commit -m "feat(auth): implement password hashing" `
  -m "- Add bcrypt hashing to AuthService.hashPassword()" `
  -m "- Salt rounds set to 10" `
  -m "- Add comparePassword method for validation" `
  -m "- All tests passing (12/12)" `
  -m "Refs: Task 2.3 from PRD-0001-authentication"

pwsh

Type prefixes:
•  feat: - New feature
•  fix: - Bug fix
•  refactor: - Code restructuring (no behavior change)
•  test: - Adding/updating tests
•  docs: - Documentation changes
•  chore: - Maintenance (deps, config, build)
•  style: - Formatting, white-space (no code change)
•  perf: - Performance improvement

Scope examples:
•  (auth) - Authentication module
•  (api) - API layer
•  (ui) - User interface
•  (db) - Database

Good commit messages:
✅ feat(auth): add JWT token refresh mechanism
✅ fix(api): handle null user ID in profile endpoint
✅ refactor(game): extract player logic to PlayerService
✅ test(auth): add integration tests for login flow
✅ docs(readme): update installation instructions

Poor commit messages:
❌ fix stuff
❌ updates
❌ working on feature
❌ asdfasdf
❌ final fix (followed by "final fix 2")


Phase 3: Pushing to Remote

When to Push

Push after:
•  Completing a logical unit of work (sub-task or parent task)
•  Before ending work session (backup)
•  Before switching to different work
•  When ready for code review

Don't need to push after every single commit - it's okay to have several local commits before pushing.

Step 1: Ensure Tests Pass
# Run your project's test command
npm test
# or
pytest
# or
npm run test
pwsh

Never push failing tests.

Step 2: Push Branch to Remote
# First time pushing this branch
git push -u origin feature/your-feature-name

# Subsequent pushes (after first time)
git push
pwsh

What -u does: Sets up tracking so future pushes/pulls know which remote branch to use.

Step 3: Verify Push Succeeded
# Check that remote branch exists
git branch -r

# See commit history including remote
git log --oneline --graph --all -10
pwsh


Phase 4: Keeping Branch Up-to-Date

When Main Branch Advances

If others have merged changes to main while you're working:
# Save your current work
git add .
git commit -m "WIP: saving progress"

# Switch to main and update
git checkout main
git pull origin main

# Switch back to your feature branch
git checkout feature/your-feature-name

# Merge main into your branch (brings in new changes)
git merge main
pwsh
If merge conflicts occur, see Phase 6 below.



Phase 5: Completing Work

Step 1: Final Verification

Before merging to main:
All tests pass
No linting errors
Code reviewed (self or peer)
Documentation updated
No debug code or console.logs
Commit messages clear and complete

Step 2: Merge to Main

Option A: Via Pull Request (Recommended for team projects)
1. Push your branch: git push
2. Create PR on GitHub/GitLab/etc.
3. Wait for review/approval
4. Merge via web interface

Option B: Direct Merge (Solo projects)
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Merge your feature branch
git merge feature/your-feature-name

# Push to remote
git push origin main
pwsh

Step 3: Clean Up
# Delete local branch (after merged)
git branch -d feature/your-feature-name

# Delete remote branch
git push origin --delete feature/your-feature-name

# Verify branches cleaned up
git branch -a
pwsh


Phase 6: Handling Merge Conflicts

When Conflicts Occur

Git will tell you which files have conflicts:
CONFLICT (content): Merge conflict in src/services/AuthService.ts

Step 1: See Conflicted Files
# List files with conflicts
git status

# Look for files marked "both modified"
pwsh

Step 2: Open Conflicted Files

Conflicts look like this:
<<<<<<< HEAD
// Your changes
const userId = req.user.id;
=======
// Changes from main branch
const userId = req.params.userId;
>>>>>>> main
typescript

Step 3: Resolve Conflicts

Choose one:
•  Keep your changes (remove markers and other version)
•  Keep their changes (remove markers and your version)
•  Combine both (write new code that includes both)

After resolving:
// Resolved version
const userId = req.user?.id || req.params.userId;
typescript

Step 4: Mark as Resolved
# After editing the file
git add src/services/AuthService.ts

# Continue the merge
git commit
# (Git will pre-fill a merge commit message)
pwsh

Step 5: Verify
# Make sure everything works
npm test

# Check that all conflicts resolved
git status
pwsh


Phase 7: Undoing Changes

Undo Uncommitted Changes
# Discard changes in specific file
git restore path/to/file.ts

# Discard ALL uncommitted changes (careful!)
git restore .
pwsh

Undo Last Commit (Keep Changes)
# Undo commit but keep changes in working directory
git reset --soft HEAD~1

# Now you can re-commit with different message or changes
pwsh

Undo Last Commit (Discard Changes)
# Undo commit AND discard changes (careful!)
git reset --hard HEAD~1
pwsh

Revert a Commit (Safe, Creates New Commit)
# Undo specific commit by creating opposite commit
git revert [commit-hash]

# Find commit hash
git log --oneline
pwsh

Going Back to Specific Commit
# See commit history
git log --oneline

# Go back to specific commit (detached HEAD state)
git checkout [commit-hash]

# To make changes from here, create a new branch
git checkout -b recovery-branch
pwsh


Common Scenarios

Scenario 1: "I Committed to Wrong Branch"
# If you committed to main but meant to be on feature branch

# Create feature branch from current state
git checkout -b feature/correct-branch

# Go back to main and undo the commit
git checkout main
git reset --hard origin/main
pwsh

Scenario 2: "I Need to Work on Something Else Urgently"
# Save current work
git stash save "WIP: feature description"

# Switch to main and create hotfix branch
git checkout main
git checkout -b hotfix/urgent-fix

# ... fix the issue ...

# After hotfix merged, return to your work
git checkout feature/original-work
git stash pop
pwsh

Scenario 3: "I Want to Split a Large Commit"
# Undo last commit but keep changes
git reset --soft HEAD~1

# Stage and commit in smaller chunks
git add file1.ts
git commit -m "feat: part 1"

git add file2.ts
git commit -m "feat: part 2"
pwsh

Scenario 4: "I Accidentally Committed Sensitive Data"
# If NOT yet pushed to remote
git reset --hard HEAD~1

# If ALREADY pushed (contact team, rotate credentials)
# Remove from history (advanced, be careful)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive/file" \
  --prune-empty --tag-name-filter cat -- --all
pwsh


.gitignore Best Practices

What to Ignore

Always add to .gitignore:
# Dependencies
node_modules/
venv/
__pycache__/

# Build outputs
dist/
build/
*.exe
*.dll

# Environment files
.env
.env.local
*.env

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/

# Test coverage
coverage/
.nyc_output/

# Temporary files
*.tmp
*.temp
~*
gitignore

Check Ignored Files
# See what would be ignored
git status --ignored

# Test if specific file is ignored
git check-ignore -v path/to/file
pwsh


Git Configuration

One-Time Setup
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set default editor (optional)
git config --global core.editor "code --wait"

# View all settings
git config --list
pwsh

Useful Aliases
# Create shortcuts
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.lg "log --oneline --graph --all"

# Now you can use
git st   # instead of git status
git lg   # pretty log
pwsh


Quick Reference Commands

Status & Information
git status                    # Current state
git log --oneline -10        # Recent commits
git diff                     # Unstaged changes
git diff --staged            # Staged changes
git branch                   # List branches
git branch -r                # Remote branches
pwsh

Making Changes
git add [file]               # Stage file
git add .                    # Stage all
git commit -m "message"      # Commit
git push                     # Push to remote
git pull                     # Get remote changes
pwsh

Branching
git checkout -b [name]       # Create & switch branch
git checkout [name]          # Switch branch
git merge [branch]           # Merge branch
git branch -d [name]         # Delete local branch
pwsh

Undoing
git restore [file]           # Discard changes
git restore --staged [file]  # Unstage
git reset --soft HEAD~1      # Undo commit, keep changes
git reset --hard HEAD~1      # Undo commit, discard changes
git revert [hash]            # Revert specific commit
pwsh


Troubleshooting

"Failed to Push - Updates Were Rejected"
# Someone else pushed to this branch
# Pull their changes first
git pull

# If conflicts, resolve them, then
git push
pwsh

"Detached HEAD State"
# You checked out a specific commit
# Create a branch to save changes
git checkout -b recovery-branch

# Or just go back to a branch
git checkout main
pwsh

"I Can't Switch Branches - Uncommitted Changes"
# Option 1: Commit changes
git add .
git commit -m "WIP: save progress"

# Option 2: Stash changes
git stash
# ... switch branches and work ...
git stash pop  # restore changes later
pwsh

"Merge Conflict Nightmare"
# Abort the merge and start over
git merge --abort

# Or get help resolving conflicts
# Open files, look for <<<<<<< markers
# Edit to resolve, then git add and git commit
pwsh


Integration with Other Workflows

With Task List Management
•  Commit after completing each sub-task
•  Reference task number in commit message
•  Push after completing parent task

With Refactoring Workflow
•  Create refactor branch before starting
•  Commit after each chunk (Phase 3 iterations)
•  Each commit should pass tests

With Debugging Workflow
•  Create fix branch when starting debug
•  Commit the fix with clear explanation
•  Reference bug report in commit message



Success Indicators

Git workflow is effective when:
•  ✅ Commit history tells a clear story
•  ✅ Each commit is self-contained and revertible
•  ✅ Main branch is always deployable
•  ✅ Merge conflicts are rare and resolvable
•  ✅ You can find and understand past changes
•  ✅ Team members can follow your work (if collaborating)



Related Guidelines

Reference in conjunction with:
•  Task List Management Rule - Commit protocol for task completion
•  Development Philosophy - Incremental progress, quality over speed
•  Refactoring Workflow - Atomic commits during refactoring