---
title: "tiny-gpu"
tldr: "A minimal GPU implementation in Verilog designed for learning GPU architecture, SIMD, and memory controllers."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [gpu, verilog, simd, hardware-design]
sources: ["https://github.com/majmudaradam/tiny-gpu"]
explored: true
confidence: high
---

# tiny-gpu

`tiny-gpu` is an educational hardware implementation that strips away the complexity of modern graphics cards to focus on general-purpose GPU (GPGPU) principles.

## Architectural Elements
- **Dispatcher**: Manages the distribution of thread blocks to compute cores.
- **Compute Cores**: Each core processes one block at a time. Each thread within a block has a dedicated ALU, LSU, PC, and register file.
- **Memory System**: Utilizes separate program and data memory with a memory controller to handle bandwidth constraints and a basic cache.
- **SIMD Execution**: Implements a Single-Instruction Multiple-Data model where all threads in a block execute the same instruction sequentially.
- **ISA**: A custom 11-instruction set including `BRnzp` for branching and `LDR`/`STR` for async global memory access.

## Advanced Concepts Discussed
- **Memory Coalescing**: Combining neighboring memory requests to minimize overhead.
- **Warp Scheduling**: Executing different batches of threads to hide latency.
- **Branch Divergence**: The challenge when threads in a SIMT model take different execution paths.

## Relation to Concepts
Primary source for [[gpu-architecture]] and [[hdl-fpga]].

## Bias Checks
- **Counter-arguments**: The implementation is "naive" by design (e.g., assuming all threads converge immediately after branching), making it a poor model for actual hardware performance but a great model for conceptual understanding.
- **Data gaps**: Does not implement full multi-layered cache or complex warp scheduling.
