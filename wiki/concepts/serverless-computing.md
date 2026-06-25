---
title: "Serverless Computing"
tldr: "A cloud computing execution model where the cloud provider dynamically manages the allocation of machine resources."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [serverless, cloud-computing, virtualization, lambda]
sources: ["[[mit-2023-os-serverless]]"]
explored: false
confidence: medium
---

# Serverless Computing

**Serverless Computing** is a cloud architectural laeyr where the developer provides code (functions) and the platform manages the underlying infrastructure, including scaling, patching, and resource allocation.

## Key Research Areas
As detailed in the MIT 6.5810 Seminar ([[mit-2023-os-serverless]]), key areas of focus include:
- **Cold Start Optimization**: Efforts to reduce the latency of loading containers (e.g., the AWS Lambda on-demand loading research).
- **State Management**: Moving from stateless functions to stateful serverless via shared logs (Boki) or stateful functions-as-a-service (Cloudburst).
- **Lightweight Isolation**: Using MicroVMs like Firecracker and gVisor to balance the security of VMs with the speed of containers.

## Counter-arguments
- "Serverless" is a misnomer as servers still exist; the abstraction can lead to inefficient resource use (over-provisioning) or "vendor lock-in" to a specific cloud provider's API.

## Data gaps
- Lacks a comparison of cost-efficiency between serverless and traditional Kubernetes/K8s orchestration for different workload profiles.
