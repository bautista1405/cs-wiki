---
title: "ddprof"
tldr: "DataDog's continuous profiler for production environments, focusing on low-overhead sampling."
date_created: 2026-05-09
date_modified: 2026-05-09
type: source
tags: [profiling, observability, production, monitoring]
url: "https://github.com/DataDog/ddprof"
---

# ddprof

ddprof is a production-grade profiler designed to minimize the "observer effect" while providing actionable performance data.

## Key Technical Points
- Employs sampling-based profiling to reduce overhead.
- Focuses on stack trace aggregation to identify hotspots across a fleet of servers.

## Integration
See [[observability-and-profiling]] and [[performance-engineering]].

## Bias Checks
- **Counter-arguments**: Sampling profilers can miss sporadic, short-lived spikes that a tracing profiler would catch.
- **Data gaps**: Exact sampling frequency and the resulting error margin in CPU time attribution.
