# Tool Call

## Purpose

A Tool Call represents a request from the LLM to execute a specific tool.

It contains:

- Tool name
- Arguments

The Tool Executor consumes this object to invoke the requested tool.

---

## Example

```json
{
  "tool_name": "calculator",
  "arguments": {
    "expression": "25*8"
  }
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

Tool Result

↓

LLM

---

## Why?

Using a dedicated ToolCall model standardizes communication between providers and tools.

Different LLM providers may return different formats, but AIFlow converts them into a common internal representation.