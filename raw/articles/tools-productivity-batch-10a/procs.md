---
original_url: https://github.com/dalance/procs
fetched_date: 2026-05-09
---

# procs - a replacement for `ps` written in Rust

`procs` is a modern replacement for the classic `ps` utility, providing a more user-friendly and colorful view of system processes.

## Key Features
- **Better Visibility**: Colored and human-readable output with automatic theme detection.
- **Advanced Search**: Supports multi-column keyword search (numeric for PID, non-numeric for USER/Command by default) with logical operations (`--and`, `--or`, `--nand`, `--nor`).
- **Extended Information**: Provides data not typically available in `ps`, such as:
    - TCP/UDP ports.
    - Read/Write throughput.
    - Docker container names.
    - Detailed memory information.
- **Modern Views**: 
    - **Watch Mode**: Real-time updates like `top` (using `--watch`).
    - **Tree View**: Shows process dependency trees (using `--tree`).
- **Customization**: Highly configurable via `config.toml` (column selection, styling, sorting, and search behavior).
- **Pager Support**: Automatically uses a pager (like `less`) if output exceeds terminal height.

## Installation
- **macOS**: `brew install procs`
- **Arch Linux**: `sudo pacman -S procs`
- **Fedora**: `sudo dnf install procs`
- **Windows**: `winget install procs` or `scoop install procs`
- **Debian/Ubuntu**: `sudo apt install procs` (if available) or via `.deb` package.
- **Cargo**: `cargo install procs`

## Usage Examples
- **Show all processes**: `procs`
- **Search for a process**: `procs zsh`
- **Filter by PIDs**: `procs --or 6000 60000`
- **Show process tree**: `procs --tree`
- **Watch mode**: `procs --watch`
- **Sort by CPU**: `procs --sortd cpu`

## Platform Support
- **Linux**: Fully supported.
- **Windows**: Supported.
- **macOS/FreeBSD**: Experimentally supported.
