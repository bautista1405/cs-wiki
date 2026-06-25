---
title: "CPU Virtual Machines"
tldr: "Software emulations of hardware CPUs, used for education, cross-platform compatibility, and isolation."
date_created: 2026-05-09
date_modified: 2026-05-09
type: concept
tags: [vm, cpu, emulation, architecture]
sources: ["[[meiners-2026-lc3vm]]"]
explored: false
confidence: high
---

# CPU Virtual Machines

A **CPU Virtual Machine (VM)** is a software layer that mimics the behavior of a physical CPU, including its instruction set, registers, and memory management.

## The Execution Cycle
The core of most VM implementations is the **Fetch-Decode-Execute** cycle:
1. **Fetch**: Get the next instruction from virtual memory.
2. **Decode**: Determine what the instruction does.
3. **Execute**: Perform the action and update registers/memory.

The LC-3 implementation [[meiners-2026-lc3vm]] provides a concrete example of this cycle in a simplified architecture.

## Counter-arguments
- Software emulation is significantly slower than hardware virtualization (VT-x, AMD-V) which allows guest OSs to run instructions directly on the hardware.

## Data gaps
- Lacks discussion on JIT (Just-In-Time) compilation for VMs, which is critical for modern VM performance (e.g., JVM, V8).
