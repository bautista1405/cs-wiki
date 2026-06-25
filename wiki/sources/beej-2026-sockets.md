---
author: beej
year: 2026
title: Guide to Network Programming
---
# Beej's Guide to Network Programming

A comprehensive guide to network programming using Internet sockets.

## Core Concepts
- **Sockets API**: The standard interface for network communication ported to Unix, Linux, and Windows.
- **Connectivity**: Covers TCP and UDP socket creation, binding, listening, and connecting.

## Utility
- Practical implementation details for creating network connections.
- Bridge between theoretical networking and C code.

## Bias Checks
- **Counter-arguments**: Modern asynchronous I/O (epoll, kqueue, io_uring) is omitted in the basic socket guide but essential for high-performance servers.
- **Data gaps**: Doesn't extensively cover TLS/SSL encryption in the core socket guide.

## Reference
- Original Source: https://beej.us/guide/bgnet/
- GitHub: https://github.com/beejjorgensen/bgnet
