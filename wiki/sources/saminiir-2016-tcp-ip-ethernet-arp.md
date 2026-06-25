---
title: "Let's Code a TCP/IP Stack: Ethernet & ARP"
tldr: "Tutorial on implementing a Linux userspace TCP/IP stack, focusing on L2 Ethernet frames and ARP."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [tcp-ip, networking, linux, ethernet, arp]
sources: []
original_url: "https://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/"
explored: false
confidence: high
---

# Summary: Let's Code a TCP/IP Stack: Ethernet & ARP

A technical guide on implementing a minimal userspace TCP/IP stack for Linux, starting from the Data Link Layer (Layer 2).

## Technical Implementation
- **TUN/TAP Devices**: Uses a Linux TAP device to intercept and manipulate Layer 2 traffic. The `IFF_TAP` and `IFF_NO_PI` flags are used to get raw Ethernet frames.
- **Ethernet Frame Parsing**: Implements the Ethernet header (Destination MAC, Source MAC, Ethertype) using `packed` structs in C to prevent compiler padding.
- **Address Resolution Protocol (ARP)**:
    - Maps L3 IP addresses to L2 MAC addresses.
    - Implements the ARP request/reply cycle.
    - Uses a translation table (ARP cache) to avoid redundant network traffic.

## Key Engineering Insights
- **Struct Packing**: Explicitly uses `__attribute__((packed))` in GNU C to ensure the memory layout matches the wire format of the protocol.
- **Userspace Networking**: Demonstrates that a full networking stack can exist outside the kernel provided a mechanism (like TAP) to feed raw frames.

## Counter-arguments
- The use of `packed` structs is a GNU extension and not strictly portable C; the author notes that manual serialization is the portable alternative.

## Data gaps
- The article is part one of a series; higher layer protocols (IPv4, TCP) are not covered here.
