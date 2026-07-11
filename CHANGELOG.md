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