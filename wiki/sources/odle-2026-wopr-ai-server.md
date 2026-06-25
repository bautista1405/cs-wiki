---
title: "WOPR: A 7x4090 AI Server"
tldr: "Project documentation for building a high-performance AI server utilizing seven NVIDIA RTX 4090 GPUs."
date_created: 2026-05-08
date_modified: 2026-05-08
type: source
tags: [hardware, gpu, ai-server, hpc]
sources: ["https://mov_axbx.com/"]
explored: true
confidence: high
---

# WOPR: A 7x4090 AI Server

Documentation of a custom-built AI server project by Nathan Odle, focusing on massive GPU compute density.

## Project Highlights
- **Hardware**: Integration of 7x NVIDIA RTX 4090 GPUs.
- **Application**: Focused on AI workloads, including running llama2.c on legacy hardware (SGI Indigo2).
- **Experimental Range**: Projects range from high-end AI servers to Sega Dreamcast development.

## Relation to Concepts
Contributes to [[gpu-architecture]] and [[computer-architecture]] by demonstrating the practical challenges and implementation of multi-GPU clusters.

## Bias Checks
- **Counter-arguments**: This is a hobbyist/experimental build; production-grade AI servers usually employ interconnects like NVLink rather than pure PCIe-based layouts seen in consumer GPU clusters.
- **Data gaps**: Specific power delivery and thermal management details are not fully detailed in the landing page.
