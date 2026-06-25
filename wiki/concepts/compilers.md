---
title: "Compilers"
tldr: "Software that translates high-level programming language code into low-level machine code."
date_created: 2026-05-09
date_modified: 2026-05-09
type: concept
tags: [compilers, parsing, optimization, toolchains]
sources: ["[[stanford-2026-cs143-compilers]]", "[[black-2026-unix-weapons-school]]"]
explored: false
confidence: high
---

# Compilers

Compilers bridge the gap between human-readable high-level languages and the machine-level instructions executed by hardware.

## The Compilation Pipeline
1. **Lexical Analysis**: Converting source code into tokens.
2. **Parsing**: Building an Abstract Syntax Tree (AST) based on formal grammars.
3. **Semantic Analysis**: Performing type checking and ensuring logical consistency.
4. **Intermediate Representation (IR)**: Translating to a platform-independent form (e.g., SSA - Static Single Assignment).
5. **Optimization**: Applying local and global optimizations (e.g., the Polyhedral Model).
6. **Code Generation**: Mapping IR to specific target machine instructions and performing register allocation.

## Compiler Limitations
As noted in [[black-2026-unix-weapons-school]], there are fundamental limits to what a compiler can optimize. Performance-critical software often requires:
- **Inline Assembly**: Bypassing the compiler for specific hardware instructions.
- **PGO (Profile-Guided Optimization)**: Using real-world execution data to inform compiler decisions.

## Counter-arguments
- The shift towards Just-In-Time (JIT) compilation in languages like Java and JavaScript challenges the traditional ahead-of-time (AOT) compilation model by allowing optimizations based on runtime behavior.

## Data gaps
- Lack of detailed comparison between different IR formats (e.g., LLVM IR vs. GCC GIMPLE).
