<div align="center">

# Any Auto Register

Account automation & management for 11+ platforms / Protocol & browser dual-mode / One-click Mac & Windows desktop app

<p>
<a href="https://github.com/aroldobossoni/any-auto-register-global/stargazers"><img src="https://img.shields.io/github/stars/aroldobossoni/any-auto-register-global?style=flat-square&logo=github&color=FFB003" alt="Stars" /></a>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases/latest"><img src="https://img.shields.io/github/v/release/aroldobossoni/any-auto-register-global?style=flat-square&logo=github&color=22c55e" alt="Release" /></a>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases"><img src="https://img.shields.io/github/downloads/aroldobossoni/any-auto-register-global/total?style=flat-square&logo=github&color=8b5cf6" alt="Downloads" /></a>
<a href="LICENSE"><img src="https://img.shields.io/github/license/aroldobossoni/any-auto-register-global?style=flat-square&color=f97316" alt="License" /></a>
</p>

<p>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases/latest"><b>Download Desktop</b></a>
&nbsp;·&nbsp;
<a href="#what-it-solves">What It Solves</a>
&nbsp;·&nbsp;
<a href="#at-a-glance">At a Glance</a>
&nbsp;·&nbsp;
<a href="#community">Community</a>
&nbsp;·&nbsp;
<a href="README_zh-CN.md">中文</a>
&nbsp;·&nbsp;
<a href="README_pt-BR.md">Português</a>
&nbsp;·&nbsp;
<a href="README_vi.md">Tiếng Việt</a>
</p>

<img src="assets/screenshots/概览.png" alt="Any Auto Register Dashboard" width="92%" />

</div>

---

> **Note:** This repository is an independent global edition of `aroldobossoni/any-auto-register-global`, fully adapted and localized.

> This project is for learning and research purposes only. Do not use it for commercial violations. Users must evaluate and comply with target platforms' terms of service.

## What It Solves

Most similar tools only solve "how to register a specific platform", leaving massive engineering gaps: how to manage emails, how to pass captchas, how to rotate proxies, how to keep using accounts after registration, what to do when tokens expire, and how to debug errors. Any Auto Register solves all of these.

| Feature | Other Tools | Any Auto Register |
| :--- | :--- | :--- |
| **Execution Mode** | CLI / Docker / .py scripts | **Mac & Windows Desktop app** (built-in React GUI, one-click start) |
| **Platform Coverage** | Single platform (1-3) | **11+ platforms** with Universal Adapter; plugin-based new platform onboarding |
| **Mailbox Solutions** | Mostly rely on IMAP | **9 built-in channels**: MoeMail / Cloudflare / TempMail / DDG Email / etc. |
| **Execution Modes** | Browser only | **Protocol (pure/fast) / Headless / Headed** |
| **Full Lifecycle** | Register and forget | Scheduled validity checks, Token auto-renewal, Trial monitoring, Risk alerts |
| **Data & Analytics** | None | Registration success rate dashboard, Error attribution (proxy risk, mailbox error, 2FA) |
| **API Gateway Integration** | Manual setup | Seamless integration with [Any2API](https://github.com/lxf746/any2api) for OpenAI-compatible gateway |
| **Extensibility** | Hardcoded | **Fully modular**: Platforms, Mailboxes, Captchas, Solvers are all hot-swappable |

Combined with the [Any2API](https://github.com/lxf746/any2api) gateway, you can achieve one-click automated batch registration and immediately use accounts as OpenAI / Claude APIs.

## Core Features & Modules

- **Platforms**: ChatGPT / Cursor / Kiro / Trae.ai / Tavily / Grok / Blink / Cerebras / OpenBlockLabs / Windsurf, plus Universal Adapter
- **Mailboxes**: MoeMail / Cloudflare Worker / Laoudo / DuckMail / Testmail / Freemail / TempMail.lol / Temp-Mail Web / DuckDuckGo Email
- **Captchas**: YesCaptcha / 2Captcha / Local Solver (Camoufox)
- **SMS / Phone Verification**: SMS-Activate / HeroSMS
- **Execution Modes**: Protocol (fastest, no browser) / Headless / Headed
- **Built-in 2FA**: TOTP calculation without third-party apps
- **Operations & Lifecycle**: Scheduled validity check, Token auto-renewal, Risk alerts

## At a Glance

### Dashboard Overview
<img src="assets/screenshots/概览.png" alt="Overview" width="90%" />

### Account Management
<img src="assets/screenshots/账号管理.png" alt="Account Management" width="90%" />

## Community

Join our community to discuss and share automation workflows.
