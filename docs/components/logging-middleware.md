# Component: Logging Middleware

## Responsibility

Intercept every HTTP request before it reaches the application.

## Input

HTTP Request

## Output

HTTP Response

## Responsibilities

- Generate Request ID
- Store Request Context
- Measure Latency
- Log Incoming Request
- Log Outgoing Response
- Add X-Request-ID header

## Why Middleware?

Cross-cutting concerns should not be duplicated across controllers or business logic.

## Future Enhancements

- User ID
- Tenant ID
- Correlation ID
- Trace ID
- Distributed Tracing
- Request Size
- Response Size