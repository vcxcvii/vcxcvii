# Varun Choraria

Group Manager, Product Marketing at [HCL Tech](https://www.hcltech.com/). B2B SaaS product marketer with 8+ years across [Vymo](https://vymo.com), [Freshworks](https://www.freshworks.com) and [GTM Buddy](https://gtmbuddy.ai). On the side, I write, ship open-source AI tools, and experiment at [Grow and Close](https://growandclose.com).  
Go-to-market strategy, product marketing, management, and whatever else is worth writing down.

Views here are my own and do not represent my employer.

[varunchoraria.com](https://www.varunchoraria.com) · [LinkedIn](https://www.linkedin.com/in/varunchoraria/)

## Latest notes

<!-- notes starts -->
- [Day 91](https://www.varunchoraria.com/day-91/) · 2026-08-16
- [My agent found 9.09%. I found one session.](https://www.varunchoraria.com/11-sessions-are-not-a-ux-audit/) · 2026-08-03
- [The models were fine. I was the bug.](https://www.varunchoraria.com/the-models-were-fine-i-was-the-bug/) · 2026-08-02
- [Who do we sell to vs. Who SHOULD we sell to (and how).](https://www.varunchoraria.com/who-do-we-sell-to-vs-who-should-we-sell-to-and-how/) · 2026-08-01
- [The Claude bill said $1,492. I paid $20. Here’s how.](https://www.varunchoraria.com/how-to-get-1492-out-of-a-20-claude-subscription/) · 2026-07-30
<!-- notes ends -->

## Free tools I've open sourced

| Repo | What it does |
|---|---|
| [interview-recon](https://github.com/vcxcvii/interview-recon) | Turns your AI coding agent into an interview research analyst. Company dossiers, JD-mapped talking points, a 90-day plan. Works without paid scraping APIs. |
| [master-shifu](https://github.com/vcxcvii/master-shifu) | 32 consulting frameworks from 19 MBA casebooks, each one an agent `/command`. |
| [michealangelo](https://github.com/vcxcvii/michealangelo) | Self-improving design-system skills so AI agents stop shipping generic UI. |
| [rainmaker](https://github.com/vcxcvii/rainmaker) | An SEO and AEO agent that ranks findings by distance to revenue and records whether each fix worked. |
| [pipeline-skills](https://github.com/vcxcvii/pipeline-skills) | Free GTM skills for AI agents: positioning, landing pages, outbound, AI-search visibility and measurement. |
| [varunchoraria-mcp](https://github.com/vcxcvii/varunchoraria-mcp) | An MCP server that lets any AI agent read varunchoraria.com live. |

## Quick links

| Page | What's there |
|---|---|
| [/about](https://www.varunchoraria.com/about/) | Who I am |
| [/work](https://www.varunchoraria.com/work/) | Roles and outcomes, newest first |
| [/blog](https://www.varunchoraria.com/blog/) | Things I write |
| [/side-quests](https://www.varunchoraria.com/side-quests/) | Projects built with AI |
| [/speaking](https://www.varunchoraria.com/speaking/) | Talks, the book and the podcast |
| [/days](https://www.varunchoraria.com/days/) | A day counter and weekly log of what shipped |
| [/uses-this](https://www.varunchoraria.com/uses-this/) | Tools I use |
| [/changelog](https://www.varunchoraria.com/changelog/) | What changed and why |

## How this site is built

Every line of code on [varunchoraria.com](https://www.varunchoraria.com) is written by Claude Code. The AI handles the full pipeline: coding, shipping, and quality checks, with a [pre-push gate](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/_scripts/qa.rb) that blocks SEO failures, missing metadata, and design drift.

The site speaks MCP. Point any [MCP-compatible client](https://modelcontextprotocol.io) at it and your AI can read every post live:

```
claude mcp add --transport http varunchoraria https://varunchoraria-mcpvercelapp.vercel.app
```

A machine-readable [`DESIGN.md`](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/DESIGN.md) keeps the AI consistent — colors, type scale, spacing, all codified so the agent doesn't guess.

---

*Latest notes refresh automatically from the RSS feed. Inspired by [Simon Willison](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/).*
