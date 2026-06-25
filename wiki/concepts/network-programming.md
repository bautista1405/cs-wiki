---
title: "Network Programming"
tldr: "The art of writing software that communicates over a network, primarily using sockets and protocol suites like TCP/UDP."
date_created: 2026-05-09
date_modified: 2026-05-09
type: concept
tags: [networking, sockets, tcp, udp, c]
sources: ["[[beej-2026-sockets]]"]
explored: false
confidence: high
---

# Network Programming

**Network Programming** involves creating applications that communicate across a network, typically utilizing the Berkeley Sockets API.

## Core Concepts
- **Sockets**: The fundamental endpoint for communication.
- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, ordered delivery.
- **UDP (User Datagram Protocol)**: Connectionless, unreliable, fast delivery.

## Implementation Details
According to [[beej-2026-sockets]], the basic flow for a TCP server includes:
1. `socket()`: Create the endpoint.
2. `bind()`: Associate the socket with an IP and port.
3. `listen()`: Wait for incoming connections.
4. `accept()`: Establish the connection.

## Counter-arguments
- Modern development often abstracts sockets via HTTP libraries or gRPC, making manual socket management a niche requirement for systems programmers.

## Data gaps
- Lacks coverage of asynchronous I/O models (e.g., `io_uring` on Linux or `IOCP` on Windows).
