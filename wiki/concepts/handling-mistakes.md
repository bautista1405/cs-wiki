---
title: "Handling Mistakes in Live Coding"
tldr: "Strategies for recovering from errors or logical blocks during a live technical interview."
date_created: 2026-05-08
date_modified: 2026-05-08
type: concept
tags: [coding-interview, psychology]
sources: ['[[blog-pramp-com-how-to-pass-the-coding-interview-]]']
explored: false
confidence: medium
---

Mistakes are inevitable in high-pressure live coding. The interview is as much about *how you recover* as it is about the initial solution.

### Recovery Strategies
1. **Acknowledge and Narrate**: If you spot a bug, don't freeze. Say: 'I just realized my loop index is off by one, let me correct that.'
2. **The 'Reset' Technique**: If completely stuck, summarize what you know and what you're missing. 'I know the target complexity is O(n), and I'm currently at O(n^2) because of this nested loop. I need a way to track X without re-scanning.'
3. **Validate Input**: When a solution isn't working, manually trace a simple test case (e.g., array of size 2) aloud to find the logic gap.

### What to Avoid
- **Silent Panicking**: Long periods of silence are a red flag for interviewers.
- **Ignoring Hints**: If an interviewer suggests a different path, acknowledge it immediately. 'That's an interesting point, if I use a Map here, I could potentially reduce the time...'

### Interviewer's Perspective
Interviewer look for 'signal' on: debugging ability, resilience, and willingness to accept feedback.

## Counter-arguments
TBD

## Data gaps
TBD

### Related
- [[coding-interview]]
- [[mock-interviews]]
