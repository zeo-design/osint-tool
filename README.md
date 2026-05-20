# OSINT Tool — Open Source Intelligence Automation Platform



![License](https://img.shields.io/badge/license-MIT-blue)




![Python](https://img.shields.io/badge/python-3.11+-green)




![Status](https://img.shields.io/badge/status-active-brightgreen)



An open source OSINT automation platform built for security researchers, penetration testers, and GRC consultants. Automates what takes 20+ minutes of manual work into a single command.

Built by [zeo-design](https://github.com/zeo-design) in collaboration with [kaifhoda1](https://github.com/kaifhoda1)

---

## The Problem

Every security researcher doing reconnaissance has to:
- Manually check WHOIS on a browser
- Use a separate tool for DNS records
- Check SSL certificates manually
- Google dork one query at a time
- Search usernames platform by platform
- Geolocate IPs on external websites

This tool does all of it in one place. Automatically. In seconds.

---

## How It Works
User runs main.py
↓
Menu appears — pick a module
↓
Enter your target — domain, IP, username, or name
↓
Tool runs selected module automatically
↓
Results displayed in clean terminal output
↓
Option 7 runs everything in sequence — full recon report
---

## Current Modules — Phase 1 and Phase 2

| Module | What It Does |
|--------|-------------|
| 1 — Domain Recon | WHOIS lookup, DNS records, SSL certificate parsing, SPF and DKIM email security analysis |
| 2 — Email Intelligence | Generates all possible email format combinations from a name and domain |
| 3 — Google Dorking | Auto generates 10 dork query categories with clickable Google search links |
| 4 — Subdomain Enumeration | Discovers hidden subdomains using DNS brute force across 50 common prefixes |
| 5 — IP Geolocation | Locates any IP address — country, city, ISP, ASN, organisation, coordinates |
| 6 — Username Search | Searches a username across 20 platforms simultaneously using parallel threading |
| 7 — Run All | Runs all modules in sequence for a complete automated recon report |

---

## What Each Module Reveals

### Domain Recon
- Who owns the domain and when it was registered
- All DNS records — A, MX, NS, TXT, CNAME
- SSL certificate issuer, expiry date, and hidden subdomains
- SPF policy — is email spoofing possible
- DKIM selectors — is the domain signing its emails

### Email Intelligence
- All possible email formats for a person at a company
- Example: John Smith at google.com generates john.smith@, johnsmith@, jsmith@, and more

### Google Dorking
- Exposed files — PDF, Excel, SQL dumps
- Login and admin pages
- Config and environment files
- Open directories
- Subdomains
- Backup files
- Exposed API keys on GitHub
- Error messages
- Camera feeds

### Subdomain Enumeration
- Finds assets like admin.target.com, api.target.com, staging.target.com
- Reveals infrastructure that is not publicly advertised

### IP Geolocation
- Physical location of any server
- ISP and hosting provider
- ASN network identification
- Useful for mapping CDN usage and infrastructure providers

### Username Search
- Searches 20 platforms simultaneously
- GitHub, Twitter, Instagram, Reddit, TikTok, LinkedIn, Telegram and more
- Parallel threading makes it fast — all platforms checked at the same time

---

## Installation

```bash
git clone https://github.com/zeo-design/osint-tool.git
cd osint-tool
pip install -r requirements.txt
Requirements
Python 3.11+
Git
Usage
python main.py
Full Roadmap
Phase 1 — Core Recon ✅ Complete
WHOIS, DNS, SSL, SPF, DKIM, Email Intel, Google Dorking
Phase 2 — Deep Intelligence ✅ Complete
Subdomain Enumeration, IP Geolocation, Username Search across 20 platforms
Phase 3 — Reporting and Web UI
Browser based dashboard
Auto generated PDF and HTML reports
Batch scanning multiple targets
Scheduled automated scans
JSON and CSV export
REST API endpoint
Phase 4 — AI Layer
AI risk scoring on all collected data
Pattern recognition across multiple scans
Anomaly detection and threat correlation
Natural language interface — type what you want, AI figures out how
Full pipeline from recon to risk report
This is the ByteFortix commercial product
Legal Disclaimer
This tool is strictly for authorized and legal security research only.
Only use on domains, IPs, and targets you own or have written permission to test
The developers hold no responsibility for any misuse
Misuse of this tool may violate local and international laws
All contributors follow responsible disclosure practices
Contributors
zeo-design
kaifhoda1
License
MIT License — Free to use, modify, and distribute with attribution.
---