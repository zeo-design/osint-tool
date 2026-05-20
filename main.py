from modules.domain_recon import domain_recon
from modules.email_intel import email_intel
from modules.dorking import generate_dorks
from modules.subdomains import enumerate_subdomains
from modules.ip_geo import geolocate_ip
from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    console.print(Panel.fit(
        "[bold cyan]OSINT Tool V1[/bold cyan]\n"
        "[dim]Domain Recon | Email Intel | Google Dorking | Subdomains | IP Geo[/dim]\n"
        "[red]For authorized and legal use only.[/red]",
        border_style="cyan"
    ))

def main():
    show_banner()
    
    console.print("\n[bold]Select Module:[/bold]")
    console.print("  [cyan]1[/cyan] - Domain Recon")
    console.print("  [cyan]2[/cyan] - Email Intelligence")
    console.print("  [cyan]3[/cyan] - Google Dorking")
    console.print("  [cyan]4[/cyan] - Subdomain Enumeration")
    console.print("  [cyan]5[/cyan] - IP Geolocation")
    console.print("  [cyan]6[/cyan] - Run All\n")
    
    choice = input("Enter choice (1-6): ").strip()
    
    if choice == "1":
        domain = input("Enter domain (e.g. google.com): ").strip()
        domain_recon(domain)
    
    elif choice == "2":
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        domain = input("Company domain: ").strip()
        email_intel(first, last, domain)
    
    elif choice == "3":
        domain = input("Enter domain: ").strip()
        generate_dorks(domain)
    
    elif choice == "4":
        domain = input("Enter domain: ").strip()
        enumerate_subdomains(domain)
    
    elif choice == "5":
        ip = input("Enter IP address: ").strip()
        geolocate_ip(ip)
    
    elif choice == "6":
        domain = input("Enter domain: ").strip()
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        console.print("\n[bold yellow]Running full recon in sequence...[/bold yellow]\n")
        domain_recon(domain)
        enumerate_subdomains(domain)
        geolocate_ip(domain)
        email_intel(first, last, domain)
        generate_dorks(domain)
    
    else:
        console.print("[red]Invalid choice[/red]")

if __name__ == "__main__":
    main()