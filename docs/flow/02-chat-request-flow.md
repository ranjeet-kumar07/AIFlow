# Chat Request Flow

## Purpose

This document explains how an AI request travels through AIFlow.

---

# Runtime Flow

```
Client

↓

LLMGateway

↓

ProviderFactory

↓

Provider

↓

LLM

↓

Provider

↓

ChatResponse

↓

Gateway

↓

Client
```

---

# Components

- Client
- LLMGateway
- ProviderFactory
- BaseProvider
- OllamaProvider
- Ollama Server

---

# Responsibilities

## Gateway

Coordinates request execution.

Does not know provider implementation.

---

## Factory

Chooses the correct provider.

---

## Provider

Communicates with a specific LLM.

---

## LLM

Generates the response.

---

# Design Patterns

- Gateway Pattern
- Factory Pattern
- Adapter Pattern

---

# Future Flow

Later this flow becomes

```
Client

↓

Gateway

↓

Authentication

↓

Rate Limiter

↓

Prompt Builder

↓

RAG

↓

Tool Calling

↓

Agent

↓

Provider

↓

LLM
```

without changing the client.

---

# Interview Questions

Why introduce Gateway?

Because orchestration responsibilities should be separated from provider implementation.

Gateway becomes the central location for logging, metrics, retries, tracing, rate limiting, authentication, and future AI workflows.


Append:

```md
## Validation Failure Flow

Client

↓

WorkflowResolver

↓

PromptRepository

↓

TemplateValidator

↓

TemplateValidationError

↓

Global Exception Handler

↓

HTTP 400