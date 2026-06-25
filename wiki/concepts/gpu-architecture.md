---
title: "GPU Architecture"
tldr: "The design of graphics processing units, characterized by massive parallelism and a SIMT (Single Instruction, Multiple Threads) execution model."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [gpu, parallel-computing, simd, hardware]
sources: ["[[majmudaradam-2026-tiny-gpu]]", "[[odle-2026-wopr-ai-server]]"]
explored: false
confidence: high
---

# GPU Architecture

**GPU Architecture** is designed to maximize throughput for data-parallel workloads by executing a single instruction across thousands of data elements simultaneously.

## Key Architectural Patterns
- **SIMT (Single Instruction, Multiple Threads)**: A variation of SIMD where multiple threads execute the same instruction stream but operate on different data (using unique thread IDs).
- **Compute Cores and Blocks**: Work is divided into **blocks**, which are dispatched to compute cores. Each core contains a scheduler and a set of execution resources (ALUs, LSUs).
- **Memory Hierarchy**: To overcome the "memory wall" (bandwidth limits), GPUs use:
    - **Global Memory**: High capacity but high latency.
    - **Caches**: Local SRAM to store frequently accessed data.
    - **Shared Memory**: Fast memory shared between threads in a block.
- **Latency Hiding**: Using techniques like **Warp Scheduling** to swap execution contexts when a thread is waiting for a memory request to return.

## Architectural Implementations
- **DVKCore**: An example of a GPU core implementation focusing on driver-level interfaces ([[tdmmykeys-2026-dvkcore]]).

## Counter-arguments
- While GPUs excel at throughput, they are inefficient for latency-sensitive, sequential tasks (branch-heavy logic) compared to CPUs.

## Data gaps
- Current sources focus on educational/simplified models; detailed analysis of modern Tensor Cores or Ray Tracing hardware is missing.
