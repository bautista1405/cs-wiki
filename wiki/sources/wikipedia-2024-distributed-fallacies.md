---
title: "Fallacies of Distributed Computing"
tldr: "Common false assumptions made when designing distributed systems, often leading to failure."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [distributed-systems, network-design, fallacies]
sources: []
original_url: "https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing"
explored: false
confidence: high
---

# Summary: Fallacies of Distributed Computing

The "Fallacies of Distributed Computing" are eight common false assumptions that developers make when designing systems that communicate over a network.

## The Eight Fallacies
1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. Network homogeneity.

## Impact
Ignoring these fallacies leads to fragile systems that fail in production despite working in local development environments. Addressing them requires implementing timeouts, retries, circuit breakers, and robust monitoring.

## Analysis
These assumptions typically stem from the habit of treating remote calls as if they were local function calls (RPC paradigm), masking the inherent instability of the network layer.

## Counter-arguments
- Some "fallacies" may be negligible in highly controlled, private high-speed data centers (e.g., extreme low latency), though they remain dangerous assumptions for general-purpose systems.

## Data gaps
- The summary focuses on the list; specific architectural patterns to solve each fallacy (e.g., idempotency for reliability) are not detailed in this specific page.
