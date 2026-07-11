# Workflow Registry

## Responsibility

The Workflow Registry is the central catalog of all AI workflows supported by AIFlow.

It maps a workflow name to its configuration.

Example:

```python
{
    "general": {
        "description": "...",
        "prompt_directory": "general"
    }
}
```

## Why?

Without a registry, every component would hardcode workflow names.

Instead, all workflow metadata lives in one place.

## Current Metadata

- description
- prompt_directory

Future metadata may include:

- default model
- temperature
- tools
- RAG enabled
- guardrails