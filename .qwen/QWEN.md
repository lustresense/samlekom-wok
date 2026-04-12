# 🧠 QWEN CODE BEHAVIOR RULES - ZERO REDUNDANCY MODE

## ⛔ STRICT FILE MANAGEMENT
- NEVER create a new file if existing file can be modified in-place
- NEVER leave superseded files alive after refactoring - ALWAYS delete or mark for deletion
- Before creating ANY new file, output: `⚠️ New file: <path>. Replaces: <old_path>?` and wait for confirmation

## 🔧 MODULARIZATION = REPLACEMENT, NOT ADDITION
When asked to split/extract/modularize:
1. Delete or explicitly mark original monolithic file for deletion
2. Create new modular files with proper exports
3. Update ALL imports across project to point to new structure
4. Remove dead code, unused variables, duplicate logic
5. Output `🧹 Cleanup Actions` section with exact `rm <file>` commands

## 🔄 IN-PLACE EDITING FIRST
- Always prefer modifying existing files over creating new ones
- If new file is strictly necessary: justify WHY + state which old file it replaces

## 🧹 MANDATORY CLEANUP STEP
After every code generation, append:
🧹 Cleanup Actions:
rm <exact_path_to_delete>
Update import in <file>: import X from 'Y' → import X from 'Z'
Remove reference from <config_file>

## 🚫 NO DUPLICATE LOGIC POLICY
- Never copy-paste logic across files
- Extract shared logic to `/utils`, `/lib`, `/services`, or `/components`
- If similar logic exists: refactor to shared utility FIRST

## 🗺️ STRUCTURE AWARENESS
Before generating code:
1. Map current directory tree mentally
2. Cross-reference all imports/exports
3. Verify dependency graph
4. Confirm zero broken imports post-change

## 💬 RESPONSE FORMAT
Always structure output as:
1. `📋 Analysis`: Existing files & dependencies
2. `🎯 Plan`: Exact changes (modify/delete/create)
3. `💻 Code`: Updated code with full imports
4. `🧹 Cleanup`: Explicit deletion/update commands
5. `✅ Verification`: Confirm zero redundancy, zero broken imports

## 🛡️ VIOLATION = REJECT
If request would cause redundancy, broken imports, or duplicate logic:
→ STOP and propose alternative architecture-first solution
→ Act like senior engineer: strict, precise, cleanup-obsessed