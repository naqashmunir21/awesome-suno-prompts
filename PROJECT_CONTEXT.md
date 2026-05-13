# Project Context — Awesome Suno Prompts

> Internal reference document for maintainers and contributors. Describes what this project is, what it owns, and how to take it forward.

---

## What This Repository Is

**Awesome Suno Prompts** is an open-source, community-curated collection of 1,000+ professional Suno AI style prompts, organized by genre and production style. It is maintained by the **Song AI Farm** team and serves as both a standalone resource and a discovery funnel for Song AI Farm's free and premium tools.

- **GitHub:** https://github.com/naqashmunir21/awesome-suno-prompts
- **License:** CC0 1.0 (Public Domain)
- **Target audience:** Music creators using Suno AI (V4.5 / V5) and Udio

---

## The Ecosystem — What Song AI Farm Owns

This repo is one piece of a larger product ecosystem:

### Free Tools
| Tool | URL | Purpose |
|------|-----|---------|
| **Melody to Lyrics** | https://www.songaifarm.com/melody-to-lyrics | Upload any melody/hum → AI writes Suno-ready lyrics matching every beat, phrase & syllable. 30+ languages, custom genre & mood. |
| **Song DNA Analyzer** | https://www.songaifarm.com/song-analyzer | Upload audio → extract lyrics, structure, theme, instrumentation. Auto-populates the song generator. |
| **Lyrics Generator** | https://www.songaifarm.com/lyrics-generator | Professional lyrics in any language, genre, mood. Free forever. Suno AI & Udio ready. |
| **Prompt Generator** | https://www.songaifarm.com | Auto-generates optimized Suno AI style prompts in 30 seconds. |

### Premium Product
| Product | URL | Description |
|---------|-----|-------------|
| **350+ SUNO AI PROMPTS PACK** | https://naqashkhan.gumroad.com/l/sbrxwh | Gumroad PDF — battle-tested prompts curated across all major genres, production styles, and moods. Copy-paste ready. |

### Marketplace — Affiliate Products
The `README.md` includes a **Marketplace** section featuring curated third-party premium products linked with our affiliate parameter (`?a=330071315`). Affiliate sales generate revenue for this project.

| ID | Title | Author | Affiliate Link |
|----|-------|--------|----------------|
| PR001 | FULL DISCOGRAPHY | Isaac Haines | https://isaachaines.gumroad.com/l/vxmswi?a=330071315 |

> To add a new product: add a row to this table and add a corresponding card to the `## 🛒 Marketplace` section in `README.md` following the existing card format.

### Community
- **Discord:** https://discord.gg/d7RKGpTbwV
- **Twitter:** https://twitter.com/songaifarm

---

## Repository Structure

```
README.md                  — Main landing page (1000+ prompts, tools, resources)
CONTRIBUTING.md            — How to submit prompts (format, quality bar, PR process)
PROMOTION_TEMPLATES.md     — Copy-paste marketing templates for Reddit, Twitter, Discord
PROJECT_CONTEXT.md         — This file: project overview & forward direction
LICENSE                    — CC0 1.0 (Public Domain)

prompts/
  pop.md                   — 200+ Pop prompts
  rock.md                  — 150+ Rock prompts
  hip-hop.md               — 120+ Hip-Hop/Rap prompts
  country.md               — 100+ Country prompts
  edm.md                   — 130+ EDM/Electronic prompts
  rnb-soul.md              — 80+ R&B/Soul prompts
  indie.md                 — 90+ Indie/Alternative prompts
  jazz-blues.md            — 60+ Jazz/Blues prompts

examples/
  advanced-techniques.md   — Layering, arrow technique, genre fusion, vocal effects
  before-after.md          — Optimization case studies
  common-mistakes.md       — Before/after bad vs good prompts
  viral-hits.md            — Case studies of prompts that produced viral results

discussions/
  welcome.md               — Pinned welcome post for GitHub Discussions
  community-guidelines.md  — Rules and moderation notes
  prompt-requests.md       — Template for requesting new prompts
  show-and-tell.md         — Guidelines for sharing audio results
```

---

## Prompt Format Standard

Every prompt entry must follow this format:

```markdown
#### [Descriptive Prompt Name]
```
[Prompt text — specific instrumentation, vocals, production details, BPM, key]
```
**Use Case:** [When/why to use this]
**Suno Version:** [V4.5, V5, or Both]
**Energy:** [1-10 scale]
```

Rules:
- Under 950 characters (Suno truncates longer prompts)
- Tested on Suno V4.5 or V5 before submission
- Specific instrumentation — never vague ("guitar" → "fingerpicked clean acoustic")
- Include BPM and Key where possible
- Each genre section links to `[🎨 Auto-generate similar →](https://www.songaifarm.com?genre=X&mood=Y)`

---

## How to Take This Forward

### Content priorities
1. **Fill out stub files** — `examples/advanced-techniques.md`, `examples/before-after.md`, and `examples/viral-hits.md` are placeholders; expand with real case studies and community-contributed examples.
2. **Add new genres** — World music, classical, K-Pop, Afrobeats, Latin are underrepresented; create new prompt files as community demand grows.
3. **Suno V5 updates** — Audit existing prompts for V5 compatibility as the platform evolves and flag outdated V4.5-only prompts.
4. **Showcase generated songs** — Add `**Example Song:**` links to as many prompts as possible; real audio results convert better than text.

### Growth / SEO
- Each genre file should have a clear H1 and introductory paragraph (helps GitHub search & Google)
- `README.md` genre sections use direct links to `songaifarm.com` with `?genre=` params — maintain these to track traffic
- Promote the **350+ Prompts Pack** (Gumroad) in every outreach post and in the README (already done)

### Tools integration
- Every prompt section references the relevant Song AI Farm tool (Melody to Lyrics, Song DNA Analyzer, Lyrics Generator)
- The Gumroad pack should be mentioned at natural conversion points: Quick Start, Best Practices, footer
- Keep all tool URLs current; if a tool URL changes, update README, PROMOTION_TEMPLATES, discussions/welcome.md, and this file simultaneously

### Community
- Pin `discussions/welcome.md` as the first GitHub Discussions post
- Use `discussions/prompt-requests.md` and `discussions/show-and-tell.md` as pinned discussion starters
- Respond to PRs within 48 hours using templates in `PROMOTION_TEMPLATES.md`
- Cross-post to r/SunoAI, r/musicproduction, and Song AI Farm Discord when adding large batches of prompts

---

## Key URLs (quick reference)

| Resource | URL |
|----------|-----|
| Repo | https://github.com/naqashmunir21/awesome-suno-prompts |
| Song AI Farm | https://www.songaifarm.com |
| Melody to Lyrics | https://www.songaifarm.com/melody-to-lyrics |
| Song DNA Analyzer | https://www.songaifarm.com/song-analyzer |
| Lyrics Generator | https://www.songaifarm.com/lyrics-generator |
| 350+ Prompts Pack | https://naqashkhan.gumroad.com/l/sbrxwh |
| Discord | https://discord.gg/d7RKGpTbwV |
| Twitter | https://twitter.com/songaifarm |
| Suno AI | https://suno.com |
| Udio | https://udio.com |

---

*Last updated: April 2026*
