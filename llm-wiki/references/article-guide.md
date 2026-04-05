# Wiki Article Writing Guide

Guidelines for writing high-quality wiki articles. Read before compiling a new concept or entity page.

## Length targets

| Page type | Target length | Notes |
|-----------|--------------|-------|
| Concept page | 400–1200 words | Dense, no padding |
| Entity page | 200–500 words | Factual, link-heavy |
| Summary page | 150–400 words | Takeaways, not a rewrite |

Avoid padding. A 400-word article that's dense beats an 800-word article with filler.

## Concept page structure

```markdown
---
title: <Title>
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [slug1, slug2]
tags: [tag1, tag2]
---

# <Title>

<One-sentence definition or core idea.>

## What it is

<Explain the concept clearly. Assume the reader is technically literate but unfamiliar with this specific topic.>

## How it works

<Mechanism, process, or structure. Use numbered steps if sequential.>

## Key properties / tradeoffs

<Bullet list or short paragraphs covering important characteristics.>

## Relationship to other concepts

<Wikilinks to related concepts with a brief note on the relationship.>
- [[Related Concept A]] — how they relate
- [[Related Concept B]] — contrast or connection

## Open questions

<What this wiki doesn't yet know about this concept. Drives future ingest.>

## Sources

- [[summaries/source-slug-1]] — (date) one-line description
- [[summaries/source-slug-2]] — (date) one-line description
```

## Entity page structure

```markdown
---
title: <Name>
type: entity
entity_type: person | tool | paper | organization
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [slug1]
tags: [tag1]
---

# <Name>

<One-sentence description.>

## Key contributions / features

<What this entity is known for in the context of this wiki's topic.>

## Related concepts

- [[Concept A]] — connection

## Sources

- [[summaries/source-slug]]
```

## Wikilink rules

1. **Link first mention of every entity or concept** — don't wait for "a natural place"
2. **Link maximum twice per article** — don't over-link the same page
3. **Link concepts that exist** — check `wiki/index.md` before creating a new link target
4. **Backlink audit** — after writing a new article, grep existing articles for the new page's title and add incoming links:
   ```bash
   grep -rln "<new article title>" wiki/concepts/ wiki/entities/
   ```

## Handling contradictions between sources

When two sources contradict each other:

1. State both claims explicitly
2. Note which source supports each claim
3. Add to the "Open questions" section
4. Do NOT silently pick one — contradictions are valuable signal

Example:
> Source A (2024) claims X. Source B (2026) claims Y, which contradicts A. It's unclear whether this reflects a methodological difference or an error in one source. See [[summaries/source-a]] and [[summaries/source-b]].

## Summary page structure

Summaries are concise representations of a single source. They are not rewrites.

```markdown
---
title: summaries/<slug>
type: summary
source_url: https://...
source_type: article | paper | gist | video | podcast
date: YYYY-MM-DD
ingested: YYYY-MM-DD
tags: [tag1]
---

# <Source Title>

**Source**: [<Author/Org>](<URL>) · <date>

## Key takeaways

- <Most important insight 1>
- <Most important insight 2>
- <Most important insight 3>

## Core claims

<2-4 sentences on the main argument or findings.>

## Notable quotes

> "<exact quote>" — <attribution>

## Concepts introduced / referenced

- [[Concept A]]
- [[Entity B]]
```
