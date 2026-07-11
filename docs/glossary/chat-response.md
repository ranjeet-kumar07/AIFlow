# ChatResponse

## Definition

ChatResponse is AIFlow's provider-independent response model.

Every LLM provider response is converted into this format before being returned to the application.

## Why?

Different providers expose different response payloads.

ChatResponse hides those differences and provides a stable contract for all downstream modules.

## Used By

- Evaluation
- Memory
- RAG
- Agent
- Workflow Engine
- Observability
- UI