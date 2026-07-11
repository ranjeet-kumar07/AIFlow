# Prompt Management Notes

## What is a System Prompt?

A system prompt gives the AI its behavior and instructions.

Examples:

- You are a helpful assistant.
- Answer in JSON.
- Never reveal confidential information.
- Respond in a professional tone.

The user does not normally see the system prompt.

---

## Why use a Prompt Manager?

Instead of building prompts in multiple places, the Prompt Manager centralizes prompt construction.

Benefits:

- Reusable
- Consistent
- Easier to maintain
- Easier to test

---

## Learning

System Prompt defines behavior.

User Prompt contains the user's request.

Later we will combine:

System Prompt

+

User Prompt

+

Conversation History

+

Retrieved Documents

+

Tool Results

into one final prompt.

---

## Why Message-Based Prompts?

Instead of creating one large prompt string, modern LLM APIs use structured messages.

Advantages:

- Clear separation of system and user instructions.
- Easy to add conversation history.
- Easy to inject retrieved knowledge.
- Easy to include tool outputs.
- Portable across multiple providers.

This approach is the foundation for chat-based AI systems.

## Prompt Repository

PromptRepository is responsible for loading prompt templates from disk.

PromptManager is responsible for assembling prompts into chat messages.

Separating these responsibilities follows the Single Responsibility Principle and makes prompt storage independent from prompt construction.

## External Prompt Templates

System prompts and chat templates are stored as files rather than Python constants.

Benefits:

- Prompt engineers can update prompts without modifying application logic.
- Prompt templates become version-controlled assets.
- The application becomes easier to extend with new workflows.

## Prompt Catalog

Prompt templates can be grouped into workflow folders.

Examples:

- general
- security
- summarizer

This enables multiple AI capabilities while reusing the same PromptManager and Provider architecture.

## Workflow-aware PromptManager

PromptManager no longer assumes a single prompt.

Instead, it receives the workflow as an input and loads the corresponding prompt templates.

This design follows the Open/Closed Principle by allowing new workflows without modifying existing logic.