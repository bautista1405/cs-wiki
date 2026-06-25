# LLM Wikid

An AI-maintained knowledge base that lives in Obsidian. Based on [Karpathy's LLM Wiki pattern](https://x.com/karpathy/status/1890540708772143562).

You dump raw sources into a folder. An AI agent reads them, compiles structured wiki pages with cross-references, runs bias checks, and maintains a master index. Every question you ask gets filed back in. The wiki compounds the more you use it.

Works with any agent that can read markdown and run shell commands: Claude Code, OpenClaw, Hermes, Codex, or your own setup.

## Quick Start

```bash
git clone https://github.com/shannhk/llm-wikid.git my-wiki
cd my-wiki

# open as an Obsidian vault
# File > Open Vault > select the my-wiki folder

# start your agent
claude --dangerously-skip-permissions   # Claude Code
# or open with OpenClaw, Hermes, Codex, etc.
```

The agent reads `CLAUDE.md` and knows everything. That file is the schema that controls the entire system.