---
title: "Algorithm Patterns for Live Coding Interviews"
tldr: "Guide on mapping problem constraints and requirements to specific algorithm patterns and data structures."
date_created: 2026-05-08
date_modified: 2026-05-08
type: output
tags: [coding-interview, algorithms, patterns]
sources: ["[[coding-interview]]", "[[algorithms]]", "[[data-structures]]"]
explored: false
confidence: medium
---

# Algorithm Patterns and Problem Detection

Passing live coding interviews requires the ability to quickly map a problem's constraints and requirements to a known **algorithmic pattern**. Instead of memorizing problems, focus on identifying "triggers" in the problem description.

## 1. Common Pattern Mapping

| If you see... | Try this Pattern | Primary Data Structure |
| :--- | :--- | :--- |
| **Sorted Array** | Binary Search / Two Pointers | Array |
| **Top K / Frequent Elements** | Heap / Priority Queue | Min/Max-Heap |
| **Permutations / Combinations** | Backtracking | Recursion Stack |
| **Shortest Path (Unweighted)** | BFS | Queue |
| **Shortest Path (Weighted)** | Dijkstra / A* | Priority Queue |
| **Connected Components / Cycle** | DFS / Union Find | Graph / Disjoint Set |
| **Subarray sum / Window limits** | Sliding Window | Deque / Two Pointers |
| **Repeated Subproblems** | Dynamic Programming | Hash Map / Array (Memo) |
| **Nested Structures / Valid Pairs** | Stack | Stack |
| **Prefixes / Dictionary search** | Trie | Trie |

## 2. How to Detect Patterns (The "Triggers")

### Two Pointers / Sliding Window
- **Trigger:** "Find a contiguous subarray", "Longest substring with K distinct characters".
- **Key Detection:** The input is typically linear (array/string) and you need to find a range that satisfies a condition.
- **Complexity:** Usually reduces $O(N^2)$ to $O(N)$.

### Breadth-First Search (BFS)
- **Trigger:** "Shortest number of steps", "Minimum distance", "Level-order traversal".
- **Key Detection:** You are dealing with a graph or tree and want the most immediate neighbors first.

### Depth-First Search (DFS) / Backtracking
- **Trigger:** "All possible paths", "Find any valid solution", "Explore all combinations".
- **Key Detection:** The problem asks to exhaustively search a state space.

### Heap (Priority Queue)
- **Trigger:** "Find the K-th largest/smallest", "Merge K sorted lists", "Top K".
- **Key Detection:** You need constant access to the extreme (min or max) element while adding new elements.

### Monotonic Stack/Queue
- **Trigger:** "Next greater element", "Largest rectangle in histogram".
- **Key Detection:** You need to find the first element to the left/right that is larger/smaller than the current one.

## 3. Live Interview Strategy

1. **Clarify Constraints:** Ask about the size of the input. $N=10^5$ suggests $O(N \log N)$ or $O(N)$. $N=20$ suggests backtracking.
2. **Brute Force First:** State the naive approach ($O(N^2)$ or $O(2^N)$) to show you understand the problem, then explain *why* it is inefficient.
3. **Pattern Match:** Look for the triggers listed above. "Sorted array" $\rightarrow$ "Binary Search".
4. **Dry Run:** Before coding, trace a small example through your chosen pattern on a whiteboard/editor.
5. **Complexity Analysis:** State the Time and Space complexity *before* you start writing the implementation.

## Counter-arguments
- Some problems are "hybrid" and require combining two patterns (e.g., Binary Search on the answer + a BFS check).
- Strict pattern matching can lead to "tunnel vision"; always be ready to pivot if the constraints change.

## Data gaps
- Specific language-level optimizations (e.g., using `collections.deque` in Python vs `ArrayList` in Java) are not detailed here.
- High-level system design patterns are outside the scope of this algorithm guide.
