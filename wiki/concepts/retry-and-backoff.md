     1|---
     2|title: "Retry and Backoff"
     3|tldr: "Strategies for handling transient failures without overloading the system."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[aws-amazon-com-builders-library-distributed-systems-]]', '[[cloud-google-com-architecture-distributed-systems-concepts]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|Blindly retrying a failed request can cause a 'thundering herd' that crashes a recovering server.
    14|
    15|### The Pattern
    16|- **Exponential Backoff**: Increasing the wait time between retries (e.g., 1s, 2s, 4s, 8s).
    17|- **Jitter**: Adding a random offset to the backoff time to prevent synchronized retry spikes.
    18|
    19|### Best Practices
    20|Combined with circuit breakers, this prevents a failing downstream service from cascading the failure to the entire system.
    21|
    22|

### Related
- [[system-design]]
- [[distributed-computing-fallacies]]

## Counter-arguments
    23|TBD
    24|
    25|## Data gaps
    26|TBD
    27|