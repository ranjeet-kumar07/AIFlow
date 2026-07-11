# Settings Loading Flow

## Purpose

This document explains how AIFlow loads application configuration from the `.env` file during startup and makes it available to all components.

---

# Business Problem

Different environments require different configuration values.

Example:

Development
- Ollama running on localhost

Testing
- Shared Ollama server

Production
- Internal Ollama cluster

Hardcoding these values inside the application would require code changes for every environment.

Instead, AIFlow externalizes configuration into `.env`.

---

# Components Involved

- .env
- Settings (Pydantic BaseSettings)
- settings.py
- Application Startup
- OllamaProvider

---

# Runtime Flow

```
Application Starts

        │

        ▼

main.py

        │

        ▼

Import settings

        │

        ▼

settings.py

        │

        ▼

Settings()

        │

        ▼

BaseSettings

        │

        ▼

Read .env

        │

        ▼

Validate Configuration

        │

        ▼

Create Settings Object

        │

        ▼

Application Uses settings
```

---

# Step-by-Step Execution

## Step 1

The application starts.

Example:

```
uvicorn app.main:app --reload
```

---

## Step 2

Python imports `app.config.settings`.

---

## Step 3

Python executes `settings.py` from top to bottom.

---

## Step 4

The `Settings` class is created.

At this point, no configuration has been loaded.

---

## Step 5

Python executes:

```python
settings = Settings()
```

---

## Step 6

`BaseSettings` checks the configured environment file.

```python
class Config:
    env_file = ".env"
```

---

## Step 7

Pydantic opens `.env`.

Example:

```
OLLAMA_BASE_URL=http://localhost:11434
```

---

## Step 8

Configuration values are validated.

Example:

```
OLLAMA_BASE_URL → string
```

If validation fails, application startup fails immediately.

This follows the **Fail Fast Principle**.

---

## Step 9

A Settings object is created.

Example:

```python
settings.OLLAMA_BASE_URL
```

returns

```
http://localhost:11434
```

---

## Step 10

Every component imports the same Settings object.

Example:

```
OllamaProvider

↓

settings.OLLAMA_BASE_URL

↓

http://localhost:11434
```

No component reads `.env` directly.

---

# Why Load Configuration Once?

Loading configuration for every request would repeatedly:

- Open the file
- Parse the file
- Validate values
- Create objects

Instead, AIFlow loads configuration once during startup and reuses the same Settings object throughout the application's lifetime.

This improves performance and keeps configuration centralized.

---

# Failure Points

## Missing .env

Application uses default values (if defined) or fails if required values are missing.

---

## Invalid Configuration

Example:

```
REQUEST_TIMEOUT=abc
```

If the field expects an integer, application startup fails with a validation error.

---

## Missing Required Variable

If a required configuration value has no default and is absent from `.env`, startup fails.

---

# Design Principles

- Externalized Configuration
- Fail Fast
- Single Source of Truth
- Centralized Configuration Management

---

# Future Configuration

Later milestones will extend the Settings object with:

- OpenAI API Key
- Anthropic API Key
- Default Model
- Default Provider
- Request Timeout
- Retry Count
- Logging Level
- Database URL
- Redis URL

No application code will change.

Only `.env` will change.

---

# Interview Questions

## Why use `.env`?

To separate configuration from application code and support multiple deployment environments.

---

## Why use Pydantic Settings?

- Validation
- Type Safety
- Default Values
- Centralized Configuration
- Startup Validation

---

## Why shouldn't every component read `.env`?

Configuration should be loaded once and shared across the application to avoid duplication, repeated file I/O, and inconsistent configuration handling.

---

# Revision Summary

```
Application Starts
        ↓
Import settings.py
        ↓
Settings()
        ↓
Read .env
        ↓
Validate
        ↓
Create Settings Object
        ↓
Reuse Everywhere
```