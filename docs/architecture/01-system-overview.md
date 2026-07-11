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