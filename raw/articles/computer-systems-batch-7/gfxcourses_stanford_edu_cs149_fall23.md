---
original_url: https://gfxcourses.stanford.edu/cs149/fall23/
fetched_date: 2026-05-09
---

[Home]
[Feed]
[Course Info]
[Lectures/Readings]
[Login]
Stanford CS149, Fall 2023
PARALLEL COMPUTING
From smart phones, to multi-core CPUs and GPUs, to the world's largest supercomputers and web sites, parallel processing is ubiquitous in modern computing. The goal of this course is to provide a deep understanding of the fundamental principles and engineering trade-offs involved in designing modern parallel computing systems as well as to teach parallel programming techniques necessary to effectively utilize these machines. Because writing good parallel programs requires an understanding of key machine performance characteristics, this course will cover both parallel hardware and software design.
Basic Info
Time: Tues/Thurs 10:30-11:50am
Location: NVIDIA Auditorium
Instructors:
Kayvon Fatahalian
and
Kunle Olukotun
See the
course info
page for more info on policies and logistics.
Fall 2023 Schedule
Sep 26
Why Parallelism? Why Efficiency?
Challenges of parallelizing code, motivations for parallel chips, processor basics
Sep 28
A Modern Multi-Core Processor
Forms of parallelism: multi-core, SIMD, and multi-threading
Oct 03
Multi-core Arch Part II + ISPC Programming Abstractions
Finish up multi-threaded and latency vs. bandwidth. ISPC programming, abstraction vs. implementation
Oct 05
Parallel Programming Basics
Ways of thinking about parallel programs, thought process of parallelizing a program in data parallel and shared address space models
Oct 10
Performance Optimization I: Work Distribution and Scheduling
Achieving good work distribution while minimizing overhead, scheduling Cilk programs with work stealing
Oct 12
Performance Optimization II: Locality, Communication, and Contention
Message passing, async vs. blocking sends/receives, pipelining, increasing arithmetic intensity, avoiding contention
Oct 17
GPU architecture and CUDA Programming
CUDA programming abstractions, and how they are implemented on modern GPUs
Oct 19
Data-Parallel Thinking
Data-parallel operations like map, reduce, scan, prefix sum, groupByKey
Oct 24
Distributed Data-Parallel Computing Using Spark
Producer-consumer locality, RDD abstraction, Spark implementation and scheduling
Oct 26
Efficiently Evaluating DNNs on GPUs
Efficiently scheduling DNN layers, mapping convs to matrix-multiplication, transformers, layer fusion
Oct 31
Cache Coherence
Definition of memory coherence, invalidation-based coherence using MSI and MESI, false sharing
Nov 02
Memory Consistency
Relaxed consistency models and their motivation, acquire/release semantics
Nov 07
Democracy Day (no class)
Take time to volunteer/educate yourself/take action!
Nov 09
Fine-Grained Synchronization and Lock-Free Programming
Fine-grained synchronization via locks, basics of lock-free programming: single-reader/writer queues, lock-free stacks, the ABA problem, hazard pointers
Nov 14
Midterm Review
The midterm will be an evening midterm on Nov 15th. We will use the class period as a review period.
Nov 16
Domain Specific Programming Languages
Performance/productivity motivations for DSLs, case studies on several DSLs
Nov 28
Transactional Memory 1
Motivation for transactions, design space of transactional memory implementations.
Nov 30
Transactional Memory 2
Finishing up transactional memory focusing on implementations of STM and HTM.
Dec 05
Hardware Specialization
Energy-efficient computing, motivation for heterogeneous processing, fixed-function processing, FPGAs, mobile SoCs
Dec 07
Accessing Memory + Course Wrap Up
How DRAM works, suggestions for post-cs149 topics
Dec 14
Final Exam
Held at 3:30pm. Location TBD
Programming Assignments
Oct 6
Assignment 1: Analyzing Parallel Program Performance on a Quad-Core CPU
Oct 20
Assignment 2: Scheduling Task Graphs on a Multi-Core CPU
Nov 8
Assignment 3: A Simple Renderer in CUDA
Dec 4
Assignment 4: Chat149 - A Flash Attention Transformer DNN
Dec 8
[Optional Assignment 5]: Big Graph Processing
Written Assignments
Oct 10
Written Assignment 1
Oct 26
Written Assignment 2
Nov 3
Written Assignment 3
Nov 11
Written Assignment 4
Dec 6
Written Assignment 5