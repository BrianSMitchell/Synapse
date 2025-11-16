---

## Improved Version 2: Hardcode Detection Workflow (Optional)

```markdown
# Hardcode Detection & Remediation Workflow

## Purpose
Systematic process to identify and eliminate hardcoded values in existing code.

## When to Use
- Code review phase
- Pre-merge quality check
- Refactoring legacy code
- Post-migration cleanup

---

## Phase 1: Detection

### Step 1: Automated Scan
Run linters and search tools:

```bash
# ESLint with magic number detection
npx eslint . --rule 'no-magic-numbers: error'

# Search for repeated strings
grep -roh '"[^"]\{10,\}"' src/ | sort | uniq -c | sort -rn

# Find potential API endpoints
grep -rE '["'\'']https?://|["'\'']/api/' src/

Step 2: Manual Review
Look for patterns:
Numbers in conditionals/calculations
String literals used multiple times
URLs, file paths, or identifiers
Configuration-like values in code



Phase 2: Categorization

For each hardcoded value found, classify:

| Category | Action | Location |
|----------|--------|----------|
| Config/Settings | Extract to config file | config/ |
| Secrets/Keys | Move to environment | .env |
| Business Constants | Create named constant | constants/ |
| Domain Values | Create enum/type | types/ |
| Universal Constant | Keep inline + comment | (same file) |



Phase 3: Extraction

Process Per Hardcode:

1. Create constant/config entry
2. Replace all occurrences (search & replace)
3. Run tests to verify behavior unchanged
4. Commit atomically

git commit -m "refactor: extract [VALUE_NAME] constant

- Replaced [N] occurrences
- Moved to [LOCATION]
- No behavior change
"
bash


Phase 4: Validation

Checklist:
All tests pass
No linting errors
Documentation updated
Constants file exported correctly
No duplicate extractions

Verify Command:
# Ensure value no longer hardcoded
grep -r "old-hardcoded-value" src/
# Should return no results (or only in constants file)
bash


Quick Reference: Extraction Templates

TypeScript Constants File
// constants/[domain].constants.ts
/**
 * [Domain] related constants
 */
export const [DOMAIN]_CONFIG = {
  MAX_[ITEM]: 100,
  DEFAULT_[SETTING]: 'value'
} as const;

export type [Domain]Config = typeof [DOMAIN]_CONFIG;
typescript

Environment Variable
# .env
[KEY_NAME]=[value]

# .env.example
[KEY_NAME]=[example-value-here]
bash
// config/env.config.ts
export const envConfig = {
  [keyName]: process.env.[KEY_NAME] || '[default]'
};
typescript


AI Agent Instructions for This Workflow

When user says: "Check for hardcodes" or "Run hardcode detection"

1. Run automated scans (grep, linting)
2. Present findings with categorization
3. Propose extraction plan
4. Wait for approval
5. Execute extractions one-by-one
6. Verify after each change
7. Commit incrementally

Do NOT proceed to extraction without user approval of the plan.