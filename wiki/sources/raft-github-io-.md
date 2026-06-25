---
title: "Raft Consensus Algorithm"
tldr: "Technical specification of the Raft algorithm for managing a replicated log."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [distributed-systems, architecture]
sources: []
original_url: N/A
explored: false
confidence: high
---

Core focus on Consensus:
- **Leader Election**: How a cluster agrees on a single leader.
- **Log Replication**: How the leader ensures all followers have the same state.
- **Safety**: The guarantee that if any server has applied a log entry, no other server can apply a different entry for that index.
