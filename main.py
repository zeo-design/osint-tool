from modules.domain_recon import domain_recon
from modules.email_intel import email_intel
from modules.dorking import generate_dorks
from modules.subdomains import enumerate_subdomains
from modules.ip_geo import geolocate_ip
from modules.username_search import search_username
from report_generator import save_report
from rich.console import Console
from rich.panel import Panel
import io
import sys

console = Console()

def capture_output(func, *args):
    buffer = io.StringIO()
    sys.stdout = buffer
    func(*args)
    sys.stdout = sys.__stdout__
    return buffer.getvalue()

def show_banner():
    console.print(Panel.fit(
        "[bold cyan]OSINT Tool V1[/bold cyan]\n"
        "[dim]Domain Recon | Email Intel | Dorking | Subdomains | IP Geo | Username[/dim]\n"
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
    console.print("  [cyan]6[/cyan] - Username Search")
    console.print("  [cyan]7[/cyan] - Run All + Save Report\n")
    
    choice = input("Enter choice (1-7): ").strip()
    
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
        username = input("Enter username: ").strip()
        search_username(username)
    
    elif choice == "7":
        domain = input("Enter domain: ").strip()
        first = input("First name: ").strip()
        last = input("Last name: ").strip()
        username = input("Enter username to search: ").strip()
        
        console.print("\n[bold yellow]Running full recon in sequence...[/bold yellow]\n")
        
        report_data = {}
        
        domain_recon(domain)
        report_data["Domain Recon"] = f"Target: {domain}"
        
        subdomains = enumerate_subdomains(domain)
        report_data["Subdomains"] = str(subdomains)
        
        geolocate_ip(domain)
        report_data["IP Geolocation"] = f"Target: {domain}"
        
        email_intel(first, last, domain)
        report_data["Email Intelligence"] = f"{first} {last} @ {domain}"
        
        generate_dorks(domain)
        report_data["Google Dorking"] = f"Target: {domain}"
        
        search_username(username)
        report_data["Username Search"] = f"Username: {username}"
        
        save_report(domain, report_data)
    
    else:
        console.print("[red]Invalid choice[/red]")

if __name__ == "__main__":
    main()