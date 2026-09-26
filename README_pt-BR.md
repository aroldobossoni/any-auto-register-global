<div align="center">

# Any Auto Register

Automação e gerenciamento de contas para 11+ plataformas / Modo dual de protocolo e navegador / Aplicativo desktop Mac e Windows com um clique

<p>
<a href="https://github.com/aroldobossoni/any-auto-register-global/stargazers"><img src="https://img.shields.io/github/stars/aroldobossoni/any-auto-register-global?style=flat-square&logo=github&color=FFB003" alt="Estrelas" /></a>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases/latest"><img src="https://img.shields.io/github/v/release/aroldobossoni/any-auto-register-global?style=flat-square&logo=github&color=22c55e" alt="Versão" /></a>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases"><img src="https://img.shields.io/github/downloads/aroldobossoni/any-auto-register-global/total?style=flat-square&logo=github&color=8b5cf6" alt="Baixagens" /></a>
<a href="LICENSE"><img src="https://img.shields.io/github/license/aroldobossoni/any-auto-register-global?style=flat-square&color=f97316" alt="Licença" /></a>
</p>

<p>
<a href="https://github.com/aroldobossoni/any-auto-register-global/releases/latest"><b>Baixar Aplicativo Desktop</b></a>
&nbsp;·&nbsp;
<a href="#o-que-ele-resolve">O Que Resolve</a>
&nbsp;·&nbsp;
<a href="#visao-geral">Visão Geral</a>
&nbsp;·&nbsp;
<a href="#comunidade">Comunidade</a>
&nbsp;·&nbsp;
<a href="README.md">English</a>
&nbsp;·&nbsp;
<a href="README_zh-CN.md">中文</a>
&nbsp;·&nbsp;
<a href="README_vi.md">Tiếng Việt</a>
</p>

<img src="assets/screenshots/概览.png" alt="Painel do Any Auto Register" width="92%" />

</div>

---

> **Nota:** Este repositório é uma edição global independente baseada no repositório original `lxf746/any-auto-register`, totalmente adaptada e localizada.

> Este projeto é apenas para fins educacionais e de pesquisa. Não use para fins comerciais ilegais. Os usuários devem avaliar e cumprir os termos de serviço das plataformas de destino.

## O Que Resolve

A maioria das ferramentas similares só resolve "como registrar uma única plataforma", deixando grandes lacunas de engenharia: como gerenciar e-mails, como passar CAPTCHAs, como rotacionar proxies, como continuar usando contas após o registro, o que fazer quando tokens expiram, e como diagnosticar erros. O Any Auto Register resolve todos esses problemas.

| Recurso | Outras Ferramentas | Any Auto Register |
| :--- | :--- | :--- |
| **Modo de Execução** | CLI / Docker / Scripts .py | **Aplicativo Desktop Mac & Windows** (GUI React integrada, início com 1 clique)
| **Cobertura de Plataformas** | Plataforma única (1-3) | **11+ plataformas** com Adaptador Universal; novos plugins dinâmicos
| **Soluções de E-mail** | Dependem de IMAP | **9 canais integrados**: MoeMail / Cloudflare / TempMail / DDG Email / etc.
| **Modos de Execução** | Apenas navegador | **Protocolo (puro/rápido) / Headless / Headed**
| **Ciclo de Vida** | Registrar e esquecer | Verificações agendadas, renovação automática de tokens, alertas de risco
| **Análise de Dados** | Nenhum | Painel de taxa de sucesso, atribuição de erros (proxy, e-mail, 2FA)
| **Integração com Gateway** | Manual | Integração direta com [Any2API](https://github.com/lxf746/any2api) para gateway compatível com OpenAI
| **Extensibilidade** | Hardcoded | **Totalmente modular**: Plataformas, E-mails, CAPTCHAs e Solvers intercambiáveis

Combinado com o gateway [Any2API](https://github.com/lxf746/any2api), você pode automatizar registros em lote e usar contas imediatamente como APIs OpenAI / Claude.

## Plataformas Suportadas

- **Plataformas**: ChatGPT / Cursor / Kiro / Trae.ai / Tavily / Grok / Blink / Cerebras / OpenBlockLabs / Windsurf + Adaptador Universal
- **E-mails**: MoeMail / Cloudflare Worker / Laoudo / DuckMail / Testmail / Freemail / TempMail.lol / Temp-Mail Web / DuckDuckGo Email
- **CAPTCHAs**: YesCaptcha / 2Captcha / Local Solver (Camoufox)
- **Verificação por SMS**: SMS-Activate / HeroSMS
- **Modos de Execução**: Protocolo (mais rápido, sem navegador) / Headless / Headed
- **2FA Nativo**: Cálculo TOTP integrado sem aplicativos externos
- **Gestão Operacional**: Monitoramento de validade, renovação de tokens e alertas

## Visão Geral

### Painel Principal
<img src="assets/screenshots/概览.png" alt="Painel Principal" width="90%" />

### Gerenciamento de Contas
<img src="assets/screenshots/账号管理.png" alt="Gerenciamento de Contas" width="90%" />

## Comunidade

Junte-se à nossa comunidade para discutir e compartilhar fluxos de automação.
