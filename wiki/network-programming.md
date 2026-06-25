---
title: Network Programming
description: Creating applications that communicate over a network.
---
# Network Programming

The process of writing programs that communicate with other programs over a computer network.

## Implementations
- [[beej-2026-sockets]]: Comprehensive guide to Internet sockets, covering TCP, UDP, and basic socket API usage across platforms.

## Core Concepts
- **Sockets**: The fundamental endpoint for sending or receiving data over a network.
- **TCP/UDP**: Understanding the trade-offs between connection-oriented (reliable) and connectionless (fast) protocols.
- **The Socket API**: Standard functions like `socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `send()`, and `recv()`.

## Bias Checks
- **Synchronous vs Asynchronous**: Basic socket programming is typically synchronous (blocking), while production-grade servers use asynchronous I/O (epoll, io_uring).
- **Security**: Low-level sockets do not provide encryption; TLS/SSL layers are required for secure communication.
