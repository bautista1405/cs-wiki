---
title: "Observability and Profiling"
tldr: "The practice of understanding a system's internal state from its external outputs, using tools like eBPF and sampling profilers."
date_created: 2026-05-09
date_modified: 2026-05-09
type: concept
tags: [observability, profiling, monitoring, linux]
sources: ["[[gregg-2026-bpf-perf-tools]]", "[[datadog-2026-ddprof]]", "[[thompson-2026-performance-tuning]]"]
explored: false
confidence: high
---

# Observability and Profiling

Observability is the ability to measure the internal state of a system by examining its outputs. Profiling is a subset of observability focused on resource utilization (CPU, memory).

## Modern Observability Stack
- **Low-overheads**: Tools like [[datadog-2026-ddprof]] use sampling to provide production insights without crashing the system.
- **Kernel-level insights**: eBPF, as detailed in [[gregg-2026-bpf-perf-tools]], allows for deep inspection of kernel events without modifying the kernel itself.
- **Visual Analysis**: Flame graphs (discussed in [[thompson-2026-performance-tuning]]) translate raw profile data into intuitive visual hierarchies of time spent in functions.

## Counter-arguments
- High-resolution observability often introduces the "observer effect," where the act of measuring changes the behavior of the system.

## Data gaps
- Comparison of eBPF versus traditional tracing (ptrace, dtrace) in terms of precision and overhead.
