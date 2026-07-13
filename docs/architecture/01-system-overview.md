## Provider Architecture

AIFlow supports multiple LLM providers through a layered architecture.

Flow:

Client Request

↓

LLMGateway

↓

ProviderFactory

↓

ProviderRegistry

↓

BaseProvider

↓

Provider Client

↓

External LLM

Benefits:

- Provider independent Gateway
- Easy provider onboarding
- Centralized configuration
- Clear separation of concerns

Request

↓

Gateway

↓

Workflow Resolver

↓

Prompt Manager

↓

Template Validator

↓

Provider Factory

↓

Provider

↓

LLM

↓

Response


## Tool Layer

```
                AI Gateway
                     │
                     ▼
              Tool Executor
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
   Calculator     Weather      Time
```

The Tool Layer provides external capabilities that can be invoked during AI workflows.

It is independent of the LLM provider implementation.

Gateway

↓

Tool Executor

↓

Tool Registry

↓

BaseTool

↓

Concrete Tool

Gateway

↓

Tool Metadata

↓

Available Tools

↓

LLM chooses Tool

↓

Tool Executor