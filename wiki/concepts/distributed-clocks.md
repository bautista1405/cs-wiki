---
title: "Distributed Clocks"
tldr: "Mechanisms to order events in a distributed system where physical clocks cannot be perfectly synchronized."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [distributed-systems, coordination]
sources: ['[[primer-system-design-primer]]']
explored: false
confidence: high
---

Physical clocks drift across nodes, making 'wall clock time' unreliable for event ordering.

### Lamport Timestamps
Assigns a simple counter to each event. If $a 
ightarrow b$ (a happened before b), then $L(a) < L(b)$. Great for partial ordering but cannot prove a cause-effect relationship if timestamps are identical.

### Vector Clocks
Each node maintains an array of clocks for all other nodes. This allows a system to detect **causal violations** (concurrence). If two events have clocks that are not comparable, they happened concurrently.

### Use Case
Critical for Conflict Resolution in DynamoDB and other AP systems.

## Counter-arguments
TBD

## Data gaps
TBD

### Related
- [[system-design]]
- [[consistency-models]]
