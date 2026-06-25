     1|---
     2|title: "Consistency Models"
     3|tldr: "The rules that determine when a read operation sees the most recent write in a distributed system."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[cloud-google-com-architecture-distributed-systems-concepts]]', '[[martin-fowler-com-guide-distributed-systems-html]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|Consistency is the 'C' in CAP. Not all systems need the same level of consistency.
    14|
    15|### Levels of Consistency
    16|- **Strong Consistency**: Read always returns the most recent write. Highest latency, lowest availability.
    17|- **Eventual Consistency**: Reads will eventually match the latest write, but there is a window of staleness. High availability, low latency.
    18|- **Causal Consistency**: Ensures that operations that are causally related are seen by all nodes in the same order.
    19|
    20|### Trade-offs
    21|Choosing between strong and eventual consistency is a business decision. For a bank, strong consistency is required. For a Twitter like, eventual consistency is sufficient.
    22|
    23|

### Related
- [[system-design]]
- [[cap-theorem]]
- [[distributed-replication]]

## Counter-arguments
    24|TBD
    25|
    26|## Data gaps
    27|TBD
    28|