---
original_url: https://github.com/sharkdp/bat
fetched_date: 2026-05-09
---

# bat - a cat clone with wings

A `cat(1)` clone with syntax highlighting and Git integration.

## Key Features
- Syntax highlighting for a large number of programming and markup languages.
- Git integration showing modifications with respect to the index.
- Show non-printable characters using `-A`/`--show-all`.
- Automatic paging: pipes output to a pager (e.g., `less`) if the output is too large for one screen.

## How to use
- Display a single file: `bat README.md`
- Display multiple files: `bat src/*.rs`
- Read from stdin: `curl -s https://sh.rustup.rs | bat`
- Specify language explicitly: `yaml2json .travis.yml | json_pp | bat -l json`
- Use as `cat` replacement: `bat > note.md`

## Installation
Available on most major distributions:
- Ubuntu/Debian: `sudo apt install bat` (may be installed as `batcat`)
- Arch Linux: `pacman -S bat`
- Fedora: `dnf install bat`
- macOS: `brew install bat`
- Windows: `winget install sharkdp.bat`

## Customization
- Themes: `bat --list-themes` to see available themes. Set via `--theme` or `BAT_THEME`.
- Output Style: Use `--style` to control components (numbers, changes, header, grid, etc.).
- Pager: Respects `PAGER` environment variable, defaults to `less`.

## Project Goals
- Provide beautiful, advanced syntax highlighting.
- Integrate with Git to show file modifications.
- Be a drop-in replacement for (POSIX) `cat`.
- Offer a user-friendly command-line interface.
