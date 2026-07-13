# Tool Metadata

## Purpose

The Tool Metadata component exposes information about available tools without executing them.

Large Language Models use this metadata to decide which tool should be invoked.

---

## Returned Information

Each tool exposes:

- Name
- Description

Example

```
calculator
```

```
Performs arithmetic calculations.
```

---

## Flow

```
Registry

↓

Instantiate Tool

↓

Read Metadata

↓

Return List
```

---

## Why not execute?

Metadata is only used during planning.

Execution happens later through the Tool Executor.

---

## Relation to OpenAI Function Calling

OpenAI Function Calling sends nearly identical metadata to the model.

The model selects a function based on the descriptions provided.

AIFlow follows the same architectural approach.