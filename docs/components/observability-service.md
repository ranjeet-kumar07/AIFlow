# Component: Observability Service

## Purpose

The Observability Service centralizes all AI request observability logic.

Instead of allowing the Gateway or Providers to write logs directly, they delegate observability responsibilities to this service.

This follows the Single Responsibility Principle and keeps logging concerns separate from business logic.

---

# Responsibilities

Current responsibilities:

- Log request start
- Log provider selection
- Log LLM completion
- Log request completion

Future responsibilities:

- Prometheus metrics
- Grafana metrics
- Cost tracking
- Audit events
- Distributed tracing
- OpenTelemetry integration

---

# Event Lifecycle

```
Request Started

↓

Provider Selected

↓

LLM Completed

↓

Request Completed
```

Each event represents an important stage of the AI request lifecycle.

---

# Why not log directly inside Gateway?

If logging code is placed inside the Gateway:

- Gateway becomes responsible for orchestration and logging.
- Future metrics and tracing will also need to be added there.
- The Gateway will violate the Single Responsibility Principle.

Instead:

```
Gateway

↓

ObservabilityService

↓

Logger
```

The Gateway only coordinates the request.

ObservabilityService handles monitoring.

---

# Why not log inside Providers?

Providers should only communicate with external LLMs.

They should not know:

- Prometheus
- Grafana
- Cost Tracking
- Audit Logging

Instead, Providers return data such as:

- Model
- Token Counts
- Finish Reason

The Gateway forwards this information to the Observability Service.

---

# Design Principles

- Single Responsibility Principle
- Separation of Concerns
- Delegation
- Centralized Observability

---

# Future Evolution

Current

```
Gateway

↓

ObservabilityService

↓

Logger
```

Future

```
Gateway

↓

ObservabilityService

├── Logger
├── Metrics
├── Cost Tracker
├── OpenTelemetry
├── Audit Events
└── Alerting
```

The Gateway will remain unchanged while the observability capabilities continue to grow.

---

# Interview Questions

### Why create an Observability Service?

To centralize monitoring concerns such as logging, metrics, tracing, and cost tracking instead of scattering them across the application.

---

### Why doesn't the Provider log directly?

Because the Provider's responsibility is to communicate with the external LLM.

Observability is a platform concern, not a provider concern.

---

# Revision Summary

```
Gateway

↓

Observability Service

↓

Logging

↓

(Metrics Later)

↓

(Tracing Later)

↓

(Cost Tracking Later)
```