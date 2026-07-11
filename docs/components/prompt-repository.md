# Prompt Repository

## Responsibility

Stores prompt templates outside application code.

Benefits:

- Prompt versioning
- Easier updates
- Prompt engineering without code changes
- Supports multiple workflows

Current prompts:

- system.txt
- chat.txt

## Prompt Catalog

Prompt templates are organized by workflow.

Example:

prompts/

general/

security/

summarizer/

Each workflow owns its own system prompt and chat template.

This allows different AI capabilities without changing application code.