---
title: "Operating Systems"
tldr: "Software that manages computer hardware and provides common services for computer programs."
date_created: 2026-05-08
date_modified: 2026-05-11
type: concept
tags: [os, kernel, virtualization, concurrency, persistence]
sources: ["[[mit-pdos-2026-xv6-riscv]]", "[[arpaci-dusseau-2026-ostep]]", "[[pervognsen-2024-announcing-bitwise]]", "[[mit-2023-os-serverless]]", "[[mit-pdos-2024-xv6-riscv-book]]"]
explored: false
confidence: high
---

# Operating Systems

Software that manages computer hardware and provides common services for computer programs.

## Core Pillars
According to [[arpaci-dusseau-2026-ostep]], modern OS design revolves around three "easy pieces":
- **Virtualization**: Creating abstractions for CPU and memory.
- **Concurrency**: Managing multiple simultaneous execution paths.
- **Persistence**: Managing non-volatile storage.

## Memory and Safety
OS-level memory management is critical for system stability. Research into [[memory-management]] and tools like [[google-2026-address-sanitizer]] highlight the tension between performance and safety in manual memory management.

## Educational Implementations
- **xv6**: See [[mit-pdos-2026-xv6-riscv]] for a teaching OS.
- **Modern OS**: See [[samyk-2026-modern-os]] for a conceptual overview.

## Related Concepts
- [[memory-management]]
- [[cpu-virtual-machines]]
- [[linux-kernel-internals]]
- [[unix-philosophy]]
- [[network-programming]]

## Specialized Architectures
- **Distributed Systems**: See [[distributed-systems]].
- **Serverless**: See [[serverless-computing]].

## Counter-arguments
- The "easy pieces" abstraction simplifies the learning curve but obscures the extreme complexity of modern monolithic kernels.

## Data gaps
- Insufficient coverage of microkernel vs monolithic kernel performance trade-offs in the current sources.

