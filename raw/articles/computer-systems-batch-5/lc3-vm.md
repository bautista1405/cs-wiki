---
original_url: https://www.jmeiners.com/lc3-vm/
date: 2026-05-09
---
# Write your Own Virtual Machine (LC-3)

Tutorial on writing a virtual machine (VM) that simulates the LC-3 (Little Computer 3) architecture.

## Key Concepts
- **VM Definition**: A program that acts like a computer, simulating a CPU and hardware components.
- **LC-3 Architecture**: Educational architecture with 8 general purpose registers, a program counter (PC), and condition flags (COND).
- **Instruction Set**: 16 opcodes (BR, ADD, LD, ST, JSR, AND, LDR, STR, RTI, NOT, LDI, STI, JMP, RES, LEA, TRAP).
- **Memory Mapped Registers**: KBSR (keyboard status) and KBDR (keyboard data) for non-blocking I/O.

## Implementation Details
- Written in C.
- Implements basic binary arithmetic and sign extension.
- Mentions a C++ generic approach to reduce code duplication in instruction execution.

## Resources
- GitHub repo: https://github.com/justinmeiners/lc3-vm
