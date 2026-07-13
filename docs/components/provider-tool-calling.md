# Provider Tool Calling

## Purpose

Providers may either return a final LLM response or request execution of a tool.

During Sprint 10 this behavior is simulated using simple rules.

In later sprints, providers will map native tool-calling responses from OpenAI, Ollama, Anthropic and Gemini into the common ProviderResponse model.

## Current Flow

User

↓

Provider

↓

Rule Detection

↓

ToolCall

or

↓

ChatResponse