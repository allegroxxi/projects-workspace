---
name: agent-protocols.md
description: The Optimized Agentic Orchestration Workflow (v2).
type: project
---

# 🤖 Agentic Orchestration Workflow (v2)

This protocol manages complex development cycles by balancing efficiency and rigor through specialized sub-agents and structured phases.

## 🚀 Workflow Phases

### Phase 1: Decomposition & Ownership (Planning)
*   **Goal:** CoT decomposition into a DAG of atomic sub-tasks.
*   **Mechanism:** Assign explicit **File-Level Ownership** to sub-agents to prevent write conflicts.
*   **Guideline:** All classes must be placed in their own files to reduce token usage and improve modularity.
*   **Loop Prevention:** Ensure each task has clear boundaries and completion criteria to avoid infinite recursion or redundant work.

### Phase 2: Parallel Execution & Hybrid Relay (Execution)
*   **Mechanism:** Spawn specialized sub-agents (e.g., `Researcher`, `Coder`).
*   **Relay:** Use distilled findings via tags to minimize token overhead.
*   **Loop Prevention:** Implement explicit timeout mechanisms and progress tracking to prevent agents from getting stuck in loops.

### Phase 3: Red-Teaming (Adversarial Review)
*   **Requirement:** A specialized Reviewer with a contrarian persona performs an adversarial pass.
*   **Goal:** Identify edge cases, logical vulnerabilities, and potential failure modes.
*   **Loop Prevention:** Apply systematic review techniques to avoid confirmation bias and ensure comprehensive testing.
*   **Example:** When reviewing a new function, the adversarial reviewer might ask "What if this function receives invalid input?" or "How would this behave under extreme load?"

### Phase 4: Verification (Validation)
*   **Action:** Atomic application $\rightarrow$ Project-standard lint/test $\rightarrow$ Outcome reporting.
*   **Loop Prevention:** Implement automated testing and validation checks to prevent regression issues from being reintroduced.
