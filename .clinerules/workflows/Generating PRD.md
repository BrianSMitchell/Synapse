Universal PRD Generation Workflow

# PRD Generation Workflow

## Purpose
Guide systematic creation of Product Requirements Documents (PRDs) through iterative questioning and structured documentation.

## When to Use This Workflow
- Starting a new feature
- Planning major functionality addition
- Documenting requirements before implementation
- Clarifying ambiguous feature requests
- Creating alignment between stakeholders and developers

---

## Phase 1: Initial Intake

### Step 1: Receive Feature Request
User provides initial prompt describing desired feature/functionality.

### Step 2: Identify Feature Category
Classify to guide question selection:

**Feature Type:**
- [ ] New user-facing feature (UI/UX changes)
- [ ] Backend/API functionality
- [ ] Integration with external service
- [ ] Data model/schema change
- [ ] Performance improvement
- [ ] Bug fix requiring requirements
- [ ] Security/compliance feature
- [ ] Refactoring/technical improvement

**Complexity Level:**
- [ ] Simple (1-2 days implementation)
- [ ] Medium (3-7 days implementation)
- [ ] Complex (1-2+ weeks implementation)

### Output
Feature category and complexity documented for scoping questions.

---

## Phase 2: Requirements Gathering

### Goals
Extract complete requirements through targeted questions.

### Question Framework

