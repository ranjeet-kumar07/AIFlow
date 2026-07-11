# AIFlow Domain Model

## Why a Domain Model?

AIFlow is an AI Platform.

Instead of letting every provider define its own request and response format, AIFlow defines its own internal domain model.

This isolates the rest of the application from provider-specific APIs.

---

# High Level Flow

Client

↓

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

# Core Domain Objects

## 1. ChatRequest

Represents an incoming API request.

Responsibilities:

- User prompt
- Selected model
- Request options

---

## 2. ChatMessage

Represents a single message exchanged with an LLM.

Examples:

- System Message
- User Message
- Assistant Message
- Tool Message

---

## 3. PromptManager

Builds the final list of messages.

Current:

System Prompt

+

User Prompt

Future:

System Prompt

+

Conversation History

+

Retrieved Documents

+

Tool Results

+

User Prompt

---

## 4. ProviderRequest

Represents AIFlow's internal request before converting it into a provider-specific request.

Future fields may include:

- messages
- temperature
- max_tokens
- tools
- response_format
- metadata

---

## 5. Provider

Responsible only for communicating with external LLM providers.

Examples:

- Ollama
- OpenAI
- Gemini
- Claude

Providers never build prompts.

Providers never perform RAG.

Providers never manage memory.

---

## 6. ProviderResponse

Represents the provider's raw response.

Contains information such as:

- generated text
- token usage
- finish reason
- model

---

## 7. ChatResponse

The response returned by AIFlow to API clients.

This hides provider-specific implementation details.

---

# Future Domain Objects

Conversation

Memory

Retriever

Embedding

VectorDocument

ToolCall

ToolResult

AgentPlan

AgentStep

AuditEvent

CostRecord

---

# Design Principles

- Single Responsibility Principle
- Provider Independence
- Clear Layer Separation
- Extensible Domain Model

---

# Architecture Diagram

Client

↓

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

The Gateway orchestrates this entire flow.

Every other component has one responsibility.

---

# ProviderRequest

ProviderRequest is an internal domain model.

It separates the public API (ChatRequest) from provider-specific communication.

Benefits:

- Public API can evolve independently.
- Providers receive a consistent internal request.
- Easier provider replacement.
- Cleaner architecture.

Flow:

Client

↓

ChatRequest

↓

Gateway

↓

ProviderRequest

↓

Provider