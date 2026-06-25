---
title: API Design Patterns
date: 2026-05-11
tags: [api, architecture, communication]
explored: false
confidence: high
---

# API Design Patterns

Designing an API involves choosing the right communication protocol, versioning strategy, and data validation approach to ensure maintainability and scalability.

## Communication Protocols

Different use cases require different protocols:

- **REST (Representational State Transfer)**:
    - The industry standard for public APIs.
    - Uses HTTP methods (GET, POST, PUT, DELETE) and status codes.
    - Focuses on resources identified by URIs.
- **GraphQL**:
    - Ideal for complex data graphs where clients need specific subsets of data.
    - Solves over-fetching and under-fetching by allowing clients to define the response shape.
    - Implemented in Nest.js via `@nestjs/graphql`.
- **gRPC (Google Remote Procedure Call)**:
    - A high-performance binary protocol using Protocol Buffers.
    - Best suited for internal microservices communication due to its efficiency and strict typing.

## Versioning Strategies

Preventing breaking changes is critical for API evolution:

- **URI Versioning**: (e.g., `/v1/resource`) The most common and explicit method.
- **Header Versioning**: Uses a custom header (e.g., `X-API-Version`) to specify the version.
- **Media Type Versioning**: Uses the `Accept` header to negotiate the version.

## Data Validation and DTOs

To ensure data integrity, APIs use **DTOs (Data Transfer Objects)**:

- **Purpose**: DTOs define the shape of data for incoming requests, separating the internal domain model from the external API contract.
- **Validation**: In Nest.js, the `ValidationPipe` combined with `class-validator` and `class-transformer` allows for automatic, declarative validation of payloads.

## Controller Architecture: Thin vs. Fat

The debate over where business logic should reside affects the maintainability of the codebase:

- **Thin Controllers (Recommended)**: Controllers only handle request translation, validation, and call the service layer. This maximizes reuse and testability.
- **Fat Controllers (Anti-pattern)**: Controllers containing business logic. This leads to code duplication and makes integration testing difficult.

## Bias Checks & Trade-offs

- **Simplicity vs. Strict Typing**: While strict DTOs and validation provide safety, they increase the amount of boilerplate code required for every new endpoint.
- **Protocol Overheads**: gRPC provides performance but sacrifices the human-readability and ease of testing provided by REST/JSON.

## Related Concepts
- [[nest-js]]
- [[node-js-backend]]
- Source: [[nest-js-2026-api-design-research]]
