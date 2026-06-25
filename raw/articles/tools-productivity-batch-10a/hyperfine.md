---
original_url: https://github.com/sharkdp/hyperfine
fetched_date: 2026-05-09
---

# hyperfine - a command-line benchmarking tool

`hyperfine` is a powerful command-line tool for benchmarking shell commands, providing statistical analysis and a wide range of features for accurate timing.

## Key Features
- **Statistical Analysis**: Performs multiple runs and provides mean, min, max, and standard deviation.
- **Arbitrary Commands**: Supports any shell command for benchmarking.
- **Warmup Runs**: Execute warmup runs before the actual benchmark to avoid cold-start bias.
- **Cache Clearing**: Support for preparation commands to clear caches before each run.
- **Outlier Detection**: Detects interference from other programs or caching effects.
- **Parameterized Benchmarks**: Vary parameters (e.g., number of threads) across a series of benchmarks.
- **Export Formats**: Export results to CSV, JSON, Markdown, and AsciiDoc.
- **Shell Correction**: Corrects for shell spawning time automatically.

## Usage
### Basic Benchmark
```sh
hyperfine 'sleep 0.3'
```

### Comparing Commands
```sh
hyperfine 'hexdump file' 'xxd file'
```

### Warmup and Prepare
- **Warmup**: `--warmup 3 'grep -R TODO *'`
- **Prepare**: `--prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' 'grep -R TODO *'`

### Parameterized Benchmarks
```sh
hyperfine --parameter-scan num_threads 1 12 'make -j {num_threads}'
```

## Installation
- **macOS**: `brew install hyperfine`
- **Ubuntu/Debian**: `apt install hyperfine`
- **Arch Linux**: `pacman -S hyperfine`
- **Windows**: `choco install hyperfine` or `scoop install hyperfine` or `winget install hyperfine`
- **Cargo**: `cargo install --locked hyperfine`
