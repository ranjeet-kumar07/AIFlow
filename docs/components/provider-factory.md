# Component: Provider Factory

## Purpose

The Provider Factory is responsible for selecting the correct LLM provider.

The Gateway never creates provider objects directly.

Instead it delegates provider creation to the factory.

---

# Current Providers

- Ollama
- OpenAI (placeholder)

Future:

- Gemini
- Claude
- Azure OpenAI
- Bedrock

---

# Why use a Factory?

Without a factory:

Gateway

↓

new OllamaProvider()

Tomorrow adding OpenAI requires changing Gateway.

With a factory:

Gateway

↓

ProviderFactory

↓

Correct Provider

Gateway never changes.

---

# Design Pattern

Factory Pattern

The factory encapsulates object creation.

Clients request an abstraction instead of creating concrete implementations.

---

# Benefits

- Loose coupling
- Easy testing
- Easy provider replacement
- Extensible architecture

---

# Interview Question

Why use a Factory instead of directly creating providers?

Answer:

The Factory centralizes provider creation and removes provider-specific dependencies from the Gateway, making it easy to introduce new providers without modifying business logic.

# Provider Factory

## Responsibility

The ProviderFactory selects the correct LLM provider based on application configuration.

## Registry Pattern

Instead of maintaining a growing chain of conditional statements, AIFlow uses a provider registry.

Benefits:

- Easy to add new providers.
- Factory remains unchanged.
- Better separation of responsibilities.

Flow:

Gateway

↓

ProviderFactory

↓

Provider Registry

↓

Provider Instance

## Supported Providers

The Provider Registry maps provider names to their implementations.

Current providers:

- OllamaProvider
- OpenAIProvider

New providers can be added by:

1. Implementing `BaseProvider`
2. Creating the corresponding Client
3. Registering the provider in `PROVIDER_REGISTRY`

No changes to the Gateway are required.