# Tool Registry

## Purpose

The Tool Registry maintains a mapping between tool names and their implementations.

Instead of hardcoding tool selection logic, AIFlow looks up the requested tool in the registry.

---

## Architecture

```
Tool Name

↓

Registry Lookup

↓

Tool Class

↓

Tool Instance

↓

Execute
```

---

## Example

```
calculator

↓

CalculatorTool
```

```
weather

↓

WeatherTool
```

---

## Benefits

- Easy to add new tools
- No changes required in the executor
- Centralized registration
- Supports runtime discovery

---

## Design Pattern

Registry Pattern

The registry acts as a centralized catalog of available tools.

It also supports the Open/Closed Principle by allowing new tools to be added without modifying execution logic.

---

## Current Status

Sprint 9

Currently the registry is empty.

Upcoming tools:

- CalculatorTool
- TimeTool
- WeatherTool
- SearchTool