# Client Layer

## Responsibility

The Client layer is responsible for communicating with external LLM APIs.

Responsibilities:

- HTTP communication
- Timeouts
- Authentication
- Retry (future)
- Connection reuse (future)

The Provider layer never performs HTTP requests directly.

Flow:

Gateway

↓

Provider

↓

Client

↓

External API

## Why separate Client from Provider?

The Provider is responsible for AI-specific business logic.

The Client is responsible for communication with external APIs.

Benefits:

- Easier testing
- Reusable network layer
- Centralized authentication
- Centralized retry logic
- Supports SDKs and REST APIs uniformly