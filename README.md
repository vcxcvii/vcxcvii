# Varun Choraria

Senior Manager, Marketing at [GTM Buddy](https://gtmbuddy.ai). I write about B2B marketing, go-to-market strategy, management, and whatever else is worth saying.

Everything lives at [varunchoraria.com](https://www.varunchoraria.com) — a Jekyll site built, maintained, and QA-checked almost entirely by AI.

## On the site

| | |
|---|---|
| [/about](https://www.varunchoraria.com/about/) | Who I am |
| [/work](https://www.varunchoraria.com/work/) | What I do |
| [/notes](https://www.varunchoraria.com/blog/) | Things I write |
| [/fun](https://www.varunchoraria.com/fun/) | A book, some talks, a podcast |
| [/side-quests](https://www.varunchoraria.com/side-quests/) | Projects built with AI |
| [/uses-this](https://www.varunchoraria.com/uses-this/) | Tools I use |
| [/changelog](https://www.varunchoraria.com/changelog/) | What changed and why |

## How AI runs this site

The site is managed by Claude Code — it writes code, ships features, and checks quality before anything goes live. A few things worth knowing:

**Pre-push QA gate** — every push runs an automated check on changed files. It blocks commits that fail SEO (missing title/description), AEO (missing structure for AI readability), design compliance, or accidentally include data files.

**MCP server** — the site exposes a live [Model Context Protocol](https://varunchoraria.com/mcp/) server. Any MCP-compatible AI client (Claude Code, Cursor, Codex CLI) can connect and read all posts and pages directly — not from training data, from the live site. Add it with:

```
claude mcp add --transport http varunchoraria https://varunchoraria-mcpvercelapp.vercel.app
```

**Machine-readable design system** — [`DESIGN.md`](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/DESIGN.md) codifies every visual decision so the AI knows the design language without being told twice.

## Latest

<!-- notes starts -->
- [Maybe going around CIRCLES is worth it](https://www.varunchoraria.com/maybe-going-around-circles-is-worth-it/) · 2026-06-26
- [Too much parenting, too little adulting](https://www.varunchoraria.com/too-much-parenting-too-little-adulting/) · 2026-06-20
- [Killed By Google](https://www.varunchoraria.com/killed-by-google/) · 2026-06-16
- [Who owns what?](https://www.varunchoraria.com/who-owns-what/) · 2026-05-17
- [Team values I value](https://www.varunchoraria.com/team-values-i-value/) · 2026-04-25
<!-- notes ends -->

## Connect

[Book 30 minutes](https://cal.com/varun-choraria/30min) · [LinkedIn](https://www.linkedin.com/in/varunchoraria/) · [MCP server](https://varunchoraria.com/mcp/)

---

*Latest posts auto-update from the site's RSS feed. Inspired by [Simon Willison](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/).*
