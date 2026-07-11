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