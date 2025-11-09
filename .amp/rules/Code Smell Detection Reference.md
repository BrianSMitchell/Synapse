# Code Smell Detection Reference

## Purpose
Quick reference for identifying refactoring targets through code smells, metrics, and business indicators.

## When to Use
- During code reviews
- Planning refactoring efforts
- Analyzing technical debt
- Prioritizing cleanup work
- Post-migration assessment

---

## Code Smell Categories (Fowler's Taxonomy)

### 🔴 Bloaters
Code that has grown too large or unwieldy.

**Indicators:**
- **Long Method:** >50-100 lines (extract sub-methods)
- **Large Class/File:** >300-500 lines (split by responsibility)
- **Primitive Obsession:** Using basic types instead of domain objects
- **Long Parameter List:** >3-4 parameters (use parameter objects)
- **Data Clumps:** Same group of variables appearing together

**Action:** Extract methods/classes, introduce domain objects

---

### 🟡 Duplicators
Repeated code that increases maintenance burden.

**Indicators:**
- Same code block in multiple places
- Similar logic with minor variations
- Copy-paste programming patterns
- >5-10% code duplication across codebase

**Action:** Extract to shared utilities, apply DRY principle

---

### 🟠 Change Preventers
Code that resists modification.

**Indicators:**
- **Shotgun Surgery:** One change requires editing many files
- **Divergent Change:** Class changes for multiple unrelated reasons
- **Parallel Inheritance:** Adding subclass requires adding another elsewhere

**Action:** Consolidate related changes, move behavior closer

---

### 🔵 Object-Orientation Abusers
Misuse of OOP principles.

**Indicators:**
- **Switch Statements:** Long switch/case instead of polymorphism
- **Temporary Fields:** Fields only used in specific scenarios
- **Refused Bequest:** Subclass ignores inherited methods
- **Alternative Classes:** Different interfaces doing similar things

**Action:** Apply polymorphism, refactor inheritance

---

### ⚪ Dispensables
Code that serves no purpose.

**Indicators:**
- **Dead Code:** Unused functions, variables, parameters
- **Speculative Generality:** Unused flexibility/abstractions
- **Comments:** Explaining bad code instead of improving it
- **Duplicate Code:** Self-explanatory

**Action:** Delete dead code, simplify unnecessary abstractions

---

### 🟣 Couplers
Excessive coupling between classes.

**Indicators:**
- **Feature Envy:** Method uses data from another class more than its own
- **Inappropriate Intimacy:** Classes too dependent on each other's internals
- **Message Chains:** Long chains like `a.b().c().d()`
- **Middle Man:** Class just delegates to another

**Action:** Move methods, introduce facades, hide delegates

---

## Industry Standard Metrics

### File/Class Size Limits

| Unit | Recommended Max | Warning Signs | Action Threshold |
|------|----------------|---------------|------------------|
| **Method/Function** | 10-50 lines | >50 lines | >100 lines - extract |
| **Class/File** | 200-500 lines | >500 lines | >1000 lines - split |
| **Parameter List** | 3-4 parameters | >4 parameters | >5 parameters - refactor |
| **Line Length** | 80-120 characters | >120 characters | >150 - reformat |

**Source:** Clean Code, Java Conventions, PEP 8

### Complexity Metrics

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| **Cyclomatic Complexity** | <10 per function | 10-15 | >15 - refactor immediately |
| **Code Duplication** | <3% | 3-10% | >10% - DRY cleanup needed |
| **Test Coverage** | >80% | 70-80% | <70% - add tests |
| **Nesting Depth** | <3 levels | 3-4 levels | >4 - flatten logic |
| **CodeHealth Score** | >9.0 | 7.0-9.0 | <7.0 - refactor |

**Tools:** ESLint, SonarQube, CodeScene, Complexity Report

---

## Business Indicators for Refactoring

### When Code Quality Impacts Business

**High Priority (Refactor Now):**
- Features take 2-3x longer than estimated
- Bugs cluster in specific files/modules
- New developers take weeks to onboard
- Production incidents tied to specific code areas
- Compliance/security standards not met

**Medium Priority (Schedule Refactor):**
- Files changed >10 times per month
- Code reviews take excessive time
- Performance bottlenecks identified
- Post-migration cleanup needed
- Technical debt visible but not blocking

**Low Priority (Monitor):**
- Metrics slightly above thresholds
- Isolated "god classes" not actively developed
- Legacy code rarely touched
- No immediate business impact

---

