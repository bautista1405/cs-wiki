---
title: "HDL and FPGA"
tldr: "Hardware Description Languages (HDL) and Field Programmable Gate Arrays (FPGA) for designing and implementing custom digital logic."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [hdl, fpga, verilog, hardware-design]
sources: ["[[majmudaradam-2026-tiny-gpu]]", "[[floooh-2026-chips-emulators]]"]
explored: false
confidence: high
---

# HDL and FPGA

**HDL (Hardware Description Language)** and **FPGA (Field Programmable Gate Array)** provide the tools to design custom hardware circuits without needing to manufacture a physical chip.

## Core Concepts
- **Verilog/VHDL**: Languages used to describe the behavior and structure of digital logic. Instead of sequential instructions, HDLs describe concurrent signal flows.
- **Synthesis**: The process of converting HDL code into a netlist of logic gates and flip-flops.
- **FPGA**: A semiconductor device based on a matrix of configurable logic blocks (CLBs) that can be programmed to implement any digital circuit.
- **Simulation**: The use of tools (like Icarus Verilog) to verify the correctness of a design before deploying it to hardware.

## Hardware Modeling Approaches
- **Structural Modeling**: Defining the circuit as a collection of interconnected gates (e.g., using a "pin-bit-mask" as seen in [[floooh-2026-chips-emulators]]).
- **Behavioral Modeling**: Describing the logic based on how it should react to inputs, which a synthesis tool then maps to hardware.

## Counter-arguments
- FPGA development has a much steeper learning curve than software development due to the requirement of thinking in terms of spatial concurrency rather than temporal sequence.

## Data gaps
- Lack of information on timing closure and clock domain crossing (CDC) in the current sources.
