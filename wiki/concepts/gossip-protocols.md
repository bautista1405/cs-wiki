---
title: "Gossip Protocols"
tldr: "A decentralized method for nodes to share information across a cluster, similar to how a virus spreads."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [distributed-systems, coordination]
sources: ['[[primer-donnemartin_system-design-primer]]']
explored: false
confidence: high
---

Gossip protocols eliminate the need for a central coordinator to propagate state.

### How it Works
Each node periodically picks a random peer and exchanges information. This ensures that a piece of data reaches all nodes in $O(\log n)$ time.

### Applications
- **Cluster Membership**: Knowing which nodes are alive/dead.
- **Failure Detection**: Detecting node crash via lack of heartbeat gossip.
- **Cassandra/Consul**: Widely used for state propagation in large clusters.

## Counter-arguments
TBD

## Data gaps
TBD

### Related
- [[system-design]]
- [[consistency-models]]