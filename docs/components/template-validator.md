# Template Validator

## Responsibility

Ensures every placeholder inside a prompt template has a corresponding runtime variable.

Example

Template

{{language}}

{{framework}}

Variables

language = Java

Result

Validation Error

Missing variable:

framework

## Why?

Fail fast before sending incomplete prompts to the LLM.