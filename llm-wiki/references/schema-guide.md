# CLAUDE.md Schema Guide

`CLAUDE.md` (also symlinked or aliased as `AGENTS.md`) is the **schema document** for a wiki topic. It tells the LLM agent the scope, conventions, and current state of the knowledge base — every session should start by reading it.

## Why it matters

Without a schema, the LLM creates inconsistent page names, overlapping articles, and drifts from the wiki's intended scope. With a well-maintained schema, the LLM becomes a disciplined, consistent wiki maintainer.

**Co-evolve it with the wiki** — update after every major compile or structural change.

## Full template

```markdown
# <Topic Title> Knowledge Base

## Scope
What this wiki covers:
- <bullet list of included areas>

What this wiki deliberately excludes:
- <bullet list of out-of-scope areas>

## Naming conventions

### Pages
- **Concept pages** (`wiki/concepts/`): Title Case noun phrases. E.g., "Market Making Strategy", not "market making" or "MarketMakingStrategy"
- **Entity pages** (`wiki/entities/`): Proper names. E.g., "Andrej Karpathy", "Obsidian", "Avellaneda-Stoikov Model"
- **Summary pages** (`wiki/summaries/`): kebab-case source slug. E.g., "karpathy-llm-wiki-gist", "avellaneda-stoikov-2008"

### Wikilinks
- Always use `[[Page Title]]` — the exact page title, case-sensitive
- For entities referenced in concept pages, always wikilink first mention
- Do NOT wikilink the same page more than twice per article

### Frontmatter
Every wiki page must have:
```yaml
---
title: <Page Title>
type: concept | entity | summary
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of raw/ slugs this page draws from]
tags: [relevant tags]
---
```

## Current articles

### Concepts
- [[<Concept Title>]] — one-line summary

### Entities
- [[<Entity Name>]] — one-line summary

### Summaries
- [[summaries/<slug>]] — source title (date)

## Open research questions

- <Questions that should drive future ingest/query work>
- <Things the wiki currently doesn't cover well>
- <Contradictions or gaps noticed between articles>

## Research gaps

Sources to ingest:
- [ ] <URL or paper title> — why it's relevant

## Notes for the LLM

<Any special instructions: tone, depth level, how to handle contradictions, etc.>
```

## What makes a good schema

**Good scope definition** prevents sprawl. A wiki about "LLM memory techniques" should exclude "LLM training" even though they're related.

**Explicit naming conventions** keep wikilinks from breaking. If you decide concept pages use Title Case, enforce it — a broken wikilink is an orphan.

**Maintained article list** lets the LLM know what already exists before creating a new page. The most common error is creating duplicate articles with slightly different names.

**Open research questions** give the LLM direction. Without them, the LLM defaults to ingesting the most obvious sources and missing your actual questions.

## Update cadence

- After every new concept page: add to "Current articles"
- After every ingest batch: update "Sources to ingest" checklist
- After every lint pass: update "Research gaps"
- Monthly: review scope, prune stale research questions
