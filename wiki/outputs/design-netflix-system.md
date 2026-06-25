---
title: "Design Netflix System"
tldr: "Architectural breakdown of Netflix, focusing on the trade-offs between availability, consistency and the use of CDNs."
date_created: 2026-05-08
date_modified: 2026-05-08
type: output
tags: [system-design, case-study, a-list-architecture]
sources: ["[[system-design]]", "[[cap-theorem]]", "[[load-balancing]]", "[[distributed-replication]]", "[[consistency-models]]", "[[idempotency]]"]
explored: false
confidence: high
---

# Designing Netflix's System Architecture

Designing a system like Netflix requires balancing massive read volume (streaming) with occasional high-volume writes (user profiles, views). The architecture must be globally distributed to minimize latency.

## 1. Functional & Non-Functional Requirements
Following the framework in [[system-design]]:
- **Functional**: User profiles, content discovery (search/recommendations), video streaming, billing.
- **Non-Functional**: 
    - **High Availability**: Netflix cannot go down; a failure in one region should not affect others.
    - **Scalability**: Needs to handle 200M+ users.
    - **Low Latency**: Video playback must be instantaneous (near-zero buffering).

## 2. High-Level Architecture
The system follows a distributed microservices pattern:

### Edge Layer (The Gateway)
- **DNS & Load Balancing**: Uses Global Server Load Balancing (GSLB) to route users to the nearest AWS region. See [[load-balancing]].
- **CDN (Open Connect)**: Netflix's secret weapon. They build their own Content Delivery Network (CDN) to place video files physically close to users, drastically reducing latency.

### Control Plane (The Brain)
- **API Gateway**: Handles authentication and routing to specific microservices.
- **Microservices**: Individual services for Billing, Profiles, and Recommendations. These are designed as **AP** systems (per [[cap-theorem]]) to ensure availability over perfect consistency.
- **Database Choice**: 
    - **Cassandra**: Used for high-availability, write-heavy data (view history). It follows the **Eventual Consistency** model ([[consistency-models]]).
    - **MySQL**: Used for structured, strongly consistent data (billing/accounts).

### Data Plane (The Video Pipeline)
- **Transcoding**: A massive pipeline that takes a high-res master file and creates thousands of versions (different resolutions/formats) to suit every device and network speed.
- **Storage**: S3 for storing the raw and transcoded files.

## 3. Distributed Systems Logic Applied
- **Consistency vs Availability**: For the 'Continue Watching' list, Netflix accepts **Eventual Consistency** ([[consistency-models]]). If you watch a show and it doesn't show up on your phone for 5 seconds, it's an acceptable trade-off for 100% availability.
- **Durability through Replication**: Data is copied across multiple regions ([[distributed-replication]]) to survive catastrophic regional AWS failures.
- **Idempotency**: In the billing service, **Idempotency Keys** ([[idempotency]]) are critical to ensure a user isn't charged twice if a network request is retried ([[retry-and-backoff]]).

## 4. System Thinking & Bottlenecks
- **The Bottleneck**: The primary bottleneck is the "last mile" of the internet. The solution is the Open Connect CDN.
- **Trade-off**: By choosing an **AP** architecture for the control plane, Netflix trades off the risk of a user seeing a slightly old profile picture for the guarantee that the app always opens instantly.

## Summary Table
| Component | Strategy | Wiki Concept |
|---|---|---|
| Global Traffic | GSLB / CDN | [[load-balancing]] |
| User History | Cassandra | [[consistency-models]] $
ightarrow$ Eventual |
| Billing | MySQL / Idempotency Keys | [[idempotency]] $
ightarrow$ Strong |
| Reliability | Multi-Region | [[distributed-replication]] |

