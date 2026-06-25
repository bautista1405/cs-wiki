---
title: "Fast UNIX Servers (Nick Black)"
tldr: "Guide to building high-performance UNIX servers, focusing on event cores, zero-copy I/O, and kernel tuning."
date_created: 2026-05-09
date_modified: 2026-05-09
type: source
tags: [unix, high-performance, networking, linux-kernel]
---

# Fast UNIX Servers (Nick Black)

## Summary
Technical guide on implementing high-performance servers on UNIX/Linux, emphasizing the elimination of bottlenecks in I/O and context switching.

## Central Design Principles
1. **Exploit all cycles/bandwidth**: Use multiple processing elements and avoid blocking I/O.
2. **Don't duplicate work**: Avoid unnecessary copies and system calls; use `splice(2)`.
3. **Measure continuously**: Use performance counters and eBPF.

## Technical Focus
- **Event Cores**: Comparison of `io_uring` (Linux), `kqueue` (FreeBSD), and `epoll`.
- **Zero-Copy I/O**: Use of `mmap(2)`, `sendfile(2)`, and `splice(2)` to minimize memory copying.
- **Hardware/OS Tuning**: NIC configuration via `ethtool`, huge pages, and CPU power states.

## Links
- Source: https://nick-black.com/dankwiki/index.php/Fast_UNIX_Servers
- Concept: [[linux-kernel-internals]]
- Concept: [[unix-philosophy]]
- Concept: [[performance-engineering]]
