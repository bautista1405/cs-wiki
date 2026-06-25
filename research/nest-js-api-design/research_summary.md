# Research: Nest.js API Design & Architecture

## 1. Nest.js Architecture
### Modular Architecture
Nest.js is built around the concept of Modules. A module is a class annotated with @Module() which organizes the application's structure.
- Modules encapsulate related controllers and providers.
- The Root Module is the starting point of the application.
- Feature Modules allow for a decoupled, domain-driven structure.

### Dependency Injection (DI)
Nest.js uses a powerful DI container. 
- Providers: Classes annotated with @Injectable() that can be shared across the app.
- DI manages the instantiation and lifecycle of these providers, promoting loose coupling and easier testing (mocking).

### Core Components:
- Controllers: Handle incoming requests and return responses. They define the API endpoints.
- Providers: The business logic layer. Services are the most common providers.
- Modules: The glue that binds controllers and providers together.

---

## 2. API Design Best Practices

### Communication Protocols
- REST: The default. Uses HTTP methods, status codes, and resources. Path-based versioning common in Nest.js.
- GraphQL: Integrated via @nestjs/graphql. Great for reducing over-fetching and under-fetching. Uses a schema-first or code-first approach.
- gRPC: High-performance, binary protocol using Protocol Buffers. Ideal for microservices communication.

### Versioning Strategies
- URI Versioning: `/v1/resource` (Most common).
- Header Versioning: Custom header like `X-API-Version`.
- Media Type Versioning: Using the `Accept` header.

### Error Handling & Validation
- DTOs (Data Transfer Objects): Define the shape of data for requests.
- ValidationPipe: Uses `class-validator` and `class-transformer` to automatically validate incoming payloads against DTOs.
- Exception Filters: Custom filters to catch specific exceptions and format the response consistently across the API.
- Interceptors: Used to transform the response or handle cross-cutting concerns (logging, caching).

### Security
- Passport.js: The standard for authentication in Nest.js.
- JWT (JSON Web Tokens): Used for stateless authentication.
- Guards: Determine if a request should be processed based on conditions (e.g., @UseGuards(AuthGuard)).

---

## 3. Performance Scaling in Node.js/Nest.js

### Event Loop Optimization
- Avoid blocking the event loop with heavy synchronous operations.
- Use `Worker Threads` for CPU-intensive tasks.
- Offload long-running tasks to a message queue (BullMQ).

### Clustering & Scaling
- Node.js Cluster Module: Create multiple instances of the app to utilize multi-core CPUs.
- Kubernetes/Docker: Horizontal scaling of pods.
- Load Balancers: Distribute traffic across multiple instances.

### Asynchronous Patterns
- Use `async/await` consistently to avoid "callback hell".
- Promise.all() for parallel execution of independent tasks.
- RxJS: Nest.js heavily utilizes Observables for streaming and complex async event handling.

---

## 4. Real-World Design Patterns

### Clean Architecture / Hexagonal Architecture
In Nest.js, this is implemented by strictly separating layers:
1. API Layer (Controllers): Purely for routing and request translation.
2. Application Layer (Services/Use Cases): Orchestrates the business logic.
3. Domain Layer (Entities/Value Objects): Pure business rules, independent of the framework.
4. Infrastructure Layer (Repositories/Adapters): Implementation of database access, external API clients.

### Design Pattern Controversies: "Thin" vs "Fat" Controllers
- Thin Controllers (Recommended): Controllers only handle request validation and call the service layer. Business logic resides in services. This ensures testability and reuse.
- Fat Controllers (Anti-pattern): Business logic embedded in the controller. Leads to duplication and hard-to-maintain code.

---

## Summary for Wiki Concepts

### [[nest-js]]
- Focus on: Modules, DI, Controllers, Providers, and the framework's influence from Angular.

### [[api-design-patterns]]
- Focus on: REST vs GraphQL vs gRPC, Versioning, DTOs, Validation, and Exception handling.

### [[node-js-backend]]
- Focus on: The event loop, clustering, asynchronous patterns with RxJS, and infrastructure scaling.
