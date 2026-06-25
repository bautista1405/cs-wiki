---
title: "Load Balancing"
tldr: "The process of distributing network traffic across multiple servers to ensure no single server is overwhelmed."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [system-design, distributed-systems]
sources: ["[[primer-system-design-primer]]"]
explored: false
confidence: high
---

Load balancers sit between the client and the server farm to ensure reliability and scalability.

### Types of Load Balancing
- **Hardware LBs**: High performance, expensive (e.g., F5).
- **Software LBs**: Flexible, cheaper (e.g., Nginx, HAProxy).

### Algorithms
- **Round Robin**: Requests are distributed sequentially. Simple, but doesn't account for server health/load.
- **Least Connections**: Sends request to the server with the fewest active connections.
- **IP Hash**: Uses the client's IP to ensure a user always hits the same server (Session Stickiness).

### Layer 4 vs Layer 7
- **L4 (Transport Layer)**: Directs traffic based on TCP/UDP ports. Fast, but blind to the application data.
- **L7 (Application Layer)**: Directs traffic based on HTTP headers, cookies, or URL paths. Slower, but smarter (can route `/api` to one server and `/static` to another).

## Counter-arguments
TBD

## Data gaps
TBD
