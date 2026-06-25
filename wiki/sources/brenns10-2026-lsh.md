---
author: brenns10
year: 2026
title: LSH (Shell in C)
---
# LSH (Shell in C)

LSH is a simple implementation of a shell in C. It demonstrates the basics of how a shell works: read, parse, fork, exec, and wait.

## Implementation Details
- Builtins: `cd`, `help`, `exit`.
- Process Cycle: Read line, parse arguments, fork a child process, execute command using `execvp`, and wait for completion.

## Limitations
- Commands must be on a single line.
- Arguments must be separated by whitespace.
- No quoting arguments or escaping whitespace.
- No piping or redirection.

## Bias Checks
- **Counter-arguments**: A production shell requires complex signal handling and terminal state management not covered here.
- **Data gaps**: Lacks implementation of job control (fg/bg) and advanced redirection.

## Reference
- Tutorial: http://brennan.io/2015/01/16/write-a-shell-in-c/
- Original Source: https://github.com/brenns10/lsh
