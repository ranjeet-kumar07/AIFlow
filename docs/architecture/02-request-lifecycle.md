# Request Lifecycle

## Purpose

Explain how every request flows through AIFlow.

---

# Current Flow

Client

↓

FastAPI

↓

Gateway

↓

ProviderFactory

↓

Provider

↓

LLM

↓

Provider

↓

Gateway

↓

Client

---

# Future Production Flow

Client

↓

Middleware

↓

Generate Request ID

↓

Authentication

↓

Rate Limiter

↓

Logger

↓

Gateway

↓

Provider

↓

LLM

↓

Provider

↓

Metrics

↓

Logger

↓

Client

---

# Why Middleware?

Middleware performs work common to every request.

Examples

- Logging
- Request ID
- Authentication
- Rate Limiting
- Tracing

without changing business logic.

---

# Benefits

- Cleaner Gateway
- Better Separation of Concerns
- Easier Debugging
- Production Ready

current: after adding workflow
Client

↓

FastAPI

↓

LoggingMiddleware

↓

LLMGateway

↓

WorkflowResolver

↓

PromptManager

↓

ProviderRequest

↓

ProviderFactory

↓

LLM Provider

↓

Response
