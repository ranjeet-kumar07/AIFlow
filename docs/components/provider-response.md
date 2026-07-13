# Provider Response

## Purpose

ProviderResponse represents the unified output returned by every LLM provider.

Instead of exposing provider-specific APIs, AIFlow converts them into a common structure.

---

## Possible Responses

### Normal completion

```
ProviderResponse
 └── ChatResponse
```

### Tool request

```
ProviderResponse
 └── ToolCall
```

---

## Why?

Different LLM vendors expose different APIs for tool calling.

ProviderResponse standardizes them into one internal model.