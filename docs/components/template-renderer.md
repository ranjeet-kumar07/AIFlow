# Template Renderer

## Responsibility

The Template Renderer replaces placeholders inside prompt templates using runtime variables.

Example:

Template

Hello {{name}}

Variables

name = Alice

Output

Hello Alice

## Why?

Separates prompt rendering from prompt loading.

PromptRepository loads templates.

TemplateRenderer renders templates.

PromptManager orchestrates both.