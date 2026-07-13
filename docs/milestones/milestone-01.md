# Milestone 1 - Basic LLM Gateway

## Goal

Build a provider-independent AI Gateway capable of communicating with a local LLM.

---

## Components Completed

- FastAPI
- ChatRequest
- ChatResponse
- BaseProvider
- OllamaProvider
- ProviderFactory
- LLMGateway
- Configuration Management

---

## Design Patterns

- Factory Pattern
- Adapter Pattern
- Gateway Pattern

---

## Request Flow

Client

↓

FastAPI

↓

Gateway

↓

Factory

↓

Provider

↓

Ollama

↓

Model

↓

Provider

↓

Gateway

↓

Client

---

## What I Learned

- How an LLM is called over HTTP
- Why adapters hide provider-specific APIs
- Why factories centralize object creation
- Why gateways orchestrate requests
- How configuration is loaded using `.env`
- How FastAPI automatically converts JSON into Python objects

---

## Future Improvements

- Structured Logging
- Request IDs
- Error Handling
- Retry
- Metrics
- Streaming
- Authentication
- Multiple Providers


## Sprint 7

### Features

- Workflow Registry
- Workflow Resolver
- Prompt Repository
- Prompt Manager improvements
- Provider Request abstraction
- Prompt loading observability

### Outcome

AIFlow now supports workflow-based prompt orchestration, enabling different AI behaviors through configurable prompt directories while maintaining provider independence.

## Sprint 8

Completed

- Dynamic prompt variables
- Template rendering
- Template validation
- Global exception handling
- Structured workflow prompts

### Sprint 9

Started Tool Calling Engine

Completed

- BaseTool abstraction
- Tool Registry
- Tool Executor
- Calculator Tool
- Tool Metadata
- ToolCall model
- ToolResult model
- ProviderResponse abstraction
- Simulated provider tool calling
- ToolExecutor
- Gateway executes tool requests
- First working agent loop
- Dynamic tool argument extraction