# Tool Execution Flow

## Current Flow

Client

↓

Gateway

↓

Provider

↓

ToolCall

↓

ToolExecutor

↓

Tool Result

↓

Client

## Future Flow

Client

↓

Gateway

↓

Provider

↓

ToolCall

↓

ToolExecutor

↓

Tool Message

↓

Provider

↓

Final Answer

The future flow mirrors OpenAI function calling, LangChain Agents, and LangGraph.




RequestStarted

↓

WorkflowResolved

↓

ProviderSelected

↓

ToolRequested

↓

ToolExecutionStarted

↓

ToolExecutionCompleted

↓

ToolResultSentBack

↓

LLMCompleted

↓

RequestCompleted

User
  │
  ▼
POST /chat
  │
  ▼
WorkflowResolver
  │
  ▼
PromptManager
  │
  ▼
OllamaProvider
  │
  ▼
ExpressionParser
  │
  ▼
ToolRequested
  │
  ▼
CalculatorTool
  │
  ▼
ToolExecutionCompleted
  │
  ▼
PromptManager.append_tool_result()
  │
  ▼
Second LLM Call
  │
  ▼
Final Answer