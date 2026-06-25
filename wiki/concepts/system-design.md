---
title: "System Design"
tldr: "Comprehensive synthesis of system design principles, scaling strategies, and interview patterns."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [architecture, scalability, system-design]
sources: ["[[donnemartin-system-design-primer]]", "[[bytebytego-system-design-intro]]"]
explored: false
confidence: high
---

# System Design

System design is the architectural process of defining the components, modules, and interfaces of a system to satisfy specific requirements of scalability, reliability, and maintainability.

## Core Architectural Pillars
- **Horizontal vs Vertical Scaling**: Moving from adding power to a single machine to adding more machines to a pool.
- **CAP Theorem**: The trade-off between Consistency, Availability, and Partition Tolerance.
- **Load Balancing**: Using algorithms (Round Robin, Least Connections) to distribute traffic.
- **Database Selection**: Choosing between Relational (SQL) for ACID compliance vs NoSQL for high availability and flexible schemas.

## Detailed Source Synthesis
### Source: donnemartin-system-design-primer.md


### Source: bytebytego-system-design-intro.md


### Source: primer-donnemartin_system-design-primer.md


### Source: bytebytego-courses_system-design-interview_introduction.md


## Counter-arguments
- **Over-engineering**: The danger of designing for "Google scale" when the actual user base is small, leading to excessive complexity.

## Data gaps
- Current real-world benchmarks for 2026-era serverless architectures are sparsely documented.
