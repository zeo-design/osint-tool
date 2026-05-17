import requests
from rich.console import Console
from rich.table import Table

console = Console()

def guess_email_formats(first, last, domain):
    first = first.lower()
    last = last.lower()
    f = first[0]
    
    formats = [
        f"{first}.{last}@{domain}",
        f"{first}{last}@{domain}",
        f"{f}{last}@{domain}",
        f"{first}@{domain}",
        f"{first}_{last}@{domain}",
        f"{last}.{first}@{domain}",
    ]
    
    table = Table(title="Possible Email Formats")
    table.add_column("Email", style="cyan")
    
    for email in formats:
        table.add_row(email)
    
    console.print(table)

def email_intel(first, last, domain):
    console.print(f"\n[bold blue]Email Intel: {first} {last} @ {domain}[/bold blue]\n")
    guess_email_formats(first, last, domain)