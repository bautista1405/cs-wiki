---
title: "xv6-riscv-book-readme"
tldr: "Build instructions for the xv6 RISC-V book, detailing LaTeX conversion and PDF generation."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [xv6, riscv, documentation]
sources: []
original_url: "https://github.com/mit-pdos/xv6-book"
explored: false
confidence: high
---

# Summary: xv6 RISC-V Book Build

This document provides the technical requirements for building the xv6 RISC-V instructional book from source.

## Build Process
- **Toolchain**: Requires a TeX distribution with `pdflatex`.
- **Automation**: Executed via `make`, which handles cloning the OS source and generating `book.pdf`.
- **Graphics**: Figures are produced using `inkscape`.

## Context
The book serves as a primary guide for studying [[operating-systems]] via the xv6-riscv kernel.

## Counter-arguments
- Not applicable (technical readme).

## Data gaps
- Does not provide the actual content of the book, only the process to build it.
