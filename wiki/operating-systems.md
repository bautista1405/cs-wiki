---
title: Operating Systems
description: Software that manages computer hardware and provides services for programs.
---
# Operating Systems

The core software that manages hardware resources and provides the interface between the user/applications and the hardware.

## Core Components
- **Kernel**: The heart of the OS, managing memory, processes, and device drivers.
- **Shell**: The command-line interface for interacting with the kernel.
- **System Calls**: The API provided by the kernel to user-space programs.

## Implementations & Examples
- **Shells**: [[brenns10-2026-lsh]] demonstrates a basic C-based shell using `fork` and `exec`.
- **Text Editors**: [[snaptoken-2026-kilo]] shows how programs interact with the terminal's raw mode to bypass standard OS input processing.
- **Teaching OS**: [[mit-pdos-2026-xv6-riscv]] provides a minimal kernel for understanding core OS concepts.

## Core Concepts
- **Process Management**: Creation, scheduling, and termination of processes.
- **Virtual Memory**: isolating processes and managing memory allocation.
- **I/O Management**: Handling device drivers and buffers.

## Bias Checks
- **Monolithic vs Microkernel**: The wiki's examples (xv6, Linux) are monolithic; microkernels (like L4 or Minix) offer different trade-offs in reliability and modularity.
- **User-space vs Kernel-space**: The distinction is critical for security and stability.
