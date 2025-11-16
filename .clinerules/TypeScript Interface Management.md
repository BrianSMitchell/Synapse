---
description: Guidelines for managing TypeScript interfaces in React components to prevent compilation errors and maintain type safety
author: Cline Self-Improvement Protocol
version: 1.0
tags: ["typescript", "react", "interfaces", "error-prevention", "component-development"]
globs: ["**/*.ts", "**/*.tsx"]
---

# TypeScript Interface Management for React Components

## Overview

This rule provides systematic guidelines for managing TypeScript interfaces in React components to prevent compilation errors, particularly when modifying component props and maintaining type consistency across large codebases.

## Core Principles

### Atomic Interface Changes

When modifying component interfaces, changes must be applied atomically across all related files to prevent TypeScript compilation errors.

**Required Sequence:**
1. Update interface definition
2. Immediately update component function signature
3. Update prop destructuring and usage
4. Test compilation before proceeding

**Critical Pattern:**
```typescript
// 1. Interface Definition
interface ComponentProps {
  empire: Empire;
  onUpdate: () => void;
  // Remove: onClose: () => void;
}

// 2. Component Signature (update immediately)
const Component: React.FC<ComponentProps> = ({ empire, onUpdate }) => {
  // 3. Remove onClose from destructuring
  // 4. Update prop usage throughout component
};
```

### Compilation Verification Protocol

**Mandatory Build Testing:**
- Test TypeScript compilation after each interface change
- Use `pnpm --filter @package build` to verify changes
- Fix errors immediately before proceeding to next component
- Never accumulate interface mismatches across multiple files

**Error Prevention Pattern:**
```bash
# After each interface change:
pnpm --filter @game/client build
# Fix any errors before continuing
```

### Component Interface Consistency

**Systematic Approach for Multiple Components:**
1. Identify all components using the interface
2. Update interface definition first
3. Update each component signature individually
4. Test compilation after each component update
5. Verify all prop usage is consistent

**Common Error Patterns to Avoid:**
- Updating interface but not component signature
- Removing props from interface but leaving in function parameters
- Updating some components but not others using the same interface
- Accumulating errors across multiple files before testing

### Windows Development Considerations

**Command Execution:**
- Use sequential commands instead of chained commands with `&&`
- Test builds individually: `cd packages/client` then `npm run build`
- PowerShell compatibility requires separate command execution

**Build Verification:**
```bash
# Correct approach for Windows:
cd packages/client
npm run build

# Avoid (fails in PowerShell):
cd packages/client && npm run build
```

## Modal System Interface Patterns

### Modal Component Interface Design

**Standard Modal Props Pattern:**
```typescript
interface ModalProps {
  empire: Empire;           // Required game data
  onUpdate: () => void;     // Required callback for data updates
  // Avoid: onClose - handled by modal system, not individual components
}
```

**Modal Manager Integration:**
- Modal components should not handle their own close logic
- Use central ModalManager with modal store for state management
- Remove `onClose` props from individual modal components
- Let base Modal component handle backdrop clicks and escape keys

### Zustand Modal Store Pattern

**Recommended Modal State Structure:**
```typescript
interface ModalState {
  isOpen: boolean;
  type: ModalType | null;
  data?: any;
}

interface ModalActions {
  openModal: (type: ModalType, data?: any) => void;
  closeModal: () => void;
}

type ModalType = 'building' | 'research' | 'galaxy' | 'fleet';
```

## Error Resolution Workflow

### Systematic TypeScript Error Resolution

**When Encountering Interface Errors:**
1. **Identify Root Cause**: Check if interface and component signature match
2. **Fix Interface First**: Ensure interface definition is correct
3. **Update Component Signature**: Match function parameters to interface
4. **Remove Unused Parameters**: Clean up any unused destructured props
5. **Test Immediately**: Verify compilation before proceeding

**Example Error Resolution:**
```typescript
// Error: Property 'onClose' does not exist on type 'ComponentProps'
// Root cause: Interface was updated but component signature wasn't

// Fix:
interface ComponentProps {
  empire: Empire;
  onUpdate: () => void;
  // onClose removed from interface
}

// Update component signature to match:
const Component: React.FC<ComponentProps> = ({ empire, onUpdate }) => {
  // onClose removed from destructuring
};
```

### Build Order Dependencies

**PNPM Workspace Build Order:**
1. Always build shared packages first: `pnpm --filter @game/shared build`
2. Build dependent packages in order
3. Verify each package builds successfully before proceeding
4. Use workspace protocol for internal dependencies: `"@game/shared": "workspace:*"`

## Best Practices

### Interface Documentation

**Component Interface Comments:**
```typescript
interface ComponentProps {
  empire: Empire;           // Current user's empire data
  onUpdate: () => void;     // Callback to refresh parent component data
  // Note: onClose handled by ModalManager, not individual components
}
```

