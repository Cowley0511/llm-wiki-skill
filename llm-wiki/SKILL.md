---
name: llm-wiki
description: Build and maintain a Karpathy-style LLM knowledge base — a self-compiling Obsidian markdown wiki where an Agent ingests raw sources, compiles cross-linked concept/entity/summary pages, files Q&A answers back into the corpus, and runs periodic lint-and-heal passes. Use when: (1) scaffolding a new knowledge base for any research topic, (2) ingesting articles, papers, PDFs, or web pages into raw/, (3) compiling or updating wiki articles from sources, (4) answering questions against the wiki and filing answers back, (5) running lint passes to find orphan pages, dead links, or coverage gaps. Not for general note-taking, daily journals, or non-wiki Obsidian use.
---

# LLM Wiki — Karpathy Knowledge Base Pattern

> **Experimental skill — will iterate over time.**  
> Authored by Lewis Liu (lylewis@outlook.com) · Inspired by [Karpathy's llm-wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Core idea

Instead of RAG (re-retrieving raw docs on every query), the LLM **compiles** raw sources into a persistent, cross-linked wiki. Every ingest, query, and lint pass makes the wiki richer. Knowledge compounds.

- **You** own: sourcing raw material, asking good questions, steering direction  
- **LLM** owns: all writing, cross-referencing, filing, bookkeeping

## Directory layout

```
<wiki-root>/
├── CLAUDE.md          ← Schema: scope, conventions, current articles, gaps
├── log.md             ← Append-only chronological audit trail
├── raw/               ← Immutable source documents (LLM reads, never writes)
│   ├── articles/      ← Web articles, saved as .md
│   ├── papers/        ← Academic papers, PDFs or extracted text
│   └── notes/         ← Personal notes, podcast summaries, meeting notes
├── wiki/              ← LLM-generated knowledge (LLM writes, you read)
│   ├── index.md       ← Master catalog: every page + one-line summary
│   ├── concepts/      ← One .md per concept/topic (3-level depth max)
│   ├── entities/      ← People, tools, papers, organizations
│   └── summaries/     ← Per-source summary pages
└── outputs/           ← Query answers, analyses, charts (filed back to wiki when durable)
    └── queries/
```

`CLAUDE.md` is the **schema file** — the single most important configuration. It tells the LLM the wiki's scope, naming conventions, and current state. Read `references/schema-guide.md` for what to put in it.

## The three operations

### 1. Ingest

Add a new source. Steps:

1. Save source to `raw/<subfolder>/<slug>.md` (web → articles/, paper → papers/, notes → notes/)
2. LLM reads source and:
   - Creates `wiki/summaries/<slug>.md` (key takeaways, 200–400 words)
   - Creates or updates relevant concept pages in `wiki/concepts/`
   - Creates or updates entity pages in `wiki/entities/`
   - Updates `wiki/index.md`
3. Append to `log.md`:  
   `## [YYYY-MM-DD] ingest | <slug> — <one-line description>`

**One source typically touches 5–15 wiki pages.**

### 2. Query

Ask any question against the wiki. Steps:

1. Read `wiki/index.md` — scan for relevant pages
2. Read the identified pages in full; follow one level of wikilinks
3. Synthesize answer grounded in wiki content (cite pages inline)
4. Save answer to `outputs/queries/<YYYY-MM-DD>-<question-slug>.md`
5. If the answer is durable (a comparison, analysis, or new synthesis) → **promote to `wiki/concepts/`**
6. Append to `log.md`:  
   `## [YYYY-MM-DD] query | <question-slug>`

**Do not answer from general knowledge alone — the wiki is the source of truth.**

### 3. Lint

Periodic health check. Run:

```bash
python3 scripts/lint_wiki.py <wiki-root>
```

The script reports:
- Dead wikilinks (link target doesn't exist)
- Orphan pages (no inbound links)
- Missing index entries
- Concepts mentioned in multiple pages but lacking their own page

For each issue, propose fix and confirm before applying. Append:  
`## [YYYY-MM-DD] lint | <N> issues found, <M> fixed`

## Starting a new wiki

```bash
python3 scripts/scaffold.py <wiki-root> "<Topic Title>"
```

Creates the full directory tree, blank `CLAUDE.md`, blank `log.md`, and blank `wiki/index.md`.

After scaffolding:
1. Fill in `CLAUDE.md` — define scope, naming conventions, initial research questions
2. Start ingesting sources (add to `raw/`, run ingest)
3. Ask questions to build up `outputs/queries/`, promote good answers to `wiki/concepts/`

## wiki/index.md format

The LLM updates `index.md` on every ingest. Format:

```markdown
# Index

## Concepts
- [[LLM Wiki]] — Karpathy-style self-compiling knowledge base pattern
- [[RAG]] — Retrieval-Augmented Generation, comparison with wiki approach

## Entities
- [[Andrej Karpathy]] — AI researcher, OpenAI co-founder, author of llm-wiki pattern

## Summaries
- [[summaries/llm-wiki-gist]] — Karpathy's original Gist (2026-04-03)
```

`index.md` + LLM context window replaces a vector database at <100 sources.

## log.md format

```markdown
## [2026-04-05] ingest | karpathy-llm-wiki-gist — Karpathy's original idea file
## [2026-04-05] compile | LLM Wiki (480 words, 1 source)
## [2026-04-05] query | rag-vs-llm-wiki-tradeoffs
## [2026-04-05] promote | RAG vs LLM Wiki (from query)
## [2026-04-05] lint | 2 orphan pages found, 2 fixed
```

Quick grep: `grep "^## \[" log.md | tail -10`

## CLAUDE.md minimal template

See `references/schema-guide.md` for full guidance. At minimum:

```markdown
# <Topic> Knowledge Base

## Scope
<What this wiki covers. What it deliberately excludes.>

## Naming conventions
- Concept pages: Title Case in wiki/concepts/
- Entity pages: Proper Name in wiki/entities/
- Summary pages: source-slug in wiki/summaries/

## Current articles
<List of existing wiki pages — update after every compile>

## Open research questions
<What you want to understand better — drives future ingest/query work>
```

## Tooling

| Tool | Purpose |
|------|---------|
| [Obsidian](https://obsidian.md) | IDE for browsing the wiki; graph view shows connections |
| [Obsidian Web Clipper](https://obsidian.md/clipper) | Browser extension → converts web pages to Markdown for `raw/` |
| [qmd](https://github.com/tobi/qmd) | Local semantic search over wiki pages (optional, useful at >100 pages) |
| `scripts/scaffold.py` | Bootstrap new wiki directory tree |
| `scripts/lint_wiki.py` | Find dead links, orphan pages, coverage gaps |

## Use cases

- **Research deep-dive** — reading papers/articles on a topic over weeks; wiki evolves with your understanding
- **Personal wiki** — Farzapedia-style: journal entries, notes, ideas compiled into personal encyclopedia
- **Team knowledge base** — fed by Slack threads, meeting notes, docs; LLM does maintenance no one wants to do
- **Reading companion** — filing each book chapter as you go; builds a rich companion wiki by the end

## References

- `references/schema-guide.md` — What to put in CLAUDE.md
- `references/article-guide.md` — How to write good wiki articles (length, wikilink density, format)
- `references/tooling-tips.md` — Obsidian setup, Web Clipper, qmd, Marp slides, Dataview
