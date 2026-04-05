# Tooling Tips

Practical setup and usage notes for the LLM Wiki stack.

## Obsidian setup

### Essential settings

1. **Attachment folder**: Settings → Files and links → "Attachment folder path" → set to `raw/assets/`
2. **Download images**: Settings → Hotkeys → search "Download attachments" → bind to Ctrl+Shift+D  
   After clipping an article, hit the hotkey to download all images locally.
3. **New file location**: Settings → Files and links → "Default location for new notes" → set to `wiki/concepts/`

### Plugins to install

- **Obsidian Web Clipper** (browser extension) — converts any webpage to Markdown and saves to your vault
- **Dataview** — query frontmatter fields; build dynamic tables of articles by tag, date, or source count
- **Marp** — render wiki content as slide decks directly from Obsidian

### Graph view

Graph view (Ctrl+G) is the best way to understand your wiki's shape:
- Dense hub = a well-connected concept page
- Isolated node = orphan page (needs inbound links or removal)
- Cluster = a sub-topic worth a dedicated section in `CLAUDE.md`

## Obsidian Web Clipper usage

1. Install from [obsidian.md/clipper](https://obsidian.md/clipper)
2. Configure template to save to `raw/articles/`
3. Clip an article → hit download-images hotkey → file is ready for ingest

For complex pages (paywalled, dynamic): copy-paste the main text manually, save as `raw/articles/<slug>.md`.

## qmd (optional, for large wikis)

[qmd](https://github.com/tobi/qmd) is a local semantic search engine for Markdown files with BM25 + vector hybrid search. Useful when the wiki grows beyond ~100 pages and `index.md` scanning becomes slow.

```bash
# Install
pip install qmd

# Index your wiki
qmd collection add wiki/ --name my-wiki
qmd embed

# Query
qmd query "what are the tradeoffs of RAG vs wiki" --collection my-wiki

# Re-index after adding pages
qmd collection remove my-wiki && qmd collection add wiki/ --name my-wiki && qmd embed
```

qmd also has an MCP server so LLMs can use it as a native tool instead of CLI.

## Marp — generating slide decks from wiki content

Marp renders Markdown as presentation slides. Useful for turning wiki content into shareable presentations.

```markdown
---
marp: true
theme: default
---

# Slide title

Content here

---

# Next slide
```

Install the Marp plugin in Obsidian to preview/export directly.

## Generating charts with matplotlib

For quantitative analyses, ask the LLM to generate a matplotlib script and save to `outputs/`:

```python
# Save to outputs/charts/my-analysis.py
import matplotlib.pyplot as plt
# ... chart code ...
plt.savefig('outputs/charts/my-analysis.png')
```

The chart can then be embedded in a wiki article: `![[my-analysis.png]]`

## Git workflow

The wiki is a git repo. Benefits:
- Version history for every article
- Branching for experimental research directions
- Collaboration: pull requests for article additions/changes

```bash
# After each work session
git add .
git commit -m "ingest: added 3 papers on attention mechanisms"
git push

# View history of a specific article
git log --oneline wiki/concepts/RAG.md
```

Keep large files (PDFs, raw images) in `.gitignore`. Only commit Markdown files and scripts.

## Interactive HTML outputs

For complex analyses, the LLM can generate interactive HTML with JavaScript:

```
"Generate an interactive comparison table of RAG vs LLM Wiki tradeoffs as HTML with sortable columns"
```

Save to `outputs/` and open in browser. These can also be embedded in Obsidian with the HTML plugin.
