---
title: CPU Virtual Machines
description: Simulation of hardware architectures in software.
---
# CPU Virtual Machines

Virtual machines that simulate a specific CPU architecture, providing an environment to run code for that architecture on a different physical host.

## Implementations
- [[meiners-2026-lc3vm]]: Implementation of the LC-3 (Little Computer 3) architecture, featuring a fetch-decode-execute cycle and memory mapped I/O.

## Core Concepts
- **Instruction Set Architecture (ISA)**: The set of basic instructions a VM must emulate.
- **Fetch-Decode-Execute**: The fundamental cycle of every CPU emulator.
- **Memory Mapping**: Using specific memory addresses to trigger I/O operations (e.g., keyboard status).

## Bias Checks
- **Hardware vs Software**: VMs focus on functional correctness over timing accuracy.
- **Performance**: Pure software emulation is significantly slower than JIT (Just-In-Time) compilation or hardware acceleration.
