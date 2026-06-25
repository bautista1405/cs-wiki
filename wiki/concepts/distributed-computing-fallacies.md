     1|---
     2|title: "Fallacies of Distributed Computing"
     3|tldr: "A set of false assumptions that often lead to the design of unstable or fragile distributed systems."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[martin-fowler-com-guide-distributed-systems-html]]', '[[azure-microsoft-com-en-us-resources-cloud-computing-dictionary-what-is-distributed-computing-]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|Designers often treat the network as a reliable pipe, which leads to systemic failure.
    14|
    15|### The Primary Fallacies
    16|1. **The network is reliable**: It isn't. Packets drop.
    17|2. **Latency is zero**: It isn't. Geographical distance matters.
    18|3. **Bandwidth is infinite**: It isn't. Congestion happens.
    19|4. **The network is secure**: It isn't. Encryption is mandatory.
    20|
    21|### Impact on Design
    22|Accepting these fallacies leads to the implementation of timeouts, retries, and circuit breakers.
    23|
    24|

### Related
- [[system-design]]

## Counter-arguments
    25|TBD
    26|
    27|## Data gaps
    28|TBD
    29|