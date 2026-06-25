---
author: meiners
year: 2026
title: LC-3 Virtual Machine
---
# LC-3 Virtual Machine

Tutorial on writing a virtual machine (VM) that simulates the LC-3 (Little Computer 3) architecture.

## Architecture
- **Registers**: 8 general purpose registers, a program counter (PC), and condition flags (COND).
- **Instruction Set**: 16 opcodes including BR, ADD, LD, ST, JSR, AND, LDR, STR, RTI, NOT, LDI, STI, JMP, RES, LEA, TRAP.
- **I/O**: Memory mapped registers (KBSR and KBDR) for keyboard interaction.

## Implementation
- Written in C.
- Focuses on binary arithmetic and sign extension.
- Uses a fetch-decode-execute cycle.

## Bias Checks
- **Counter-arguments**: This is an educational architecture; real-world CPUs use pipelining and complex caching.
- **Data gaps**: The tutorial focuses on a simple VM; it does not dive into hardware-level timing.

## Reference
- Original Source: https://www.jmeiners.com/lc3-vm/
- GitHub: https://github.com/justinmeiners/lc3-vm
