---
title: "Bare Metal Programming"
tldr: "The practice of writing software directly for hardware without the abstraction of an operating system or heavy runtime libraries."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [embedded, firmware, hardware, low-level]
sources: ["[[cpq-2026-bare-metal-guide]]"]
explored: false
confidence: high
---

# Bare Metal Programming

**Bare Metal Programming** is the process of developing firmware that runs directly on the processor's hardware, without an intervening Operating System (OS) or Hardware Abstraction Layer (HAL).

## Core Principles
- **Direct Hardware Access**: Interacting with peripherals via **Memory Mapped I/O (MMIO)**, where specific memory addresses correspond to hardware registers.
- **Control of the Boot Process**: The developer must manually define the **Vector Table** (the set of entry points for interrupts and resets) so the CPU knows where to start execution upon power-on.
- **Memory Management**: Since there is no OS to manage memory, the developer must use **Linker Scripts** to explicitly map code (`.text`), initialized data (`.data`), and uninitialized data (`.bss`) to physical Flash and SRAM addresses.
- **Resource Constraints**: Requires precise management of the stack pointer and hardware registers to prevent system crashes.

## Implementation Workflow
1. **Datasheet Study**: Understanding the register map of the target MCU.
2. **Linker Configuration**: Defining memory origins and lengths.
3. **Startup Code**: Writing the `_reset` handler to initialize the environment.
4. **Peripheral Configuration**: Setting bits in registers to enable hardware functionality (e.g., setting a pin to Output mode).

## Counter-arguments
- **Complexity**: Writing bare metal code is time-consuming and error-prone compared to using a HAL or RTOS.
- **Portability**: Bare metal code is typically locked to a specific chip architecture; moving to a different MCU often requires a complete rewrite of the hardware interface layer.

## Data gaps
- Lack of coverage on real-time constraints and deterministic timing analysis in the current source.
