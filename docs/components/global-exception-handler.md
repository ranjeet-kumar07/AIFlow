# Global Exception Handler

## Purpose

Converts internal exceptions into consistent HTTP responses.

Instead of returning Python stack traces, AIFlow returns structured JSON.

Example:

```json
{
  "error": "Template validation failed",
  "missing_variables": [
    "framework",
    "language"
  ]
}