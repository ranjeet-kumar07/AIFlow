# HTTP Request Flow

## Purpose

Explains how an HTTP request reaches the LLM and returns a response.

---

# Runtime Flow

```
HTTP Client
      │
      ▼
FastAPI
      │
      ▼
ChatRequest
      │
      ▼
LLMGateway
      │
      ▼
ProviderFactory
      │
      ▼
OllamaProvider
      │
      ▼
Ollama
      │
      ▼
ChatResponse
      │
      ▼
FastAPI
      │
      ▼
HTTP Response
```

---

# Responsibilities

## FastAPI

- Receive HTTP request
- Validate JSON
- Convert JSON into ChatRequest
- Convert ChatResponse into JSON

---

## Gateway

Coordinate request execution.

---

## Provider

Communicate with the LLM.

---

# Design Principles

- Separation of Concerns
- Layered Architecture
- Single Responsibility Principle

---

# Interview Question

Why shouldn't FastAPI call Ollama directly?

Because controllers should only handle HTTP concerns.
Business orchestration belongs in the Gateway.
Provider-specific communication belongs in the Provider.