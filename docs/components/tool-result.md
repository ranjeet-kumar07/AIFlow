# Tool Result

## Purpose

Represents the output produced after executing a tool.

It is returned by ToolExecutor and can later be supplied back to the LLM.

---

## Example

```json
{
  "tool_name": "calculator",
  "result": "42"
}
```

---

## Flow

LLM

↓

ToolCall

↓

ToolExecutor

↓

ToolResult

↓

LLM

---

## Why?

Using a common ToolResult model allows every tool to expose a consistent interface regardless of its internal implementation.