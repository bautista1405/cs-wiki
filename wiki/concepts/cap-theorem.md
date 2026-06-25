---
title: "CAP Theorem"
tldr: "The principle that a distributed system can only simultaneously provide two out of three guarantees: Consistency, Availability, and Partition Tolerance."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [system-design, distributed-systems]
sources: ["[[primer-donnemartin_system-design-primer]]"]
explored: false
confidence: high
---

The CAP Theorem is the baseline for all distributed database decisions.

### The Three Pillars
- **Consistency (C)**: Every read receives the most recent write or an error.
- **Availability (A)**: Every request receives a (non-error) response, without guarantee that it contains the most recent write.
- **Partition Tolerance (P)**: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

### The Trade-off
In the presence of a network partition (P), you must choose between C and A.
- **CP (Consistency & Partition Tolerance)**: The system returns an error if it cannot guarantee the most recent data (e.g., HBase, MongoDB in some configs). Use case: Bank transactions.
- **AP (Availability & Partition Tolerance)**: The system returns the most recent available data, even if it's stale (e.g., Cassandra, DynamoDB). Use case: Social media feeds.

### Related
- See [[system-design]] for how to apply this in interviews.

## Counter-arguments
TBD

## Data gaps
TBD