---
title: "Computer Architecture"
tldr: "The conceptual design and operational structure of a computer system, encompassing both hardware and software interfaces."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [hardware, cpu, isa, computer-architecture]
sources: ["[[nand2tetris-2026-nand2tetris]]", "[[riscv-programming-2026-book]]"]
explored: false
confidence: high
---

# Computer Architecture

**Computer Architecture** describes the functional requirements, design, and implementation of a computer's hardware and software interface.

## From Gates to Software
The **Nand2Tetris** project ([[nand2tetris-2026-nand2tetris]]) demonstrates that a full computer can be built starting from a simple **NAND gate**, progressing through:
- ALU and CPU design.
- Memory architecture.
- The software stack (Assembler -> Compiler -> OS).

## Instruction Set Architecture (ISA)
At the heart of architecture is the ISA, such as **RISC-V** ([[riscv-programming-2026-book]], [[riscv-intl-2026-isa-manual]]), which defines the set of basic instructions the processor can execute.

## Counter-arguments
- Educational models (like the Hack CPU in Nand2Tetris) often omit complex features like pipelining and out-of-order execution found in modern CPUs.

## Data gaps
- Current sources do not cover the specifics of Memory Management Units (MMU) and Cache hierarchies beyond basic memory.
