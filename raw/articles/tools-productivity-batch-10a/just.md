---
original_url: https://github.com/casey/just
fetched_date: 2026-05-09
---

# just - a handy way to save and run project-specific commands

`just` is a command runner, not a build system. It allows you to store project-specific commands (called recipes) in a `justfile` with syntax inspired by `make`, but without its complexity and idiosyncrasies.

## Key Features
- **Not a Build System**: Avoids `make`'s complexity; no need for `.PHONY` recipes as all recipes are treated as phony.
- **Cross-platform**: Supports Linux, macOS, Windows, and other Unixes.
- **Recipe Arguments**: Recipes can accept command line arguments.
- **Env File Support**: Loads `.env` files to populate environment variables.
- **Arbitrary Languages**: Recipes can be written in any language using shebangs (e.g., Python, Node.js).
- **Flexible Invocation**: Can be invoked from any subdirectory.
- **Informative Errors**: Provides specific and informative syntax and runtime errors.

## Usage
Recipes are defined in a `justfile`. You run them with:
```bash
just <recipe-name>
```

## Installation
- **Cargo**: `cargo install just`
- **Homebrew**: `brew install just`
- **Arch Linux**: `pacman -S just`
- **Fedora**: `dnf install just`
- **Windows**: `choco install just` or `scoop install just` or `winget install --id Casey.Just --exact`

## Key Differences from `make`
- **Phony by default**: `just` doesn't check if a file with the recipe name exists; it always runs the recipe.
- **Simplified Syntax**: Avoids confusing distinctions like `=` vs `:=` for assignments.
- **Better Error Reporting**: Syntax errors are reported with source context.
