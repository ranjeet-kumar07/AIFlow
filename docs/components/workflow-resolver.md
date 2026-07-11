# Workflow Resolver

The WorkflowResolver determines which workflow should handle an incoming request.

Currently every request resolves to:

general

In future versions it can route requests based on:

- endpoint
- user role
- request metadata
- AI capability
- feature flags

This keeps routing logic separate from the Gateway.

# Workflow Resolver

## Responsibility

Converts an incoming ChatRequest into a workflow configuration.

Input:

- ChatRequest

Output:

- Workflow configuration dictionary

## Responsibilities

- validates workflow exists
- loads workflow metadata
- prevents unsupported workflows

## Why?

The gateway should not know how workflows are configured.

The resolver isolates workflow lookup from business logic.