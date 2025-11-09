Enhanced Version with CLI:

# Supabase Tooling Preferences

## Overview
When working with Supabase in my projects, use the appropriate tool for each task type to maximize efficiency and consistency.

---

## Tool Selection Guide

### 1. Supabase MCP Server (Preferred for Database Operations)

**Use for:**
- ✅ Reading data from tables
- ✅ Creating/updating/deleting records
- ✅ Querying with filters
- ✅ Schema inspection
- ✅ Real-time data access

**Why preferred:**
- Structured, type-safe operations
- Built-in error handling
- Consistent interface
- Available in Warp sessions

**Example usage:**
```markdown
"Use the Supabase MCP server to get all users with role='admin'"
markdown
Fallback: If MCP server unavailable, use Supabase client SDK or raw SQL.



2. Supabase CLI (Preferred for Development Tasks)

Use for:
•  ✅ Database migrations (supabase db push, supabase db reset)
•  ✅ Type generation (supabase gen types typescript)
•  ✅ Local development (supabase start, supabase stop)
•  ✅ Linking projects (supabase link)
•  ✅ Checking database status (supabase status)
•  ✅ Generating migration files (supabase migration new)

Why use CLI:
•  Official Supabase tooling
•  Handles complex operations safely
•  Generates TypeScript types automatically
•  Manages local development environment

Common commands:
# Start local Supabase (Docker required)
supabase start

# Generate TypeScript types from database schema
supabase gen types typescript --local > types/supabase.ts

# Create new migration
supabase migration new add_users_table

# Push migrations to database
supabase db push

# Reset local database
supabase db reset
bash

Prerequisites:
•  Supabase CLI installed (npm install -g supabase)
•  Docker running (for local development)
•  Linked to project (supabase link --project-ref [your-ref])



3. Direct SQL (Last Resort)

Use when:
•  ❌ MCP server unavailable
•  ❌ CLI doesn't support the operation
•  ❌ Debugging schema issues
•  ❌ One-off administrative queries

Example:
-- Check table structure
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'users';
sql


Decision Tree
Need to interact with Supabase?
│
├─ Database query/CRUD? → Use MCP Server
│  └─ MCP unavailable? → Use Supabase SDK/SQL
│
├─ Schema change/migration? → Use Supabase CLI
│  └─ CLI unavailable? → Manual SQL + document
│
├─ Type generation? → Use Supabase CLI
│
├─ Local development? → Use Supabase CLI
│
└─ Debugging/inspection? → Use appropriate tool
   ├─ Data issue → MCP Server
   ├─ Schema issue → Supabase CLI or SQL
   └─ Connection issue → Check status with CLI


Communication Preferences

When Using MCP Server:
I'll use the Supabase MCP server to fetch that data.

Tool: `supabase_query_table`
Table: `users`
Filter: `status = 'active'`

Result: Found 15 active users.
markdown

When Using Supabase CLI:
I'll use the Supabase CLI to generate TypeScript types from your database schema.

Command: `supabase gen types typescript --local`

This will create type definitions matching your database tables, 
so you get autocomplete and type checking in your code.

Running: [show command output]
markdown

When Using Direct SQL:
The MCP server isn't available, so I'll use direct SQL to check the database.

Query: `SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '7 days'`

This counts users created in the last 7 days.
markdown


Project-Specific Considerations

This rule applies to projects using:
•  Supabase as backend/database
•  TypeScript (for type generation)
•  Local development setup

For projects NOT using Supabase:
•  Use appropriate database tooling (Prisma, Drizzle, raw SQL, etc.)
•  This rule doesn't apply



Troubleshooting

MCP Server Not Available
"I don't see the Supabase MCP server in Warp. I'll use [alternative approach] instead."
markdown

CLI Command Fails
The Supabase CLI command failed with: [error]

This usually means:
1. Supabase CLI not installed (run: npm install -g supabase)
2. Not linked to project (run: supabase link)
3. Docker not running (for local commands)

Would you like help resolving this?
markdown


Best Practices

1. Always explain which tool you're using and why
2. Show commands before running them (for CLI)
3. Provide fallbacks if primary tool unavailable
4. Regenerate types after schema changes (CLI)
5. Use local Supabase for testing migrations (CLI)
6. Document any manual SQL used (for future migrations)



Success Indicators

Tooling usage is effective when:
•  ✅ Right tool used for each task type
•  ✅ Operations complete successfully
•  ✅ TypeScript types stay synchronized with schema
•  ✅ Migrations tracked and versioned
•  ✅ Local development mirrors production