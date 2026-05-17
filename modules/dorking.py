import requests
from rich.console import Console
from rich.table import Table

console = Console()

DORKS = {
    "Exposed Files":     "site:{domain} ext:pdf OR ext:xlsx OR ext:docx OR ext:sql",
    "Login Pages":       "site:{domain} inurl:login OR inurl:admin OR inurl:dashboard",
    "Config Files":      "site:{domain} ext:env OR ext:cfg OR ext:config",
    "Open Directories":  'site:{domain} intitle:"index of"',
    "Subdomains":        "site:*.{domain} -www",
    "Emails":            "site:{domain} intext:@{domain}",
    "API Keys GitHub":   'site:github.com "{domain}" api_key OR secret OR password',
    "Backup Files":      "site:{domain} ext:bak OR ext:old OR ext:zip",
    "Error Messages":    "site:{domain} intext:error OR intext:warning",
    "Camera Feeds":      "site:{domain} inurl:view/index.shtml",
}

def generate_dorks(domain):
    console.print(f"\n[bold blue]Google Dorks: {domain}[/bold blue]\n")
    
    table = Table(title="Generated Dork Queries")
    table.add_column("Category", style="cyan", width=22)
    table.add_column("Dork Query", style="white")
    
    for category, template in DORKS.items():
        dork = template.replace("{domain}", domain)
        table.add_row(category, dork)
    
    console.print(table)
    
    console.print("\n[bold yellow]Google Search Links:[/bold yellow]\n")
    
    for category, template in DORKS.items():
        dork = template.replace("{domain}", domain)
        encoded = requests.utils.quote(dork)
        url = f"https://www.google.com/search?q={encoded}"
        console.print(f"[cyan]{category}:[/cyan]")
        console.print(f"{url}\n")