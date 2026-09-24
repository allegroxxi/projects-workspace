---
name: editing.md
description: Safe and reliable text replacement strategies.
type: feedback
---

# 🛠️ File Editing Protocol

**Goal**: To modify codebase files safely and reliably by avoiding brittle text-replacement errors.

**Why**: Using `edit` with large blocks of text or empty `old_string` is highly fragile and leads to "zero occurrences found" errors due to subtle whitespace or newline mismatches.

**How to apply (Decision Tree)**:

1.  **Is the change small and targeted (< 10 lines)?**
    *   ✅ **YES**: Use `edit`.
        *   *Requirement*: Include at least 3 lines of context *before* and *after* the target text to ensure uniqueness and precision.
2.  **Is the change large (> 10 lines) or structural?**
    *   ✅ **YES**: Use `write_file`. Overwriting the target section or file is safer than hunting for non-existent strings.
3.  **Did an `edit` attempt fail?**
    *   ⚠️ **DO NOT REPEAT THE SAME ATTEMPT.** Follow this recovery sequence:
        1.  **Ingest Current State**: Use `read_file` to pull the absolute latest version of the file.
        2.  **Verify Content**: Check for exact whitespace, indentation, or recent changes by others.
        3.  **Attempt Incremental Fix**: Try a much smaller, more focused `edit` block.
        4.  **Fallback to Hard Reset**: If incremental edits fail, use `write_file` for the entire target section/file to ensure integrity.
