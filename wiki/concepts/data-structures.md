---
title: "Data Structures"
tldr: "Concept related to Coding Interview University"
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: []
sources: ["[[coding-interview-university]]"]
explored: false
confidence: high
explored: true
tags: [\"computer-science\", \"data-structures\", \"coding-interview\"]
---

# Data Structures

Data structures are specialized formats for organizing, processing, retrieving and storing data. They are fundamental to the efficiency of algorithms.

## Classification
- **Linear Data Structures**:
    - **Arrays**: Fixed-size, contiguous memory.
    - **Linked Lists**: Singly, doubly, and circular; dynamic size.
    - **Stacks**: LIFO (Last-In-First-Out).
    - **Queues**: FIFO (First-In-First-Out), Deques.
- **Non-Linear Data Structures**:
    - **Trees**: Binary Trees, BST, AVL, Red-Black Trees, Heaps, Tries.
    - **Graphs**: Directed, Undirected, Weighted; Adjacency list/matrix representation.
    - **Hash Tables**: Key-value pairs with $O(1)$ average time complexity for lookup.

## Time and Space Complexity (Big O)
- **Access**: Array $O(1)$, Linked List $O(n)$.
- **Search**: Balanced BST $O(\log n)$, Hash Table $O(1)$ average.
- **Insertion/Deletion**: Stack/Queue $O(1)$, Balanced BST $O(\log n)$.

## Implementation Tips
- Always consider memory overhead (e.g., pointers in linked lists).
- Choose based on the dominant operation (read-heavy vs write-heavy).

## Counter-arguments
- Over-reliance on standard library collections can lead to a lack of understanding of underlying memory layouts.

## Data gaps
- Advanced concurrent data structures (e.g., lock-free queues).