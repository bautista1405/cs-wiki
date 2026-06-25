     1|---
     2|title: "Idempotency"
     3|tldr: "The property of an operation where performing it multiple times has the same effect as performing it once."
     4|date_created: 2026-05-08
     5|date_modified: 2026-05-08
     6|type: concept
     7|tags: [distributed-systems, architecture]
     8|sources: ['[[aws-amazon-com-builders-library-distributed-systems-]]', '[[cloud-google-com-architecture-distributed-systems-concepts]]']
     9|explored: false
    10|confidence: high
    11|---
    12|
    13|In a distributed system, network failures mean requests can be sent multiple times (at-least-once delivery). Idempotency prevents duplicate data or duplicate charges.
    14|
    15|### Implementation Patterns
    16|- **Idempotency Keys**: Clients send a unique UUID for each request. The server stores this key; if the key is seen again, the server returns the previous result without reprocessing.
    17|- **Upsert (Insert or Update)**: Using a unique constraint in the DB to ensure that duplicate writes simply overwrite the same record.
    18|
    19|### Critical for Distributed Systems
    20|Essential for payment gateways, order fulfillment, and any system relying on asynchronous message queues (like Kafka).
    21|
    22|

### Related
- [[system-design]]

## Counter-arguments
    23|TBD
    24|
    25|## Data gaps
    26|TBD
    27|