---
title: "Distributed Systems"
tldr: "A collection of independent computers that appear to the user as a single coherent system."
date_created: 2026-05-08
date_modified: 2026-05-11
type: concept
tags: [distributed-systems, fault-tolerance, replication, consistency]
sources: ["[[mit-2026-distributed-systems]]", "[[wikipedia-2024-distributed-fallacies]]"]
explored: false
confidence: medium
---

# Distributed Systems

**Distributed Systems** consist of multiple independent nodes that coordinate to achieve a common goal, appearing to the user as a single system.

## Key Engineering Challenges
As taught in MIT's [[mit-2026-distributed-systems]], the primary challenges in building these systems include:
- **Fault Tolerance**: Maintaining availability despite the failure of individual components.
- **Replication**: Copying data across nodes to improve reliability and performance.
- **Consistency**: Ensuring that updates are propagated such that all nodes see a consistent state.

### The Eight Fallacies
Building on these challenges, the "Fallacies of Distributed Computing" ([[wikipedia-2024-distributed-fallacies]]) identify common false assumptions developers make, such as assuming a reliable network, zero latency, or infinite bandwidth. Ignoring these leads to fragile systems.

## Related Concepts
- [[consensus-algorithms]]
- [[cap-theorem]]
- [[distributed-clocks]]
- [[consistency-models]]
- [[distributed-replication]]
- [[load-balancing]]
- [[idempotency]]
- [[gossip-protocols]]

## Counter-arguments
- The focus onSTRONG consistency in academic courses often overlooks the trade-offs of EVENTUAL consistency used in many global-scale systems.

## Data gaps
- Lacks specific examples of production-grade distributed algorithms (e.g., Paxos, Raft) beyond the general concepts.
