---
original_url: https://github.com/junegunn/fzf
fetched_date: 2026-05-09
---

# fzf - a command-line fuzzy finder

fzf is a general-purpose command-line fuzzy finder. It is an interactive filter program for any kind of list: files, command history, processes, hostnames, bookmarks, git commits, etc.

## Highlights
- **Portable**: Distributed as a single binary for easy installation.
- **Fast**: Optimized to process millions of items instantly.
- **Versatile**: Fully customizable through an event-action binding mechanism.
- **All-inclusive**: Comes with integrations for Bash, Zsh, Fish, Vim, and Neovim.

## Usage
fzf reads the list from STDIN and writes the selected item to STDOUT.
- **Basic use**: `find * -type f | fzf > selected`
- **Command substitution**: `vim $(fzf)`
- **Custom source**: Set `$FZF_DEFAULT_COMMAND` (e.g., `export FZF_DEFAULT_COMMAND='fd --type f'`).

## Key Bindings (via shell integration)
- `CTRL-T`: Paste selected files and directories onto the command-line.
- `CTRL-R`: Paste selected command from history onto the command-line.
- `ALT-C`: cd into the selected directory.

## Fuzzy Completion
Triggered by default with `**<TAB>`.
- **Files/Dirs**: `vim **<TAB>`
- **PIDs**: `kill -9 **<TAB>`
- **Hostnames**: `ssh **<TAB>`
- **Env Vars/Aliases**: `unset **<TAB>`, `export **<TAB>`, `unalias **<TAB>`

## Display Modes
- **Fullscreen**: Default mode.
- **Height mode**: `--height 40%` starts the finder below the cursor with the given height.
- **Popup mode**: `--popup` starts in a popup window (requires tmux 3.3+ or Zellij 0.44+).

## Advanced Features
- **Preview Window**: Use `--preview 'bat --color=always {}'` to show file contents.
- **Reloading**: Bind keys to `reload` action to dynamically update the list.
- **Process Transformation**: Use `become(...)` to turn fzf into another process (e.g., `fzf --bind 'enter:become(vim {})'`).

## Installation
- macOS/Linux: `brew install fzf`
- Debian/Ubuntu: `sudo apt install fzf`
- Arch Linux: `sudo pacman -S fzf`
- Windows: `choco install fzf` or `scoop install fzf` or `winget install fzf`
