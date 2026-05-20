import whois
import dns.resolver
import ssl
import socket
import requests
from rich.console import Console
from rich.table import Table

console = Console()

def run_whois(domain):
    try:
        w = whois.whois(domain)
        table = Table(title="WHOIS Results")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="white")
        table.add_row("Registrar", str(w.registrar))
        table.add_row("Creation Date", str(w.creation_date))
        table.add_row("Expiry Date", str(w.expiration_date))
        table.add_row("Name Servers", str(w.name_servers))
        table.add_row("Emails", str(w.emails))
        console.print(table)
    except Exception as e:
        console.print(f"[red]WHOIS failed: {e}[/red]")

def run_dns(domain):
    try:
        table = Table(title="DNS Records")
        table.add_column("Type", style="cyan")
        table.add_column("Value", style="white")
        for record in ["A", "MX", "NS", "TXT", "CNAME"]:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = ["8.8.8.8", "8.8.4.4"]
                resolver.timeout = 10
                resolver.lifetime = 10
                answers = resolver.resolve(domain, record)
                for ans in answers:
                    table.add_row(record, str(ans))
            except:
                pass
        console.print(table)
    except Exception as e:
        console.print(f"[red]DNS failed: {e}[/red]")

def run_ssl(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(10)
            s.connect((domain, 443))
            cert = s.getpeercert()
        table = Table(title="SSL Certificate")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="white")
        subject = dict(x[0] for x in cert["subject"])
        issuer = dict(x[0] for x in cert["issuer"])
        sans = [v for t, v in cert.get("subjectAltName", []) if t == "DNS"]
        table.add_row("Common Name", subject.get("commonName", "N/A"))
        table.add_row("Issuer", issuer.get("organizationName", "N/A"))
        table.add_row("Valid Until", cert.get("notAfter", "N/A"))
        table.add_row("Subdomains", "\n".join(sans[:10]))
        console.print(table)
    except Exception as e:
        console.print(f"[red]SSL failed: {e}[/red]")

def run_spf_dkim(domain):
    console.print("\n[bold yellow][ SPF / DKIM Check ][/bold yellow]")
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8", "8.8.4.4"]
        resolver.timeout = 10
        resolver.lifetime = 10
        answers = resolver.resolve(domain, "TXT")
        spf_found = False
        for r in answers:
            txt = str(r).replace('"', '').strip()
            if "v=spf1" in txt:
                console.print(f"[green]SPF Found:[/green] {txt}")
                spf_found = True
        if not spf_found:
            console.print("[red]No SPF record found — email spoofing may be possible[/red]")
    except Exception as e:
        console.print(f"[red]SPF check failed: {e}[/red]")

    selectors = ["default", "google", "mail", "selector1", "selector2", "k1", "ms"]
    dkim_found = False
    for sel in selectors:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = ["8.8.8.8", "8.8.4.4"]
            resolver.timeout = 10
            resolver.lifetime = 10
            resolver.resolve(f"{sel}._domainkey.{domain}", "TXT")
            console.print(f"[green]DKIM Found:[/green] selector = {sel}")
            dkim_found = True
        except:
            pass
    if not dkim_found:
        console.print("[red]No DKIM selectors found[/red]")

def domain_recon(domain):
    console.print(f"\n[bold blue]Target: {domain}[/bold blue]\n")
    run_whois(domain)
    run_dns(domain)
    run_ssl(domain)
    run_spf_dkim(domain)