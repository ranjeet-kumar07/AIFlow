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

## Prompt Loading Flow

PromptManager no longer stores prompt text.

Instead it:

1. Loads templates from PromptRepository
2. Replaces template variables
3. Creates ChatMessage objects

This separates prompt storage from prompt assembly.

## Workflow Selection

PromptManager accepts a workflow name.

The workflow determines which prompt templates are loaded.

Examples:

- general
- security
- summarizer

This enables multiple AI capabilities while reusing the same PromptManager.

## Current Responsibilities

PromptManager now performs:

1. Loads system prompt
2. Loads chat template
3. Replaces template variables
4. Builds ChatMessage objects
5. Emits prompt loading observability events