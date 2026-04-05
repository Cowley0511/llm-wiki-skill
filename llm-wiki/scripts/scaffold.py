#!/usr/bin/env python3
"""
scaffold.py — Bootstrap a new LLM Wiki directory structure.

Usage:
    python3 scaffold.py <wiki-root> "<Topic Title>"

Example:
    python3 scaffold.py ~/wikis/ai-research "AI Research"

Creates:
    <wiki-root>/
    ├── CLAUDE.md          (schema template)
    ├── log.md             (empty log)
    ├── raw/
    │   ├── articles/
    │   ├── papers/
    │   └── notes/
    ├── wiki/
    │   ├── index.md       (empty catalog)
    │   ├── concepts/
    │   ├── entities/
    │   └── summaries/
    └── outputs/
        └── queries/
"""

import os
import sys
from datetime import date


def scaffold(root: str, title: str) -> None:
    today = date.today().isoformat()

    dirs = [
        "raw/articles",
        "raw/papers",
        "raw/notes",
        "wiki/concepts",
        "wiki/entities",
        "wiki/summaries",
        "outputs/queries",
    ]

    for d in dirs:
        os.makedirs(os.path.join(root, d), exist_ok=True)
    print(f"✓ Created directory tree under {root}/")

    # CLAUDE.md
    claude_md = f"""# {title} Knowledge Base

> Schema document — read at the start of every session.  
> Update after every major compile, ingest batch, or structural change.

## Scope

What this wiki covers:
- <describe the topic area>

What this wiki deliberately excludes:
- <describe out-of-scope areas>

## Naming conventions

- **Concept pages** (`wiki/concepts/`): Title Case noun phrases
- **Entity pages** (`wiki/entities/`): Proper names
- **Summary pages** (`wiki/summaries/`): kebab-case source slug

All pages require frontmatter: `title`, `type`, `created`, `updated`, `sources`, `tags`.

## Current articles

*None yet — update this list after every compile.*

## Open research questions

- <What do you want to understand better?>
- <What are the key open questions in this domain?>

## Research gaps

Sources to ingest:
- [ ] <URL or paper title> — why it's relevant
"""
    _write(root, "CLAUDE.md", claude_md)
    print("✓ Created CLAUDE.md")

    # log.md
    log_md = f"""# Log

Append-only chronological record of all wiki operations.  
Format: `## [YYYY-MM-DD] <op> | <description>`  
Ops: `ingest`, `compile`, `query`, `lint`, `promote`, `split`

Quick grep: `grep "^## \\[" log.md | tail -10`

---

## [{today}] scaffold | Initialized {title} knowledge base
"""
    _write(root, "log.md", log_md)
    print("✓ Created log.md")

    # wiki/index.md
    index_md = f"""# Index — {title}

Master catalog of all wiki pages. Updated by LLM on every ingest.

## Concepts

*(none yet)*

## Entities

*(none yet)*

## Summaries

*(none yet)*
"""
    _write(root, "wiki/index.md", index_md)
    print("✓ Created wiki/index.md")

    print(f"""
✅ Wiki scaffolded at: {root}/

Next steps:
  1. Fill in CLAUDE.md — define scope and naming conventions
  2. Add sources to raw/ (use Obsidian Web Clipper for web articles)
  3. Run ingest: tell your LLM agent "ingest raw/<file>.md"
  4. Ask questions: "what does the wiki say about X?"
  5. Run lint periodically: python3 lint_wiki.py {root}/
""")


def _write(root: str, path: str, content: str) -> None:
    full = os.path.join(root, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    scaffold(sys.argv[1], sys.argv[2])
