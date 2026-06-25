---
title: "Address Sanitizer (ASan)"
tldr: "Fast memory error detector for C/C++ that catches out-of-bounds and use-after-free bugs."
date_created: 2026-05-09
date_modified: 2026-05-09
type: source
tags: [memory-safety, tool, c-cpp, debugging]
url: "https://github.com/google/sanitizers/wiki/AddressSanitizer"
---

# Address Sanitizer (ASan)

AddressSanitizer is a memory error detector for C/C++. It is used to detect out-of-bounds accesses (buffer overflows) and use-after-free bugs.

## Key Technical Points
- Uses shadow memory to track the validity of each byte of application memory.
- Instruments memory accesses to check against the shadow memory.
- Detects heap, stack, and global buffer overflows.

## Integration
See [[memory-management]] and [[operating-systems]] for system-level memory layout context.

## Bias Checks
- **Counter-arguments**: ASan has significant CPU and memory overhead, making it unsuitable for production environments where extreme performance is required.
- **Data gaps**: Detailed implementation of the shadow memory mapping for different architectures is not fully explored here.
