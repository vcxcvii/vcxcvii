# Varun Choraria

Senior Manager, Marketing at [GTM Buddy](https://gtmbuddy.ai).  
B2B SaaS marketing, go-to-market strategy, management, and whatever else is worth writing down.

[varunchoraria.com](https://www.varunchoraria.com) · [LinkedIn](https://www.linkedin.com/in/varunchoraria/) · [Book 30 min](https://cal.com/varun-choraria/30min)

## Latest notes

<!-- notes starts -->
- [I now have my own Master Shifu](https://www.varunchoraria.com/i-now-have-my-own-master-shifu/) · 2026-07-02
- [Maybe going around CIRCLES is worth it](https://www.varunchoraria.com/maybe-going-around-circles-is-worth-it/) · 2026-06-26
- [Too much parenting, too little adulting](https://www.varunchoraria.com/too-much-parenting-too-little-adulting/) · 2026-06-20
- [Killed By Google](https://www.varunchoraria.com/killed-by-google/) · 2026-06-16
- [Who owns what?](https://www.varunchoraria.com/who-owns-what/) · 2026-05-17
<!-- notes ends -->

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

Every line of code on [varunchoraria.com](https://www.varunchoraria.com) is written by Claude Code. The AI handles the full pipeline — coding, shipping, and quality checks — with a [pre-push gate](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/scripts/qa) that blocks SEO failures, missing metadata, and design drift.

The site speaks MCP. Point any [MCP-compatible client](https://modelcontextprotocol.io) at it and your AI can read every post live:

```
claude mcp add --transport http varunchoraria https://varunchoraria-mcp.vercel.app
```

A machine-readable [`DESIGN.md`](https://github.com/vcxcvii/vcxcvii.github.io/blob/main/DESIGN.md) keeps the AI consistent — colors, type scale, spacing, all codified so the agent doesn't guess.

---

*Latest notes refresh automatically from the RSS feed. Inspired by [Simon Willison](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/).*
