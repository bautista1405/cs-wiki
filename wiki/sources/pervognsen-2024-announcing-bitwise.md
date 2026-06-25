---
title: "Announcing Bitwise"
tldr: "Initiative to demonstrate building low-level systems (CPUs, GPUs, kernels) from scratch using simplicity and simulation."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [low-level, hardware-design, systems-programming, education]
sources: []
original_url: "https://github.com/pervognsen/bitwise"
explored: false
confidence: high
---

# Summary: Announcing Bitwise

Bitwise is an educational project by a veteran systems programmer (formerly Epic Games, NVIDIA) aimed at demonstrating how to build complex low-level computing systems from scratch. The project prioritizes simplicity over marginal performance or feature gains to make understanding accessible.

## Core Objectives
The project focuses on the "create to understand" philosophy, building a full stack including:
- **Hardware**: RISC-V CPU, GPU, HDMI controllers, Ethernet MAC, and DDR3 PHY using HDLs and FPGAs.
- **Software**: Kernels (schedulers, VM managers, file systems), systems libraries (GUIs, memory allocators), and tooling (compilers, assemblers, debuggers).
- **Infrastructure**: Testing frameworks using property-based and fuzz testing.

## Methodology
- **Simulated First**: Development primarily uses free software tools and simulation to avoid the friction of real hardware.
- **Bootstrapping**: A C-like systems language is built first to implement subsequent tools (emulator, assembler, etc.).
- **Public Domain**: All code is released for free to serve as a community resource.

## Key Components Mentioned
- [[riscv]] (CPU architecture)
- [[operating-systems]] (Kernel development)
- [[compilers]] (Systems language toolchain)
- [[fpga]] (Hardware synthesis)

## Counter-arguments
- Simplicity-first approach may omit critical real-world constraints (e.g., complex timing issues, hardware errata) that are essential for professional-grade production systems.

## Data gaps
- Specifics on the "C-like systems language" grammar and design goals are not detailed in the announcement.
