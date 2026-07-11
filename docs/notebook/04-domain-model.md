# Domain Model Notes

## Why create internal models?

Every LLM provider has different APIs.

Instead of exposing provider-specific objects throughout the application, AIFlow defines its own internal models.

Benefits:

- Easier provider replacement
- Cleaner architecture
- Better testing
- Easier future extensions

---

## Important Models

ChatRequest

↓

PromptManager

↓

ProviderRequest

↓

Provider

↓

ProviderResponse

↓

ChatResponse

---

## Learning

Public API models should not be tightly coupled to external provider APIs.

Internal domain models protect the rest of the application from external changes.

---

## Refactoring Decision: Single ChatMessage Model

Initially the project had two message models:

- Message
- ChatMessage

This created duplication.

The project was refactored to use ChatMessage as the single internal representation.

Benefits:

- Clearer naming
- Better domain model
- No duplicate schemas
- Easier maintenance
- Consistent message flow across the platform