# Component: Prompt Manager

## Purpose

The Prompt Manager is responsible for preparing prompts before they are sent to the LLM.

Instead of allowing every API or service to manually build prompts, all prompt construction is centralized.

---

# Responsibilities

Current:

- Provide the default system prompt.

Future:

- Prompt templates
- Prompt versioning
- Dynamic variables
- Persona management
- A/B testing
- Prompt validation

---

# Why not hardcode prompts everywhere?

If prompts are scattered across the application:

- Difficult to update
- Difficult to test
- Inconsistent AI behavior

Centralizing prompt creation makes maintenance easier and keeps responses consistent.

---

# Design Principle

Single Responsibility Principle

The Gateway coordinates requests.

The Provider communicates with the LLM.

The Prompt Manager constructs prompts.

---

# Future Architecture

User Prompt

↓

Prompt Manager

↓

System Prompt

↓

Conversation History

↓

RAG Context

↓

Tool Results

↓

Provider

---

# Message-Based Prompt Construction

The Prompt Manager builds a list of messages instead of concatenating strings.

Current structure:

```text
System Message

↓

User Message
```

Future structure:

```text
System Message

↓

Conversation History

↓

Retrieved Context (RAG)

↓

Tool Results

↓

User Message
```

This design aligns with modern chat-based LLM APIs and makes future features easier to add without redesigning the prompt flow.