# ChatRequest

## Definition

ChatRequest is AIFlow's internal request model.

It represents a provider-independent request sent to the LLM Gateway.

## Why do we need it?

Every LLM provider has a different API.

Instead of exposing provider-specific payloads to clients, AIFlow defines a standard request model.

This keeps business logic independent from LLM providers.

## Fields

- model
- messages
- temperature
- max_tokens