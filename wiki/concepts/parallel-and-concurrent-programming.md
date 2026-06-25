---
title: "Parallel and Concurrent Programming"
tldr: "The study of executing multiple computations simultaneously to improve performance and responsiveness."
date_created: 2026-05-09
date_modified: 2026-05-09
type: concept
tags: [parallelism, concurrency, multi-core, gpu]
sources: ["[[aalto-2026-programming-parallel-computers]]", "[[stanford-2023-cs149-parallel-computing]]", "[[cambridge-2022-conc-dis-sys]]", "[[black-2026-unix-weapons-school]]"]
explored: false
confidence: high
---

# Parallel and Concurrent Programming

Parallelism and concurrency are distinct but related concepts used to increase the throughput and efficiency of software.

## Core Paradigms
- **Data Parallelism**: Applying the same operation to multiple data elements (e.g., SIMD, GPU warps).
- **Task Parallelism**: Executing different tasks concurrently (e.g., multi-threading, distributed workers).
- **Shared Address Space**: Multiple threads accessing the same memory, requiring synchronization primitives.
- **Message Passing**: Communicating between isolated processes (common in distributed systems).

## Key Implementation Challenges
- **Synchronization**: Managing access to shared resources via locks, mutexes, or lock-free structures (e.g., hazard pointers, ABA problem) as detailed in [[stanford-2023-cs149-parallel-computing]].
- **Communication Overhead**: The tension between latency and bandwidth in multi-core and distributed environments.
- **Consistency Models**: The rules governing the order of memory operations (e.g., acquire/release semantics).

## Architectural Exploitation
Modern hardware provides multiple levels of parallelism:
- **Instruction Level**: Pipelining and superscalar execution.
- **Thread Level**: Multi-core CPUs and SMT.
- **Data Level**: Vector instructions (SSE/AVX) and GPU architectures.

## Counter-arguments
- The assumption that adding cores linearly increases performance is often invalidated by Amdahl's Law (serial bottlenecks) and synchronization overhead.

## Data gaps
- Limited information on the specific performance trade-offs of different lock-free data structures in production environments.
