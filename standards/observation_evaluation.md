---
name: observation_evaluation.md
description: Decoupling discovery from decision-making.
type: project
---

# 🎲 Observation-Evaluation Protocol

This protocol decouples non-deterministic environmental discovery from deterministic decision-making logic.

**Why:** To maintain a clear boundary between the non-deterministic "discovery" of the environment and the deterministic "processing," ensuring that while exploration is fluid, the system's decision-making remains testable and robust.

**How to apply (The Hand-off):**

*   **Observation (Agentic):** Agents are responsible for the non-deterministic discovery of state, codebase exploration, and real-time research. They provide the **Raw Observations** (the "What").
*   **Evaluation (Python):** All formal reasoning, semantic scoring, heuristic-based routing, and decision-making logic MUST be implemented as robust, testable Python code. This code processes observations to produce **Structured Insights** (the "So What").
