# Agent Loop

## Purpose

An agent does not stop after the first LLM response.

If the model requests a tool, the runtime executes it, appends the tool result to the conversation, and invokes the model again.

## Flow

User

↓

LLM

↓

Tool Call

↓

Tool Execution

↓

Tool Result

↓

LLM

↓

Final Answer

## Why

This iterative execution loop is the foundation of modern AI agent frameworks such as LangChain Agents, LangGraph, OpenAI Agents SDK, Anthropic Tool Use, and Google Gemini function calling.