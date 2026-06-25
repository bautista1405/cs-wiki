---
original_url: https://github.com/brenns10/lsh
date: 2026-05-09
---
# LSH (Shell in C)

LSH is a simple implementation of a shell in C. It demonstrates the basics of how a shell works: read, parse, fork, exec, and wait.

## Limitations
- Commands must be on a single line.
- Arguments must be separated by whitespace.
- No quoting arguments or escaping whitespace.
- No piping or redirection.
- Builtins: `cd`, `help`, `exit`.

## Running
Use `gcc -o lsh src/main.c` to compile, and then `./lsh` to run.
Alternatively: `gcc -DLSH_USE_STD_GETLINE -o lsh src/main.c`.

## Reference
Tutorial: http://brennan.io/2015/01/16/write-a-shell-in-c/
