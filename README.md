OSINT Tool — Open Source Intelligence Automation Platform

"License" (https://img.shields.io/badge/license-MIT-blue)

"Python" (https://img.shields.io/badge/python-3.11+-green)

"Status" (https://img.shields.io/badge/status-active-brightgreen)

An open source reconnaissance and OSINT automation platform built for cybersecurity researchers, security students, penetration testers, analysts, and open source contributors.

The goal is simple:

Automate repetitive reconnaissance workflows while helping people understand how infrastructure intelligence and OSINT actually work behind the scenes.

Built by "zeo-design" (https://github.com/zeo-design) in collaboration with "kaifhoda1" (https://github.com/kaifhoda1)

---

About The Project

Most people use cybersecurity tools.

We wanted to learn how they are actually engineered.

So we started building an open source modular reconnaissance framework that combines:

- infrastructure intelligence
- DNS analysis
- subdomain discovery
- IP intelligence
- OSINT automation
- reconnaissance workflows

This project is actively being developed and improved publicly.

---

The Problem

Security researchers often have to:

- manually check WHOIS data
- use multiple tools for DNS records
- inspect SSL certificates separately
- search Google dorks individually
- search usernames platform by platform
- geolocate IP addresses manually
- combine outputs from multiple disconnected tools

This framework centralizes those workflows into one modular platform.

---

How It Works

User runs main.py
        ↓
Menu appears — select a module
        ↓
Enter target (domain, IP, username, or name)
        ↓
Selected module runs automatically
        ↓
Results displayed in clean terminal output
        ↓
Option 7 runs all modules sequentially

---

Current Modules — Phase 1 & Phase 2

Module| Description
Domain Recon| WHOIS lookup, DNS records, SSL analysis, SPF & DKIM inspection
Email Intelligence| Generates possible corporate email formats
Google Dorking| Generates categorized Google dork queries
Subdomain Enumeration| Discovers hidden subdomains through DNS resolution
IP Geolocation| Maps IP infrastructure, ISP, ASN, and geolocation
Username Search| Searches usernames across multiple platforms
Run All| Executes all modules sequentially

---

What Each Module Reveals

Domain Recon

- Domain ownership information
- Registration timeline
- DNS records (A, MX, NS, TXT, CNAME)
- SSL certificate details
- SPF policies
- DKIM selectors

Email Intelligence

Generates possible email combinations for employees or targets.

Examples:

- john.smith@
- jsmith@
- johnsmith@
- smith.john@

Google Dorking

Helps identify:

- exposed files
- login panels
- open directories
- configuration leaks
- backup files
- public error messages
- indexed sensitive pages

Subdomain Enumeration

Discovers assets such as:

- api.target.com
- admin.target.com
- staging.target.com
- dev.target.com

Useful for infrastructure visibility and attack surface discovery.

IP Geolocation

Provides:

- country
- city
- ISP
- ASN
- organization
- hosting provider
- infrastructure mapping

Username Search

Searches usernames across multiple platforms simultaneously to identify digital footprints.

---

Installation

git clone https://github.com/zeo-design/osint-tool.git

cd osint-tool

pip install -r requirements.txt

---

Requirements

- Python 3.11+
- Git

---

Usage

python main.py

---

Roadmap

Phase 1 — Core Reconnaissance

- WHOIS Intelligence
- DNS Enumeration
- SSL Analysis
- SPF / DKIM Inspection
- Email Intelligence
- Google Dorking

Phase 2 — Infrastructure Intelligence

- Subdomain Enumeration
- IP Geolocation
- Username Search

Phase 3 — Reporting & Web Interface

- Browser-based dashboard
- Automated PDF & HTML reports
- Batch scanning
- Scheduled scans
- JSON & CSV export
- REST API support

Phase 4 — AI-Assisted Intelligence Layer

- AI-based risk scoring
- Pattern recognition
- Threat correlation
- Natural language workflows
- Recon-to-report pipeline

---

Project Philosophy

This project exists because we believe:

- cybersecurity is best learned by building
- open source accelerates learning
- security knowledge should remain accessible
- useful tools should help researchers and learners
- engineering creates deeper understanding than passive consumption

We are not building this project for hype.

We are building it to:

- learn
- solve problems
- improve our engineering skills
- contribute to the cybersecurity community
- create something genuinely useful

---

Ethical Use & Legal Disclaimer

This tool is intended strictly for:

- authorized security research
- educational purposes
- defensive security operations
- legal reconnaissance activities

The developers do NOT support or encourage:

- unauthorized access
- illegal scanning
- malicious exploitation
- privacy violations
- harmful activities against systems without permission

Users are solely responsible for how they use this software.

Always obtain proper authorization before scanning or testing any target.

By using this project, you agree to comply with all applicable local and international laws.

---

Contributors

- "zeo-design" (https://github.com/zeo-design)
- "kaifhoda1" (https://github.com/kaifhoda1)

---

License

MIT License

Free to use, modify, and distribute with attribution.