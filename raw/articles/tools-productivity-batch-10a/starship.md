---
original_url: https://github.com/starship/starship
fetched_date: 2026-05-09
---

# Starship - Cross-shell prompt

Starship is a minimal, blazing-fast and infinitely customizable prompt for any shell.

## Key Features
- **Fast**: Extremely high performance, written in Rust.
- **Customizable**: Every aspect of the prompt can be configured.
- **Universal**: Works on any shell (Bash, Zsh, Fish, Nushell, PowerShell, etc.) and any operating system.
- **Intelligent**: Shows relevant information at a glance (e.g., git status, package versions, etc.).
- **Feature rich**: Built-in support for all your favorite tools and languages.

## Installation
Quick installation via script:
```sh
curl -sS https://starship.rs/install.sh | sh
```

Alternatively, via package managers:
- macOS: `brew install starship`
- Arch Linux: `pacman -S starship`
- Ubuntu/Debian: `apt install starship`
- Windows: `choco install starship` or `scoop install starship` or `winget install --id Starship.Starship`

## Setup
Depending on the shell, add the initialization command to your config file (e.g., `~/.zshrc`, `~/.bashrc`, etc.):
- **Bash**: `eval "$(starship init bash)"`
- **Zsh**: `eval "$(starship init zsh)"`
- **Fish**: `starship init fish | source`
- **PowerShell**: `Invoke-Expression (&starship init powershell)`

## Configuration
Detailed configuration options and presets are available at [starship.rs/config/](https://starship.rs/config/).
