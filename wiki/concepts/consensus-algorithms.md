     1|---
     2|title: "Consensus Algorithms"
     3|tldr: "Mechanisms that ensure a set of distributed nodes agree on a single value or state, even in the presence of failures."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[raft-github-io-]]', '[[cloud-google-com-architecture-distributed-systems-concepts]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|Consensus is the most difficult problem in distributed systems. It ensures that a cluster of nodes acts as a single cohesive unit.
    14|
    15|### Key Algorithms
    16|- **Raft**: Designed for understandability. Uses a strong leader and log replication to ensure all nodes are in sync.
    17|- **Paxos**: The foundational (but complex) algorithm for consensus. Most modern systems use a variation of Paxos or Raft.
    18|
    19|### Why it Matters
    20|Without consensus, systems cannot reliably implement distributed locks, leader election, or atomic commits across shards.
    21|
    22|

### Related
- [[system-design]]
- [[distributed-replication]]

## Counter-arguments
    23|TBD
    24|
    25|## Data gaps
    26|TBD
    27|