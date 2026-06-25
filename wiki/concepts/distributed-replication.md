     1|---
     2|title: "Distributed Replication"
     3|tldr: "The process of copying data across multiple nodes to ensure durability and high availability."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[cloud-google-com-architecture-distributed-systems-concepts]]', '[[raft-github-io-]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|Replication is the primary tool for overcoming single points of failure.
    14|
    15|### Replication Strategies
    16|- **Single-Leader**: One node handles writes; others handle reads. Simplest, but the leader is a bottleneck.
    17|- **Multi-Leader**: Multiple nodes can handle writes. Complex conflict resolution required (last-write-wins).
    18|- **Leaderless (Quorum)**: Any node can handle writes. Requires a quorum (majority) for read/write success (e.g., Cassandra).
    19|
    20|### Trade-offs
    21|Synchronous replication ensures zero data loss but increases latency. Asynchronous replication is fast but risks data loss during failover.
    22|
    23|

### Related
- [[system-design]]

## Counter-arguments
    24|TBD
    25|
    26|## Data gaps
    27|TBD
    28|