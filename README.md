# Varun Choraria

B2B SaaS marketing operator and consultant. About a decade across Freshworks, Vymo, and [GTM Buddy](https://gtmbuddy.ai) (Jan-Aug 2026), now building [Grow & Close](https://growandclose.com).  
Go-to-market strategy, product marketing, management, and whatever else is worth writing down.

**Open to full-time roles and consulting engagements.**

[varunchoraria.com](https://www.varunchoraria.com) · [LinkedIn](https://www.linkedin.com/in/varunchoraria/) · [Book 30 min](https://cal.com/varun-choraria/30min)

## Latest notes

<!-- notes starts -->
- [Hunting Season for the Rest of Us](https://www.varunchoraria.com/hunting-season-for-the-rest-of-us/) · 2026-07-24
- [Github-ing](https://www.varunchoraria.com/github-ing/) · 2026-07-16
- [How to design without AI Slop](https://www.varunchoraria.com/how-to-design-without-ai-slop/) · 2026-07-08
- [I now have my own Master Shifu](https://www.varunchoraria.com/i-now-have-my-own-master-shifu/) · 2026-07-02
- [Maybe going around CIRCLES is worth it](https://www.varunchoraria.com/maybe-going-around-circles-is-worth-it/) · 2026-06-26
<!-- notes ends -->

## Free tools I've open sourced

| Repo | What it does |
|---|---|
| [interview-recon](https://github.com/vcxcvii/interview-recon) | Turns your AI coding agent into an interview research analyst. Company dossiers, JD-mapped talking points, a 90-day plan. Works without paid scraping APIs. |
| [master-shifu](https://github.com/vcxcvii/master-shifu) | 32 consulting frameworks from 19 MBA casebooks, each one an agent `/command`. |
| [michealangelo](https://github.com/vcxcvii/michealangelo) | Self-improving design-system skills so AI agents stop shipping generic UI. |

## Quick links

| Page | What's there |
|---|---|
| [/about](https://www.varunchoraria.com/about/) | Who I am |
| [/work](https://www.varunchoraria.com/work/) | What I do |
| [/blog](https://www.varunchoraria.com/blog/) | Things I write |
| [/side-quests](https://www.varunchoraria.com/side-quests/) | Projects built with AI |
| [/uses-this](https://www.varunchoraria.com/uses-this/) | Tools I use |
| [/changelog](https://www.varunchoraria.com/changelog/) | What changed and why |

## How this site is built

Every line of code on [varunchoraria.com](https://www.varunchoraria.com) is written by Claude Code. The AI handles the full pipeline: coding, shipping, and quality checks, with a [pre-push gate](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/_scripts/qa.rb) that blocks SEO failures, missing metadata, and design drift.

The site speaks MCP. Point any [MCP-compatible client](https://modelcontextprotocol.io) at it and your AI can read every post live:

```
claude mcp add --transport http varunchoraria https://varunchoraria-mcp.vercel.app
```

A machine-readable [`DESIGN.md`](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/DESIGN.md) keeps the AI consistent — colors, type scale, spacing, all codified so the agent doesn't guess.

---

*Latest notes refresh automatically from the RSS feed. Inspired by [Simon Willison](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/).*
