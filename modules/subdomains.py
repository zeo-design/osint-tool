import dns.resolver
from rich.console import Console
from rich.table import Table

console = Console()

SUBDOMAINS = [
    "www", "mail", "ftp", "admin", "api", "dev", "staging",
    "test", "blog", "shop", "store", "portal", "vpn", "remote",
    "support", "help", "docs", "cdn", "static", "assets",
    "login", "dashboard", "app", "mobile", "beta", "old",
    "new", "secure", "ssl", "mx", "email", "webmail", "smtp",
    "pop", "imap", "cloud", "git", "gitlab", "jenkins", "jira",
    "confluence", "wiki", "intranet", "internal", "corp", "hr"
]

def enumerate_subdomains(domain):
    console.print(f"\n[bold blue]Subdomain Enumeration: {domain}[/bold blue]\n")
    
    found = []
    
    table = Table(title="Discovered Subdomains")
    table.add_column("Subdomain", style="cyan")
    table.add_column("IP Address", style="green")
    
    for sub in SUBDOMAINS:
        target = f"{sub}.{domain}"
        try:
            answers = dns.resolver.resolve(target, "A")
            for ans in answers:
                found.append(target)
                table.add_row(target, str(ans))
                break
        except:
            pass
    
    if found:
        console.print(table)
        console.print(f"\n[green]Found {len(found)} subdomains[/green]")
    else:
        console.print("[red]No subdomains found[/red]")
    
    return found