**Present questions in multiple-choice format when possible:**
```markdown
**Question:** What is the primary user role for this feature?

A. End user (customer/consumer)
B. Admin/moderator
C. Developer/API consumer
D. Internal team member
E. Other (please specify)

Your answer: [Wait for response]
markdown
Core Questions (Always Ask)

1. Problem Definition
•  What problem does this feature solve?
•  What is the pain point or opportunity?
•  What happens currently without this feature?

2. Target Audience
•  Who is the primary user of this feature?
•  Are there secondary users?
•  What is their technical skill level?

3. Success Criteria
•  How will we know this feature is successful?
•  What metrics will we track?
•  What does "done" look like?

4. Scope Boundaries
•  What must this feature include?
•  What should it NOT include (non-goals)?
•  What can be deferred to future iterations?

Conditional Questions (Based on Feature Type)

For User-Facing Features:
•  What are the key user actions/interactions?
•  Are there UI/design requirements or examples?
•  What devices/platforms must be supported?
•  Are there accessibility requirements?

For API/Backend Features:
•  What data inputs are required?
•  What data outputs are expected?
•  What are the performance requirements?
•  Are there rate limiting or security considerations?

For Integrations:
•  Which external service/API?
•  What authentication method?
•  What data is being synced/exchanged?
•  What happens if the external service is unavailable?

For Data Changes:
•  What existing data is affected?
•  Is migration required?
•  What are data retention requirements?
•  Are there compliance/privacy considerations?

User Stories Elicitation

Prompt user for stories using this format:
Please provide 2-5 user stories in this format:

As a [type of user]
I want to [perform action]
So that [achieve benefit]

Example:
As a customer
I want to save items to a wishlist
So that I can purchase them later
markdown

Step 3: Validate Understanding
After gathering responses, summarize understanding:
## Summary of Understanding

**Feature:** [Name]
**Primary User:** [Role]
**Problem Solved:** [Brief description]
**Key Functionality:** [Bullet points]
**Success Metrics:** [Measurements]

Does this accurately capture your requirements? (Yes/No/Clarify)
markdown

Wait for confirmation before proceeding.



Phase 3: PRD Generation

Goals
Create comprehensive, actionable PRD document.

PRD Template Structure
# PRD: [Feature Name]

**Status:** Draft | In Review | Approved | In Development | Complete
**Author:** [AI/Human]
**Date:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]
**Priority:** Critical | High | Medium | Low

---

## 1. Overview

### Problem Statement
[2-3 sentences describing the problem this feature solves]

### Proposed Solution
[2-3 sentences describing how this feature solves the problem]

### Success Metrics
- [Metric 1: e.g., Increase conversion by 15%]
- [Metric 2: e.g., Reduce support tickets by 30%]
- [Metric 3: e.g., Improve page load time to <2s]

---

## 2. Goals

### Primary Goals
1. [Specific, measurable objective]
2. [Specific, measurable objective]

### Secondary Goals
1. [Nice-to-have objective]
2. [Nice-to-have objective]

---

## 3. User Stories

### Story 1: [Title]
**As a** [user type]
**I want to** [action]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] [Specific testable criteria]
- [ ] [Specific testable criteria]
- [ ] [Specific testable criteria]

### Story 2: [Title]
[Repeat format]

---

## 4. Functional Requirements

### Core Functionality

**REQ-001: [Requirement Title]**
- **Description:** [Clear, concise description]
- **Priority:** Must Have | Should Have | Nice to Have
- **User Story Reference:** Story 1, Story 2

**REQ-002: [Requirement Title]**
[Repeat format]

### User Interface Requirements (if applicable)

**REQ-UI-001: [UI Requirement]**
- **Description:** [What user sees/interacts with]
- **Mockup/Reference:** [Link or description]

### API/Integration Requirements (if applicable)

**REQ-API-001: [API Requirement]**
- **Endpoint:** [Method and path]
- **Request:** [Format/schema]
- **Response:** [Format/schema]
- **Error Handling:** [Expected error cases]

### Data Requirements

**REQ-DATA-001: [Data Requirement]**
- **Data Model:** [Entities/tables affected]
- **Fields:** [Required fields and types]
- **Validation Rules:** [Constraints]
- **Migration:** [If existing data affected]

---

## 5. Non-Goals (Out of Scope)

Explicitly list what this feature will NOT include:

- ❌ [Non-goal 1]
- ❌ [Non-goal 2]
- ❌ [Non-goal 3]

*Rationale: Manage expectations and prevent scope creep*

---

## 6. User Experience & Design

### User Flow
markdown

[Step 1] → [Step 2] → [Step 3] → [Outcome]
### Mockups/Wireframes
- [Link to designs or description]
- [Key UI elements to include]

### Accessibility Requirements
- [ ] Keyboard navigation support
- [ ] Screen reader compatibility
- [ ] Color contrast ratios meet WCAG 2.1 AA
- [ ] [Other specific requirements]

---

## 7. Technical Considerations

### Architecture
- [High-level technical approach]
- [Key technologies/frameworks to use]
- [Integration points]

### Dependencies
- [External APIs or services]
- [Other features or modules]
- [Third-party libraries]

### Performance Requirements
- [Response time targets]
- [Throughput requirements]
- [Scalability considerations]

### Security Considerations
- [Authentication requirements]
- [Authorization/permissions]
- [Data encryption]
- [Input validation]

### Known Constraints
- [Technical limitations]
- [Resource constraints]
- [Timeline constraints]

---

## 8. Edge Cases & Error Handling

### Expected Error Scenarios

**Scenario 1: [Error condition]**
- **Trigger:** [What causes this error]
- **Expected Behavior:** [How system should respond]
- **User Experience:** [What user sees]

**Scenario 2: [Error condition]**
[Repeat format]

### Edge Cases

1. **[Edge case description]**
   - **Expected Behavior:** [How to handle]

2. **[Edge case description]**
   - **Expected Behavior:** [How to handle]

---

## 9. Testing Strategy

### Test Scenarios
1. [Happy path test]
2. [Error condition test]
3. [Edge case test]
4. [Performance test]
5. [Security test]

### Acceptance Testing
- [ ] All functional requirements met
- [ ] All user stories validated
- [ ] Performance metrics achieved
- [ ] Accessibility standards met
- [ ] Security review completed

---

## 10. Release Plan

### Phased Rollout (if applicable)

**Phase 1:** [MVP features]
- Timeline: [Target date]
- Scope: [What's included]

**Phase 2:** [Additional features]
- Timeline: [Target date]
- Scope: [What's included]

### Rollback Plan
[How to revert if issues arise]

---

## 11. Open Questions

*To be resolved before implementation begins:*

1. ❓ [Question 1]
   - **Status:** Open | In Discussion | Resolved
   - **Assigned To:** [Person/team]

2. ❓ [Question 2]
   - **Status:** Open | In Discussion | Resolved
   - **Assigned To:** [Person/team]

---

## 12. Appendix

### Glossary
- **[Term]:** [Definition]
- **[Term]:** [Definition]

### References
- [Link to related documents]
- [Link to research/data]
- [Link to designs]

### Revision History
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| [Date] | 1.0 | Initial draft | [Name] |

Step 4: Determine File Location

Ask user:
Where should I save this PRD?

A. Create `/docs/prds/` directory (recommended)
B. Create `/tasks/` directory
C. Use existing `/requirements/` directory
D. Specify custom location: [___________]

Your choice: [Wait for response]
markdown

Step 5: Determine Naming Convention

Ask user:
What naming convention should I use?

A. Sequential number: `0001-prd-feature-name.md`
B. Date-based: `2025-01-15-prd-feature-name.md`
C. Feature-based: `prd-feature-name.md`
D. Custom: [___________]

Your choice: [Wait for response]
markdown

Step 6: Generate and Save

Create PRD file with chosen naming/location.

Present to user:
✅ PRD created: [filename]
📁 Location: [path]
📝 Status: Draft

**Next Steps:**
1. Review PRD for accuracy
2. Share with stakeholders for approval
3. Once approved, use "Generate Task List from PRD" workflow
4. Begin implementation

Would you like me to:
A. Make changes to this PRD
B. Generate task list now
C. Save and exit

Your choice: [Wait]
markdown


Phase 4: PRD Review & Iteration

Goals
Refine PRD based on feedback.

Step 1: Gather Feedback

Ask user:
Please review the PRD and provide feedback:

1. Are the requirements clear and complete?
2. Are there any missing scenarios?
3. Do the success metrics align with goals?
4. Are non-goals clearly defined?
5. Any technical concerns?

What changes are needed? (Type "approved" if ready to proceed)
markdown

Step 2: Iterate

For each requested change:
1. Update specific section
2. Show diff of what changed
3. Ask for confirmation
4. Update version number and revision history

Step 3: Finalize

When approved:
✅ PRD Status: Approved
📅 Approval Date: [Date]
🎯 Ready for task breakdown

Update PRD status to "Approved" and proceed to task generation?
markdown


AI Agent Guidelines

Do's ✅
•  Ask clarifying questions before writing PRD
•  Use multiple-choice questions when possible
•  Summarize understanding before generating
•  Adapt questions based on feature complexity
•  Include concrete examples in requirements
•  Make acceptance criteria testable
•  Separate must-haves from nice-to-haves
•  Define non-goals explicitly
•  Wait for user confirmation at checkpoints

Don'ts ❌
•  Don't assume requirements
•  Don't start implementation discussions
•  Don't skip clarifying questions
•  Don't use jargon without definitions
•  Don't leave success metrics vague
•  Don't forget edge cases
•  Don't proceed without user approval

Question Quality Checklist

Good questions:
•  ✅ Specific and focused
•  ✅ Have multiple-choice options when possible
•  ✅ Build on previous answers
•  ✅ Extract measurable criteria
•  ✅ Identify constraints early

Poor questions:
•  ❌ Too broad or vague
•  ❌ Lead to yes/no answers only
•  ❌ Ask about implementation details
•  ❌ Duplicate information already gathered



Examples

Good Requirement
**REQ-001: User Authentication**
**Description:** System must allow users to log in using email and password
**Acceptance Criteria:**
- [ ] Email validation (RFC 5322 compliant)
- [ ] Password minimum 8 characters
- [ ] Failed login attempts locked after 5 tries
- [ ] Session expires after 30 minutes of inactivity
- [ ] "Remember me" extends session to 30 days
**Priority:** Must Have
markdown

Poor Requirement
**REQ-001: Login**
Users should be able to log in somehow.
markdown

Good User Story
**As a** returning customer
**I want to** view my order history
**So that** I can track past purchases and reorder items easily

**Acceptance Criteria:**
- [ ] Display all orders from past 2 years
- [ ] Show order date, total, and status
- [ ] Allow filtering by date range
- [ ] Include "Reorder" button for each item
- [ ] Paginate results (20 per page)
markdown

Poor User Story
**As a** user
**I want to** see orders
**So that** I can see them
markdown


Success Indicators

PRD is complete when:
•  ✅ All clarifying questions answered
•  ✅ Requirements clear and testable
•  ✅ User stories have acceptance criteria
•  ✅ Non-goals explicitly stated
•  ✅ Success metrics defined
•  ✅ Edge cases documented
•  ✅ Technical constraints identified
•  ✅ User approves document
•  ✅ No open questions remain (or assigned for resolution)



Related Workflows

Use this workflow before:
•  Generate Task List from PRD - Break down into implementation tasks
•  Refactoring Workflow - If PRD involves code changes
•  Debugging Workflow - If PRD addresses bug fixes

Reference during:
•  Code Quality Standards - Ensure requirements lead to quality code
•  Preventing Hardcoding - Plan constants/configs upfront