### Prop Validation

**Runtime Prop Validation:**
- Use TypeScript strict mode to catch unused parameters
- Implement prop validation for critical game data
- Handle undefined/null cases gracefully
- Provide meaningful error messages for missing required props

### Testing Strategy

**Interface Change Testing:**
1. Unit test component with new interface
2. Integration test with parent components
3. Build verification across entire workspace
4. Manual testing of UI functionality

### Naming Clarity for Data Loaders

When a data loader expands its responsibility beyond the original name, rename it to reflect scope to avoid drift and confusion.

- Example: If `loadPlanetEnergyContext` begins fetching additional fields (e.g., metalYield, crystalsYield, fertility), prefer renaming to `loadPlanetContext`.
- Rationale: Prevents misleading function names as responsibilities evolve and makes call-sites self-documenting.
- Pattern:
  - Keep the loader cohesive and focused on a single domain (planet context).
  - Update all call-sites atomically and run a build to verify interface/symbol updates immediately.
  - Add a brief JSDoc comment summarizing exactly which fields are returned.

```ts
// Before
async function loadPlanetEnergyContext() {
  // solarEnergy, gas
}

// After
/** Loads planet context for UI hints and derived display. */
async function loadPlanetContext() {
  // solarEnergy, gas, metal, crystals, fertility
}
```

## Success Metrics

A successful TypeScript interface management implementation should achieve:
- ✅ Zero TypeScript compilation errors
- ✅ Consistent interface definitions across components
- ✅ Clean component function signatures without unused parameters
- ✅ Successful build verification after each change
- ✅ Maintainable and readable component interfaces

## Multi-Component System Interface Management

### Complex Component Architecture Patterns

**Hierarchical Component Structure:**
- Implement Store → Management → Overview/Detail → Card hierarchy
- Use utility types like `Omit<Colony, 'buildings'>` to resolve model/UI interface conflicts
- Create computed getters in stores for derived state calculations
- Maintain interface consistency across 5+ components with atomic change management

**Large System Error Resolution Protocol:**
```typescript
// Pattern for resolving model/UI interface conflicts:
interface BaseData extends Omit<Colony, 'buildings'> {
  buildings: Building[];  // Full Building objects instead of string IDs
  productionRates: ProductionRates;
  constructionQueue: Building[];
}
```

**Systematic Multi-Component Updates:**
1. **Identify All Affected Components**: List all components using the interface
2. **Update Interface Definition**: Make changes to shared interface first
3. **Update Component Signatures**: Fix each component function signature individually
4. **Remove Unused Parameters**: Clean up unused imports and parameters systematically
5. **Test After Each Component**: Build verification prevents error accumulation
6. **Verify Integration**: Test component interactions and data flow

### Unused Import/Parameter Management

**Critical Error Patterns:**
- `'useAuthStore' is declared but its value is never read` - Remove unused imports immediately
- Unused function parameters in component signatures - Remove from both interface and function
- Accumulated TypeScript errors across multiple components - Fix systematically, one component at a time

**Resolution Workflow:**
```typescript
// Before: Unused import and parameter
import { useAuthStore } from '../../stores/authStore';
const Component: React.FC<Props> = ({ empire, onUpdate, user }) => {
  // user parameter never used
};

// After: Clean interface and signature
const Component: React.FC<Props> = ({ empire, onUpdate }) => {
  // Only used parameters remain
};
```

## Common Pitfalls to Avoid

1. **Partial Interface Updates**: Updating interface but not component signature
2. **Accumulated Errors**: Making multiple interface changes before testing compilation
3. **Inconsistent Patterns**: Using different prop patterns across similar components
4. **Windows Command Issues**: Using Unix-style command chaining in PowerShell
5. **Build Order Violations**: Not building shared packages before dependent packages
6. **Unused Import Accumulation**: Leaving unused imports after interface changes
7. **Multi-Component Error Cascade**: Not fixing errors immediately after each component update
8. **Interface/Model Mismatches**: Not using utility types to resolve data structure conflicts

## Advanced Interface Management

### State Management Integration

**Zustand Store Interface Patterns:**
```typescript
interface BaseStore {
  // State
  selectedBaseId: string | null;
  bases: BaseData[];
  loading: boolean;
  error: string | null;
  
  // Actions
  setSelectedBase: (id: string | null) => void;
  setBases: (bases: BaseData[]) => void;
  
  // Computed getters
  getSelectedBase: () => BaseData | null;
  getTotalProduction: () => ProductionRates;
}
```

**API Integration Type Safety:**
- Handle type mismatches between API responses and UI state
- Use proper error boundaries for authentication and data fetching
- Implement loading states with proper TypeScript typing
- Create authenticated API instances with proper interceptor typing

This rule ensures TypeScript interface changes are managed systematically to prevent compilation errors and maintain type safety across React component hierarchies, especially in complex multi-component systems.
