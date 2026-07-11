# Observability Notes

## What is Observability?

Observability is the ability to understand what is happening inside a running system.

It helps engineers answer questions like:

- Why is the request slow?
- Which provider handled the request?
- How many tokens were consumed?
- Which request failed?
- Where did the failure occur?

---

## Three Pillars of Observability

### 1. Logging

Records important events.

Example:

- Request Started
- Provider Selected
- LLM Completed
- Request Completed

---

### 2. Metrics

Numerical measurements.

Examples:

- Requests/sec
- Average Latency
- Token Usage
- Error Rate

Usually collected by Prometheus.

---

### 3. Tracing

Shows how one request flows through multiple services.

Example:

Client

↓

Gateway

↓

Retriever

↓

LLM

↓

Tool

↓

Database

Each step has its own latency.

---

## Why ObservabilityService?

Instead of every component writing logs directly, all observability responsibilities are centralized.

Benefits:

- Single Responsibility Principle
- Easy to extend
- Supports logging, metrics and tracing
- Gateway remains focused on orchestration

---

## Event Lifecycle

RequestStarted

↓

ProviderSelected

↓

LLMCompleted

↓

RequestCompleted

---

## Learning

Providers produce information.

Gateway orchestrates.

ObservabilityService records what happened.

Each component has one responsibility.