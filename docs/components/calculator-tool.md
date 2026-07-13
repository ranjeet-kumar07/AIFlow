# Calculator Tool

## Purpose

The Calculator Tool performs arithmetic calculations on behalf of the AI system.

Instead of relying on the LLM to compute mathematical expressions, AIFlow delegates the task to this tool.

---

## Responsibilities

- Accept an arithmetic expression
- Evaluate the expression
- Return the result as text

---

## Example

Input

```
{
    "expression": "25 * 4"
}
```

Output

```
100
```

---

## Flow

```
Gateway

↓

Tool Executor

↓

Calculator Tool

↓

Result

↓

LLM
```

---

## Current Implementation

The current implementation uses Python's `eval()` with restricted built-ins for educational purposes.

This is sufficient for learning the tool architecture but should not be used in production.

Future versions will replace it with a safe expression parser.

---

## Interview Notes

Why use a Calculator Tool instead of asking the LLM?

Large Language Models are optimized for reasoning and language generation, not deterministic computation.

Delegating arithmetic to a tool guarantees consistent and accurate results while reducing hallucinations.