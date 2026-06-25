---
original_url: https://github.com/BurntSushi/ripgrep
fetched_date: 2026-05-09
---

# ripgrep (rg)

ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern. It is designed to be faster than other search tools like The Silver Searcher, ack, and grep.

## Key Features
- **Default Filtering**: Respects `.gitignore` rules and automatically skips hidden files/directories and binary files (can be disabled with `rg -uuu`).
- **Recursive Search**: Defaults to recursive search.
- **Type-based Search**: Can search specific types of files (e.g., `rg -tpy foo` for Python files).
- **Unicode Support**: Full Unicode support is always on and maintains high performance.
- **Advanced Regex**: Optional support for PCRE2, enabling look-around and backreferences (`-P/--pcre2`).
- **Compressed Files**: Can search files compressed in common formats (brotli, bzip2, gzip, lz4, lzma, xz, or zstandard) with `-z/--search-zip`.
- **Speed**: Built on top of Rust's regex engine, utilizing finite automata, SIMD, and aggressive literal optimizations.

## Installation
Binary name is `rg`.
- macOS: `brew install ripgrep`
- Windows: `choco install ripgrep` or `scoop install ripgrep` or `winget install BurntSushi.ripgrep.MSVC`
- Arch Linux: `sudo pacman -S ripgrep`
- Fedora: `sudo dnf install ripgrep`
- Debian/Ubuntu: `sudo apt-get install ripgrep`

## Why use ripgrep?
- Generally faster than alternatives.
- Better default for code search (respects gitignore).
- Full Unicode support by default.
- Flexible configuration via configuration files.
