# Windows Development Environment

## System Information
- **Operating System:** Windows 11
- **Shell:** PowerShell 5.1
- **Terminal:** Warp (Windows version)

---

## PowerShell Command Syntax

### Command Chaining

**PowerShell 5.1 does NOT support `&&` or `||` operators.**

```powershell
# ❌ WRONG - Does not work in PowerShell 5.1
cd C:\Project\frontend && npm run build

# ✅ CORRECT - Use semicolon for sequential commands
cd C:\Project\frontend ; npm run build

# ✅ ALTERNATIVE - Use separate lines
cd C:\Project\frontend
npm run build

# ✅ CONDITIONAL - Only if first succeeds
cd C:\Project\frontend
if ($?) { npm run build }

Note: PowerShell 7+ supports && and ||, but I'm using 5.1.



Path Conventions

File Paths
# ✅ Windows paths use backslashes
cd C:\Users\roand\Desktop\project

# ✅ PowerShell also accepts forward slashes
cd C:/Users/roand/Desktop/project

# ✅ Use quotes for paths with spaces
cd "C:\Program Files\MyApp"

# ✅ Relative paths
cd ..\parent-folder
cd .\subfolder
pwsh

Environment Variables
# ❌ WRONG - Unix/Bash syntax
echo $HOME
export API_KEY=value

# ✅ CORRECT - PowerShell syntax
echo $env:USERPROFILE
$env:API_KEY = "value"

# ✅ Reading environment variables
$env:PATH
$env:TEMP
pwsh


Common Command Translations

File Operations

| Unix/Linux | PowerShell Equivalent | Notes |
|------------|----------------------|-------|
| ls | Get-ChildItem or ls | ls is an alias in PowerShell |
| cat file.txt | Get-Content file.txt | cat is an alias |
| rm file.txt | Remove-Item file.txt | rm is an alias |
| cp src dst | Copy-Item src dst | cp is an alias |
| mv src dst | Move-Item src dst | mv is an alias |
| find . -name "*.txt" | Get-ChildItem -Recurse -Filter "*.txt" | Different syntax |
| grep "pattern" | Select-String "pattern" | Different command |
| pwd | Get-Location or pwd | pwd is an alias |

Text Processing
# ❌ Unix grep
grep "error" logfile.txt

# ✅ PowerShell Select-String
Select-String "error" logfile.txt

# ❌ Unix awk/sed
cat file.txt | awk '{print $1}'

# ✅ PowerShell object manipulation
Get-Content file.txt | ForEach-Object { $_.Split()[0] }
pwsh

Process Management
# ❌ Unix ps/kill
ps aux | grep node
kill -9 1234

# ✅ PowerShell
Get-Process | Where-Object { $_.Name -like "*node*" }
Stop-Process -Id 1234 -Force
pwsh


Package Manager Commands

NPM/Node (Works the Same)
# ✅ These work identically on Windows
npm install
npm run build
npm test
node app.js
npx create-react-app my-app
pwsh

Python
# ✅ Python commands work the same
python script.py
pip install package
python -m venv venv

# Activate virtual environment (Windows-specific)
.\venv\Scripts\activate
pwsh

Git (Works the Same)
# ✅ Git commands identical on Windows
git clone https://github.com/user/repo
git add .
git commit -m "message"
git push origin main
pwsh


When to Use Different Shells

PowerShell (Default - What I'm Using)
Use for:
•  ✅ Windows-native operations
•  ✅ File system operations
•  ✅ Running Node.js/Python/Git commands
•  ✅ Most development tasks

Git Bash (If Installed)
Use for:
•  Unix shell scripts (.sh files)
•  Commands requiring Unix tools
•  When Unix syntax required

Switch to Git Bash:
# Open Git Bash from PowerShell
& "C:\Program Files\Git\bin\bash.exe"
pwsh

WSL (Windows Subsystem for Linux - If Installed)
Use for:
•  Linux-specific development
•  Docker containers (native Linux support)
•  Full Unix environment

Switch to WSL:
wsl
pwsh


PowerShell-Specific Tips

Execution Policy
# If scripts won't run, check execution policy
Get-ExecutionPolicy

# Allow local scripts (run as Administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
pwsh

Tab Completion
# PowerShell has excellent tab completion
Get-Child<TAB>     # Completes to Get-ChildItem
cd C:\Prog<TAB>    # Completes to C:\Program Files\
pwsh

Piping Objects (Not Text)
# PowerShell pipes objects, not text
Get-Process | Where-Object { $_.CPU -gt 100 } | Select-Object Name, CPU

# This is more powerful than Unix text piping
pwsh


File Encoding
# PowerShell defaults to UTF-16 for output
# Specify UTF-8 when needed

# ❌ Creates UTF-16 file
"Hello" > file.txt

# ✅ Creates UTF-8 file
"Hello" | Out-File -Encoding utf8 file.txt

# ✅ Also UTF-8
Set-Content -Path file.txt -Value "Hello" -Encoding utf8
pwsh


AI Agent Guidelines

Command Generation

When generating commands for me:

1. Always use PowerShell syntax (unless I specify otherwise)
2. Use semicolons (;) not && for command chaining
3. Use PowerShell cmdlets or their aliases
4. Use Windows paths with backslashes or forward slashes
5. Use $env:VAR for environment variables
6. Test that commands work in PowerShell 5.1

Verification Questions

Before suggesting a command, check:
•  ❓ Does this use Unix-only syntax?
•  ❓ Does this require bash/zsh?
•  ❓ Does this use && or ||?
•  ❓ Does this assume Unix paths?
•  ❓ Would this work in PowerShell 5.1?

Communication Preference

When suggesting commands:
✅ GOOD:
Here's the PowerShell command to list files:

`Get-ChildItem -Recurse -Filter "*.txt"`

This recursively searches for all .txt files in the current directory
and subdirectories.
markdown

❌ BAD:
Run: `find . -name "*.txt"`

(This is a Unix command that won't work in PowerShell)
markdown


Common Gotchas

1. Case Sensitivity
# PowerShell is case-INSENSITIVE
cd C:\users\roand  # Works
cd C:\Users\Roand  # Also works
cd C:\USERS\ROAND  # Also works
pwsh

2. Command Not Found
# If a command doesn't work, try:
Get-Command <command-name>  # Check if command exists
Get-Alias <alias>           # Check what alias maps to
pwsh

3. Long Paths
# Windows has 260-character path limit (can be enabled to 32,767)
# Use short paths or enable long path support
pwsh


Success Indicators

Commands work correctly when:
•  ✅ No "command not found" errors
•  ✅ Paths resolve correctly
•  ✅ Environment variables accessible
•  ✅ Scripts execute without permission errors
•  ✅ Output encoding is correct (UTF-8)