## Detection Commands

### Automated Analysis

**JavaScript/TypeScript:**
```bash
# Complexity analysis
npx eslint . --plugin complexity --rule "complexity: ['error', 10]"

# Find large files
Get-ChildItem -Recurse *.ts | Where-Object { (Get-Content $_ | Measure-Object -Line).Lines -gt 500 }

# Duplication detection
npx jscpd src/

Python:
# Complexity
radon cc . -a -nb

# Find large files
Get-ChildItem -Recurse *.py | Where-Object { (Get-Content $_ | Measure-Object -Line).Lines -gt 500 }

# Code smells
pylint src/ --disable=all --enable=R,C

General:
# Lines of code per file
Get-ChildItem -Recurse *.{ts,js,py} | ForEach-Object { 
  "$($_.Name): $((Get-Content $_ | Measure-Object -Line).Lines) lines" 
}

# Find dead code (requires tool like vulture for Python, ts-unused-exports for TS)
npx ts-unused-exports tsconfig.json

Quick Assessment Questions

Ask these during code reviews:

Readability
•  ❓ Can I understand this in <5 minutes?
•  ❓ Would a junior dev understand this?
•  ❓ Is naming clear and consistent?

Maintainability
•  ❓ Can I add a feature without touching unrelated code?
•  ❓ Are tests easy to write for this?
•  ❓ If I changed X, what else breaks?

Modularity
•  ❓ Does this do one thing well?
•  ❓ Could this be reused elsewhere?
•  ❓ Are dependencies clear and minimal?

If you answer "no" to most questions → Refactor target identified



Prioritization Framework

ROI-Based Prioritization
Refactor Priority = (Business Impact × Change Frequency) / Refactor Effort

Where:
- Business Impact: 1-10 (how much it slows development)
- Change Frequency: Times changed per month
- Refactor Effort: Estimated hours to fix

Example:
•  File: game.ts (4000 lines)
•  Business Impact: 8 (slows feature development significantly)
•  Change Frequency: 15 times/month
•  Refactor Effort: 40 hours

Priority Score: (8 × 15) / 40 = 3.0 (High priority)



Integration with Other Workflows

Use This Reference During:

Refactoring Workflow - Phase 1 (Assessment):
•  Reference metrics to establish baseline
•  Use smell categories to identify issues
•  Apply business indicators to justify refactor

Code Quality Standards - Detection Phase:
•  Check metrics during code generation
•  Verify complexity thresholds
•  Ensure file sizes within limits

Code Reviews:
•  Quick checklist for smell categories
•  Metrics to justify refactor requests
•  Business impact assessment



Tool Recommendations by Language

JavaScript/TypeScript
•  ESLint - Complexity, code smells
•  SonarQube - Overall code health
•  jscpd - Duplication detection
•  TypeScript Compiler - Unused exports, dead code

Python
•  Pylint - Code smells, complexity
•  Radon - Cyclomatic complexity metrics
•  Vulture - Dead code detection
•  Bandit - Security smells

Universal
•  SonarQube - Multi-language support
•  CodeScene - CodeHealth scoring
•  CodeClimate - Maintainability scores
•  Git history - Change frequency analysis



AI Agent Instructions

When analyzing code for refactoring:

1. Run metrics first
◦  File size, complexity, duplication
◦  Present findings with thresholds
2. Categorize smells found
◦  Map to Fowler's categories
◦  Identify patterns
3. Assess business impact
◦  Check change frequency
◦  Estimate refactor effort
◦  Calculate priority score
4. Propose refactoring plan
◦  Reference Refactoring Workflow
◦  Present phased approach
◦  Wait for user approval

Do NOT:
•  Start refactoring without metrics
•  Prioritize without business justification
•  Refactor low-impact code just because metrics say so



Success Indicators

Code is refactor-ready when:
•  ✅ Metrics exceed thresholds consistently
•  ✅ Business impact documented
•  ✅ Multiple smell categories present
•  ✅ Change frequency high (>5-10 times/month)
•  ✅ Team consensus it's slowing development

Code might NOT need refactoring if:
•  ❌ Metrics slightly over but stable
•  ❌ Rarely changed (legacy, working code)
•  ❌ No business impact
•  ❌ Would take longer to refactor than rewrite
•  ❌ Scheduled for deprecation



Related Guidelines

Reference in conjunction with:
•  Code Quality Standards - Prevention during development
•  Refactoring Workflow - Execution of refactoring
•  Debugging Workflow - When smells cause bugs