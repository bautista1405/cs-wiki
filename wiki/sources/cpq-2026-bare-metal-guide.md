---
title: "Bare Metal Programming Guide"
tldr: "Comprehensive guide to microcontroller programming using GCC and a bare-metal approach (without HAL/CMSIS) on STM32F429."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [bare-metal, stm32, arm-cortex-m4, embedded-c]
sources: ["https://github.com/cpq/bare-metal-programming-guide"]
explored: true
confidence: high
---

# Bare Metal Programming Guide

A practitioner's guide to programming ARM Cortex-M4 microcontrollers (specifically STM32F429ZI) using only a compiler and the MCU datasheet.

## Core Technical Concepts
- **Memory Mapped I/O (MMIO)**: Controlling peripherals by writing to specific 32-bit registers at fixed memory addresses.
- **GPIO Control**: Using the MODER register to configure pins as input or output via bit manipulation.
- **Boot Process**: The MCU reads a **Vector Table** from flash at boot, where the 2nd 32-bit value is the address of the boot function.
- **Linker Scripts**: Defining memory regions (Flash at 0x08000000, SRAM at 0x20000000) and ensuring the `.vectors` section is placed at the beginning of flash.
- **Startup Sequence**: The `_reset` function initializes the stack pointer, copies `.data` from flash to RAM, and zeroes the `.bss` section before calling `main()`.

## Relation to Concepts
Primary source for [[bare-metal-programming]].

## Bias Checks
- **Counter-arguments**: The "no-library" approach is excellent for learning but impractical for complex production systems where vendor-provided HALs (Hardware Abstraction Layers) and CMSIS provide portability and stability.
- **Data gaps**: Focuses primarily on GPIO and UART; advanced peripherals like DMA or I2C are not detailed in the summary.
