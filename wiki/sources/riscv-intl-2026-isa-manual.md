---
title: "RISC-V Instruction Set Manual"
tldr: "The formal specifications for the RISC-V ISA, encompassing both user-level and privileged architectures."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [isa, risc-v, specification, architecture]
sources: ["https://github.com/riscv/riscv-isa-manual"]
explored: true
confidence: high
---

# RISC-V Instruction Set Manual

The canonical reference for the RISC-V Instruction Set Architecture (ISA).

## Structure
- **Volume I: User-Level ISA**: Defines the instructions available to applications.
- **Volume II: Privileged Architecture**: Defines the interface between the hardware and the operating system (machine, supervisor, and user modes), including CSRs (Control and Status Registers).

## Relation to Concepts
The foundational specification for [[riscv]] and [[computer-architecture]].

## Bias Checks
- **Counter-arguments**: Specifications describe the "what" but not the "how" of microarchitectural implementation (e.g., they don't dictate whether to use a 5-stage or 7-stage pipeline).
- **Data gaps**: The manual is a draft/specification and does not include performance metrics or implementation trade-offs.
