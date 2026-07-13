# Base Tool

## Purpose

`BaseTool` defines the common contract for every executable tool inside AIFlow.

A tool represents an external capability that an LLM can use to accomplish tasks it cannot reliably perform by itself.

Examples include:

- Calculator
- Current Time
- Weather
- Elasticsearch Search
- SQL Query
- Jira Lookup
- GitHub Repository Search
- Vulnerability Scanner

Every tool must implement the same interface, allowing AIFlow to execute them without knowing their concrete implementation.

---

## Architecture

```
                BaseTool
                    │
        ┌───────────┼────────────┐
        │           │            │
CalculatorTool   TimeTool   WeatherTool
        │           │            │
        └───────────┼────────────┘
                    │
             Tool Executor
                    │
                 AI Gateway
```

---

## Responsibilities

Every tool must provide:

### name()

Returns the unique identifier of the tool.

Example:

```
calculator
```

This identifier is used by the Tool Registry and eventually by the LLM when selecting a tool.

---

### description()

Returns a human-readable description explaining what the tool does.

Example:

```
Performs arithmetic calculations.
```

Future LLM providers such as OpenAI use this description when deciding whether a tool should be invoked.

---

### execute(arguments)

Executes the business logic of the tool.

Input:

```
{
    "expression": "25 * 4"
}
```

Output:

```
100
```

The implementation is completely hidden behind the BaseTool interface.

---

## Why use an interface?

Without a common interface:

```
Calculator.calculate()

Weather.getWeather()

Time.now()

Search.find()
```

Every tool has a different API.

With BaseTool:

```
tool.execute(arguments)
```

The Tool Executor never needs to know which tool it is executing.

This follows the Open/Closed Principle.

- Open for extension
- Closed for modification

New tools can be added without changing existing application logic.

---

## Relationship with Provider Architecture

AIFlow uses the same architectural pattern for providers and tools.

```
BaseProvider
    │
    ├── OllamaProvider
    └── OpenAIProvider
```

```
BaseTool
    │
    ├── CalculatorTool
    ├── TimeTool
    ├── WeatherTool
    └── SearchTool
```

Both rely on polymorphism.

---

## Current Status

Sprint 9

Current abstraction:

- BaseTool

Upcoming implementations:

- CalculatorTool
- TimeTool
- WeatherTool
- SearchTool

Future enterprise tools:

- Elasticsearch Tool
- SQL Tool
- Redis Tool
- Kubernetes Tool
- GitHub Tool
- Jira Tool
- HexaShield Scan Tool

---

## Interview Notes

### Why introduce BaseTool instead of calling functions directly?

A common interface allows the AI runtime to execute any capability without depending on a specific implementation.

This improves extensibility, testing, maintainability, and supports runtime tool discovery.

### Which design pattern is used?

- Strategy Pattern
- Polymorphism
- Dependency Inversion Principle

### How does LangChain relate?

LangChain provides its own `BaseTool`.

AIFlow implements the same architectural concept manually to understand the underlying design before introducing LangChain.