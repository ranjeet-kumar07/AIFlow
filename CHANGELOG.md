# Changelog

## v0.1.0 (Unreleased)

### Added

- FastAPI application
- LLM Gateway
- Provider abstraction
- Ollama integration
- Prompt Manager
- ChatMessage domain model
- ProviderRequest internal model
- Logging middleware
- Request ID tracking
- Observability service

### Changed

- Refactored request flow to use PromptManager.
- Introduced ProviderRequest to separate API and provider layers.
- Unified message handling with ChatMessage.

### Notes

This release establishes the architectural foundation for AIFlow.
Future releases will add multi-provider support, streaming, memory, RAG, and agent workflows.

## v0.2.0

### Added
- ProviderRequest internal model
- Prompt pipeline integration

### Changed
- ChatRequest now accepts a prompt instead of messages
- PromptManager is now part of the runtime execution flow
- Gateway converts ChatRequest to ProviderRequest

### Architecture
- Clean separation between API DTOs and internal provider models