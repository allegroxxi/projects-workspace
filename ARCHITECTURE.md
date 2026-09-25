# Architecture: Onion Architecture

This project implements the **Onion Architecture** pattern to ensure a high degree of decoupling between core routing logic and external technical implementations (such as LLMs, vector databases, and embedding providers).

## Core Principle: Dependency Inversion
All dependencies point **inward** toward the Domain. High-level routing policies do not depend on low-level infrastructure details. Instead, the infrastructure implements interfaces (Ports) defined by the core.

