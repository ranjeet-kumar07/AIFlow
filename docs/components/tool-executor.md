# Tool Executor

## Purpose

The Tool Executor is responsible for executing a tool dynamically at runtime.

It receives:

- Tool name
- Arguments

It looks up the tool inside the Tool Registry, creates an instance, and executes it.

---

## Flow

```
Tool Name

↓

Registry Lookup

↓

Tool Class

↓

Create Instance

↓

Execute

↓

Return Result
```

---

## Responsibilities

- Find the requested tool
- Validate that the tool exists
- Instantiate the tool
- Execute the tool
- Return the result

---

## Error Handling

If the requested tool does not exist:

```
Unknown tool: calculator
```

an exception is raised.

Future versions will convert this into a structured API response.

---

## Benefits

- Dynamic execution
- Loose coupling
- Supports unlimited tools
- No switch-case statements

---

## Design Pattern

Registry Pattern

Combined with

Factory-like runtime object creation.


# Tool Executor

## Purpose

ToolExecutor executes a ToolCall by locating the correct tool from ToolRegistry.

## Flow

ToolCall

↓

ToolRegistry

↓

Tool Instance

↓

execute(arguments)

↓

Tool Result

## Responsibility

ToolExecutor is responsible only for tool execution.

It does not decide which tool should run.
It does not decide when tools should run.

Those responsibilities belong to the provider and gateway.