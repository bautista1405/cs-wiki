---
original_url: https://en.algorithmica.org/hpc/
fetched_date: 2026-05-09
---
# Algorithms for Modern Hardware - Algorithmica

This is an upcoming high performance computing book titled "Algorithms for Modern Hardware" by Sergey Slotin.

## Overview
The book focuses on practical ways to speed up programs, moving beyond asymptotic complexity to consider modern hardware characteristics.

## Planned Table of Contents
- Complexity Models (Modern Hardware, Programming Languages, Models of Computation, When to Optimize)
- Computer Architecture (ISA, Assembly, Loops, Functions, Indirect Branching, Machine Code Layout, System Calls, Virtualization)
- Instruction-Level Parallelism (Pipeline Hazards, Cost of Branching, Branchless Programming, Instruction Tables, Scheduling, Throughput Computing)
- Compilation (Stages, Flags, Situational Optimizations, Contract Programming, Non-Zero-Cost Abstractions, Compile-Time Computation, Arithmetic Optimizations)
- Profiling (Instrumentation, Statistical Profiling, Program Simulation, Machine Code Analyzers, Benchmarking)
- Arithmetic (Floating-Point, Interval Arithmetic, Newton's Method, Fast Inverse Square Root, Integers, Division, Bit Manipulation)
- Number Theory (Modular Inverse, Montgomery Multiplication, Cryptography, Hashing, Random Number Generation)
- External Memory (Hierarchy, Virtual Memory, EM Model, External Sorting, List Ranking, Eviction Policies, Cache-Oblivious Algorithms, Locality)
- RAM & CPU Caches (Bandwidth, Latency, Cache Lines, Memory Sharing, Memory-Level Parallelism, Prefetching, Alignment, Pointer Alternatives, Cache Associativity, Paging, AoS and SoA)
- SIMD Parallelism (Intrinsics, Moving Data, Reductions, Masking, In-Register Shuffles, Auto-Vectorization)
- Algorithm Case Studies (Binary GCD, Integer Factorization, Logistic Regression, Big Integers, FFT, NTT, Argmin with SIMD, Prefix Sum with SIMD, Parsing, Sorting, Matrix Multiplication)
- Data Structure Case Studies (Binary Search, Static B-Trees, Search Trees, Segment Trees, Hash Tables)

## Performance Goals
Examples of achieved speedups:
- 2x faster GCD
- 8-15x faster binary search
- 5-10x faster segment trees
- 5x faster hash tables
- 100x faster matrix multiplication
