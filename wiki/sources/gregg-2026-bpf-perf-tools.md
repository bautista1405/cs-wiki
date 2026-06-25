---
title: "BPF Performance Tools Book"
tldr: "Comprehensive guide to using eBPF (extended Berkeley Packet Filter) for observability and performance analysis on Linux."
date_created: 2026-05-09
date_modified: 2026-05-09
type: source
tags: [ebpf, linux, observability, performance]
url: "https://github.com/brendangregg/bpf-perf-tools-book"
---

# BPF Performance Tools Book

This source provides an extensive look at utilizing eBPF for low-level system observability.

## Key Technical Points
- eBPF allows running sandboxed programs inside the kernel without changing kernel source code.
- Essential for profiling I/O, networking, and scheduler latency.
- Bridges the gap between high-level metrics and low-level kernel events.

## Integration
See [[observability-and-profiling]] and [[linux-kernel-internals]].

## Bias Checks
- **Counter-arguments**: eBPF's power comes with complexity; writing safe eBPF programs requires understanding the kernel verifier.
- **Data gaps**: Specific performance overhead of eBPF hooks compared to traditional kprobes.
